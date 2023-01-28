

import telebot
import json
from aiogram.utils.markdown import hbold,hlink
from parsing import get_data


bot = telebot.TeleBot('5856369779:AAFFBjAZl5vI3SVN9Z_pbjokOEG08IGyY9Q')



@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.reply_to(message, "Название коллекции")
    bot.register_next_step_handler(sent,get_information_cats)




def get_information_cats(message):
    message_to_save = message.text
    get_data(message_to_save)

    with open('result.json') as file:
        data = json.load(file)

    for item in data:
        card = f'{hlink(item.get("Title"),item.get("link on site"))}\n' \
               f'{hbold("Коллекция: ")}{item.get("Collection")}\n' \
               f'{hbold("Цена: ")}{item.get("Price")}\n' \
               f'{hbold("Trait: ")}{item.get("Trait")}\n'

        bot.send_message(message.chat.id, card,parse_mode='html')
bot.polling()


