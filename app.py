import streamlit as st
import os

# --- 1. CONFIGURAÇÃO DE ESTILO VIP ---
st.set_page_config(page_title="Heleninha videos - Exclusive", layout="wide", page_icon="🔥")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;700&display=swap');
    .stApp { background: #0a0a0a; color: #ffffff; font-family: 'Inter', sans-serif; }
    .vip-header {
        background: linear-gradient(145deg, #1a1a1a, #000000);
        padding: 50px; border-bottom: 2px solid #d4af37; text-align: center; border-radius: 0 0 50px 50px; margin-bottom: 40px;
    }
    .gold-title { font-family: 'Playfair Display', serif; color: #d4af37; font-size: 4rem; text-transform: uppercase; letter-spacing: 3px; }
    .gallery-card { background: #161616; border: 1px solid #333; border-radius: 15px; padding: 15px; text-align: center; transition: 0.3s; }
    .gallery-card:hover { border-color: #d4af37; transform: scale(1.02); }
    .caption-style { color: #d4af37; font-weight: bold; margin-top: 10px; font-size: 1.1rem; }
    .detail-section { background: rgba(255,255,255,0.03); padding: 30px; border-radius: 20px; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNÇÃO DE CHECKOUT ATUALIZADA (R$ 20) ---
@st.dialog("🔐 FINALIZAR PEDIDO - HELENINHA VIDEOS")
def checkout_final(item, valor):
    st.write(f"### Conteúdo: {item}")
    st.write(f"## Valor Promocional: **R$ {valor}**")
    st.divider()
    
    st.write("💎 **PAGAMENTO VIA PIX:**")
    st.info("Copie a chave abaixo e cole no seu banco:")
    st.code("mariahelenadossantos339@gmail.com", language="text")
    
    st.markdown("---")
    st.write("🚀 **COMO RECEBER:**")
    st.write("Após confirmar o PIX de R$ 20,00, clique no botão abaixo para me enviar o comprovante no Telegram:")
    
    st.link_button("✈️ ENVIAR COMPROVANTE (@Helenagbysi)", "https://t.me/Helenagbysi")
    st.caption("Atendimento rápido para liberação do acesso.")

# --- 3. HEADER PRINCIPAL ---
st.markdown('<div class="vip-header"><h1 class="gold-title">Heleninha videos</h1><p style="color:#d4af37;">O melhor conteúdo exclusivo em alta definição</p></div>', unsafe_allow_html=True)

# --- 4. GALERIA DE PRODUTOS ---
fotos_venda = [
    {"arq": "photo_5174912881735175080_y.jpg", "legenda": "📸 Fotos e vídeos com meu pai", "id": "btn_pai", "preco": "20,00"},
    {"arq": "photo_5174912881735175079_y.jpg", "legenda": "📸 Fotos e vídeos com minha mãe", "id": "btn_mae", "preco": "20,00"},
    {"arq": "photo_5174912881735175078_y.jpg", "legenda": "📸 Fotos e vídeos sozinha", "id": "btn_sozinha", "preco": "20,00"}
]

col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

for i, item in enumerate(fotos_venda):
    with colunas[i]:
        st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
        if os.path.exists(item["arq"]):
            st.image(item["arq"], use_container_width=True)
        else:
            st.warning(f"Imagem {item['id']} não encontrada.")
        
        st.markdown(f'<p class="caption-style">{item["legenda"]}</p>', unsafe_allow_html=True)
        st.write(f"🔥 **Apenas R$ {item['preco']}**")
        
        if st.button(f"LIBERAR AGORA", key=item["id"], use_container_width=True):
            checkout_final(item["legenda"], item["preco"])
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. DETALHES ADICIONAIS (FAQ E TERMOS) ---
st.markdown('<div class="detail-section">', unsafe_allow_html=True)
st.subheader("📌 Informações Importantes")

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    **Dúvidas Frequentes:**
    * **Como recebo o conteúdo?** Imediatamente após o envio do comprovante no Telegram.
    * **O conteúdo é vitalício?** Sim, uma vez adquirido, o acesso é seu para sempre.
    * **Quais as formas de pagamento?** Atualmente aceitamos PIX para maior agilidade.
    """)

with col_b:
    st.markdown("""
    **Termos de Uso:**
    * 🔞 Proibido para menores de 18 anos.
    * 🚫 É estritamente proibido o compartilhamento ou revenda deste material.
    * 🔒 Sua privacidade é nossa prioridade total.
    """)
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. RODAPÉ ---
st.divider()
st.markdown(f"""
    <div style='text-align: center; color: #555;'>
        <p>© 2026 Heleninha videos - Todos os direitos reservados</p>
        <p>Suporte: @Helenagbysi | mariahelenadossantos339@gmail.com</p>
    </div>
""", unsafe_allow_html=True)
