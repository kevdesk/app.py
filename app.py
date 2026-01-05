import streamlit as st
import pandas as pd

st.set_page_config(page_title="Programa MO", layout="wide")

st.title("Carga Programa MO Semanal")

# -----------------------------
# FILTROS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    sociedad = st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

with col2:
    unidad = st.selectbox("Unidad Agrícola", ["Compositan"])

with col3:
    semana = st.number_input("Semana", min_value=1, max_value=52, value=23)

st.divider()

# -----------------------------
# IMPORTAR (SIN MODAL)
# -----------------------------
if st.button("📥 Importar Programa MO"):
    st.session_state["mostrar_importar"] = True

if st.session_state.get("mostrar_importar", False):
    with st.expander("IMPORTAR PROGRAMA MO", expanded=True):

        archivo = st.file_uploader(
            "Seleccionar archivo Excel",
            type=["xlsx"]
        )

        if archivo:
            try:
                df = pd.read_excel(archivo)
                st.success("Archivo cargado correctamente")
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error("Error al leer el archivo Excel")

        colA, colB = st.columns(2)
        with colA:
            if st.button("Importar"):
                st.success("Importación simulada")

        with colB:
            if st.button("Cerrar"):
                st.session_state["mostrar_importar"] = False
