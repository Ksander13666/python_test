#!/usr/bin/python
# coding:utf8

import telebot
import jira.client
from jira.client import JIRA
import re

token='ENTER YOU TOKEN'
bot = telebot.TeleBot(token)
jiraMAIL = JIRA('https://JIRA', basic_auth=('LOGIN', 'PASS'))


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Привет! Введи номер HW таска. \
""")

@bot.message_handler(regexp="^\d{4,}$")
def regexp_message(message):
	issue=jiraMAIL.issue('HW-'+message.text)
	TemaTask=issue.fields.summary
	bot.send_message(message.chat.id, TemaTask)
	ReporTask=issue.fields.reporter.displayName
	bot.send_message(message.chat.id, "Reporter: "+ReporTask)
	TextTask=issue.fields.description
	bot.send_message(message.chat.id, TextTask)
	HostTask=str(issue.fields.customfield_24000)  #hostname
	bot.send_message(message.chat.id, "Hostname: "+HostTask)

	i=0
	a=len(issue.fields.comment.comments)

	while i < a:
		ComTask=issue.fields.comment.comments[i].body
		ComAuthor=issue.fields.comment.comments[i].author.displayName
		i +=1
		bot.send_message(message.chat.id, ComAuthor+': '+ComTask)

bot.polling(none_stop=True)
