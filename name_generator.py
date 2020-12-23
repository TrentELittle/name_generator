"""--------------------Name Generator-----------------------"""
# Dependencies
import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import random

#---------------------------------------------------------------------
#------------------Creation of List of Names--------------------------

# Create empty lists for boy names and girl names
boys_names = []
girls_names = []

# Define url's for the list of boy and girl names to scrape
b_url = 'https://www.verywellfamily.com/top-1000-baby-boy-names-2757618'
g_url = 'https://www.verywellfamily.com/top-1000-baby-girl-names-2757832'

# Set response for urls
b_response = requests.get(b_url)
g_response = requests.get(g_url)

# Use bs to clean the html
b_soup = bs(b_response.text, 'html.parser')
g_soup = bs(g_response.text, 'html.parser')


# Find the list within html and use for loop to append names into lists for boys and girls
b_list = b_soup.find('ol')
b_names = b_list.find_all('li')
for b in b_names:
	result = b.text.strip()
	boys_names.append(result)
# print(boys_names)

g_list = g_soup.find('ol')
g_names = g_list.find_all('li')
for g in g_names:
	result = g.text.strip()
	girls_names.append(result)
# print(girls_names)


#-------------------------------------------------------------------
#===================Main Function for name generator================

print("Hello! Welcome to the First & Middle Name Generator!\n")

while True:
	choice = input("Do you want a Boy's name (b), Girl's name (g), or a Suprise (s)?\n"
				   "Enter the corresponding letter within parenthesis for your choice.\n")
	if choice.lower() == "b":
		firstName = random.choice(boys_names)
		middleName = random.choice(boys_names)
		
		print("\n\n")
		print("{} {}".format(firstName, middleName), file=sys.stderr)
		print("\n\n")

		try_again = input("\n\nTry again? (Press Enter, else enter 'Q' to quit)\n")
		if try_again.upper() == 'Q':
			break
	elif choice.lower() == "g":
		firstName = random.choice(girls_names)
		middleName = random.choice(girls_names)
		
		print("\n\n")
		print("{} {}".format(firstName, middleName), file=sys.stderr)
		print("\n\n")

		try_again = input("\n\nTry again? (Press Enter, else enter 'Q' to quit)\n")
		if try_again.upper() == 'Q':
			break
	elif choice.lower() == "s":
		res = random.choice([True, False])
		if res == "True":
			firstName = random.choice(boys_names)
			middleName = random.choice(boys_names)
			
			print("\n\n")
			print("{} {}".format(firstName, middleName), file=sys.stderr)
			print("\n\n")

			try_again = input("\n\nTry again? (Press Enter, else enter 'Q' to quit)\n")
			if try_again.upper() == 'Q':
				break
		else:
			firstName = random.choice(girls_names)
			middleName = random.choice(girls_names)
			
			print("\n\n")
			print("{} {}".format(firstName, middleName), file=sys.stderr)
			print("\n\n")

			try_again = input("\n\nTry again? (Press Enter, else enter 'Q' to quit.)\n")
			if try_again.upper() == 'Q':
				break
	else:
		try_again = ("Incorrect Entry. Try Again? (Press Enter, else enter 'Q' to quit.)\n")
		if try_again.upper == "Q":
			break
print("Enjoy the new name!")		
	

