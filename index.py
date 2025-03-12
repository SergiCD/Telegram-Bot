

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurar el logging para ver los errores de forma más fácil
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Comando de inicio
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia un mensaje cuando el comando /start es usado"""
    await update.message.reply_text("¡Hola! Soy tu bot. ¿Cómo puedo ayudarte hoy?")

# Configurar el bot con el token
def main():
    # Reemplaza con el token que te dio BotFather
    token = '7077644643:AAFJrmehzk3LdIuunnPKynwkYqzd0o0iySg'  # Asegúrate de reemplazarlo con tu token

    # Crea una instancia de Application
    application = Application.builder().token(token).build()

    # Comando /start
    application.add_handler(CommandHandler("start", start))

    # Comienza a escuchar por actualizaciones
    application.run_polling()

if __name__ == '__main__':
    main()
