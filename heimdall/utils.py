import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data # Cacheia os dados para evitar recarregamentos desnecessários
def carregar_dados_sfn():
    """Carrega base de dados do SFN na visão de instituições individuais

    Returns:
        pd.DataFrame: Tabela com informações de instituições financeiras do SFN
    """
    relatorio_sfn = pd.read_csv(r"G:\Meu Drive\Heimdall\data\processed\resumo\instituicoes_individuais.csv")
    relatorio_sfn['Data'] = pd.to_datetime(relatorio_sfn['Data'], format='%m/%Y').dt.to_period('M')
    
    # Transformação do Ativo Total em Numérica
    relatorio_sfn['Ativo Total'] = pd.to_numeric(
        relatorio_sfn['Ativo Total']
        .astype(str)
        .str.replace(r'\.(?=\d{3}(?:\D|$))', '', regex=True),
        errors='coerce'
    )
    
    # Transformação do Ativo Total em Numérica
    relatorio_sfn['Carteira de Crédito'] = pd.to_numeric(
        relatorio_sfn['Carteira de Crédito']
        .astype(str)
        .str.replace(r'\.(?=\d{3}(?:\D|$))', '', regex=True),
        errors='coerce'
    )
    
    # Transformação do Ativo Total em Numérica
    relatorio_sfn['Títulos e Valores Mobiliários'] = pd.to_numeric(
        relatorio_sfn['Títulos e Valores Mobiliários']
        .astype(str)
        .str.replace(r'\.(?=\d{3}(?:\D|$))', '', regex=True),
        errors='coerce'
    )
    
    # de-para de Tipo de Controle (TC)
    relatorio_sfn['TC'] = relatorio_sfn['TC'].replace(
        {
            1.0: 'Público',
            2.0: 'Privado Nacional',
            3.0: 'Privado com Controle Estrangeiro',
            np.nan: 'Não Informado'
        }
    )
    
    # de-para de Tipo de Instituição (TI)
    relatorio_sfn['TI'] = relatorio_sfn['TI'].replace(
        {
            1.0: 'Banco do Brasil - Banco Múltiplo',
            2.0: 'Banco Comercial',
            3.0: 'Banco Comercial Cooperativo',
            4.0: 'BNDES',
            5.0: 'Banco de Desenvolvimento',
            6.0: 'Caixa Econômica Federal',
            7.0: 'Caixa Econômica Estadual',
            8.0: 'Banco Múltiplo',
            9.0: 'Cooperativa de Crédito',
            10.0: 'Sociedade de Crédito ao Microempreendedor',
            11.0: 'Banco Múltiplo Cooperativo',
            13.0: 'Banco de Investimento',
            14.0: 'Sociedade de Crédito, Financiamento e Investimento',
            15.0: 'Sociedade Corretora de TVM',
            16.0: 'Sociedade Distribuidora de TVM',
            19.0: 'Sociedade de Arrendamento Mercantil',
            21.0: 'Sociedade Corretora de Câmbio',
            25.0: 'Associação de Poupança e Empréstimo',
            28.0: 'Banco Comercial Estrangeiro - Filial no país',
            29.0: 'Companhia Hipotecária',
            30.0: 'Agência de Fomento',
            31.0: 'Sociedade de Crédito Imobiliário - Repassadora',
            39.0: 'Banco de Câmbio',
            41.0: 'Instituições de Pagamento',
            43.0: 'Sociedades de Crédito Direto',
            44.0: 'Sociedades de Empréstimo entre Pessoas',
            np.nan: 'Não Informado'
        }
    )
    
    return relatorio_sfn
