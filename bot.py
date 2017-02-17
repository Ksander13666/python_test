#!/usr/bin/python
# coding:utf8
import telepot
import os, sys
import time
import re
from grab import Grab

bot=telepot.Bot('Enter you TOKEN')
g = Grab()

#def handle(msg):
#	mesg1=msg

#bot.message_loop(handle)

#mesg=bot.getUpdates()
#mesg1=bot.getUpdates(mesg[0].get('update_id')+1)
while 1:
	mesg=bot.getUpdates()
	#mesg1=bot.getUpdates(mesg[0].get('update_id')+1)
	if mesg: 
		#mesg1=bot.getUpdates(mesg[0].get('update_id')+1)
		EdMsg=mesg[0].get(u'message')
		if EdMsg:
			ChatID=mesg[0].get(u'message').get(u'from').get(u'id')
                        TExt=mesg[0].get(u'message').get(u'text')
		else:
			ChatID=mesg[0].get(u'edited_message').get(u'from').get(u'id')
			TExt=mesg[0].get(u'edited_message').get(u'text')
#mesg=bot.getUpdates()
#mesg1=bot.getUpdates(mesg[0].get('update_id')+1)
#ChatID=mesg[0].get(u'message').get(u'from').get(u'id')
#TExt=mesg[0].get(u'message').get(u'text')
		mesg1=bot.getUpdates(mesg[0].get('update_id')+1)
		if TExt.isdigit():
   			g.setup(cookies={'JSESSIONID': 'ENTER YOUR COOKIE'})
        		g.go('https://jira.mail.ru/browse/HW-'+TExt)
        		task=g.response.body
			LogYes=re.findall(r'Войти в Jira', task)
			if LogYes:
				bot.sendMessage(ChatID, "Login Fail")
			else:
        			TaskServer=re.findall(r'.<div class="flooded">(.*?)</div', task, re.DOTALL)
				TaskContent=re.findall(r'.<div class="user-content-block">(.*?)</div', task, re.DOTALL)
				if TaskServer:
       					Server=re.sub(r'\s+Total.*', '', re.sub(r'\n', ' ', TaskServer[1]).strip())
       			#		task2=re.findall(r'.<div class="user-content-block">(.*?)</div', task, re.DOTALL)
					if TaskContent:
                                        	#print 123123123
                                        	Telo=re.sub(r'<p>|<a>|<br/>|</p>|</a>', '', TaskContent[0].strip())
                                        	Telo1=Telo.split('<')[0]
                                        	#bot.sendMessage(ChatID, Server)
                                        	bot.sendMessage(ChatID, Telo1)
						bot.sendMessage(ChatID, Server)
                                	else:
                                        	bot.sendMessage(ChatID, Server)
				else:
					if TaskContent:
						Telo=re.sub(r'<p>|<a>|<br/>|</p>|</a>', '', TaskContent[0].strip())
                                		Telo1=Telo.split('<')[0]
#                                bot.sendMessage(ChatID, Server)
                                		bot.sendMessage(ChatID, Telo1)

				#if task2:
	       				#print 123123123
				#	Telo=re.sub(r'<p>|<a>|<br/>|</p>|</a>', '', task2[0].strip())
				#	Telo1=Telo.split('<')[0]
       					#bot.sendMessage(ChatID, Server)
       				#	bot.sendMessage(ChatID, Telo1)
					else:
						bot.sendMessage(ChatID, "FAIL!!!")
		else:
        		bot.sendMessage(ChatID, 'Fail! Enter number')
			print "FAIL!"
	else:
		next


#bot.polling()
#bot.message_loop(handle)
