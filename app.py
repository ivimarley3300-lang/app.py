import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- 1. CONFIGURAÇÃO E CACHE DE ALTA VELOCIDADE ---
st.set_page_config(page_title="GameVault Ultra-Fast", layout="wide", page_icon="⚡")

# Cache de Token para não pedir autorização toda hora
@st.cache_data(ttl=3600)
def get_auth():
    r = requests.post(f"https://id.twitch.tv/oauth2/token?client_id=eakvrhyzodw5xcr7e2q6gsz94ybiap&client_secret=fsrgfhqs98tpxfantkwhde786paxls&grant_type=client_credentials")
    return r.json().get('access_token')

# Função de consulta otimizada
def query_igdb(endpoint, query):
    token = get_auth()
    headers = {'Client-ID': 'eakvrhyzodw5xcr7e2q6gsz94ybiap', 'Authorization': f'Bearer {token}'}
    r = requests.post(f"https://api.igdb.com/v4/{endpoint}", headers=headers, data=query)
    return r.json() if r.status_code == 200 else []

# --- 2. ESTILO CSS (Otimizado para não pesar no render) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;700&display=swap');
    .stApp { background: #050505; color: #eee; font-family: 'Inter', sans-serif; }
    .game-card {
        background: #111; border: 1px solid #222; border-radius: 12px;
        padding: 10px; transition: 0.2s ease-in-out; text-align: center;
    }
    .game-card:hover { border-color: #00f2ff; transform: scale(1.02); }
    /* Efeito de carregamento suave */
    .stImage img { animation: fadeIn 0.5s; border-radius: 8px; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE VELOCIDADE (CARREGAMENTO EM BLOCO) ---
if 'pg' not in st.session_state: st.session_state.pg = 0

with st.sidebar:
    st.title("⚡ Ultra-Fast")
    busca = st.text_input("Busca Instantânea")

# Puxamos TUDO o que precisamos de uma vez (Summary, Screenshots, Websites) 
# para que o modal não precise de uma nova consulta à internet.
off = st.session_state.pg * 12
campos_completos = "fields name, summary, rating, first_release_date, cover.url, screenshots.url, websites.url, websites.category;"

if busca:
    q = f'search "{busca}"; {campos_completos} limit 12;'
else:
    q = f"{campos_completos} where rating_count > 10; sort rating desc; limit 12; offset {off};"

# Esta é a única chamada de rede que o app fará por página
jogos = query_igdb("games", q)

# --- 4. MODAL INSTANTÂNEO (SEM CONSULTA DE REDE) ---
@st.dialog("INFO TÉCNICA", width="large")
def modal_detalhes(g):
    nome = g.get('name')
    st.header(f"🚀 {nome}")
    
    c1, c2 = st.columns([1, 1.5])
    with c1:
        # Usamos a URL que já veio na busca inicial
        img = "https:" + g['cover']['url'].replace('t_thumb', 't_720p') if 'cover' in g else ""
        st.image(img, use_container_width=True)
        search_query = urllib.parse.quote(nome)
        st.link_button("📊 TECHNICAL CITY (BENCHMARK)", f"https://technical.city/pt/can-i-run-it?game={search_query}", use_container_width=True)

    with c2:
        st.write(f"⭐ **NOTA:** {int(g.get('rating', 0))}/100")
        st.write(g.get('summary', 'Sem descrição.'))
        
        st.markdown("### 🛒 LINKS")
        sites = g.get('websites', [])
        if sites:
            cols = st.columns(2)
            for i, s in enumerate(sites[:4]):
                with cols[i%2]:
                    st.link_button(f"Link {i+1}", s.get('url'), use_container_width=True)

    if 'screenshots' in g:
        st.divider()
        imgs = ["https:" + s['url'].replace('t_thumb', 't_med') for s in g['screenshots'][:3]]
        st.image(imgs, use_container_width=True)

# --- 5. GRID ---
if jogos:
    cols = st.columns(4)
    for i, j in enumerate(jogos):
        with cols[i % 4]:
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            # Capa otimizada (t_cover_big é mais leve que t_720p)
            capa = "https:" + j.get('cover', {}).get('url', '').replace('t_thumb', 't_cover_big') if j.get('cover') else "https://via.placeholder.com/264x352"
            st.image(capa, use_container_width=True)
            st.markdown(f"**{j.get('name')}**")
            
            # O SEGREDO: Passamos o dicionário 'j' inteiro para a função
            # assim o modal abre na hora porque já tem os dados na memória!
            if st.button("ANALISAR", key=f"id_{j['id']}", use_container_width=True):
                modal_detalhes(j)
            st.markdown('</div>', unsafe_allow_html=True)

    # Navegação
    st.markdown("---")
    b1, b2, b3 = st.columns([1,1,1])
    if b1.button("⬅️ VOLTAR") and st.session_state.pg > 0:
        st.session_state.pg -= 1
        st.rerun()
    if b3.button("MAIS ➡️"):
        st.session_state.pg += 1
        st.rerun()
