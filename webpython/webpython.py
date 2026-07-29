# webpython/webpython.py
import reflex as rx
from webpython.chat import chat_component

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("¡Hola, soy Víctor Manuel! 👋", size="8"),
            rx.text("Desarrollador de Software | Python & Full-Stack", size="4"),
            rx.divider(),
            
            # Insertamos el chat interactivo aquí
            chat_component(),
            
            spacing="5",
            align="center",
            width="100%",
        ),
        padding="2em",
        min_height="100vh",
    )

app = rx.App()
app.add_page(index, route="/")