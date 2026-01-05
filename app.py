import streamlit as st
import pandas as pd

# --------------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------------
st.set_page_config(
    page_title="Carga Programa MO Semanal",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS (COLORES + PANEL IZQUIERDO)
# --------------------------------------------------
st.markdown("""
<style>
/* Ocultar menú Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Panel izquierdo rojo */
section[data-testid="stSidebar"] {
    background-color: #b11226;
}

/* Texto sidebar */
section[data-testid="stSidebar"] * {
    color: white;
    font-weight: 600;
}

/* Botones */
.stButton > button {
    height: 38px;
    border-radius: 6px;
    font-weight: 600;
}

/* Botones principales */
div[data-testid="column"] button {
    background-color: #b11226;
    color: white;
    border: none;
}

/* Tabla */
thead tr th {
    background-color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR (PANEL IZQUIERDO)
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 📋 Programa MO")
    st.markdown("---")

    st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])
    st.selectbox("Unidad Agrícola", ["Compositan"])
    st.selectbox("Cultivo", ["Pimiento", "Arándano"])
    st.selectbox("Semana", list(range(1, 53)), index=22)
    st.selectbox("Año", ["2024", "2025"])

# --------------------------------------------------
# CONTENIDO PRINCIPAL
# --------------------------------------------------
st.title("Carga Programa MO Semanal")

# ---------------------------
# FILTROS SUPERIORES (COMO IMAGEN)
# ---------------------------
f1, f2, f3, f4, f5 = st.columns(5)

with f1:
    st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

with f2:
    st.selectbox("Unidad Agrícola", ["Compositan"])

with f3:
    st.selectbox("Cultivo", ["Pimiento", "Arándano"])

with f4:
    st.selectbox("Semana", list(range(1, 53)), index=22)

with f5:
    st.selectbox("Año", ["2024", "2025"])

# ---------------------------
# BOTONES A LA DERECHA
# ---------------------------
_, _, _, _, _, b1, b2, b3, b4 = st.columns([3,3,3,3,3,1,1,1.2,1.8])

with b1:
    st.button("📤 Exportar")

with b2:
    if st.button("📥 Importar"):
        st.session_state["importar"] = True

with b3:
    st.button("💾 Guardar")

with b4:
    st.button("➕ Agregar actividades")

# ---------------------------
# MODAL / IMPORTACIÓN
# ---------------------------
if st.session_state.get("importar", False):
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
            except:
                st.error("Error al leer el archivo")

        if st.button("Cerrar"):
            st.session_state["importar"] = False

# ---------------------------
# TABLA PRINCIPAL
# ---------------------------
st.markdown("---")
st.subheader("Detalle del Programa")

data = {
    "Actividad": ["Cosecha", "Poda"],
    "Personal Programado": [25, 10],
    "Horas": [8, 6]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
