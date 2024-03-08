import telebot
import os
import random

import keyboards

# Initialize your bot token obtained from @BotFather
TOKEN = "5385126708:AAHLVLLs708YePNRDYvk6dswfd0v-qkMG84"  # 'your_telegram_bot_token_here'

# Initialize telebot
bot = telebot.TeleBot(TOKEN)


# Function to send a random meme from the memes folder
def send_random_meme(message):
    meme_folder = 'memes'
    meme_files = os.listdir(meme_folder)
    random_meme = random.choice(meme_files)
    meme_path = os.path.join(meme_folder, random_meme)
    with open(meme_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


# Handler for the "/start" command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привiт! Я бот-мемчик. Нажми кнопку 'Мем', щоб отримати випадковий мем!", reply_markup=keyboards.meme_button())


# Handler for the "Мем" button
@bot.message_handler(func=lambda message: True)
def send_random_meme_on_button_press(message):
    if message.text == "Мем":
        send_random_meme(message)


if __name__ == '__main__':
    # Start the bot
    bot.polling()
