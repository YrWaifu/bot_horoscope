from myparser import pars
from mytoken import TOKEN
import telebot
from telebot import types
import time
from datetime import datetime


bot = telebot.TeleBot(TOKEN)
buf = ["♈️ Овен", "♉️ Телец", "♊️ Близнецы", "♋️ Рак", "♌️ Лев", "♍️ Дева", "♎️ Весы", "♏️ Скорпион", "♐️ Стрелец", "♑️ Козерог", "♒️ Водолей", "♓️ Рыбы"]
zodiac = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет! Я бот-гороскоп, который может каждый день присылать тебе новейшие '
                                           'пожелния. Снизу ты можешь увидеть список моих комманд 😀\n'
                                           '/choose - команда для выбора вашего знака зодиака.\n/today - с помощью '
                                           'этой команды вы можете получить сегодняшний гороскоп в любое время.\n'
                                           '/time - с помощью этой команды вы можете настроить время, в которое бот '
                                           'будет ежедневно скидывать вам текущий горскоп')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, '/choose - команда для выбора вашего знака зодиака.\n/today - с помощью '
                                           'этой команды вы можете получить сегодняшний гороскоп в любое время.\n'
                                           '/time - с помощью этой команды вы можете настроить время, в которое бот '
                                           'будет ежедневно скидывать вам текущий горскоп')


@bot.message_handler(commands=['time'])
def time(message):
    bot.send_message(message.from_user.id, "Данная функция находится в разработке.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("/today")
    btn3 = types.KeyboardButton("/choose")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Выбери дальнейшие действия. Если забыл, что какие команды означают, "
                                           "выбери /help", reply_markup=markup)


@bot.message_handler(commands=['today'])
def today(message):
    if not zodiac:
        bot.send_message(message.from_user.id, '😳Ты еще не выбрал свой знак зодиака. Введи команду /choose')
    else:
        pred = pars(zodiac)
        bot.send_message(message.from_user.id, *pred)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("/choose")
    btn3 = types.KeyboardButton("/time")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Выбери дальнейшие действия. Если забыл, что какие команды означают, "
                                           "выбери /help", reply_markup=markup)


@bot.message_handler(commands=['choose'])
def choose(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("♈️ Овен")
    btn2 = types.KeyboardButton("♉️ Телец")
    btn3 = types.KeyboardButton("♊️ Близнецы")
    btn4 = types.KeyboardButton("♋️ Рак")
    btn5 = types.KeyboardButton("♌️ Лев")
    btn6 = types.KeyboardButton("♍️ Дева")
    btn7 = types.KeyboardButton("♎️ Весы")
    btn8 = types.KeyboardButton("♏️ Скорпион")
    btn9 = types.KeyboardButton("♐️ Стрелец")
    btn10 = types.KeyboardButton("♑️ Козерог")
    btn11 = types.KeyboardButton("♒️ Водолей")
    btn12 = types.KeyboardButton("♓️ Рыбы")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    bot.send_message(message.from_user.id, "Выбери свой знак зодиака", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text in buf:
        global zodiac
        zodiac = message.text
        bot.send_message(message.from_user.id, "Отлично, я запомнил тебя!😉")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/help")
        btn2 = types.KeyboardButton("/today")
        btn3 = types.KeyboardButton("/time")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выбери дальнейшие действия. Если забыл, что какие команды означают, "
                                               "выбери /help", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Я тебя не очень понял, попробуй воспользоваться встроенными "
                                               "функциями. Если ты их подзабыл, можешь ввести команду /help")


bot.polling(none_stop=True, interval=0)
