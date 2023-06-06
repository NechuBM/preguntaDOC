
# 📚🗨️  preguntaDOC: Convierte tus documentos en conversaciones con chatGPT

:link: [Web demo](https://nechubm-preguntadoc-app-tutorial-ct21ps.streamlit.app/)

🚀 [Tutorial en Español | Youtube](https://youtu.be/iDrpdkIHMq8)

¿Sabías que chatGPT puede tener conversaciones con documentos? ¡En este taller de Python, descubriremos cómo hacerlo posible! Olvídate de las limitaciones, ahora podrás chatear y explorar tus documentos de una manera completamente nueva.


## Introduccion
📄🧠 Con preguntaDOC, en menos de 50 líneas de código, aprenderás a aprovechar todo el potencial de chatGPT y convertir tus documentos en conversaciones interactivas. No más lecturas aburridas o búsquedas tediosas, ahora podrás hacer preguntas directamente a tus documentos y obtener respuestas de chatGPT.
Para desarrollar esta aplicación en menos de 50 líneas de código necesitaremos:
* ChatGPT API
* Streamlit


## ¿Cómo funciona?
1. Divide documento en cachos (o chunks)
2. Crea los embeddings de los cachos de texto
3. Guarda los cachos y los embeddings en una base de conocimiento
4. Busca los cachos más similares a la pregunta del usuario gracias a los embeddings.
5. Pasa los cachos más similares junto a la pregunta a chatGPT que genera la respuesta


## Instalar preguntaDOC
¡Usar preguntaDOC es fácil! Aquí están los pasos:
1. Clone o descargue el repositorio en su máquina local.
2. Instale las bibliotecas requeridas ejecutando el siguiente comando en su terminal:
```console
pip install -r requirements.txt
```
3. Ejecute la aplicación con el siguiente comando:
```console
streamlit run app.py
```
4. Obtenga una clave API de OpenAI para usar su API ChatGPT.
5. Suba un documento a la aplicación.
6. Escriba su pregunta y disfrute de la magia.
