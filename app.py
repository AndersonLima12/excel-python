import streamlit as st
import pandas as pd
import os

from utils.data_processing import filter_dataframe
from utils.charts import create_charts
from components.filters import generate_filters
from components.metrics import display_metrics

# =========================
# Configurações da página
# =========================
st.set_page_config(page_title="Painel Excel Inteligente", layout="wide")
st.title("📊 Painel Inteligente a partir de Excel")

# =========================
# Carregar CSS customizado
# =========================
STYLE_PATH = "assets/style.css"
if os.path.exists(STYLE_PATH):
    with open(STYLE_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# Pasta de uploads
# =========================
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# =========================
# Upload de arquivo
# =========================
uploaded_file = st.file_uploader("📂 Faça upload de um arquivo Excel", type=["xlsx", "xls"])

if uploaded_file:
    # Salvar arquivo
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Carregar DataFrame
    df = pd.read_excel(file_path)

    # =========================
    # Filtros Laterais
    # =========================
    st.sidebar.header("⚙️ Filtros Globais")
    filters = generate_filters(df)
    df_filtered = filter_dataframe(df, filters)

    # =========================
    # Layout principal com abas
    # =========================
    tabs = st.tabs(["📄 Dados", "📊 Métricas", "📈 Gráficos"])

    # ---- Aba de Dados ----
    with tabs[0]:
        st.subheader("📄 Visualização dos Dados Originais")
        st.dataframe(df)

    # ---- Aba de Métricas ----
    with tabs[1]:
        st.subheader("📊 Métricas")
        # Exibe os cards de métricas modernos, estilo Power BI
        display_metrics(df_filtered)

    # ---- Aba de Gráficos ----
    # ---- Aba de Gráficos ----
    with tabs[2]:
        st.subheader("📈 Gráficos Interativos")
        create_charts(df_filtered)


    st.success("✅ Painel criado com sucesso!")
