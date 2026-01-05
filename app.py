import streamlit as st
import pandas as pd

st.set_page_config(page_title="Programa MO", layout="wide")

st.title("Carga Programa MO Semanal")

col1, col2, col3 = st.columns(3)

with col1:
    sociedad = st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

with col2:
    unidad = st.selectbox("Unidad Agrícola", ["Compositan"])

with col3:
    semana = st.number_input("Semana", min_value=1, max_value=52, value=23)

st.divider()

if st.button("📥 Importar"):
    with st.modal("Importar Programa MO"):
        archivo = st.file_uploader("Subir archivo Excel", type=["xlsx"])

        if archivo:
            df = pd.read_excel(archivo)
            st.success("Archivo cargado correctamente")
            st.dataframe(df, use_container_width=True)
