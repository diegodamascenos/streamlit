from pathlib import Path

import streamlit as st
import pandas as pd

pasta_dataset = Path (__file__).parent.parent / 'dataset'
df_vendas = pd.read_csv(pasta_dataset / 'train.csv', decimal = ',', index_col='Order Date')
df_customers = pd.read_csv(pasta_dataset / 'customers.csv', decimal = ',')
df_products = pd.read_csv(pasta_dataset / 'products.csv', decimal = ',')

st.dataframe(df_vendas)
st.dataframe(df_customers)
st.dataframe(df_products)