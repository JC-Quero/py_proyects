import logging
import json
import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import CommandHandler, Dispatcher
import requests

# Inicializamos Flask para recibir las peticiones de Telegram
app = Flask(__name__)

# Configuración básica del bot de Telegram
TELEGRAM_TOKEN = os.getenv("7923314678:AAEwI-qA3KcY2GZFoZKB82FeNvQCSM41mgM")  # Asegúrate de tener la variable de entorno o poner el token aquí
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# Crear una instancia de Bot
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Función para responder al comando /start
def start(update: Update, context):
    update.message.reply_text("¡Hola! Soy el bot para organizar tus partidos de fútbol. Usa el comando /equipos para agregar jugadores.")

# Función para manejar el comando /equipos
def equipos(update: Update, context):
    jugadores = context.args
    if len(jugadores) < 2:
        update.message.reply_text("Necesito al menos 2 jugadores para armar equipos.")
        return
    
    # Aquí puedes agregar la lógica para dividir los jugadores en equipos
    mensaje = "Jugadores agregados: \n" + "\n".join(jugadores)
    update.message.reply_text(mensaje)

# Ruta para manejar las actualizaciones de Telegram (Webhook)
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = Update.de_json(json.loads(json_str), bot)
    dispatcher.process_update(update)
    return 'OK', 200

# Configuración del webhook de Telegram
def set_webhook():
    # Aquí debes poner la URL de tu proyecto en Vercel
    webhook_url = f"https://py-proyects-eg27zp0hg-jcs-projects-e0381550.vercel.app/webhook"  # O la URL de tu proyecto
    url = f"{TELEGRAM_URL}/setWebhook?url={webhook_url}"
    response = requests.get(url)
    print(f"Webhook configurado: {response.text}")

# Inicializamos los handlers para los comandos
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("equipos", equipos))

# Ejecutamos el Webhook para que el bot empiece a recibir mensajes
if __name__ == '__main__':
    set_webhook()  # Establecer el webhook
    app.run(host='0.0.0.0', port=5000)  # Ejecutamos el servidor Flask
