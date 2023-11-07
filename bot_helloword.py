import telepot
import time
 
def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
 
    if content_type == 'text' and msg['text'] == 'oi':
        bot.sendMessage(msg['chat']['id'], 'Olá Mundo!')
 
bot = telepot.Bot('6557010890:AAG1X5OCyP2wMHRnbbN_lQEvtPErZvr5u6g')
 
bot.message_loop(principal)
 
while True:
    time.sleep(5)
