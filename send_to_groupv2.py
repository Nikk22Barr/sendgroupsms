import telebot

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['send'])
def send_to_group(message):
    text = message.text.split()[1:]
    bot.send_message('id group', ' '.join(text))
    
bot.polling() 
