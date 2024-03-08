import telebot


def meme_button():
    mem_btn = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    mem_btn.row("Мем")

    return mem_btn
