from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Swaggy')



bot.set_trainer(ListTrainer)

for _file in os.listdir('files'):
    chats=open('files/' + _file,'r').readlines()
    bot.train(chats)





name=input('Swaggy:what is your name?')

while True:
    reqest = input(name + ':')
    response = bot.get_response(reqest)
    print('Swaggy:',response)
