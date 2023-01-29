import telebot
import json
from aiogram.utils.markdown import hbold,hlink
from parsing import get_data
import time
from telebot import types

bot = telebot.TeleBot('5856369779:AAFFBjAZl5vI3SVN9Z_pbjokOEG08IGyY9Q')

@bot.message_handler(commands=['start'])
def start(message):
    global parsing_continue
    parsing_continue = True
    collection = bot.reply_to(message, "Введите название коллекции, цену, trait и вид trait (Пример: bvdcat 2 Glasses None) ")
    bot.register_next_step_handler(collection, get_information)

@bot.message_handler(commands=['stop'])
def stop(message):
    global parsing_continue
    parsing_continue = False
    bot.send_message(message.chat.id, "стоп")

@bot.message_handler(content_types=['text'])
def get_information(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('/stop')
    markup.add(item)
    bot.send_message(message.chat.id, 'Waiting...', reply_markup=markup)

    while parsing_continue:
        time.sleep(5)

        ms = message.text

        information = ms.split()
        collection = information[0].lower()
        price = information[1].replace(',', '.')
        trait = information[2].title()
        if len(information) == 4:
            type_trait = information[3].title()
            get_data(collection, price, trait, type_trait)
        elif len(information) == 5:
            type_trait = information[3].title() + ' ' + information[4].title()
            get_data(collection, price, trait, type_trait)
        elif len(information) == 6:
            type_trait = information[3].title() + ' ' + information[4].title() + ' ' + information[5].title()
            get_data(collection, price, trait, type_trait)
        elif len(information) == 7:
            type_trait = information[3].title() + ' ' + information[4].title() + ' ' + information[5].title() + ' ' \
                         + information[6].title()
            get_data(collection, price, trait, type_trait)

        with open('result.json') as file:
            data = json.load(file)

        for item in data:
            card = f'{hlink(item.get("Title"),item.get("link on site"))}\n' \
                   f'{hbold("Коллекция: ")}{item.get("Collection")}\n' \
                   f'{hbold("Цена: ")}{item.get("Price")}\n' \
                   f'{hbold("Trait: ")}{item.get("Trait")}\n'

            bot.send_message(message.chat.id, card, parse_mode='html')


bot.polling(none_stop = True)


