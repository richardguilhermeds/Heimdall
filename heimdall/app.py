import streamlit as st

st.set_page_config(
    page_title="Heimdall | O Observador do Sistema Financeiro Nacional",
    page_icon="📯",
    layout = "wide"
)


pages = st.navigation([
    st.Page("pages/01_Resumo.py", title="Resumo", icon="📊"),
    st.Page("pages/02_Metricas_do_SFN.py", title="Informações Adicionais", icon="📉"),
])

pages.run()