import streamlit as st
import pandas as pd
import altair as alt

from utils import carregar_dados_sfn


relatorio_sfn = carregar_dados_sfn()

# Instituição filter
if 'Instituição' in relatorio_sfn.columns:
    instituicoes = relatorio_sfn['Instituição'].dropna().unique().tolist()
    selecionada = st.selectbox('Selecionar Instituição', options=instituicoes)
    df_filtrado = relatorio_sfn[relatorio_sfn['Instituição'] == selecionada]
else:
    df_filtrado = relatorio_sfn.copy()

if not df_filtrado.empty and 'Data' in df_filtrado.columns:
    df_temp = df_filtrado.copy()
    df_temp['Data'] = pd.to_datetime(df_temp['Data'], errors='coerce')
    if df_temp['Data'].notna().any():
        latest_date = df_temp['Data'].max()
        latest_rows = df_temp[df_temp['Data'] == latest_date]

        uf_col = next((c for c in ['UF', 'Unidade da Federação', 'Estado'] if c in df_temp.columns), None)
        agencias_col = next((c for c in ['Número de Agências', 'Número de Agencias', 'Num_agencias', 'num_agencias', 'agencias'] if c in df_temp.columns), None)

        uf_value = 'N/A'
        if uf_col is not None:
            uf_values = latest_rows[uf_col].dropna().unique().tolist()
            uf_value = ', '.join(map(str, uf_values)) if uf_values else 'N/A'

        agencias_value = 'N/A'
        delta_value = 'N/A'
        percent_value = 'N/A'
        if agencias_col is not None:
            df_agencias = df_temp[['Data', agencias_col]].copy()
            df_agencias[agencias_col] = pd.to_numeric(df_agencias[agencias_col], errors='coerce')
            df_agencias = df_agencias.dropna(subset=[agencias_col])
            if not df_agencias.empty:
                agencias_series = (df_agencias.groupby('Data')[agencias_col]
                                .sum()
                                .sort_index())
                if latest_date in agencias_series.index:
                    latest_sum = agencias_series.loc[latest_date]
                    if pd.notna(latest_sum):
                        agencias_value = int(latest_sum) if float(latest_sum).is_integer() else latest_sum
                    if len(agencias_series) >= 2:
                        previous_date = agencias_series.index[agencias_series.index < latest_date].max()
                        if pd.notna(previous_date):
                            previous_sum = agencias_series.loc[previous_date]
                            if pd.notna(previous_sum):
                                delta_calc = latest_sum - previous_sum
                                if float(delta_calc).is_integer():
                                    delta_value = f"{int(delta_calc):+}"
                                else:
                                    delta_value = f"{delta_calc:+.2f}"
                                if previous_sum != 0:
                                    percent_calc = delta_calc / previous_sum * 100
                                    percent_value = f"{percent_calc:+.2f}%"
        
        col1, col2 = st.columns(2)
        col1.metric('UF', uf_value)
        if delta_value != 'N/A':
            col2.metric('Número de Agências', agencias_value, delta=delta_value, delta_color='normal')
        else:
            col2.metric('Número de Agências', agencias_value)

        if percent_value != 'N/A':
            color = 'green' if percent_value.startswith('+') else 'red'
            st.markdown(
                f"<div style='font-size: 1.05rem; margin-top: 0.5rem;'>"
                f"<strong>Variação percentual de Agências:</strong> <span style='color: {color};'>{percent_value}</span>"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.info('Não foi possível calcular a variação percentual. Verifique os dados de "Número de Agências".')

        if agencias_col is not None:
            series = (df_temp.groupby('Data')[agencias_col]
                      .sum()
                      .sort_index())
            st.line_chart(series)
        else:
            st.info('Não foi possível criar o gráfico: verifique se as colunas "Data" e "Número de Agências" existem.')
    else:
        st.info('Não foi possível determinar a data mais recente. Verifique a coluna "Data".')
else:
    st.info('Não foi possível criar o gráfico: verifique se as colunas "Data" e "Número de Agências" existem.')

