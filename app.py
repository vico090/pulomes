
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="La Gran Ruta de Airel", page_icon="🫁", layout="centered")

# Título y bienvenida
st.title("🫁 La Gran Ruta de Airel")
st.subheader("Una aventura educativa por el sistema respiratorio")

# Menú de navegación
seccion = st.sidebar.selectbox("Explora:", ["📘 Introducción", "🔬 Anatomía", "❓ Quiz"])

# Introducción
if seccion == "📘 Introducción":
    st.markdown("""
    **¡Hola! Soy Airel, una molécula de oxígeno.**
    
    Acompáñame en un viaje por el sistema respiratorio humano, desde la nariz hasta los alvéolos.
    En esta historia conocerás cómo funciona tu cuerpo mientras respiro contigo.
    """)
    st.image("airel_nariz.png", caption="Airel entrando por la nariz", use_column_width=True)

# Anatomía
elif seccion == "🔬 Anatomía":
    st.header("Etapas del Viaje de Airel")

    with st.expander("1. Vías respiratorias superiores"):
        st.markdown("""
        - **Nariz:** Filtra, humedece y calienta el aire.
        - **Cornetes nasales:** Estructuras que aumentan la superficie interna.
        - **Faringe:** Paso compartido entre aire y alimentos.
        """)

    with st.expander("2. Vías respiratorias inferiores"):
        st.markdown("""
        - **Tráquea:** Tubo reforzado con anillos cartilaginosos.
        - **Bronquios principales:** Bifurcación hacia los pulmones derecho e izquierdo.
        """)

    with st.expander("3. Pulmones"):
        st.markdown("""
        - **Pulmón derecho:** Más corto y ancho, con 3 lóbulos (superior, medio, inferior).
        - **Pulmón izquierdo:** Más estrecho y largo, con 2 lóbulos y una incisura cardiaca.
        - **Fisuras:** Oblicua (ambos pulmones), horizontal (solo derecho).
        """)

    with st.expander("4. Bronquios, bronquiolos y alvéolos"):
        st.markdown("""
        - **Bronquios secundarios y bronquiolos:** Ramificaciones cada vez más pequeñas.
        - **Alvéolos:** Pequeñas bolsas donde ocurre el intercambio gaseoso.
        """)

# Quiz interactivo
elif seccion == "❓ Quiz":
    st.header("¿Cuánto aprendiste?")

    preguntas = {
        "¿Cuántos lóbulos tiene el pulmón derecho?": ["2", "3", "4"],
        "¿Qué estructura evita que colapse la tráquea?": ["Músculo liso", "Anillos cartilaginosos", "Bronquios"],
        "¿Por qué el pulmón izquierdo es más pequeño?": [
            "Porque tiene más bronquios",
            "Por la presión arterial",
            "Por la ubicación del corazón"
        ],
    }

    respuestas_correctas = {
        "¿Cuántos lóbulos tiene el pulmón derecho?": "3",
        "¿Qué estructura evita que colapse la tráquea?": "Anillos cartilaginosos",
        "¿Por qué el pulmón izquierdo es más pequeño?": "Por la ubicación del corazón",
    }

    puntaje = 0
    for pregunta, opciones in preguntas.items():
        respuesta = st.radio(pregunta, opciones, key=pregunta)
        if respuesta == respuestas_correctas[pregunta]:
            puntaje += 1

    if st.button("Ver resultados"):
        st.success(f"¡Obtuviste {puntaje} de {len(preguntas)} respuestas correctas!")
