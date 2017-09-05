# pentesterschool: https://t.me/joinchat/AAAAADxx23-T1S9MTK8WnQ
# backconnect : https://t.me/joinchat/AAAAAEMfX635WpKcCd5yyg

import re
import requests
import json
from bs4 import BeautifulSoup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, TelegramError
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters)

from telegram.ext.dispatcher import run_async
import logging
TOKEN = "BOT_TOKEN"

def getAdminCount(channel):
	if channel == "":
		print("No channel entered. ")
	else:
		membersCount = requests.post('https://api.telegram.org/bot'+ TOKEN + '/' + 'getChatMembersCount', data={'chat_id' : channel}).text
		members = json.loads(membersCount)['result']
		bs = BeautifulSoup(requests.get('http://t.me/{}'.format(channel[1:])).text, 'html.parser')
		bs.find('div', class_='tgme_page_extra')
		members2=int(re.sub('[A-Za-z ]','', bs.find('div', class_="tgme_page_extra").text))
		adminCount = members - members2
		return adminCount

def start(bot, update):
	update.message.reply_text("به ربات پیدا کردن تعداد ادمین های  کانال خوش آمدید. برای استفاده از ربات فقط کافیه که شناسه کانال را برای ما بفرستید . \n برای مثال : \n @Channel")

def main_message(bot, update):
	channel_id = update.message.text
	try:
		count = getAdminCount(channel_id)
		update.message.reply_text(text="تعداد ادمین های کانال : {}".format(count))
	except:
		update.message.reply_text(text="کانال مورد نظر یافت نشد")


updater = Updater(TOKEN, workers=32)

dp = updater.dispatcher
logging.info('[+] Robot started')
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, main_message))
# Start the Bot
updater.start_polling()

updater.idle()


