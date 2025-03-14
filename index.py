import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# Configuración de Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Token del Bot (REEMPLAZA ESTO POR TU TOKEN REAL)
TOKEN = 'TU_TOKEN_AQUI'
CHAT_ID = 'TU_CHAT_ID_AQUI'  # ID del chat donde enviar noticias

# Crear la instancia del bot
application = Application.builder().token(TOKEN).build()

# 📌 1️⃣ Función para obtener noticias sobre UX/UI y tecnología
def obtener_noticias():
    noticias = [
        "🔹 [Smashing Magazine - UX](https://www.smashingmagazine.com/category/uxdesign/)",
        "🔹 [UX Collective](https://uxdesign.cc/)",
        "🔹 [Wired - Tech](https://www.wired.com/category/tech/)",
        "🔹 [A List Apart](https://alistapart.com/)",
        "🔹 [CSS Tricks](https://css-tricks.com/)"
    ]
    return random.choice(noticias)  # Devuelve una noticia aleatoria

# 📌 2️⃣ Función para enviar noticias cuando el usuario escribe /news
async def enviar_noticias(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía una noticia aleatoria sobre UX/UI o tecnología."""
    noticia = obtener_noticias()
    await update.message.reply_text(f"📰 *Noticias de hoy:*\n{noticia}", parse_mode="Markdown")

# 📌 3️⃣ Función de bienvenida con /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mensaje de bienvenida personalizado."""
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f"👋 ¡Hola, {user_first_name}! Escribe /help para ver los comandos disponibles.")

# 📌 4️⃣ Comando /help con botones interactivos
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje con la lista de comandos y botones interactivos."""

    help_text = "🆘 *Lista de Comandos* 🆘\n\n"
    help_text += "✅ /start - Inicia el bot\n"
    help_text += "✅ /help - Muestra este mensaje de ayuda\n"
    help_text += "✅ /news - Recibe noticias de UX/UI y tecnología\n"

    # Crear botones
    keyboard = [
        [InlineKeyboardButton("🔹 Ver Noticias", callback_data='news')],
        [InlineKeyboardButton("📩 Contacto", url="https://t.me/tuusuario")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(help_text, reply_markup=reply_markup, parse_mode="Markdown")

# 📌 5️⃣ Manejo de botones interactivos
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja las acciones cuando el usuario presiona un botón en /help."""
    query = update.callback_query
    await query.answer()  # Confirma la acción para el usuario

    if query.data == "news":
        noticia = obtener_noticias()
        await query.message.reply_text(f"📰 *Noticias de hoy:*\n{noticia}", parse_mode="Markdown")

# 📌 6️⃣ Servidor Flask para mantener el bot activo
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Estoy vivo y funcionando! 🚀"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    thread = Thread(target=run_flask)
    thread.start()

# 📌 7️⃣ Función principal del bot
def main():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("news", enviar_noticias))
    application.add_handler(telegram.ext.CallbackQueryHandler(button_handler))

    keep_alive()
    application.run_polling()

# 📌 8️⃣ Ejecutar el bot
if __name__ == '__main__':
    main()
