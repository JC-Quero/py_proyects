import logging
import json
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Inicializamos Flask para recibir las peticiones de Telegram
app = Flask(__name__)

# Configuración básica del bot de Telegram
TELEGRAM_TOKEN = os.getenv("7923314678:AAEwI-qA3KcY2GZFoZKB82FeNvQCSM41mgM")  # Asegúrate de poner el token de tu bot aquí
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# Función para responder al comando /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("¡Hola! Soy el bot para organizar tus partidos de fútbol. Usa el comando /equipos para agregar jugadores.")

# Función para manejar el comando /equipos
def equipos(update: Update, context: CallbackContext):
    jugadores = context.args
    if len(jugadores) < 2:
        update.message.reply_text("Necesito al menos 2 jugadores para armar equipos.")
        return
    
    # Aquí puedes agregar la lógica para dividir los jugadores en equipos
    # Este es un ejemplo simple para enviar la lista de jugadores
    mensaje = "Jugadores agregados: \n" + "\n".join(jugadores)
    update.message.reply_text(mensaje)

# Ruta para manejar las actualizaciones de Telegram (Webhook)
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = Update.de_json(json.loads(json_str), updater.bot)
    updater.dispatcher.process_update(update)
    return 'OK'

# Configuración del webhook de Telegram
def set_webhook():
    # Aquí debes poner la URL de tu proyecto en Vercel
    webhook_url = f"https://{os.getenv('VERCEL_URL')}/webhook"
    url = f"{TELEGRAM_URL}/setWebhook?url={webhook_url}"
    response = requests.get(url)
    print(f"Webhook configurado: {response.text}")

# Inicializamos el Updater y Dispatcher para manejar los comandos
updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("equipos", equipos))

# Ejecutamos el Webhook para que el bot empiece a recibir mensajes
if __name__ == '__main__':
    set_webhook()  # Establecer el webhook
    app.run(host='0.0.0.0', port=5000)  # Ejecutamos el servidor Flask
