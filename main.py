import telebot
import os
from random import choice
from settings import TG_API_TOKEN

bot = telebot.TeleBot(TG_API_TOKEN)

@bot.message_handler(commands=['tips'])
def send_help(message):
    bot.reply_to(message, "Что хочешь отсортировать. Пластиковая бутылка, Коробки, Остатки еды, Бутылки од пива, Батарейки. Пожалуйста напищи вещь также как здесь указано.")

@bot.message_handler(func=lambda message: 'Бутылки од пива' in message.text)
def handle_sab_text(message):
    bot.reply_to(message, 'Бутылки од пива выкидавай в стекло.')

@bot.message_handler(func=lambda message: 'Пластиковая бутылка' in message.text)
def handle_gag_text(message):
    bot.reply_to(message, 'Пластиковые бутылки выкидовай в пластик.')

@bot.message_handler(func=lambda message: 'Батарейки' in message.text)
def handle_pvb_text(message):
    bot.reply_to(message, 'Батарейки не выкидовай их надо сдавать.')

@bot.message_handler(func=lambda message: 'Остатки еды' in message.text)
def handle_99nitf_text(message):
    bot.reply_to(message, 'Остатки еды выкидовай в смешаный мусор.')

@bot.message_handler(func=lambda message: 'Коробки' in message.text)
def handle_doors_text(message):
    bot.reply_to(message, 'Коробки выкидовай в бумагу. ')


@bot.message_handler(commands=['start'])
def send_welcome(message):
#    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Команды : /bye ends the bot, /tips")
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Команды : /tips подсказывает что куда сортировать, /mem sends a meme')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    random_mem = choice(os.listdir('images')) #'mem2.jpeg'
    with open(f'images/{random_mem }', 'rb') as f:
        bot.send_photo(message.chat.id, f)

bot.polling()