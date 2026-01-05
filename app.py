import streamlit as st
import pandas as pd

# ---------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------
st.set_page_config(
    page_title="Carga Programa MO Semanal",
    layout="wide"
)

# ---------------------------
# ESTILOS
# ---------------------------
st.markdown("""
<style>
.stButton > button {
    margin-top: 22px;
    height: 38px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# TÍTULO
# ---------------------------
st.title("Carga Programa MO Semanal")

# ---------------------------
# FILTROS SUPERIORES
# ---------------------------
f1, f2, f3, f4 = st.columns(4)

with f1:
    st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

with f2:
    st.selectbox("Unidad Agrícola", ["Compositan"])

with f3:
    st.selectbox("Semana", list(range(1, 53)), index=22)

with f4:
    st.text_input("Año", value="2025")

# ---------------------------
# BOTONES ALINEADOS A LA DERECHA
# ---------------------------
_, _, _, _, _, b1, b2, b3, b4 = st.columns([3,3,3,3,3,1,1,1.2,1.8])

with b1:
    st.button("📤 Exportar")

with b2:
    if st.button("📥 Importar"):
        st.session_state["mostrar_modal"] = True

with b3:
    st.button("💾 Guardar")

with b4:
    st.button("➕ Agregar actividades")

# ---------------------------
# MODAL DE IMPORTACIÓN
# ---------------------------
if st.session_state.get("mostrar_modal", False):
    with st.expander("📥 Importar Programa MO", expanded=True):
        archivo = st.file_uploader(
            "Selecciona la plantilla Excel",
            type=["xlsx"]
        )

        if archivo:
            try:
                df = pd.read_excel(archivo)
                st.success("Archivo cargado correctamente")
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error("Error al leer el archivo Excel")

        if st.button("Cerrar"):
            st.session_state["mostrar_modal"] = False

# ---------------------------
# TABLA PRINCIPAL (SIMULADA)
# ---------------------------
st.markdown("---")

st.subheader("Detalle del Programa")

data = {
    "Actividad": ["Cosecha", "Poda"],
    "Personal": [25, 10],
    "Horas": [8, 6]
}

df_main = pd.DataFrame(data)

st.dataframe(df_main, use_container_width=True)
