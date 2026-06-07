import streamlit as st
import pandas as pd

from utils import carregar_dados_sfn

# %%
print("oi")


# %%

relatorio_sfn = carregar_dados_sfn()

def formata_conglomerado(conglomerado : pd.DataFrame, col) -> str:
    total_conglomerado = conglomerado.loc[
        conglomerado['Data'] == conglomerado['Data'].max(),
        col
    ].sum()

    if total_conglomerado == 0:
        valor_exibicao = "Não Informado"
    else:
        valor_exibicao = f"R$ {total_conglomerado:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    return valor_exibicao

def formata_delta_conglomerado(conglomerado : pd.DataFrame, col) -> str:
    
    lista_datas = sorted(conglomerado['Data'].unique())
    
    valor_atual = conglomerado.loc[
        conglomerado['Data'] == lista_datas[-1],
        col
    ].sum()

    valor_anterior = conglomerado.loc[
        conglomerado['Data'] == lista_datas[-2],
        col
    ].sum()
    
    if valor_anterior == 0:
        delta_exibicao = 'Não Informado'        
    else:
        delta_valor = valor_atual - valor_anterior
        delta_formatado = f"R$ {delta_valor:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        delta_exibicao = f"vs quad. ant.: {delta_formatado} ({((valor_atual - valor_anterior) / valor_anterior * 100):.2f}%)"

    return delta_exibicao

data_referencia = relatorio_sfn['Data'].max().strftime('%m/%Y')
st.title(f"Resumo por Conglomerado Prudencial - {data_referencia}")

# Filtros para seleção de Conglomerado Prudencial, Tipo de Controle e Tipo de Instituição
col_conglomerado, col_tc, col_ti = st.columns(3)

with col_conglomerado:
    filtro_conglomerado = sorted(relatorio_sfn['Conglomerado Prudencial'].dropna().unique().tolist())
    conglomerado_selecionado = st.selectbox('Selecionar Conglomerado', options=filtro_conglomerado) # Filtre de instituição a ser analisada
    relatorio_sfn_visao_conglomerado = relatorio_sfn[relatorio_sfn['Conglomerado Prudencial'] == conglomerado_selecionado]

    
with col_tc:
    st.metric(
        label = "Tipo de Controle", 
        value = relatorio_sfn_visao_conglomerado[relatorio_sfn_visao_conglomerado['Data'] == relatorio_sfn_visao_conglomerado['Data'].max()]['TC'].values[0],
    )
    
with col_ti:
    st.metric(
        label = "Tipo de Instituição", 
        value = relatorio_sfn_visao_conglomerado[relatorio_sfn_visao_conglomerado['Data'] == relatorio_sfn_visao_conglomerado['Data'].max()]['TI'].values[0]
    )

col_ativo, col_carteira, col_tvm = st.columns(3)


with col_ativo:
    st.metric(
        label = "Ativo Total", 
        value = formata_conglomerado(relatorio_sfn_visao_conglomerado, 'Ativo Total'),
        delta = formata_delta_conglomerado(relatorio_sfn_visao_conglomerado, 'Ativo Total')
    )
    
with col_carteira:
    st.metric(
        label = "Carteira de Crédito", 
        value = formata_conglomerado(relatorio_sfn_visao_conglomerado, 'Carteira de Crédito'),
        delta = formata_delta_conglomerado(relatorio_sfn_visao_conglomerado, 'Carteira de Crédito')
    )
    
with col_tvm:
    st.metric(
        label = "Títulos e Valores Mobiliários", 
        value = formata_conglomerado(relatorio_sfn_visao_conglomerado, 'Títulos e Valores Mobiliários'),
        delta = formata_delta_conglomerado(relatorio_sfn_visao_conglomerado, 'Títulos e Valores Mobiliários')
    )


st.divider()

st.title("Resumo por Instituição Independente")

filtro_instituicao = sorted(relatorio_sfn_visao_conglomerado['Instituição'].dropna().unique().tolist())
instituicao_selecionada = st.selectbox('Selecionar Instituição', options=filtro_instituicao) # Filtre de instituição a ser analisada
relatorio_sfn_visao_instituicao = relatorio_sfn_visao_conglomerado[relatorio_sfn_visao_conglomerado['Instituição'] == instituicao_selecionada]








