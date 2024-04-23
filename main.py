import telebot
from telebot import types
from requests.exceptions import ConnectionError, Timeout
from config import TOKEN
import time

bot = telebot.TeleBot(TOKEN)

MAX_RETRIES = 5
RETRY_DELAY = 5  

def listener(messages):
    for message in messages:
        if message.content_type == 'text':
            chat_id = message.chat.id
            text = message.text
            print(f"Отримано повідомлення: {text}")
            handle_message(message)

bot.set_update_listener(listener)

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

def handle_message(message):
    for _ in range(MAX_RETRIES):
        try:
            if message.text == "Показати сьогоднішнє меню":
                with open("menu.txt", "r", encoding="utf-8") as file:
                    menu_text = file.read()
                bot.reply_to(message, menu_text)
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
            break
        except Timeout:
            print(f"Timeout error, retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
        except telebot.apihelper.ApiTelegramException as e:
            if e.error_code == 502:  # Bad Gateway
                print(f"Bad Gateway error, retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                raise e
    else:
        print("Maximum number of retries reached. Skipping message.")

if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout = 5)
        except ConnectionError as e:
            print(f"Connection error during polling: {e}")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"Unhandled error during polling: {e}")
            time.sleep(5)
            break