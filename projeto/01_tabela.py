from pathlib import Path

import streamlit as st # importando biblioteca streamlit
import pandas as pd # importando biblioteca pandas

pasta_dataset = Path(__file__).parent.parent / 'dataset' # Declarando variável do caminho da pasta onde estão armazenados os datasets
df_vendas = pd.read_csv(pasta_dataset / 'train.csv', decimal=',', index_col='Order Date') # Importando o DataFrame através da variável caminho

colunas = list(df_vendas.columns) # Transformando as colunas em listas
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas: ', colunas, colunas) # Criando seleção de itens na side bar do webapp

coluna1, coluna2 = st.sidebar.columns(2)
coluna_filtro = coluna1.selectbox('Coluna:', [c for c in colunas if c not in ['Row ID', 'Postal Code',]])
coluna_valor = coluna2.selectbox('Valor:', list(df_vendas[coluna_filtro].unique()))

status_filtrar = coluna1.button('Filtrar')
status_limpar = coluna2.button('Limpar')

if status_filtrar:
    st.dataframe(df_vendas.loc[df_vendas[coluna_filtro] == coluna_valor, colunas_selecionadas], height=800)
elif status_limpar:
    st.dataframe(df_vendas[colunas_selecionadas], height=800) # Visualizando o Data Frame 
else:
    st.dataframe(df_vendas[colunas_selecionadas], height=800)