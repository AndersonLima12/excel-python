# components/metrics.py
import streamlit as st

def display_metrics(df):
    """
    Mostra cards de métricas principais em estilo moderno tipo Power BI.
    """
    st.subheader("📊 Principais Métricas")

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        col1, col2, col3, col4 = st.columns(4)

        # Card 1 - Total registros
        col1.markdown(f"""
        <div class="metric-card bg-blue">
            <p>Total Registros</p>
            <h2>{len(df)}</h2>
        </div>
        """, unsafe_allow_html=True)

        # Card 2 - Média
        col2.markdown(f"""
        <div class="metric-card bg-green">
            <p>Média {numeric_cols[0]}</p>
            <h2>{round(df[numeric_cols[0]].mean(),2)}</h2>
        </div>
        """, unsafe_allow_html=True)

        # Card 3 - Máximo
        col3.markdown(f"""
        <div class="metric-card bg-orange">
            <p>Máx {numeric_cols[0]}</p>
            <h2>{df[numeric_cols[0]].max()}</h2>
        </div>
        """, unsafe_allow_html=True)

        # Card 4 - Mínimo
        col4.markdown(f"""
        <div class="metric-card bg-red">
            <p>Mín {numeric_cols[0]}</p>
            <h2>{df[numeric_cols[0]].min()}</h2>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("Nenhuma coluna numérica disponível para métricas.")