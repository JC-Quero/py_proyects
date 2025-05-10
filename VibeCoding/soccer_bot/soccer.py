# api/index.py

import os
import json
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

# Crear la app de Flask
app = Flask(__name__)

# Configurar el bot de Telegrama
TELEGRAM_TOKEN = os.getenv("7923314678:AAEwI-qA3KcY2GZFoZKB82FeNvQCSM41mgM")  # ¡NO pongas el token directo aquí!
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Comando /start
def start(update: Update, context):
    update.message.reply_text("¡Hola! Soy el bot para organizar tus partidos de fútbol. Usa /equipos seguido de los nombres.")

# Comando /equipos
def equipos(update: Update, context):
    jugadores = context.args
    if len(jugadores) < 2:
        update.message.reply_text("Necesito al menos 2 jugadores para armar equipos.")
        return
    mensaje = "Jugadores agregados:\n" + "\n".join(jugadores)
    update.message.reply_text(mensaje)

# Registrar handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("equipos", equipos))

# Ruta que Telegram usará para enviar los mensajes
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(json.loads(request.data), bot)
    dispatcher.process_update(update)
    return "OK"
