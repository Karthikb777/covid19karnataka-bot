from bs4 import BeautifulSoup
import requests
from datetime import date

#search url
url = "https://mobile.twitter.com/DHFWKA/?lang=en"

# gets the link to the daily stats pdf
def twBot():
	res = requests.get(url)
	soup = BeautifulSoup(res.content, 'html5lib')

	link = soup.findAll(class_ = "dir-ltr")
	for item in link:
	#	print(item.prettify())
		if f"Today's Media Bulletin {date.today().strftime('%d/%m/%Y')}" in item.get_text():
		#	print(item.parent.prettify())
			tweet = item.parent
	try:	
		for link in tweet.findAll('a'):
			if "drive.google" in link.text:
		#	print(link)
				with open('link.txt', 'w') as f:
					f.write(link.attrs['data-expanded-url'])
					f.close()
					print(link.attrs['data-expanded-url'])
	except:
		pass

if __name__ == "__main__":
	twBot()
