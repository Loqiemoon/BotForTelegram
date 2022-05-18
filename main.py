import telebot
from telebot import types
bot = telebot.TeleBot('1710954735:AAGBciQIaewG_wuUXEzKnb3H_uKAl3KyrC0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Выбирай занятие под настроение:", reply_markup=knopki)


knopki = types.InlineKeyboardMarkup(row_width=1)
button1 = types.InlineKeyboardButton(" -Идём гулять", callback_data='walk')
button2 = types.InlineKeyboardButton(" -Идём есть(пить)", callback_data='eat')
button3 = types.InlineKeyboardButton(" -Идем в кино", callback_data='cinema')
button4 = types.InlineKeyboardButton(" -Сидим дома и смотрим...", callback_data='home')
knopki.add(button1, button2, button3, button4)

snova = types.ReplyKeyboardMarkup(row_width=1)
button1 = types.KeyboardButton(" /start")
snova.add(button1)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "walk":
                bot.send_message(call.message.chat.id, "Вопрос куда?", reply_markup=knopki1)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            if call.data == "eat":
                bot.send_message(call.message.chat.id, "Здесь немного поподробнее", reply_markup=knopki2)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            if call.data == "cinema":
                bot.send_message(call.message.chat.id, "Кто выбирает?", reply_markup=knopki3)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            if call.data == "home":
                bot.send_message(call.message.chat.id, "Что хочешь посмотреть?", reply_markup=knopki4)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            if call.data == "city" or call.data == "park" or call.data == "crazy":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(774162980, call.data)
                bot.send_message(call.message.chat.id, "Всё будет)", reply_markup=snova)
            if call.data == "shava" or call.data == "MD" or call.data == "cafe" or call.data == "dorogo" or call.data == "bar":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(774162980, call.data)
                bot.send_message(call.message.chat.id, "Всё будет)", reply_markup=snova)
            if call.data == "i" or call.data == "you" or call.data == "we":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(774162980, call.data)
                bot.send_message(call.message.chat.id, "Всё будет)", reply_markup=snova)
            if call.data == "film" or call.data == "serial" or call.data == "multiki":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(774162980, call.data)
                bot.send_message(call.message.chat.id, "Всё будет)", reply_markup=snova)
    except Exception as e:
        print(repr(e))


knopki1 = types.InlineKeyboardMarkup(row_width=1)
button1 = types.InlineKeyboardButton(" -Простая прогулка по городу", callback_data='city')
button2 = types.InlineKeyboardButton(" -Идем в парк", callback_data='park')
button3 = types.InlineKeyboardButton(" -ТВОРИТЬ ДИЧЬ", callback_data='crazy')
knopki1.add(button1, button2, button3)

knopki2 = types.InlineKeyboardMarkup(row_width=1)
button1 = types.InlineKeyboardButton(" -За шавой", callback_data='shava')
button2 = types.InlineKeyboardButton(" -В мак", callback_data='MD')
button3 = types.InlineKeyboardButton(" -В кафе", callback_data='cafe')
button4 = types.InlineKeyboardButton(" -В ресторан", callback_data='dorogo')
button5 = types.InlineKeyboardButton(" -ВЫПЬЕМ", callback_data='bar')
knopki2.add(button1, button2, button3, button4, button5)

knopki3 = types.InlineKeyboardMarkup(row_width=1)
button1 = types.InlineKeyboardButton(" -Я", callback_data='i')
button2 = types.InlineKeyboardButton(" -Ты", callback_data='you')
button3 = types.InlineKeyboardButton(" -Вместе", callback_data='we')
knopki3.add(button1, button2, button3)

knopki4 = types.InlineKeyboardMarkup(row_width=1)
button1 = types.InlineKeyboardButton(" -Фильм", callback_data='film')
button2 = types.InlineKeyboardButton(" -Сериал", callback_data='serial')
button3 = types.InlineKeyboardButton(" -Мультики", callback_data='multiki')
knopki4.add(button1, button2, button3)

bot.polling(none_stop=True)
