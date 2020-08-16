import requests
import telegram
import time
from bs4 import BeautifulSoup
from datetime import datetime

my_token = '1136456443:AAHnhXqpT-NqUZiK909_5017pah7wJ6LQ04'
bot = telegram.Bot(token = my_token)

date = 20200901
confirm_date = 20200900
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=07&theatercode=0013&date=20200831&screencodes=&screenratingcode=02&regioncode=cf'
response = requests.get(url)
html = response.text
while True:
	now = datetime.now()
	if date == 20200905:
		date = confirm_date + 1
		time.sleep(5)
	elif str(date) in html:
		bot.sendMessage(chat_id = -1001299873599, text = "%d 예매오픈!" % date) 
		confirm_date = date
		date = date + 1
	else:
		if(now.hour == 11 and now.minute == 59):
			bot.sendMessage(chat_id = -1001299873599, text = "%d:%d 용아맥알리미 정상작동중!" % (now.hour, now.minute))
		print(now)
		print(date)
		date = date + 1


