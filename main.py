import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = '5286040884:AAGJ5Qx-2uc4tu0mCJ9ewN4cWdRoWQptbTg'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['test'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup() # создаём клавиатуру
    button1 = types.InlineKeyboardButton(text='Всё супер', callback_data=1) # создаём кнопки
    button2 = types.InlineKeyboardButton(text='Всё хорошо', callback_data=2) # создаём кнопки
    keyboard.add(button1) # добавляем кнопки к клавиатуре
    keyboard.add(button2) # добавляем кнопки к клавиатуре
    bot.send_message(message.chat.id, text="Привет, как дела?", reply_markup=keyboard)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://<Название_вашего_хероку_приложения>.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
