import pandas as pd

def filter_dataframe(df, filters):
    """
    Filtra o DataFrame com base nos filtros fornecidos.
    filters: dict {coluna: valor/intervalo/seleção}
    """
    filtro_df = df.copy()
    
    for col, val in filters.items():
        if pd.api.types.is_numeric_dtype(df[col]):
            filtro_df = filtro_df[(filtro_df[col] >= val[0]) & (filtro_df[col] <= val[1])]
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            filtro_df = filtro_df[(filtro_df[col] >= pd.to_datetime(val[0])) & (filtro_df[col] <= pd.to_datetime(val[1]))]
        else:
            filtro_df = filtro_df[filtro_df[col].isin(val)]
    
    return filtro_df
