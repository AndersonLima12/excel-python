import streamlit as st
import pandas as pd

def generate_filters(df):
    """
    Cria filtros dinâmicos na sidebar e retorna um dicionário com os valores selecionados
    """
    st.sidebar.header("Filtros")
    filters = {}
    
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            min_val = float(df[col].min())
            max_val = float(df[col].max())
            selected_range = st.sidebar.slider(
                f"{col}", 
                min_val, 
                max_val, 
                (min_val, max_val),
                key=f"{col}_slider"
            )
            filters[col] = selected_range

        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            min_date = df[col].min()
            max_date = df[col].max()
            selected_date = st.sidebar.date_input(
                f"{col}", 
                [min_date, max_date],
                key=f"{col}_date"
            )
            filters[col] = selected_date

        else:
            unique_values = df[col].dropna().unique().tolist()
            selected_values = st.sidebar.multiselect(
                f"{col}", 
                unique_values, 
                default=unique_values,
                key=f"{col}_multiselect"
            )
            filters[col] = selected_values
    
    return filters
