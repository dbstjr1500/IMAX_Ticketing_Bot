import requests
import telegram
import time
import calendar

from bs4 import BeautifulSoup
from datetime import datetime


my_token = '1136456443:AAHnhXqpT-NqUZiK909_5017pah7wJ6LQ04'
bot = telegram.Bot(token = my_token)


# Telegram test reply function
def test_command(bot, update) :
    update.message.reply_text("용아맥알리미 정상작동중")

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('test', test_command)
updater.dispatcher.add_handler(test_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()



date = 20200830
confirm_date = 20200900
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=07&theatercode=0013&date=20200831&screencodes=&screenratingcode=02&regioncode=cf'
response = requests.get(url)
html = response.text

while True:
	now = datetime.now()
	
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
		bot.sendMessage(chat_id = -1001299873599, text = "%d 예매오픈!" % date) 
		confirm_date = date
		date = date + 1
	
	else:
		if(now.hour == 8 and now.minute == 10):
			bot.sendMessage(chat_id = -1001299873599, text = "%d:%d 용아맥알리미 정상작동중!" % (now.hour, now.minute))
		print(now)
		print('date =', date)
		print('정상작동중')
		date = date + 1


