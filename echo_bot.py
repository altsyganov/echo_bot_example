import telebot


bot = telebot.TeleBot("945106294:AAFWKOQIMKLKEnQXADL4m8Zyd71LBJjZVsY", parse_mode=None)

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "WeLcOmE")


@bot.message_handler(content_types=["text"])
def echo_all(message):
    bot.reply_to(message, message.text)

# def

bot.polling(none_stop=True)
