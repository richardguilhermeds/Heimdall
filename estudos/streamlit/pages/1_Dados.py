import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dados | Heimdall SFN", layout="wide")

st.title("Dados brutos")

@st.cache_data
def carregar_dados():
    return pd.read_csv(r"G:\Meu Drive\Heimdall\data\raw\instituicoes_financeiras_202412.csv")

df = carregar_dados()

st.dataframe(df, hide_index=True, use_container_width=True)
