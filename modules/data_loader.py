import streamlit as st
import pandas as pd
from modules.filters_dataframe import apply_filters

def load_excel(file) -> pd.DataFrame:
    """
    Carrega um arquivo Excel enviado pelo usuário e retorna um DataFrame.
    """
    try:
        df = pd.read_excel(file)
        st.success("✅ Arquivo carregado com sucesso!")
        return df
    except Exception as e:
        st.error(f"❌ Erro ao carregar o arquivo: {e}")
        return pd.DataFrame()

def process_data(file, apply_filter: bool = True) -> pd.DataFrame:
    """
    Carrega e (opcionalmente) aplica filtros nos dados.
    """
    df = load_excel(file)

    if not df.empty and apply_filter:
        df = apply_filters(df)

    return df
