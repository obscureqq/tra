from subprocess import check_output
import telebot
import time

bot = telebot.TeleBot("6158419008:AAE7iHfbonsfKLtOZD6SW98Nvqfjs9_wdLk")#токен бота
user_id = 652735087 #id вашего аккаунта
@bot.message_handler(content_types=["text"])
def main(message):
    if (user_id == message.chat.id):
        comand = message.text
        try:
            bot.send_message(message.chat.id, check_output(comand, shell = True))
        except:
            bot.send_message(message.chat.id, "Invalid input")
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)
