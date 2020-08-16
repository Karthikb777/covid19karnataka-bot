import wget
import os

def download():
	#removes the old pdf file and downloads the latest pdf file.
	os.remove("src.pdf")
	with open("link.txt", "r") as f:
		link = f.read().split("/")
		f.close()

	for i in range(len(link)):
		if link[i] == "d":
		#print(link[i+1])
			id_ = link[i+1]
		
	url = f"https://drive.google.com/u/0/uc?id={id_}&export=download"	
	wget.download(url, "src.pdf")
	
	
