import streamlit as st

# Configuración de la página
st.set_page_config(page_title="La Gran Ruta de Airel", page_icon="🫁", layout="centered")

# Título principal
st.title("🫁 La Gran Ruta de Airel")
st.subheader("Una aventura educativa por el sistema respiratorio")

# Menú de navegación
seccion = st.sidebar.selectbox("Explora:", ["📘 Introducción", "🔬 Anatomía del pulmón", "❓ Quiz de Anatomía del Pulmón"])

# Introducción
if seccion == "📘 Introducción":
    st.markdown("""
    **¡Hola! Soy Airel, una molécula de oxígeno.**

    Acompáñame en un viaje por el sistema respiratorio humano. Hoy exploraremos a fondo los **pulmones**, nuestros protagonistas.
    """)
    st.image("airel_nariz.png", caption="Airel entrando por la nariz", use_column_width=True)

# Anatomía del pulmón
elif seccion == "🔬 Anatomía del pulmón":
    st.markdown("""
    Los pulmones son órganos vitales del sistema respiratorio. Se encargan del **intercambio de gases**, tomando oxígeno del aire y eliminando dióxido de carbono.

    ### Principales estructuras:
    - **Tráquea**: conducto que lleva el aire hacia los pulmones.
    - **Bronquios**: se ramifican desde la tráquea hacia cada pulmón.
    - **Bronquiolos**: subdivisiones de los bronquios dentro del pulmón.
    - **Alvéolos**: pequeños sacos donde ocurre el intercambio gaseoso.
    - **Pleura**: membrana que recubre y protege a los pulmones.

    Los pulmones tienen una estructura asimétrica:
    - El **pulmón derecho** tiene tres lóbulos.
    - El **pulmón izquierdo** tiene dos lóbulos y una escotadura para el corazón.
    """)

# Quiz
elif seccion == "❓ Quiz de Anatomía del Pulmón":
    st.markdown("## ❓ Quiz: Anatomía del Pulmón")
    st.write("Responde las siguientes preguntas para evaluar tus conocimientos.")

    preguntas = [
        {
            "pregunta": "1. ¿Cuál es la función principal de los pulmones?",
            "opciones": ["Filtrar sangre", "Intercambio de gases", "Producir hormonas", "Regular la temperatura corporal"],
            "respuesta": "Intercambio de gases"
        },
        {
            "pregunta": "2. ¿Cómo se llaman las pequeñas estructuras donde ocurre el intercambio de oxígeno y dióxido de carbono?",
            "opciones": ["Bronquios", "Alvéolos", "Bronquiolos", "Tráquea"],
            "respuesta": "Alvéolos"
        },
        {
            "pregunta": "3. ¿Cuántos lóbulos tiene el pulmón derecho?",
            "opciones": ["1", "2", "3", "4"],
            "respuesta": "3"
        },
        {
            "pregunta": "4. ¿Qué estructura conecta la nariz y la boca con los pulmones?",
            "opciones": ["Esófago", "Tráquea", "Bronquiolos", "Diafragma"],
            "respuesta": "Tráquea"
        },
        {
            "pregunta": "5. ¿Qué membrana recubre a los pulmones y permite su movimiento sin fricción?",
            "opciones": ["Diafragma", "Pleura", "Pericardio", "Peritoneo"],
            "respuesta": "Pleura"
        },
        {
            "pregunta": "6. ¿Cuál de estos órganos NO forma parte del sistema respiratorio?",
            "opciones": ["Laringe", "Tráquea", "Esófago", "Bronquios"],
            "respuesta": "Esófago"
        },
        {
            "pregunta": "7. ¿Cuál es el órgano muscular que ayuda a los pulmones a expandirse y contraerse?",
            "opciones": ["Corazón", "Diafragma", "Hígado", "Bazo"],
            "respuesta": "Diafragma"
        },
        {
            "pregunta": "8. ¿Qué pulmón es más pequeño debido a la posición del corazón?",
            "opciones": ["Derecho", "Izquierdo", "Ambos son iguales", "Depende del individuo"],
            "respuesta": "Izquierdo"
        },
    ]

    puntaje = 0

    for idx, q in enumerate(preguntas):
        st.write(q["pregunta"])
        respuesta_usuario = st.radio("", q["opciones"], key=idx)
        if respuesta_usuario == q["respuesta"]:
            puntaje += 1

    if st.button("Calcular resultados"):
        st.success(f"Obtuviste {puntaje} de {len(preguntas)} respuestas correctas.")
        if puntaje == 8:
            st.balloons()
            st.info("¡Excelente! Eres un experto en anatomía del pulmón.")
        elif puntaje >= 5:
            st.info("¡Muy bien! Conoces bastante sobre el tema.")
        else:
            st.warning("Sigue estudiando, puedes mejorar.")
