import json

from aiogram import Bot, Dispatcher,executor, types
from aiogram.dispatcher.filters import Text
from parsing import get_data
from aiogram.utils.markdown import hbold,hlink

bot = Bot(token='5641417625:AAE7fVz2613J4eU-vMoVzsa577l3wp9cmhU', parse_mode=types.ParseMode.HTML)
desp = Dispatcher(bot)

@desp.message_handler(commands='start')
async def start(message: types.Message):
    buttons = ['bvdcat', 'pixel guild']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@desp.message_handler(Text(equals='bvdcat'))
async def get_information_cats(message: types.Message):
    await message.answer('Waiting...')
    get_data()

    with open('result.json') as file:
        data = json.load(file)

    for item in data:
        card = f'{hlink(item.get("Title"),item.get("link on site"))}\n' \
               f'{hbold("Коллекция: ")}{item.get("Collection")}\n' \
               f'{hbold("Цена: ")}{item.get("Price")}\n'
        await message.answer(card)






def main():
    executor.start_polling(desp)


if __name__ == '__main__':
    main()


