import telepot
import time

def principal(mgs):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg[ 'chat'] ['id']
        mensagem = msg['text']

    if mensagem =='oi':
        bot.sendMessage(chat_id, 'Olá Mundo!')

bot = telepot.Bot('6557010890:AAG1X5OCyP2wMHRnbbN_lQEvtPErZvr5u6g')

bot.message_loop(principal)

while True:
    time.sleep(5)
