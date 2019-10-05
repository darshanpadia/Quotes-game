from csv import DictReader
from random import choice 

def read_data():
	with open('quotes.csv',encoding = 'utf-8') as file:
		csv_reader = DictReader(file) 
		return list(csv_reader)

def play_game(data):
	answer = ''
	current = choice(data)
	print(f"Here's a quote:\n {current['text']}\n Can you guess who said it?")
	print(current['author'])
	attempts = 4
	while answer != current['author'].lower() and attempts>0:
		if attempts == 3:
			print(f"Here's a hint:\nInitials of the author are {current['initials']}")
		elif attempts == 2:
			print(f"Here's another hint:\n***** was born in {current['dob']} {current['loc']}")
		elif attempts == 1:
			print(f"Here's a final hint:\n {current['about']}")
		answer = input(f"You have {attempts} attempts remaining: ").lower()
		attempts -= 1
	if answer == current['author'].lower():
		print("You Win :D ")
	elif attempts == 0:
		print(f"You Lose :/\nCorrect Answer is {current['author']}")
	rematch = ''
	while rematch not in ['yes', 'y', 'no', 'n']:
		rematch = input("Wanna play again?(y/n) ").lower()
	if rematch == "y":
		play_game(data)
	if rematch == "n":
		print("GOODBYE")

data = read_data()
play_game(data)



	