
# -*- coding: utf-8 -*-
import telebot
bot = telebot.TeleBot("7600951342:AAE_FTva76FuozChuLWggGSULXjRCoC5YpQ")

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Оклад по званию?  ⭐')
    bot.register_next_step_handler(message, num1_fun)

def validate_input(min_value, max_value):
    def decorator(func):
        def wrapper(message, *args, **kwargs):
            if message.text.isdigit():
                salary = int(message.text)
                if min_value <= salary <= max_value:
                    bot.send_message(message.chat.id, f'Подходит ✅ {salary}')
                    return func(message, *args, **kwargs)
                else:
                    bot.send_message(message.chat.id, 'Укажи верное значение 🐒')
            else:
                bot.send_message(message.chat.id, 'Это должно быть число 🐒')
            bot.register_next_step_handler(message, lambda msg: wrapper(msg, *args, **kwargs))
        return wrapper
    return decorator

def next_step(message, func, data):
    bot.register_next_step_handler(message, lambda msg: func(msg, data))

@validate_input(7000, 35000)
def num1_fun(message):
    data = {}
    data['num1'] = int(message.text)
    bot.send_message(message.chat.id, 'Оклад по должности?  👮')
    next_step(message, num2_fun, data)

@validate_input(15000, 35000)
def num2_fun(message, data):
    data['num2'] = int(message.text)
    bot.send_message(message.chat.id, 'Процентная надбавка за выслугу лет?  📅')
    text_with_markdown_table = """
    ```
    |   период    |   процент   |
    |-------------|-------------|
    | 10 - 15 лет |    20  %    |
    | 15 - 20 лет |    25  %    |
    | 20 - 25 лет |    30  %    |
    | 25 и больше |    40  %    |
    ```
    """
    bot.send_message(message.chat.id, text_with_markdown_table, parse_mode='Markdown')
    next_step(message, num3_fun, data)

@validate_input(10, 40)
def num3_fun(message, data):
    data['num3'] = int(message.text)
    bot.send_message(message.chat.id, 'Размер пенсии в процентах?  💵')
    text_with_markdown_table = """
    ```
    |    стаж     |   процент   |
    |-------------|-------------|
    |   20 лет    |    50  %    |
    |   21 лет    |    53  %    |
    |   22 лет    |    56  %    |
    |   23 лет    |    59  %    |
    |   24 лет    |    62  %    |
    |   25 лет    |    65  %    |
    |   26 лет    |    68  %    |
    |   27 лет    |    71  %    |
    |   28 лет    |    74  %    |
    |   29 лет    |    77  %    |
    |   30 лет    |    80  %    |
    |   31 лет    |    83  %    |
    |   32 лет    |    85  %    |
    ```
    """
    bot.send_message(message.chat.id, text_with_markdown_table, parse_mode='Markdown')
    next_step(message, num4_fun, data)

@validate_input(50, 85)
def num4_fun(message, data):
    data['num4'] = int(message.text)
    num5_fun(message, data)

def num5_fun(message, data):
    num1 = data['num1']
    num2 = data['num2']
    num3 = data['num3']
    num4 = data['num4']

    # Расчет значений
    A = num1 + num2
    B = A * num3 / 100
    X = A + B
    C = X * 0.8983
    result = C * num4 / 100

    bot.send_message(message.chat.id, f'Результат: {result:.2f}')

bot.polling(none_stop=True)
