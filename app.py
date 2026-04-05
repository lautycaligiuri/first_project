import streamlit as st
from supabase import create_client, Client

# --- CONEXIÓN A BASE DE DATOS ---
# Buscamos las llaves en el archivo de secretos que creamos recién
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# --- INTERFAZ ---
st.set_page_config(page_title="Experimento Ético", page_icon="🚆")

st.title("🚆El Dilema del Tranvía Exponencial.")
st.write("¿Qué decisión tomarías si cada omisión duplica el problema?")

with st.form("form_encuesta"):
    st.subheader("Tu Voto")
    
    opcion = st.radio(
        "Tu acción:",
        ("Jalar la palanca (Muere 1)", "Pasar (Se duplica el riesgo)")
    )
    
    porque = st.text_area("Justificación:")
    
    boton = st.form_submit_button("Enviar Respuesta")

# --- LÓGICA DE ENVÍO ---
if boton:
    if len(porque) < 5:
        st.warning("Por favor, escribí un poco más en la justificación.")
    else:
        # Los nombres de la izquierda deben ser IGUALES a como los pusiste en Supabase
        nueva_fila = {
            "eleccion": opcion,
            "justificacion": porque
        }
        
        try:
            # Enviamos a la tabla 'respuestas_tranvia'
            supabase.table("respuestas_tranvia").insert(nueva_fila).execute()
            st.success("¡Datos guardados en la nube con éxito! 🚀")
        except Exception as e:
            st.error(f"Error al conectar: {e}")