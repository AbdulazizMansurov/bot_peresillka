from data import bot
from telebot.types import Message
from config import *

@bot.message_handler(chat_types=["supergroup", "group"], func=lambda message: message.chat.id in groups)
def reaction_to_message(message: Message):
    group_id = message.chat.id
    from_user_id = message.from_user.id
    for link in link_of_admins:
        if link in message.text:
            text = f"""Сообщение!
Название группы: {message.chat.title}
Отправитель: {message.from_user.first_name}, @{message.from_user.username}
Текст: <b>{message.text}</b>"""
            bot.send_message(group_id_of_admins, text)
