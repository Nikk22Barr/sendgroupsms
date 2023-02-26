import telebot

bot = telebot.TeleBot('2056947414:AAHZ41zKLmoTIN5-CB3WmO97M1uqF3hFm_w')

@bot.message_handler(commands=['send'])
def send_to_group(message):
    bot.send_message('-1001727744204', '')
    
bot.polling()