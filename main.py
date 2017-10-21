import telebot
import db

import pymysql
import pymysql.cursors



token = "400994008:AAF_AngoYyaakmuAhsv63kSR_fXkO6NA8ek"
bot = telebot .TeleBot(token)

print(bot.get_me())

def log(message,answer):
    print("\n ------------")
    from _datetime import datetime
    print(datetime.now())
    print("Сообщение от (0) (1). (id = (2)) \n Текст: (3)".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)



@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message (message.chat.id, "Начнём💸	" + "\r\n\r\n\r\nДля начала я даю тебе " + str(db.startBonus)+ " рублей💰" +
                                                    "\r\n\r\nА благодаря этому боту можно влёгкую поднять денег!👑 " +
                                                    "\r\n\r\nВсеголишь угадывая монету. " +
                                                    "\r\n\r\nПрямо сейчас можешь начать зарабатывать!")

    conn = pymysql.connect(user='root', password='0000', host='localhost', database='eagletilesbot')

    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()
    def getid(idi):  # проверяем есть ли id пользователя в базе
        query = 'INSERT INTO eagletilesbot.bd (id,balance) VALUES (' + str(message.chat.id) + ',' + str(db.startBonus)+');'
        try:
            cursor.execute(query)
            conn.commit()
            print('Insert new id.')

        except pymysql.Error as error:
            select = 'SELECT id FROM eagletilesbot.bd WHERE id = (' + str(message.chat.id) + ');'
            cursor.execute(select)
            conn.commit()
            print(error)
        finally:
            conn.close()
            print('Connection closed.')

    getid(message.chat.id)



@bot.message_handler(commands=['balance'])
def handle_text(message):
    def getbalance(idi):
        conn = pymysql.connect(user='root', password='0000', host='localhost', database='eagletilesbot')

        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
        checkBalance = 'SELECT balance FROM eagletilesbot.bd WHERE id = ' + str(message.chat.id)+';'
        try:
            cursor.execute(checkBalance)
            conn.commit()
            results = cursor.fetchone()
            print(results)
            bot.send_message(message.chat.id,"Твой баланс "+str(results)+" 💰")
        except pymysql.Error as error:
            print(error)
        finally:
            conn.close()
            print('Connection closed.')
    getbalance(message.chat.id)

bot.polling(none_stop=True,interval=0)