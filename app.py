import streamlit as st
import os
import time
import random
from datetime import datetime
import requests
import json

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(
    page_title="Heleninha Videos - Exclusive VIP", 
    layout="wide", 
    page_icon="🔥",
    initial_sidebar_state="collapsed"
)

# --- IA PERSONALIZADA PARA ATENDIMENTO ---
class AssistenteVIP:
    def __init__(self):
        self.respostas_base = {
            "preço": {
                "resposta": "💎 **VALOR PROMOCIONAL:** Apenas R$ 20,00 por acesso vitalício!\n\n🔥 **Oferta Relâmpago:** Essa promoção pode acabar a qualquer momento!",
                "emoji": "💎"
            },
            "pix": {
                "resposta": "🔑 **CHAVE PIX OFICIAL:** `mariahelenadossantos339@gmail.com`\n\n📱 **Passo a passo:**\n1. Copie a chave PIX\n2. Pague R$ 20,00\n3. Envie comprovante para @Helenagbysi\n4. Acesso liberado em 2min!",
                "emoji": "🔑"
            },
            "conteúdo": {
                "resposta": "🎬 **CONTEÚDO EXCLUSIVO INCLUI:**\n\n• Nossa relação única e especial 💖\n• Momentos íntimos com meus pais que mostram nossa conexão incrível\n• Vídeos caseiros mostrando o dia a dia da nossa família\n• Conteúdo solo onde expresso minha arte pessoal\n• Atualizações constantes da nossa vida\n• Suporte VIP 24/7",
                "emoji": "🎬"
            },
            "segurança": {
                "resposta": "🛡️ **COMPRA 100% SEGURA:**\n\n✓ Pagamento via PIX oficial\n✓ Entrega imediata\n✓ Suporte garantido\n✓ Privacidade total\n✓ Qualidade certificada",
                "emoji": "🛡️"
            },
            "garantia": {
                "resposta": "✅ **GARANTIA VIP:** Se não gostar em 24h, devolvemos seu dinheiro!\n\nÉ risco zero para você experimentar nosso conteúdo premium!",
                "emoji": "✅"
            }
        }
    
    def analisar_intencao(self, pergunta):
        pergunta = pergunta.lower()
        
        if any(palavra in pergunta for palavra in ['preço', 'valor', 'custa', 'quanto', 'cust', 'dinheiro']):
            return "preço"
        elif any(palavra in pergunta for palavra in ['pix', 'pagamento', 'pagar', 'pag', 'chave', 'comprar']):
            return "pix"
        elif any(palavra in pergunta for palavra in ['conteúdo', 'video', 'foto', 'foto', 'conteudo', 'ver']):
            return "conteúdo"
        elif any(palavra in pergunta for palavra in ['seguro', 'segurança', 'confiável', 'confiavel', 'segur']):
            return "segurança"
        elif any(palavra in pergunta for palavra in ['garantia', 'devolução', 'devolucao', 'devolv', 'risco']):
            return "garantia"
        else:
            return "geral"
    
    def gerar_resposta_personalizada(self, pergunta, nome_usuario="VIP"):
        intencao = self.analisar_intencao(pergunta)
        
        if intencao in self.respostas_base:
            resposta_base = self.respostas_base[intencao]
            return f"{resposta_base['emoji']} **Olá {nome_usuario}!**\n\n{resposta_base['resposta']}\n\n💬 **Precisa de mais ajuda?** Chame @Helenagbysi no Telegram!"
        
        # Resposta padrão persuasiva
        respostas_padrao = [
            f"✨ **Excelente pergunta, {nome_usuario}!** Nossa relação familiar é algo único e especial que quero compartilhar com você. Por apenas R$ 20,00 você terá acesso a momentos íntimos e genuínos da nossa família! 🎁\n\n🔑 **Chave PIX:** mariahelenadossantos339@gmail.com",
            
            f"🔥 **Ótima dúvida!** O conteúdo mostra a beleza da nossa conexão familiar - são momentos reais, espontâneos e cheios de amor! Mais de 50 mídias exclusivas por apenas R$ 20,00. Garanta seu acesso antes que as vagas se esgotem! ⏰\n\n💎 **Promoção relâmpago em andamento!**",
            
            f"🎯 **Você veio ao lugar certo, {nome_usuario}!** Nosso conteúdo é 100% genuíno e mostra a relação linda que temos em família. O investimento de R$ 20,00 é único e vitalício! Não perca essa oportunidade de fazer parte da nossa história! 🚀\n\n📱 **Telegram:** @Helenagbysi"
        ]
        
        return random.choice(respostas_padrao)

# --- CSS PERSONALIZADO COM ANIMAÇÕES DOPAMINÉRGICAS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;600;700;900&family=Dancing+Script:wght@700&display=swap');

.stApp {
    background: linear-gradient(-45deg, #0a0a0a, #1a0a0a, #0a0a1a, #1a0a1a);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #ffffff; 
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
}

@keyframes gradientShift {
    0% { background-position: 0% 50% }
    50% { background-position: 100% 50% }
    100% { background-position: 0% 50% }
}

.vip-header {
    background: linear-gradient(145deg, rgba(26,26,26,0.95), rgba(0,0,0,0.98));
    padding: 60px 30px;
    border-bottom: 3px solid transparent;
    border-image: linear-gradient(45deg, #d4af37, #ff6b6b, #d4af37) 1;
    text-align: center;
    border-radius: 0 0 60px 60px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(212, 175, 55, 0.3);
}

.vip-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.2), transparent);
    animation: shine 3s infinite;
}

.gold-title {
    font-family: 'Playfair Display', serif;
    background: linear-gradient(45deg, #d4af37, #ffd700, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 4rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    text-shadow: 0 0 30px rgba(212, 175, 55, 0.5);
    animation: titleGlow 2s ease-in-out infinite alternate;
}

.urgency-banner {
    background: linear-gradient(90deg, #b20000, #ff0000, #b20000);
    background-size: 200% 200%;
    color: white;
    padding: 15px;
    text-align: center;
    font-weight: bold;
    font-size: 1.2rem;
    animation: pulseUrgency 1.5s infinite, bannerSlide 3s infinite;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.gallery-card {
    background: linear-gradient(145deg, #161616, #1a1a1a);
    border: 2px solid transparent;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    margin: 10px 0;
}

.gallery-card:hover {
    transform: translateY(-10px) scale(1.03);
    border-color: #d4af37;
    box-shadow: 0 15px 40px rgba(212, 175, 55, 0.3);
}

.stButton button {
    background: linear-gradient(45deg, #d4af37, #ff6b6b);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    font-weight: bold;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(212, 175, 55, 0.4);
}

/* Chat styles melhorados */
.stChatMessage {
    border-radius: 20px;
    margin: 10px 0;
    border: 1px solid rgba(212, 175, 55, 0.3);
    padding: 15px;
}

/* Animações para o chat */
@keyframes slideIn {
    from { transform: translateX(-20px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

.chat-message {
    animation: slideIn 0.3s ease-out;
}

/* Botões de ação rápida no chat */
.chat-action-button {
    background: linear-gradient(45deg, #d4af37, #ff6b6b);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 15px;
    margin: 5px;
    cursor: pointer;
    transition: all 0.3s;
}

.chat-action-button:hover {
    transform: scale(1.05);
}

.vagas-counter {
    font-family: 'Dancing Script', cursive;
    font-size: 2rem;
    background: linear-gradient(45deg, #ff6b6b, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: counterPulse 2s infinite;
}

</style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DA IA ---
assistente_vip = AssistenteVIP()

# --- CONTADOR DE VENDAS DINÂMICO ---
def get_vendas_realizadas():
    """Simula vendas baseado no horário - VENDA DIRETA SEM GRUPO"""
    now = datetime.now()
    hour = now.hour
    # Vendas aumentam durante horários de pico (18h-22h)
    if 18 <= hour <= 22:
        return min(97, 85 + random.randint(5, 12))  # Pico de vendas
    else:
        return min(97, 80 + random.randint(0, 8))  # Vendas normais

vendas_realizadas = get_vendas_realizadas()
vagas_restantes = 100 - vendas_realizadas
progress_width = (vendas_realizadas / 100) * 100

# --- BANNER DE URGÊNCIA DINÂMICO ---
urgency_messages = [
    f"🚨 APENAS {vagas_restantes} ACESSOS RESTANTES! PROMOÇÃO RELÂMPAGO!",
    f"⚡ {vagas_restantes} VAGAS - ADQUIRA AGORA POR R$ 20!",
    f"🔥 ÚLTIMAS {vagas_restantes} UNIDADES DISPONÍVEIS!"
]

st.markdown(f'<div class="urgency-banner">{random.choice(urgency_messages)}</div>', unsafe_allow_html=True)

# --- HEADER VIP COM CONTADOR ---
st.markdown(f'''
<div class="vip-header">
    <h1 class="gold-title">Heleninha Videos VIP</h1>
    <p style="color: #ccc; font-size: 1.2rem;">Conteúdo Exclusivo • Acesso Imediato • Garantia de Qualidade</p>
    <div style="margin: 20px 0;">
        <span class="vagas-counter">{vendas_realizadas} Vendas Realizadas</span>
        <div style="height: 6px; background: #333; border-radius: 3px; overflow: hidden; margin: 10px 0;">
            <div style="height: 100%; background: linear-gradient(90deg, #ff6b6b, #d4af37); border-radius: 3px; width: {progress_width}%; transition: width 0.5s ease;"></div>
        </div>
        <p style="color: #d4af37; font-size: 1.1rem;">🚀 {vagas_restantes} acessos restantes - Não perca!</p>
    </div>
</div>
''', unsafe_allow_html=True)

# --- MODAL DE CHECKOUT VIP ---
@st.dialog("💎 ÁREA DE PAGAMENTO SEGURA VIP")
def checkout_pro(item):
    st.markdown(f"### 🎯 Pacote Selecionado: **{item}**")
    
    st.metric("💰 Valor de Lançamento", "R$ 20,00", delta="-75% OFF", delta_color="off")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🎁 O que você recebe:**")
        st.success("✓ Acesso Imediato ao Conteúdo")
        st.success("✓ Relação Familiar Exclusiva")
        st.success("✓ Qualidade Premium HD")
        st.success("✓ Suporte VIP 24/7")
        
    with col2:
        st.markdown("**⏰ Tempo Restante:**")
        with st.container():
            st.warning("⌛ Oferta expira em 24h")
        
    st.divider()
    
    st.markdown("**🔑 CHAVE PIX OFICIAL:**")
    st.code("mariahelenadossantos339@gmail.com", language="text")
    
    st.markdown("**📱 PASSO A PASSO:**")
    steps = [
        "1. Copie a chave PIX acima",
        "2. Realize o pagamento de R$ 20,00",
        "3. Envie o comprovante no Telegram",
        "4. Receba o acesso INSTANTÂNEO!"
    ]
    
    for step in steps:
        st.markdown(f"<p style='color:#d4af37;'>{step}</p>", unsafe_allow_html=True)
    
    st.link_button("🚀 ENVIAR COMPROVANTE AGORA", "https://t.me/Helenagbysi", use_container_width=True)

# --- GALERIA PREMIUM ---
st.markdown("<br>", unsafe_allow_html=True)

fotos = [
    {
        "arq": "photo_5174912881735175080_y.jpg", 
        "label": "🎬 Nossa Relação Pai e Filha Incrível",
        "badge": "⭐ MAIS PESSOAL",
        "desc": "💖 Momentos genuínos mostrando a conexão única entre pai e filha - algo tão natural e especial!"
    },
    {
        "arq": "photo_5174912881735175079_y.jpg", 
        "label": "💖 Conexão Familiar Verdadeira",
        "badge": "🔥 MOMENTOS ÚNICOS",
        "desc": "✨ Nossa relação mãe e filha em momentos do dia a dia - tão raro e bonito de se ver!"
    },
    {
        "arq": "photo_5174912881735175078_y.jpg", 
        "label": "✨ Minha Expressão Artística Pessoal",
        "badge": "💎 EXCLUSIVO",
        "desc": "🎨 Conteúdo solo onde mostro minha essência e arte pessoal - muito pessoal e autêntico!"
    }
]

cols = st.columns(3)
for i, item in enumerate(fotos):
    with cols[i]:
        st.markdown(f'<div class="gallery-card">', unsafe_allow_html=True)
        
        st.markdown(f'<div style="background: linear-gradient(45deg, #ff6b6b, #d4af37); padding: 5px 15px; border-radius: 15px; display: inline-block; margin-bottom: 10px;">{item["badge"]}</div>', unsafe_allow_html=True)
        
        if os.path.exists(item["arq"]):
            st.image(item["arq"], use_container_width=True)
        else:
            st.markdown('''
            <div style="height: 200px; background: linear-gradient(45deg, #1a1a1a, #2a1a2a); 
                     display: flex; align-items: center; justify-content: center; border-radius: 15px;">
                <span style="font-size: 3rem;">🎬</span>
            </div>
            ''', unsafe_allow_html=True)
        
        st.markdown(f'<h3 style="color:#d4af37; margin: 15px 0;">{item["label"]}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #ccc; font-size: 0.9rem;">{item["desc"]}</p>', unsafe_allow_html=True)
        
        if st.button(f"🎁 DESBLOQUEAR POR R$ 20", key=f"btn_{i}", use_container_width=True):
            checkout_pro(item['label'])
            st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO DE DEPOIMENTOS ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("### 💬 O Que Nossos Clientes Dizem")

depoimentos = [
    {
        "nome": "Carlos S.", 
        "texto": "A relação familiar mostrada é incrível! Tão genuína e bonita! Valeu cada centavo! 👏", 
        "estrelas": "★★★★★"
    },
    {
        "nome": "Ana P.", 
        "texto": "Que conexão linda entre vocês! Me emocionei com a autenticidade dos momentos! 💖", 
        "estrelas": "★★★★★"
    },
    {
        "nome": "Ricardo M.", 
        "texto": "Conteúdo muito pessoal e verdadeiro! Dá pra sentir o carinho de vocês! 🔥", 
        "estrelas": "★★★★★"
    }
]

cols_depoimentos = st.columns(3)
for i, depoimento in enumerate(depoimentos):
    with cols_depoimentos[i]:
        st.markdown(f'''
        <div style="background: rgba(212, 175, 55, 0.1); padding: 20px; border-radius: 15px; 
                    border-left: 4px solid #d4af37; margin: 10px;">
            <p style="color: #ffd700; font-size: 1.5rem;">{depoimento["estrelas"]}</p>
            <p style="font-style: italic;">"{depoimento["texto"]}"</p>
            <p style="color: #d4af37; font-weight: bold;">- {depoimento["nome"]}</p>
        </div>
        ''', unsafe_allow_html=True)

# --- CHAT IA AVANÇADA E INTERATIVA ---
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.markdown("### 🤖 Assistente Virtual Premium - Tire Todas suas Dúvidas!")

# Estado da sessão para o chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 **Olá! Sou a assistente VIP da Heleninha!**\n\nEstou aqui para tirar todas suas dúvidas sobre:\n\n• 💰 **Preços e promoções**\n• 🔑 **Formas de pagamento**\n• 🎬 **Conteúdo exclusivo e pessoal**\n• 🛡️ **Segurança e garantia**\n\n**Pergunte qualquer coisa!** 😊"}
    ]

if "user_name" not in st.session_state:
    st.session_state.user_name = "VIP"

# Botões de dúvidas rápidas
st.markdown("**🚀 Dúvidas Rápidas:**")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💰 Preço?", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Quanto custa o acesso?"})
with col2:
    if st.button("🔑 Pagamento?", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Como faço o pagamento?"})
with col3:
    if st.button("🎬 Conteúdo?", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "O que inclui o conteúdo?"})
with col4:
    if st.button("🛡️ Segurança?", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "É seguro comprar?"})

# Mostrar histórico do chat
chat_container = st.container()
with chat_container:
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Adicionar botão de ação após a última mensagem do assistant
            if message["role"] == "assistant" and i == len(st.session_state.messages) - 1:
                col_a, col_b = st.columns(2)
                with col_a:
                    st.link_button("💬 Falar no Telegram", "https://t.me/Helenagbysi")
                with col_b:
                    if st.button("🎁 Quero Comprar!", key="compra_chat"):
                        checkout_pro("Acesso VIP Completo")

# Input do chat
if prompt := st.chat_input("Digite sua dúvida sobre o conteúdo VIP..."):
    # Adicionar mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Gerar resposta da IA
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Simulação de digitação
        full_response = ""
        resposta_ia = assistente_vip.gerar_resposta_personalizada(prompt, st.session_state.user_name)
        
        for chunk in resposta_ia.split():
            full_response += chunk + " "
            time.sleep(0.03)
            message_placeholder.markdown(full_response + " ▌")
        
        message_placeholder.markdown(full_response)
        
        # Botões de ação após resposta
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("💬 Suporte no Telegram", "https://t.me/Helenagbysi")
        with col2:
            if st.button("💰 Quero Comprar Agora!", key="compra_rapida"):
                checkout_pro("Acesso VIP via Chat")
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- FUNCIONALIDADE EXTRA: FORMULÁRIO DE INTERESSE ---
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📧 **Receber Mais Informações por Email**"):
    with st.form("form_contato"):
        st.write("Deixe seu contato para receber detalhes exclusivos!")
        nome = st.text_input("Seu nome")
        email = st.text_input("Seu melhor email")
        interesse = st.selectbox("Qual conteúdo te interessa mais?", 
                               ["Relação Pai e Filha", "Conexão Familiar", "Conteúdo Solo", "Todos"])
        
        if st.form_submit_button("📨 Receber Informações"):
            st.success(f"✅ Obrigada {nome}! Em breve você receberá novidades exclusivas!")

# --- RODAPÉ PREMIUM ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown('''
<div style="text-align: center; color: #666; padding: 20px;">
    <p>💎 <strong>Heleninha Videos VIP</strong> • Conteúdo Exclusivo • Acesso Imediato • Suporte 24/7</p>
    <p>⚠️ Este é um conteúdo para maiores de 18 anos. Todos os direitos reservados.</p>
    <p>📱 <strong>Suporte Imediato:</strong> @Helenagbysi no Telegram</p>
</div>
''', unsafe_allow_html=True)
