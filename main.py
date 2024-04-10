import telebot
from telebot import types
from requests.exceptions import ConnectionError
from config import TOKEN
import time

# YOUR_BOT_TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Вітання! Я бот для показу сьогоднішнього меню. Натисніть кнопку, щоб побачити меню.")
    show_menu_button(message)

def show_menu_button(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = types.KeyboardButton("Показати сьогоднішнє меню")
    contact_button = types.KeyboardButton("Показати контакти")
    markup.add(item, contact_button)
    bot.send_message(message.chat.id, "Виберіть дію:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Показати сьогоднішнє меню":
        try:
            with open("menu.txt", "r", encoding="utf-8") as file:
                menu_text = file.read()
            bot.reply_to(message, menu_text)
            show_menu_button(message)
        except Exception as e:
            print(f"Error reading menu file: {e}")
            bot.reply_to(message, "Сталася помилка при зчитуванні меню. Спробуйте ще раз.")
            show_menu_button(message)
    elif message.text == "Показати контакти":
        contact_info = "Вінниця\n" \
                   "вул. М. Литвиненко-Вольгемут, 5\n" \
                   "Email: info@medilux.ua\n" \
                   "Телефон: 0 800 330 130"
        bot.send_message(message.chat.id, contact_info)
        show_menu_button(message)
    else:
        bot.reply_to(message, "Я не розумію, спробуй ще раз.")
        show_menu_button(message)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=3)
        except ConnectionError as e:
            print(f"Connection error during polling: {e}")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"Unhandled error during polling: {e}")
            time.sleep(5)
            break
