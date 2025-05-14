
import json
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7612152837:AAGS68HRoCcPuxiD8uhMsFxWP3vuBwIa3YA"
OWNER_ID = 7573442239  # Цифрами, без кавычек
CHANNEL_LINK = "https://t.me/nexxor404bio"

bot = telebot.TeleBot(BOT_TOKEN)

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_user(user_id):
    users = load_users()
    if user_id not in users:
        users.append(user_id)
        with open("users.json", "w") as f:
            json.dump(users, f)

@bot.message_handler(commands=["start"])
def start_handler(message):
    user_id = message.from_user.id
    save_user(user_id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Перейти в канал", url=CHANNEL_LINK))
    bot.send_message(user_id, "Нажми на кнопку, чтобы перейти в мой канал:", reply_markup=markup)

@bot.message_handler(commands=["check"])
def check_users(message):
    if message.from_user.id == OWNER_ID:
        users = load_users()
        bot.send_message(message.chat.id, f"Количество переходов: {len(users)}
ID пользователей:
" + "\n".join(map(str, users)))
    else:
        bot.send_message(message.chat.id, "Недостаточно прав.")

bot.polling()
