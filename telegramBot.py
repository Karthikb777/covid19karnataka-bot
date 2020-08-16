import telebot
from twitterBot import twBot
from downloader import download
from pdfParser import parsePdf

def getData():
	twBot()
	download()
	parsePdf()

def telegramBot():
	API_KEY = "YOUR API KEY"
	bot = telebot.TeleBot(API_KEY, parse_mode="none")
#  welcome message	
	@bot.message_handler(commands=['start', 'help'])
	
# the refresh command is not included in the welcome message because I don't want everyone to spam refresh messages
	def hello(message):
		  bot.reply_to(message,"I provide the latest stats of covid19 in Karnataka.\n\nHere are the commands: \nData - To get the current stats.\n/help - To get the commands and details.\n\nThe source of the data is the official twitter handle of Karnataka Health Dept.")
		  
#  Data provider(and refresher)		
	@bot.message_handler(func=lambda m:True)
	def todayData(message):
		if (message.text == "update" or message.text == "Update"):
			getData()
			with open("src.txt","r") as f:
				if f.read() == "err:True":
					reply = "Some error occured!"
				else:
					reply = "Refreshed successfully!"
				f.close()
			bot.reply_to(message, reply)
		if (message.text == "data" or message.text == "Data"):
		  	with open("src.txt", "r") as f:
		  		data = f.read()
		  		f.close()
		  	payload = f"Covid-19 Karnataka Stats: \n\n{data}\n\n"
		  	bot.reply_to(message, payload)
	  
#  sleeps for 5 seconds before requesting telegram's server for any new messages
	bot.polling(interval=5)
	
#  To keep the main thread running
	while True:
		pass
		
if __name__ == "__main__":
	  print("bot running...")
	  telegramBot()
	  
	  
	  
	  
	  
 
