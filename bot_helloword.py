#!/usr/bin/python3
# coding: utf-8

import telepot

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        mensagem = msg['text']

    if mensagem == 'oi':
        bot.sendMessage(chat_id, 'olá Mundo')

bot = telepot.Bot('6557010890:AAG1X5OCyP2wMHRnbbN_lQEvtPErZvr5u6g')

bot.message_loop(principal)
