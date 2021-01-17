# Author : Moots (github.com/mootss)
# A simple python web scraper that retrieves Maldives weather information from meteorology.gov.mv
# This is mainly a personal project that I'm doing for learning more about web scraping

__version__ = "1.0.0"
__author__ = "Moots"

# Importing dependencies
import error
import scrap

args = [
    "male",
    "hanimadhoo",
    "kahdhoo",
   	"kaadehdhoo",
   	"gan"
   	]

def weather(arg="male"):

    if arg.lower() not in args: # check if the provided arg is in stations, raises error if not
        raise error.InvalidArgument(f'Invalid station name provided\nAvailable stations: {args}')

    if arg.lower() in args:

        return scrap.getWeather(arg)
 



print(weather())