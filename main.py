import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = '5206622849:AAF1cPEbHNmlzMTeXs511DCUnqrtDm7ebnc'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

import telebot
from telebot import types
import random as r

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add("/wish10")
    keyboard.add("/hatch")
    keyboard.add("/wepon")
    bot.send_message(message.from_user.id, "Здравствуй! Что собираешься делать", reply_markup=keyboard)

@bot.message_handler(commands=['привет'])
def handle_command(message):
  bot.send_message(message.chat.id, 'Привет,что хотите сейчас делать?')

@bot.message_handler(commands=['пока'])
def handle_command(message):
  bot.send_message(message.chat.id, 'Пока')

@bot.message_handler(commands=['wish10'])
def handle_command(message):
  pers1 = open("lola.jpeg", "rb")
  pers2 = open("toma.jpg", "rb")
  pers3 = open("cece.jpeg", "rb")
  pers4 = open("roza.jpeg", "rb")
  pers5 = open("LIO.jpeg", "rb")
  pers6 = open("barbara.jpeg", "rb")
  pers7 = open("kok.jpeg", "rb")
  pers8 = open("riden.jpeg", "rb")
  pers9 = open("sara.jpeg", "rb")
  pers10 = open("sau.jpeg", "rb")
  pers11 = open("ded.jpeg", "rb")
  pers12 = open("Venti.jpg", "rb")
  pers13 = open("goro.jpg", "rb")
  pers14 = open("hutao.jpg", "rb")
  pers15 = open("aiato.jpg", "rb")
  pers16 = open("Sio.jpg", "rb")
  pers17 = open("zchun lee.jpg", "rb")
  pers18 = open("schen.png", "rb")
  pers19 = open("fen.jfif", "rb")
  pers20 = open("an.jpg", "rb")
  pers21 = open("itto.jpg", "rb")
  pers22 = open("klee.jfif", "rb")
  pers23 = open("tort.jpg", "rb")
  pers24 = open("fishl.jpeg", "rb")
  pers25 = open("nin.jpg", "rb")
  pers26 = open("mona.jpg", "rb")
  pers27 = open("001h.jpg", "rb")
  s = {"Элой": pers1,"Кокоми": pers7, "Баал": pers8, "Сара": pers9, "Саю": pers10, "Тома": pers2, "Ци Ци": pers3,"Розария": pers4, "Альбедо": pers5, "Барбара": pers6, "Дилюк": pers11, "Венти": pers12, "Горо": pers13, "Ху Тао": pers14, "Аято": pers15, "Сяо": pers16, "Чжун Ли": pers17, "Шэнь Хэ": pers18, "Янь Фэй": pers19, "яэ мико": pers20, "итто": pers21, "кли": pers22, "тарталия": pers23, "фишль": pers24, "нин гуан": pers25, "мона": pers26, "кадзуха": pers27}
  sl = r.choice(list(s.keys()))
  bot.send_message(message.chat.id, sl)
  bot.send_photo(message.chat.id, s[sl])
@bot.message_handler(commands=['hatch'])
def handle_command(message):
  s1 = open("gromel.jpeg", "rb")
  s2 = open("ro.png", "rb")
  s3 = open("zmeevic.jpeg", "rb")
  s4 = open("r.jpg", "rb")
  s5 = open("kost.png", "rb")
  s6 = open("oop.png", "rb")
  s7 = open("firebon.png", "rb")
  s8 = open("voice.png", "rb")
  s9 = open("killer.png", "rb")
  s10 = open("threekils.jpg", "rb")
  s11 = open("aquakiller.jpg", "rb")
  o = {"сарделька": s1,"роза ветров": s2, "змеевик": s3, "Болт и Поплавок": s4, "Костолом": s5, "Катастрофический Землетряс": s6, "Огнеброн": s7, "Лохматый Вой": s8, "Скорожал": s9, "Тройной Удар": s10, "Подводный Потрошитель": s11}
  el = r.choice(list(o.keys()))
  bot.send_message(message.chat.id, el)
  bot.send_photo(message.chat.id, o[el])

@bot.message_handler(commands=['wepon'])
def handle_command(message): 
  r1000 = open("dr.jpg", "rb")
  r1 = open("dance.jpg", "rb")
  r2 = open("002.jpg", "rb")
  r4 = open("bow1.png", "rb")
  r3 = open("-0-0.jpg", "rb")
  r5 = open("bow2.jpg", "rb")
  r7 = open("bow3.jpg", "rb")
  r6 = open("c6.jpg", "rb")
  r8 = open("c8.png", "rb")
  r9 = open("i.jfif", "rb")
  r10 = open("-0=-.jpg", "rb")
  r11 = open("00-0.jpg", "rb")
  r12 = open("1-0.jpg", "rb")
  r13 = open("9.png", "rb")
  r14 = open("5.jpg", "rb")
  r15 = open("6.jpg", "rb")
  r16 = open("homa.jpg", "rb")
  sp = {"Гроза драконов": r1000, "Вальс Нирваны Ночи": r1, "Око сознания" : r4, "Церемониальный лук": r3, "Кодекс Фавония": r2, "Ржавый лук": r5, "Боевой лук Фавония": r7, "Копьё Фавония": r6, "Меч-колокол": r8, "Бесструнный": r9, "Песнь странника": r10, "Церемониальный меч": r11, "Дождерез": r12, "Меч Фавония": r13, "Некованый": r14, "Полярная звезда": r15,"Хома": r16}
  ls = r.choice(list(sp.keys())) 
  bot.send_message(message.chat.id, ls)
  bot.send_photo(message.chat.id, sp[ls])


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://timonn.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
