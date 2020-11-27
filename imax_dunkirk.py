import requests
import telegram
import time
import calendar

from bs4 import BeautifulSoup
from datetime import datetime
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

# 텔레그램 봇 토큰 
my_token = '1136456443:AAHnhXqpT-NqUZiK909_5017pah7wJ6LQ04'
bot = telegram.Bot(token = my_token)

#시작날짜 및 마지막으로 메세지가 발송된 날짜
date = 20201206
confirm_date = 20201205



while True:
	# date의 용아맥 예매 데이터 크롤링 
	now = datetime.now()
	url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=07&theatercode=0013&date='+ str(date) +'&screencodes=&screenratingcode=02&regioncode=cf'
	response = requests.get(url)
	html = response.text

	# 연월일 마지막 예외처리
	if date - (now.year * 10000 + now.month * 100) > calendar.monthrange(now.year, now.month)[1] and date - (now.year * 10000 + (now.month+1) * 100) < 1:
		if now. month == 12:
			date = (now.year + 1) * 10000 + 101
		else:
			date = now.year * 10000 + (now.month + 1) * 100 + 1
		print(now)
		print('date =', date)
		print('confirm_date =', confirm_date)
		print('다음달로넘어감')
	
	# 스캔을 끝낼 날짜 지정, 이후 5초간 대기
	elif date == 20201211:
		date = confirm_date + 1
		time.sleep(5)
	
	# 영화제목이 크롤링 데이터 내에 있는지 확인후 메세지 전송
	elif str(date) in html:
		if str('덩케르크') in html:
			bot.sendMessage(chat_id = -1001299873599, text = "%d 덩케르크 예매오픈!" % date) 
			confirm_date = date
		print(now)
		print('date =', date)
		print('정상작동중')
		date = date + 1
	
	# 매일 1회 정상작동 메세지 출력, 이후 1분간 휴식
	else:
		if(now.hour == 12 and now.minute == 50):
			bot.sendMessage(chat_id = -1001299873599, text = "%d:%d 용아맥알리미 덩케르크 정상작동중!" % (now.hour, now.minute))
			time.sleep(60)
		print(now)
		print('date =', date)
		print('정상작동중')
		date = date + 1


