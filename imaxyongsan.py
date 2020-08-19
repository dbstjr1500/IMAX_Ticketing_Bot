import requests
import telegram
import time
import calendar

from bs4 import BeautifulSoup
from datetime import datetime
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)


my_token = '1136456443:AAHnhXqpT-NqUZiK909_5017pah7wJ6LQ04'
bot = telegram.Bot(token = my_token)


date = 20200819
confirm_date = 20200818


while True:
	now = datetime.now()
	url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=07&theatercode=0013&date='+ str(date) +'&screencodes=&screenratingcode=02&regioncode=cf'
	response = requests.get(url)
	html = response.text

	if date - (now.year * 10000 + now.month * 100) > calendar.monthrange(now.year, now.month)[1] and date - (now.year * 10000 + (now.month+1) * 100) < 1:
		if now. month == 12:
			date = (now.year + 1) * 10000 + 101
		else:
			date = now.year * 10000 + (now.month + 1) * 100 + 1
		print(now)
		print('date =', date)
		print('confirm_date =', confirm_date)
		print('다음달로넘어감')
	
	elif date == 20200905:
		date = confirm_date + 1
		time.sleep(5)
	
	elif str(date) in html:
		if str('테넷') in html:
			bot.sendMessage(chat_id = -1001299873599, text = "%d 테넷 예매오픈!" % date) 
			confirm_date = date
		print(now)
		print('date =', date)
		print('정상작동중')
		date = date + 1
	
	else:
		if(now.hour == 8 and now.minute == 10):
			bot.sendMessage(chat_id = -1001299873599, text = "%d:%d 용아맥알리미 정상작동중!" % (now.hour, now.minute))
			time.sleep(60)
		print(now)
		print('date =', date)
		print('정상작동중')
		date = date + 1


