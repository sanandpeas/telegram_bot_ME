import telebot
import json
from aiogram.utils.markdown import hbold,hlink
from parsing import get_data


bot = telebot.TeleBot('5856369779:AAFFBjAZl5vI3SVN9Z_pbjokOEG08IGyY9Q')



@bot.message_handler(commands=['start'])
def start(message):

    collection = bot.reply_to(message, "Введите название коллекции, цену, trait и вид trait (Пример: bvdcat 2 Glasses None) ")
    bot.register_next_step_handler(collection,get_information_cats)



def get_information_cats(message):
    ms = message.text
    information = ms.split()
    collection = information[0].lower()
    price = information[1].replace(',', '.')
    trait = information[2].title()
    type_trait = information[3].title()
    get_data(collection, price, trait, type_trait)

    with open('result.json') as file:
        data = json.load(file)

    for item in data:
        card = f'{hlink(item.get("Title"),item.get("link on site"))}\n' \
               f'{hbold("Коллекция: ")}{item.get("Collection")}\n' \
               f'{hbold("Цена: ")}{item.get("Price")}\n' \
               f'{hbold("Trait: ")}{item.get("Trait")}\n'

        bot.send_message(message.chat.id, card, parse_mode='html')

bot.polling()


