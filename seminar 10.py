 
# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

from tkinter import *
from bot import send_answer

global answer
global count
count = -1
answer = ''


def NextQ():
     global count
     count += 1
     data = open('user_message.txt', 'r', encoding='utf-8')
     text = data.readlines()
     data.close()
     if count == len(text):
         return 'Больше сообщений нет'
     else:
         return ''.join(text[count])


def PrintNextQ():
     Label(root, text=f'{NextQ()}').grid(column=0, row=2)


def SendAnsver():
     Label.destroy
     global answer
     global count
     answer = entryAnswer.get(1.0, END)
     Label(root, text='Сообщение отправлено').grid(column=2, row=3)
     send_answer(answer, count)
     entryAnswer.delete(1.0, END)
     return 'Сообщение отправлено'


root = Tk()
root.title('Техподдержка')
root.geometry('600x400')


ButtonNext = Button(root, text="Следующий вопрос", command=PrintNextQ)
ButtonNext.grid(column=0, row=6)
ButtonSend = Button(root, text="Отправить ответ", command=SendAnsver)
ButtonSend.grid(column=2, row=6)
ButtonExit = Button(root, text="Выход", command=root.destroy)
ButtonExit.grid(column=1, row=8)

LabelAnswer = Label(root, text="Поле для ответа")
LabelAnswer.grid(column=2, row=1)
entryAnswer = Text(root, width=30, height=10)
entryAnswer.grid(column=2, row=2)


root.mainloop()


# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.


import telebot

bot = telebot.TeleBot(" ")


def send_answer(answer, count):
     data = open('user_id.txt', 'r', encoding='utf-8')
     users_id = data.readlines()
     a = users_id[count]
     bot.send_message(a, f'{answer}')
     data.close()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

     def Help(message):
         user_id = str(message.from_user.id) + '\n'
         data = open('user_id.txt', 'a', encoding='utf-8')
         data.writelines(user_id)
         data.close()
         messageText = str(message.text) + '\n'
         data = open('user_message.txt', 'a', encoding='utf-8')
         data.writelines(messageText)
         data.close()
         bot.send_message(
             message.chat.id, 'Спасибо, ответим в ближайшее время.')

     r = bot.send_message(message.chat.id, 'Здравствуйте, ' +
                          message.from_user.first_name + '. Чем могу помочь?')
     bot.register_next_step_handler(r, Help)


bot.infinity_polling()