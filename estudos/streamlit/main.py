import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Heimdall SFN"
)

st.markdown("""
# Boas vindas!

## Heimdall | SFN

Espero que você curta a experiência da nossa solução! (:
         
""")



df = pd.read_csv(r"G:\Meu Drive\Heimdall\data\raw\instituicoes_financeiras_202412.csv")

exp1 = st.expander("Dados brutos")

exp1.dataframe(df, hide_index = True)

exp2 = st.expander("Gráficos")

tab_data, tab_history, tb_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])

with tab_data:
    
    st.date_input("Data de referência")
    
    st.dataframe(df.groupby("Uf").size().reset_index(name = "Quantidade"), hide_index = True)
    
with tab_history:
    st.bar_chart(df.groupby("Uf").size().reset_index(name = "Quantidade"), x = "Uf", y = "Quantidade")
    
    
