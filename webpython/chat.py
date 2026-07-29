# webpython/chat.py
import reflex as rx
import os
from dotenv import load_dotenv
from webpython.cv_data import CV_CONTEXT
from groq import Groq
# Cargar las variables del archivo .env
load_dotenv()
#client de groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
class ChatState(rx.State):

#se guarda el historial de dupla ["pregunta"]:["respuesta"]
    chat_history: list[tuple[str, str]] = []
    question: str = ""
    is_loading: bool = False

    def set_question(self, value: str):
        self.question = value 

    def answer_question(self):
        #si no existe el texto return y no devolver nada
        if not self.question.strip():
            return 
        user_input = self.question
        self.question = ""  # Limpiamos el input
        self.is_loading = True
        yield  # Actualiza la UI para mostrar que está cargando
        #2 se construye el contexto e historial 
        messages =[{"role":"system","content":CV_CONTEXT}]
        for q,a in self.chat_history:
            messages.append({"role":"user","content":q})
            messages.append({"role": "assistant", "content": a})        
        messages.append({"role":"user","content":user_input})
        #3llamada a groq
        try:
            response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Modelo groq
            messages=messages,
            )
            answer =response.choices[0].message.content
        except Exception as e:
            answer =f"Error al conectar con la IA:{str(e)}"
        self.chat_history.append((user_input,answer))
        self.is_loading=False
def qa_pair(question: str, answer: str) -> rx.Component:
    """Componente para renderizar cada par de Pregunta/Respuesta."""
    return rx.vstack(
        rx.box(
            rx.text(question, color="white"),
            background_color="#2b303c",
            padding="1em",
            border_radius="10px",
            align_self="flex-end",
            max_width="80%",
        ),
        rx.box(
            rx.text(answer, color="white"),
            background_color="#1e222a",
            padding="1em",
            border_radius="10px",
            align_self="flex-start",
            max_width="80%",
        ),
        width="100%",
        spacing="3",
    )


def chat_component() -> rx.Component:
    """Componente principal del chat."""
    return rx.vstack(
        rx.heading("🤖 Pregúntale a mi Asistente IA sobre mi CV", size="6"),
        rx.text("Hazme cualquier pregunta sobre mi experiencia, proyectos o tecnologías."),
        
        # Area de mensajes
        rx.scroll_area(
            rx.vstack(
                rx.foreach(ChatState.chat_history, lambda q_a: qa_pair(q_a[0], q_a[1])),
                width="100%",
            ),
            height="350px",
            width="100%",
            border="1px solid #333",
            padding="1em",
            border_radius="8px",
        ),
        
        # Input y Botón
        rx.hstack(
            rx.input(
                placeholder="Ej. ¿Qué experiencia tiene Víctor en FastAPI?",
                value=ChatState.question,
                on_change=ChatState.set_question,
                width="80%",
            ),
            rx.button(
                "Enviar",
                on_click=ChatState.answer_question,
                loading=ChatState.is_loading,
                color_scheme="green",
            ),
            width="100%",
        ),
        width="100%",
        max_width="700px",
        spacing="4",
    )