
import streamlit as st
import streamlit.components.v1 as components

# Título do app
st.set_page_config(page_title="Academia Social Media", layout="wide")

# Carregar o conteúdo HTML
with open("Site_corrigido.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Exibir no Streamlit
components.html(html_content, height=1000, scrolling=True)
