import streamlit as st
import pandas as pd

st.set_page_config(page_title="Visualizações | Heimdall SFN", layout="wide")

st.title("Visualizações")

@st.cache_data
def carregar_dados():
    return pd.read_csv(r"G:\Meu Drive\Heimdall\data\raw\instituicoes_financeiras_202412.csv")

df = carregar_dados()

st.subheader("Quantidade de instituições por UF")

col1, col2 = st.columns(2)

with col1:
    st.dataframe(
        df.groupby("Uf").size().reset_index(name="Quantidade"),
        hide_index=True,
        use_container_width=True,
    )

with col2:
    st.bar_chart(
        df.groupby("Uf").size().reset_index(name="Quantidade"),
        x="Uf",
        y="Quantidade",
        use_container_width=True,
    )
