#pyTelegramBotAPI, pytz, sqlite3
import telebot
import pytz
import sqlite3
from pytz import timezone
from datetime import datetime
from telebot import types


bot = telebot.TeleBot("2064152487:AAEU7x4xEGNi7Cuv1odxF3k3bnXkKWmlxk4")
    

# COMMANDS


@bot.message_handler(commands=['start'])
def welcome(message):

    #DATABASE
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            id INTEGER
    )""")
    connect.commit()

    # проверка id на повтор
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    print(data)
    if data is None:
        # добавляем значение
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()


    # Keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("⏳ Time")
    item2 = types.KeyboardButton("♿ Change TimeZone")
    item3 = types.KeyboardButton("🚀 Help")

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Добро пожаловать\nЭто тестовый бот, который имеет минимальный "
                                      "функционал.\nПропишите /func, чтобы узнать список команд.",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['func'])
def get_func(message):
    bot.send_message(message.chat.id, "/start - Начать нашу историю заново!\n/time - Узнать время\n/help - Помощь")


@bot.message_handler(commands=['time'])
def get_time(message):
    bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Europe/Moscow'))) + "\nЕсли хотите изменить часовой пояс напишите"
                                                                    "\n/start и выберите ♿ Change TimeZone")


@bot.message_handler(commands=['help'])
def hel(message):
    bot.send_message(message.chat.id, "Вк - vk.com/ssto4cv\n"
                                      "GitHub - github.com/Sstocv")


@bot.message_handler(content_types=['text'])
def keyboard(message):
    if message.chat.type == 'private':
        if message.text == "⏳ Time":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Europe/Moscow'))) + "\nЕсли хотите изменить часовой пояс напишите" 
                                                                            "\n/start и выберите ♿ Change TimeZone")
        elif message.text == "♿ Change TimeZone":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            pol1 = types.KeyboardButton("KALT +2")
            pol2 = types.KeyboardButton("MSK +3")
            pol3 = types.KeyboardButton("SAMT +4")
            pol4 = types.KeyboardButton("YEKT +5")
            pol5 = types.KeyboardButton("OMST +6")
            pol6 = types.KeyboardButton("KRAT +7")
            pol7 = types.KeyboardButton("IRKT +8")
            pol8 = types.KeyboardButton("YAKT +9")
            pol9 = types.KeyboardButton("VLAT +10")
            pol10 = types.KeyboardButton("MAGT +11")
            pol11 = types.KeyboardButton("PETT +12")

            markup1.add(pol1, pol2, pol3, pol4, pol5, pol6, pol7, pol8, pol9, pol10, pol11)
            bot.send_message(message.chat.id, "Выберите свой часовой пояс", parse_mode='html', reply_markup=markup1)
        elif message.text == "KALT +2":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Africa/Khartoum'))))
        elif message.text == "MSK +3":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Europe/Moscow'))))
        elif message.text == "SAMT +4":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Asia/Baku'))))
        elif message.text == "YEKT +5":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Asia/Aqtau'))))
        elif message.text == "OMST +6":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Antarctica/Vostok'))))
        elif message.text == "KRAT +7":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Asia/Bangkok'))))
        elif message.text == "IRKT +8":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Asia/Brunei'))))
        elif message.text == "YAKT +9":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Asia/Chita'))))
        elif message.text == "VLAT +10":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Antarctica/DumontDUrville'))))
        elif message.text == "MAGT +11":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Antarctica/Casey'))))
        elif message.text == "PETT +12":
            bot.send_message(message.chat.id, str(datetime.now(pytz.timezone('Asia/Anadyr'))))
        elif message.text == "🚀 Help":
            bot.send_message(message.chat.id, "Вк - vk.com/ssto4cv\n"
                                              "GitHub - github.com/Sstocv")
        else:
            bot.send_message(message.chat.id, "Я не раслышал, повторите!")

if __name__ == '__main__':
    print("TeleBot online!")
    bot.infinity_polling()