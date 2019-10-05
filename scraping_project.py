import requests
from bs4 import BeautifulSoup
from random import choice

i = 1
whole = []  ## [quote, author , url, initials, loc, dob, about]
while True:
	response = requests.get(f"http://quotes.toscrape.com/page/{i}/")
	soup = BeautifulSoup(response.text, 'html.parser')
	try:
		soup.find(class_="next").find('a').get_text()
	except AttributeError:
		break
	else:
		i += 1
	finally:
		data = soup.find_all(class_="quote")
		for d in data:
			quote = d.find(class_="text").get_text()
			author = d.find(class_="author").get_text()
			url = requests.get(f"http://quotes.toscrape.com{d.find('a')['href']}")
			sop = BeautifulSoup(url.text, 'html.parser')
			
			## to get initials of the author
			initials = ''
			parts = author.split(' ')
			for p in parts:
				sub_parts = p.split('.')
				sub = filter(None,sub_parts)
				for s in list(sub):
					initials += s[0]
			
			dob = sop.find(class_='author-born-date').get_text()
			loc = sop.find(class_='author-born-location').get_text()
			abot = sop.find(class_='author-description').get_text()
			abut = abot.replace(author, "******")
			about = abut.split(".")[0]
			whole.append([quote, author, initials, dob, loc,about])

			
## Game logic
while True:
	current = choice(whole)
	print(current[0])
	answer = input("who wrote this quote? You have 4 attempts ")
	attempts = 4
	while answer != current[1]:
		attempts -= 1
		if attempts == 3:
			print(f"Initials of the author are {current[2]}")
		elif attempts == 2:
			print(f"dob and pob of the author are: {current[3]}, {current[4]}")
		elif attempts == 1:
			print(current[5])
		elif attempts == 0:
			break
		answer = input(f"{attempts} attempts remaining: ")
	if answer == current[1]:
		print("You Won :)")
	if attempts == 0:
		print("you lose :/")
	rematch = input("Wanna play again?(y/n) ")
	if rematch == "y":
		pass
	if rematch == "n":
		break










			