import os
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, WebAppData
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TOKEN)

# Comando /start com botão do WebApp
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    
    # Cria um botão que abre o WebApp
    webapp_button = InlineKeyboardButton(
        text="🌐 Abrir Instante Infinito",
        web_app=WebAppInfo(url="https://ve-scores-vacuum-mall.trycloudflare.com")  # Substitua pelo seu domínio
    )
    
    keyboard.add(webapp_button)

    bot.send_message(
        message.chat.id,
        "Olá! Clique no botão abaixo para abrir o Instante Infinito:",
        reply_markup=keyboard
    )

# Captura dados retornados do WebApp (caso você envie algo de volta)
@bot.message_handler(content_types=["web_app_data"])
def receive_webapp_data(message):
    data: WebAppData = message.web_app_data
    bot.send_message(message.chat.id, f"Você enviou: {data.data}")

if __name__ == "__main__":
    bot.infinity_polling()
