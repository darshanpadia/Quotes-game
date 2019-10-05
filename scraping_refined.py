import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter


BASE_URL = "http://quotes.toscrape.com"
all_quotes = []
ext_url = "/page/1/"

def scraping():
	global ext_url               #### This is how you call global variable 
	url = f"{BASE_URL}{ext_url}"   ## no need to make local BASE_URL global as its only referenced as it is, not updated.
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	quotes = soup.find_all(class_="quote")
	for quote in quotes:
		initials = ''
		author = quote.find(class_="author").get_text()
		parts = author.split(' ')

		## hints content
		for part in parts:
			sub_parts = part.split('.')
			sub = filter(None,sub_parts)
			for s in list(sub):
				initials += s[0]
		author_url = quote.find('a')['href']
		res = requests.get(f"{BASE_URL}{author_url}")
		sop = BeautifulSoup(res.text, 'html.parser')
		dob = sop.find(class_='author-born-date').get_text()
		loc = sop.find(class_='author-born-location').get_text()
		abot = sop.find(class_='author-description').get_text()
		abut = abot.replace(author, "******")
		about = abut.split(".")[0]
		all_quotes.append({ 'initials' : initials,    ## Why not make all_quotes global
			'dob' : dob,                              ## (more of why it isnt required(why does it work!))
			'text' : quote.find(class_="text").get_text(),    ###  
			'author' : author,
			'loc' : loc,
			'about' : about
		})
	page = soup.find(class_='next')
	ext_url = page.find('a')['href'] if page else None # Not put global as prefix here(global ext_url), it gets updated
	while ext_url:
		scraping()
	return all_quotes

quotes = scraping()
	
with open('quotes.csv', 'w',encoding = 'utf-8') as file:               ##  .encode('utf8') to prevent UnicodeDecode Error
	headers = ['initials', 'dob' , 'text', 'author', 'loc', 'about']   ##   while opening such files
	csv_writer = DictWriter(file,fieldnames = headers) 
	csv_writer.writeheader()
	for quote in quotes:
		csv_writer.writerow(quote)











