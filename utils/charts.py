import plotly.express as px
import streamlit as st

def create_charts(df):
    """
    Cria gráficos automaticamente e organiza em duas colunas
    """
    st.subheader("📈 Gráficos Interativos")
    col1, col2 = st.columns(2)

    # Numéricos -> histogramas
    for i, col in enumerate(df.select_dtypes(include=['number']).columns):
        if df[col].notna().any():
            fig = px.histogram(df, x=col, nbins=30, title=f"Distribuição de {col}")
            (col1 if i % 2 == 0 else col2).plotly_chart(fig, use_container_width=True)

    # Categóricos -> barras
    for i, col in enumerate(df.select_dtypes(include=['object']).columns):
        if df[col].notna().any():
            counts = df[col].value_counts().reset_index()
            counts.columns = [col, 'Quantidade']
            fig = px.bar(counts, x=col, y='Quantidade', title=f"{col} - Contagem")
            (col1 if i % 2 == 0 else col2).plotly_chart(fig, use_container_width=True)

    # Datas -> séries temporais
    for i, col in enumerate(df.select_dtypes(include=['datetime']).columns):
        if df[col].notna().any():
            df_time = df.groupby(col).size().reset_index(name='Contagem')
            fig = px.line(df_time, x=col, y='Contagem', title=f"Evolução de {col}")
            (col1 if i % 2 == 0 else col2).plotly_chart(fig, use_container_width=True)
