import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# Configurar el logging para ver los errores de forma más fácil
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Iniciar el bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje cuando el comando /start es usado"""
    await update.message.reply_text("¡Hola! Soy tu bot. ¿Cómo puedo ayudarte hoy Sergi?")

# Servidor Flask para mantener el bot activo
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Estoy vivo y funcionando! 🚀"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    thread = Thread(target=run_flask)
    thread.start()

# Configurar el bot con el token
def main():
    # Reemplaza con el token que te dio BotFather
    token = '7077644643:AAFJrmehzk3LdIuunnPKynwkYqzd0o0iySg'  # <-- Reemplaza esto con tu token real

    # Crea una instancia de Application
    application = Application.builder().token(token).build()

    # Comando /start
    application.add_handler(CommandHandler("start", start))

    # Mantener el bot activo con Flask
    keep_alive()

    # Comienza a escuchar por actualizaciones
    application.run_polling()

if __name__ == '__main__':
    main()
