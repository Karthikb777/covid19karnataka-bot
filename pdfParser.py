import PyPDF2 as pdf
import re
from datetime import date, timedelta

def parsePdf():
#  opens the pdf file and reads the data
	src = open('src.pdf','rb')
#	print(src)
	pdffile = pdf.PdfFileReader(src)
	page1 = pdffile.getPage(0)
	t = page1.extractText()
	x = t.replace("\n","").replace(t[t.find("("):t.find(")")],"")
	d = date.today()
#  removing some unnecessary stuff that always messes things up
	cleaned = x.replace(f"({(d - timedelta(days=1)).strftime('%d/%m/%Y')}, 00:00 to 23:59)","")

#  assigns all the required data to the variables
	try:
		discharges = re.findall("Discharges [0-9]+", cleaned)
		print(discharges[0])
		totalDischarges = re.findall("Total Discharges [0-9]+", cleaned)
		print(totalDischarges[0])
		new = re.findall("New Cases Reported  [0-9]+", cleaned)
		print(new[0])
		active = re.findall("Total Active Cases [0-9]+", cleaned)
		print(active[0])
		total = re.findall("Total Positive Cases [0-9]+", cleaned)
		print(total[0])
		newDeaths = re.findall("New Covid Deaths [0-9]+", cleaned)
		print(newDeaths[0])
		totalDeaths = re.findall("Total Covid Deaths [0-9]+", cleaned)
		print(totalDeaths[0])
	
#  writes all the required data to a '.txt' file to be accessed by the bot
	
		with open("src.txt", "w") as f:
			f.write(f"{active[0]},\n{new[0]},\n{total[0]},\n{discharges[0]},\n{totalDischarges[0]},\n{newDeaths[0]},\n{totalDeaths[0]}")
			f.close()
				
	except:
		print("some error occured")
		with open("src.txt", "w") as f:
			f.write("err:True")
			f.close()
	
	src.close()
	
if __name__ == "__main__":
	parsePdf()	