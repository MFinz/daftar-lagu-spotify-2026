import streamlit as st
import pandas as pd
import json

st.title("Lagu Favorit Spotify Malfin 2026")

# Buka JSON pakai modul bawaan Python
with open('laguSuka.json','r',encoding='utf-8') as f:
    data_spotify = json.load(f)

df = pd.json_normalize(data_spotify['tracks'])

# Artis dan Lagunya
st.subheader("Daftar Lagu")
df.sort_values(by='artist', inplace=True)
df.rename(columns={'artist':'Nama Artis','track':'Judul Lagu'}, inplace=True)
df.drop(columns=['album','uri'], inplace=True, errors='ignore')

df = df.reset_index(drop=True) 
df.index.name = "No"
df.index = df.index + 1 
st.dataframe(df)

# Jumlah Para Artis
st.subheader("Daftar Artis")
df2 = pd.json_normalize(data_spotify['tracks'])
df2.sort_values(by='artist', inplace=True)

df2.rename(columns={'artist':'Nama Artis'}, inplace=True)
df2['Jumlah Lagu'] = df2['Nama Artis'].map(df2['Nama Artis'].value_counts())

df2.drop(columns=['album','track','uri'], inplace=True, errors='ignore')
df2.drop_duplicates(subset=['Nama Artis'], inplace=True)

st.dataframe(df2, hide_index=True)
