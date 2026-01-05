import streamlit as st
import pandas as pd

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
st.set_page_config(
    page_title="Programa MO",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "mostrar_submenu" not in st.session_state:
    st.session_state.mostrar_submenu = False

if "opcion_activa" not in st.session_state:
    st.session_state.opcion_activa = None

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------
st.markdown("""
<style>
/* Sidebar rojo */
section[data-testid="stSidebar"] {
    background-color: #c81d11;
}

/* Desactivar hover de botones Streamlit */
.stButton > button:hover {
    background-color: white !important;
    color: black !important;
}

/* Botón blanco menú */
.menu-btn button {
    background-color: white !important;
    color: black !important;
    border-radius: 6px !important;
    border: none !important;
    font-weight: 600;
    padding: 10px 12px;
    text-align: left;
}

/* Item activo amarillo */
.menu-activo {
    background-color: #f4c430;
    color: black;
    padding: 10px 12px;
    border-radius: 6px;
    font-weight: 700;
    margin-top: 6px;
}

/* Botones generales */
.stButton > button {
    height: 38px;
    font-weight: 600;
}

/* Botón consultar */
.consultar button {
    background-color: #c81d11;
    color: white;
    border: none;
}

/* Botones acción */
.accion button {
    background-color: #c81d11;
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR - MENÚ
# --------------------------------------------------
with st.sidebar:
    st.markdown("#FFFFFF Danper")

    # Gestión Agrícola (solo muestra submenú)
    st.markdown("<div class='menu-btn'>", unsafe_allow_html=True)
    if st.button("Gestión Agrícola", use_container_width=True):
        st.session_state.mostrar_submenu = True
    st.markdown("</div>", unsafe_allow_html=True)

    # Carga de MO (un solo clic: activa + pinta + muestra)
    if st.session_state.mostrar_submenu:

        if st.session_state.opcion_activa == "carga_mo":
            st.markdown(
                "<div class='menu-activo'>Carga de MO</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div class='menu-btn'>", unsafe_allow_html=True)
            if st.button("Carga de MO", use_container_width=True):
                st.session_state.opcion_activa = "carga_mo"
            st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# CONTENIDO PRINCIPAL
# --------------------------------------------------
st.title("Programa Mano de Obra")

# --------------------------------------------------
# CONTENIDO SOLO SI CARGA MO ESTÁ ACTIVO
# --------------------------------------------------
if st.session_state.opcion_activa == "carga_mo":

    # ---------------------------
    # FILTROS
    # ---------------------------
    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

    with f2:
        st.selectbox("Unidad Agrícola", ["Compositan"])

    with f3:
        st.selectbox("Sub Unidad Agrícola", ["Sector A", "Sector B"])

    with f4:
        st.selectbox("Tipo Cultivo", ["Pimiento", "Arándano"])

    with f5:
        st.selectbox("Proceso", ["Cosecha", "Poda"])

    f6, f7, f8, f9, _ = st.columns(5)

    with f6:
        st.selectbox("Año", ["2024", "2025"])

    with f7:
        st.selectbox("Semana", list(range(1, 53)), index=22)

    with f8:
        st.selectbox("Tipo Proyección", ["Programado", "Ejecutado"])

    with f9:
        st.markdown("<div class='consultar'>", unsafe_allow_html=True)
        st.button("🔍 Consultar")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------
    # BOTONES DERECHA
    # ---------------------------
    _, _, _, b1, b2, b3 = st.columns([5,5,5,1.3,1.5,2])

    with b1:
        st.markdown("<div class='accion'>", unsafe_allow_html=True)
        st.button("📤 Exportar")
        st.markdown("</div>", unsafe_allow_html=True)

    with b2:
        st.markdown("<div class='accion'>", unsafe_allow_html=True)
        st.button("📥 Importar")
        st.markdown("</div>", unsafe_allow_html=True)

    with b3:
        st.markdown("<div class='accion'>", unsafe_allow_html=True)
        st.button("➕ Agregar actividades")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------
    # TABLA
    # ---------------------------
    st.markdown("---")
    st.subheader("Detalle Programa MO")

    df = pd.DataFrame({
        "Actividad": ["Cosecha", "Poda"],
        "Personal": [30, 15],
        "Horas": [8, 6]
    })

    st.dataframe(df, use_container_width=True)

else:
    st.info("Seleccione Gestión Agrícola para comenzar")
