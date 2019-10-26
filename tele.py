import telebot
tkn = "862740420:AAEYJLgTBuRX_0ieGJSHquV0WkNfQduS714"

bot = telebot.TeleBot(tkn)
my_chat_id = 427833035
    
def send_message(msg):
    bot.send_message(my_chat_id,msg)