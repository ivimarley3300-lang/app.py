import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import random

# --- 1. CONFIGURAÇÃO DE ALTA PERFORMANCE ---
st.set_page_config(page_title="GameVault Pro | Steam Reviews", layout="wide", page_icon="🎮")

@st.cache_data(ttl=3600)
def get_auth():
    r = requests.post(f"https://id.twitch.tv/oauth2/token?client_id=eakvrhyzodw5xcr7e2q6gsz94ybiap&client_secret=fsrgfhqs98tpxfantkwhde786paxls&grant_type=client_credentials")
    return r.json().get('access_token')

def query_igdb(endpoint, query):
    token = get_auth()
    headers = {'Client-ID': 'eakvrhyzodw5xcr7e2q6gsz94ybiap', 'Authorization': f'Bearer {token}'}
    r = requests.post(f"https://api.igdb.com/v4/{endpoint}", headers=headers, data=query)
    return r.json() if r.status_code == 200 else []

def traduzir_resumo(texto):
    if not texto: return "Descrição não disponível."
    try:
        url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(texto[:500])}&langpair=en|pt-BR"
        r = requests.get(url)
        return r.json()['responseData']['translatedText']
    except:
        return texto

# --- NOVO: BUSCA DE COMENTÁRIOS REAIS DA STEAM ---
def exibir_comentarios_steam(nome_jogo):
    st.markdown("### 🗣️ O QUE DIZEM OS JOGADORES NA STEAM")
    try:
        # 1. Busca o AppID na Steam pelo nome
        search_url = f"https://store.steampowered.com/api/storesearch/?term={urllib.parse.quote(nome_jogo)}&l=brazilian&cc=BR"
        res_search = requests.get(search_url).json()
        
        if res_search.get('total') > 0:
            appid = res_search['items'][0]['id']
            # 2. Busca as reviews reais usando o AppID
            reviews_url = f"https://store.steampowered.com/appreviews/{appid}?json=1&language=brazilian&filter=summary&num_per_page=3"
            res_reviews = requests.get(reviews_url).json()
            
            if res_reviews.get('reviews'):
                for rev in res_reviews['reviews']:
                    col_icon, col_txt = st.columns([1, 10])
                    with col_icon:
                        st.write("👍" if rev['voted_up'] else "👎")
                    with col_txt:
                        # Limita o tamanho do comentário para não quebrar o layout
                        texto_review = rev['review'][:300] + "..." if len(rev['review']) > 300 else rev['review']
                        st.markdown(f"*{texto_review}*")
                    st.markdown("---")
            else:
                st.info("Ainda não há comentários brasileiros para este título na Steam.")
        else:
            st.warning("Jogo não localizado na base de dados da Steam.")
    except:
        st.error("Erro ao conectar com os servidores da Steam.")

# --- 2. DESIGN SYSTEM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Plus+Jakarta+Sans:wght@300;400;700&display=swap');
    .stApp { background: #020205; color: #f8f9fa; font-family: 'Plus Jakarta Sans', sans-serif; }
    .game-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px; padding: 15px; transition: all 0.3s; text-align: center; backdrop-filter: blur(10px);
    }
    .game-card:hover { transform: translateY(-8px); border-color: #00f2ff; box-shadow: 0 10px 30px rgba(0, 242, 255, 0.2); }
    .score-box { background: linear-gradient(135deg, #00f2ff, #7000ff); padding: 5px 12px; border-radius: 8px; font-weight: 800; font-family: 'Orbitron'; color: white; }
    .company-tag { color: #00f2ff; font-size: 0.8rem; text-transform: uppercase; font-weight: 700; margin-bottom: 5px;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE NAVEGAÇÃO ---
if 'pg' not in st.session_state: st.session_state.pg = 0
with st.sidebar:
    st.title("🌌 GameVault Pro")
    busca = st.text_input("🔍 PESQUISAR JOGO")
    ordem = st.selectbox("ORDENAR", ["Populares", "Crítica", "Lançamentos"])

off = st.session_state.pg * 12
campos = "fields name, summary, rating, aggregated_rating, first_release_date, cover.url, screenshots.url, websites.url, websites.category, involved_companies.company.name, involved_companies.developer;"

if busca:
    q = f'search "{busca}"; {campos} limit 12;'
else:
    sort_q = "rating desc" if ordem == "Crítica" else "first_release_date desc"
    q = f"{campos} where rating_count > 10; sort {sort_q}; limit 12; offset {off};"

jogos = query_igdb("games", q)

# --- 4. MODAL COM COMENTÁRIOS DA STEAM ---
@st.dialog("DOSSIÊ DO JOGO", width="large")
def modal_detalhes(g):
    nome = g.get('name')
    st.title(f"👾 {nome}")
    
    c1, c2 = st.columns([1.2, 2])
    with c1:
        img = "https:" + g['cover']['url'].replace('t_thumb', 't_720p') if 'cover' in g else ""
        st.image(img, use_container_width=True)
        col_n1, col_n2 = st.columns(2)
        col_n1.metric("PÚBLICO", f"{int(g.get('rating', 0))}%")
        col_n2.metric("CRÍTICA", f"{int(g.get('aggregated_rating', 0))}%")
        st.link_button("📊 REQUISITOS (Technical.City)", f"https://technical.city/pt/can-i-run-it?game={urllib.parse.quote(nome)}", use_container_width=True)

    with c2:
        empresas = [comp['company']['name'] for comp in g.get('involved_companies', []) if comp.get('developer')]
        st.markdown(f"<div class='company-tag'>DESENVOLVEDOR: {', '.join(empresas) if empresas else 'Indie'}</div>", unsafe_allow_html=True)
        
        st.markdown("### 📜 RESUMO EM PORTUGUÊS")
        with st.spinner('Traduzindo dossiê...'):
            resumo_pt = traduzir_resumo(g.get('summary', ''))
            st.write(resumo_pt)
        
        st.write(f"📅 **LANÇAMENTO:** {datetime.fromtimestamp(g.get('first_release_date', 0)).strftime('%d/%m/%Y') if g.get('first_release_date') else 'TBA'}")
        
        st.divider()
        # SUBSTITUÍDO: Agora exibe comentários REAIS da Steam
        exibir_comentarios_steam(nome)

    if 'screenshots' in g:
        st.divider()
        st.markdown("### 📸 GALERIA DE FOTOS")
        fotos = ["https:" + s['url'].replace('t_thumb', 't_720p') for s in g['screenshots']]
        st.image(fotos, use_container_width=True)

# --- 5. GRID ---
if jogos:
    cols = st.columns(4)
    for i, j in enumerate(jogos):
        with cols[i % 4]:
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:right;'><span class='score-box'>{int(j.get('rating', 0))}</span></div>", unsafe_allow_html=True)
            capa = "https:" + j.get('cover', {}).get('url', '').replace('t_thumb', 't_cover_big') if j.get('cover') else "https://via.placeholder.com/264x352"
            st.image(capa, use_container_width=True)
            st.markdown(f"<p style='font-weight:bold; height:50px;'>{j.get('name')}</p>", unsafe_allow_html=True)
            if st.button("ABRIR DOSSIÊ", key=f"id_{j['id']}", use_container_width=True):
                modal_detalhes(j)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    b1, b2, b3 = st.columns([1,1,1])
    if b1.button("⬅️ VOLTAR") and st.session_state.pg > 0:
        st.session_state.pg -= 1
        st.rerun()
    if b3.button("MAIS ➡️"):
        st.session_state.pg += 1
        st.rerun()
