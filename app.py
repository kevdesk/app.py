import streamlit as st
import pandas as pd

st.set_page_config(page_title="Carga Programa MO Semanal", layout="wide")

# =========================
# ESTILOS GENERALES
# =========================
st.markdown("""
<style>
/* BOTONES GENERALES */
.stButton>button {
    border-radius: 6px;
    height: 42px;
    font-weight: 600;
}

/* EXPORTAR */
.btn-exportar button {
    background-color: #6c757d;
    color: white;
}

/* IMPORTAR */
.btn-importar button {
    background-color: #198754;
    color: white;
}

/* AGREGAR */
.btn-agregar button {
    background-color: #0d6efd;
    color: white;
}

/* BOTON CONSULTAR */
.btn-consultar button {
    background-color: #ffc107;
    color: black;
    font-weight: 700;
}

/* INPUTS */
div[data-baseweb="select"] > div {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "mostrar_importar" not in st.session_state:
    st.session_state.mostrar_importar = False

# =========================
# TITULO
# =========================
st.title("Carga Programa MO Semanal")

# =========================
# FILTROS + BOTONES
# =========================
st.markdown("### Filtros")

# fila principal
f1, f2, f3, f4, f5, f6, f7, f8, espacio, b1, b2, b3 = st.columns(
    [1.2,1.5,1.5,1.5,1.3,1,1,1.2,2,1,1,1.5]
)

with f1:
    sociedad = st.selectbox("Sociedad", ["DANPER TRUJILLO SAC"])

with f2:
    unidad = st.selectbox("Unidad Agrícola", ["Compositan"])

with f3:
    subunidad = st.selectbox("Sub Unidad Agrícola", ["Todas"])

with f4:
    cultivo = st.selectbox("Tipo Cultivo", ["Espárrago", "Palta", "Arándano"])

with f5:
    proceso = st.selectbox("Proceso", ["Cosecha", "Campo"])

with f6:
    anio = st.selectbox("Año", [2024, 2025])

with f7:
    semana = st.selectbox("Semana", list(range(1, 53)))

with f8:
    tipo = st.selectbox("Tipo Proyección", ["Semanal", "Mensual"])

# =========================
# BOTON CONSULTAR
# =========================
st.markdown("")
c1, _, _ = st.columns([1,8,3])
with c1:
    st.markdown('<div class="btn-consultar">', unsafe_allow_html=True)
    consultar = st.button("🔍 Consultar")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# BOTONES DERECHA
# =========================
with b1:
    st.markdown('<div class="btn-exportar">', unsafe_allow_html=True)
    st.button("📤 Exportar")
    st.markdown('</div>', unsafe_allow_html=True)

with b2:
    st.markdown('<div class="btn-importar">', unsafe_allow_html=True)
    if st.button("📥 Importar"):
        st.session_state.mostrar_importar = True
    st.markdown('</div>', unsafe_allow_html=True)

with b3:
    st.markdown('<div class="btn-agregar">', unsafe_allow_html=True)
    st.button("➕ Agregar actividades")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MODAL IMPORTAR
# =========================
if st.session_state.mostrar_importar:
    with st.modal("Importar Programa MO"):
        archivo = st.file_uploader(
            "Seleccione la plantilla Excel",
            type=["xlsx"]
        )

        if archivo:
            df = pd.read_excel(archivo)
            st.success("Archivo cargado correctamente")
            st.dataframe(df, use_container_width=True)

            if st.button("Confirmar Importación"):
                st.success("Programa importado con éxito")
                st.session_state.mostrar_importar = False

        if st.button("Cancelar"):
            st.session_state.mostrar_importar = False

# =========================
# RESULTADO CONSULTA
# =========================
if consultar:
    st.info("Consulta ejecutada con los filtros seleccionados")
