import streamlit as st
import pandas as pd

# ---------------- CONFIGURACIÓN GENERAL ----------------
st.set_page_config(page_title="Programa MO", layout="wide")

st.markdown("""
<style>
/* Fondo general */
.main {
    background-color: #f5f6fa;
}

/* Título */
h1 {
    font-size: 26px;
    font-weight: 600;
}

/* Labels */
label {
    font-weight: 600;
}

/* Botones */
.stButton > button {
    background-color: #b11226;
    color: white;
    border-radius: 6px;
    height: 38px;
}

/* Botón secundario */
.secondary button {
    background-color: #6c757d !important;
}

/* Tabla */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 8px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TÍTULO ----------------
st.title("Carga Programa MO Semanal")

# ---------------- FILTROS SUPERIORES ----------------
f1, f2, f3, f4, f5, f6, f7, f8 = st.columns(8)

with f1:
    sociedad = st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

with f2:
    unidad = st.selectbox("Unidad Agrícola", ["Compositan"])

with f3:
    subunidad = st.selectbox("SubUnidad", ["Compositan 1"])

with f4:
    tipo_cultivo = st.selectbox("Tipo Cultivo", ["Arándano"])

with f5:
    proceso = st.selectbox("Proceso", ["Riego", "Indirectos", "Proyecto"])

with f6:
    año = st.number_input("Año", value=2024)

with f7:
    semana = st.number_input("Semana", min_value=1, max_value=52, value=23)

with f8:
    tipo_proy = st.selectbox("Tipo Proyección", ["Proyectado"])

st.divider()

# ---------------- BOTONES DE ACCIÓN ----------------
b1, b2, b3, b4, _ = st.columns([1,1,1,2,6])

with b1:
    st.button("📤 Exportar")

with b2:
    if st.button("📥 Importar"):
        st.session_state["importar"] = True

with b3:
    st.button("💾 Guardar")

with b4:
    st.button("➕ Agregar actividades")

# ---------------- IMPORTAR EXCEL ----------------
if st.session_state.get("importar", False):
    with st.expander("IMPORTAR PROGRAMA MO", expanded=True):
        archivo = st.file_uploader(
            "Seleccionar archivo Excel",
            type=["xlsx"]
        )

        if archivo:
            df = pd.read_excel(archivo)
            st.session_state["df"] = df
            st.success("Archivo cargado correctamente")

        if st.button("Cerrar"):
            st.session_state["importar"] = False

st.divider()

# ---------------- TABLA CENTRAL ----------------
if "df" in st.session_state:
    st.dataframe(st.session_state["df"], use_container_width=True)
else:
    st.info("No hay información cargada")
