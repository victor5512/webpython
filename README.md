# 🤖 Portfolio Web & Asistente IA sobre mi CV

Este es mi sitio web de portafolio interactivo desarrollado totalmente en **Python** utilizando **Reflex** como framework Full-stack y la **API de Groq (Llama 3.1)** para responder preguntas sobre mi experiencia profesional en tiempo real.

---

## 🚀 Características

* **Python Full-stack:** Frontend y Backend unificados bajo el ecosistema de Python gracias a Reflex.
* **Integración con IA:** Asistente conversacional contextualizado con la información de mi CV.
* **Respuesta Ultra-Rápida:** Potenciado por la infraestructura de Llama 3.1 en Groq.
* **Modo Oscuro / Interfaz Moderna:** Diseño responsive enfocado en la experiencia de usuario.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.11+**
* **Reflex** (Framework web)
* **Groq SDK** (LLM API - Llama 3.1 8B)
* **python-dotenv** (Gestión de variables de entorno)

---

## ⚙️ Instrucciones de Instalación y Configuración Local

Si deseas probar o clonar este proyecto en tu máquina local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/victor5512/webpython.git](https://github.com/victor5512/webpython.git)
cd webpython

#activar entorno virtual
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
#dependencias 
pip install -r requirements.txt
#ejecutar aplicacion
reflex run