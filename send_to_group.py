import telebot

bot = telebot.TeleBot('token_bot')

@bot.message_handler(commands=['send'])

def send_to_group(message):

    bot.send_message('<id_группы', '<рандом_sms')

    

bot.polling()
