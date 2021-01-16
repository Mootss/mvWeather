# Author : Moots (github.com/Mootss)
# Webscraper for Maldives Meteorology Service
# Last updated : 16/01/2021

__version__ = "1.0.0-alpha"

# Importing dependencies
import error 
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Opening the url and parsing the html from it
page = urlopen("https://www.meteorology.gov.mv/")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# narrowing down where to search
res = soup.find("div", class_="row mainwtop")
weElems = res.find("ul", class_="small-block-grid-3 medium-block-grid-5 large-block-grid-5 largelocwrp") 

# searching for the location, temperature and description
locs = weElems.find_all("div", class_="toploc2")
temps = weElems.find_all("div", class_="temp") 
descs = weElems.find_all("div", class_="desc")

'''
0 - Male
1 - Hanimadhoo
2 - Kahdhoo
3 - Kaadehdhoo
4 - Gan
'''

def weather(station= "Male"):

	stations = {
		"male" : 0,
		"hanimadhoo" : 1,
		"kahdhoo" : 2,
		"Kaadehdhoo" : 3,
		"gan" : 4
	}

	err = False

	try:

		if station.lower() not in stations:
			raise error.InvalidArgument("Invalid argument provided")
		err == True
	
	except AttributeError:
		raise error.InvalidArgument("argument must be passed in as a string")

	else:

		if station.lower() in stations and err != True:

			info = {

				"station" : locs[stations[station.lower()]].text.strip(),
				"temp" : temps[stations[station.lower()]].text, 
				"status" : descs[stations[station.lower()]].text
			}

			return info

