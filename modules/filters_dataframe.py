import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica filtros interativos ao DataFrame usando streamlit-extras.
    """
    if df is None or df.empty:
        st.warning("Nenhum dado disponível para aplicar filtros.")
        return df

    st.subheader("🔎 Filtros dos Dados")
    filtered_df = dataframe_explorer(df, case=False)
    return filtered_df
