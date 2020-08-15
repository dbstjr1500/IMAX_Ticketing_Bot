import requests
import telegram
from bs4 import BeautifulSoup
from datetime import datetime

my_token = '1136456443:AAHnhXqpT-NqUZiK909_5017pah7wJ6LQ04'
bot = telegram.Bot(token = my_token)
now = datetime.now()


date = 20200901
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=07&theatercode=0013&date=20200831&screencodes=&screenratingcode=02&regioncode=cf'
response = requests.get(url)
html = response.text
while date <= 20200905:
	if str(date) in html:
		bot.sendMessage(chat_id = -1001299873599, text = "%d 예매오픈!" % date) 
	else:
		if(now.hour == 4 and now.minute == 25):
			bot.sendMessage(chat_id = -1001299873599, text = "04:25 용아맥알리미 정상작동중!" % date)
		print(now)
		print(date)
	date = date + 1


