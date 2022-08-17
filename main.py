import telebot
from telebot import types


bot = telebot.TeleBot('5482846649:AAEr_5SWB3IrQTlGrHxuWiteNcg9UQFeCE0')
list = ''
adressat = 'https://t.me/IsBeter'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Напитки")
    btn2 = types.KeyboardButton("Пицца")
    btn3 = types.KeyboardButton("Десерты")
    btn4 = types.KeyboardButton("Обнулить заказ")
    btn5 = types.KeyboardButton("Отправить заказ")
    markup.add(btn1, btn2, btn3, btn4,btn5)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Выберите позицию".format(
                         message.from_user), reply_markup=markup)



@bot.message_handler(content_types=['text'])
def func(message):
    global list
    if (message.text == "Напитки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Кола")
        btn2 = types.KeyboardButton("Спрайт")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Напитки", reply_markup=markup)
    elif (message.text == "Пицца"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Маргарита")
        btn2 = types.KeyboardButton("Грибная")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Пицца", reply_markup=markup)

    elif (message.text == "Десерт"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пирожок")
        btn2 = types.KeyboardButton("Мороженое")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Десерт", reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Напитки")
        btn2 = types.KeyboardButton("Пицца")
        btn3 = types.KeyboardButton("Десерт")
        btn4 = types.KeyboardButton("Обнулить заказ")
        btn5 = types.KeyboardButton("Отправить заказ")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif(message.text == "Обнулить заказ"):
        list = ''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Напитки")
        btn2 = types.KeyboardButton("Пицца")
        btn3 = types.KeyboardButton("Десерт")
        btn4 = types.KeyboardButton("Обнулить заказ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        templist = list
        if templist == '' :
            templist = "Нет позиций"
        bot.send_message(message.chat.id, text="Ваш заказ:\n" + templist, reply_markup=markup)
    elif (message.text == "Отправить заказ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Напитки")
        btn2 = types.KeyboardButton("Пицца")
        btn3 = types.KeyboardButton("Десерт")
        btn4 = types.KeyboardButton("Обнулить заказ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Ваш заказ:\n" + list + "\n" + "Заказ отправим: " + adressat, reply_markup=markup)
    else:
        list += message.text + '\n'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Напитки")
        btn2 = types.KeyboardButton("Пицца")
        btn3 = types.KeyboardButton("Десерт")
        btn4 = types.KeyboardButton("Обнулить заказ")
        btn5 = types.KeyboardButton("Отправить заказ")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        templist = list
        if templist == '' :
            templist = "Нет позиций"
        bot.send_message(message.chat.id, text="Ваш заказ:\n" + templist, reply_markup=markup)





bot.polling(none_stop=True)