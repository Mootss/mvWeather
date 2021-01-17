# scraper for mvWeather

# importing stuff
import json, error
from urllib.request import urlopen
from bs4 import BeautifulSoup



def getWeather(station):

	# Opening the url and parsing the html from it
	try:
		page = urlopen("https://www.meteorology.gov.mv/")

	except HTTPError:
		try:
			page = urlopen("https://www.meteorology.gov.mv/")
		except HTTPError:
			raise error.HTTPError500("Error 500: Internal Server Error")

	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	# narrowing down where to search
	weTop = soup.find("div", class_="row mainwtop")
	weElems = weTop.find("ul", class_="small-block-grid-3 medium-block-grid-5 large-block-grid-5 largelocwrp")

	weContent = soup.find("div", class_="row mainwcontent")
	weParams = weContent.find("ul", class_="large-12 medium-12 small-12 columns wparamstabsc general_w")
	tideParams = weContent.find("ul", class_="large-12 medium-12 small-12 columns wparamstabsc tparamstabsc general_t")
	threeDayF = weContent.find("div", class_="large-12 medium-12 small-12 columns threedaywrp")


	# searching for the stuffs we want
	locs = weElems.find_all("div", class_="toploc2")
	temps = weElems.find_all("div", class_="temp") 
	descs = weElems.find_all("div", class_="desc")

	# weather params
	sunrise = weParams.find("div", id="sunrise")
	sunset = weParams.find("div", id="sunset")
	moonrise = weParams.find("div", id="moonrise")
	moonset = weParams.find("div", id="moonset")
	humidity = weParams.find("div", id="humidity")
	rainfall = weParams.find("div", id="rainamount")
	wind = weParams.find("div", id="wind")
	sunshine = weParams.find("div", id="sunshine")

	# tide params
	high1 = tideParams.find("div", id="high1")
	high1time = tideParams.find("div", id="high1time")
	high2 = tideParams.find("div", id="high2")
	high2time = tideParams.find("div", id="high2time")
	low1 = tideParams.find("div", id="low1")
	low1time = tideParams.find("div", id="low1time")
	low2 = tideParams.find("div", id="low2")
	low2time = tideParams.find("div", id="low2time")

	# three day forecast
	fDayDate = threeDayF.find("h5", id="1_date")
	fDayCond = threeDayF.find("div", id="1_cond")
	fDayWind = threeDayF.find("span", id="1_wind")	
	fDaySea = threeDayF.find("span", id="1_sea")

	sDayDate = threeDayF.find("h5", id="2_date")
	sDayCond = threeDayF.find("div", id="2_cond")
	sDayWind = threeDayF.find("span", id="2_wind")	
	sDaySea = threeDayF.find("span", id="2_sea")

	tDayDate = threeDayF.find("h5", id="3_date")
	tDayCond = threeDayF.find("div", id="3_cond")
	tDayWind = threeDayF.find("span", id="3_wind")	
	tDaySea = threeDayF.find("span", id="3_sea")



	stations = {
    	"male" : 0,
    	"hanimadhoo" : 1,
	"kahdhoo" : 2,
    	"kaadehdhoo" : 3,
    	"gan" : 4
    }
	
	# output json format
	infoList = [
		{
			"general_weather" : {

				"temp" : temps[stations[station.lower()]].text,
				"condition" : descs[stations[station.lower()]].text,
				"station" : locs[stations[station.lower()]].text.strip(),

				"sunrise" : sunrise.text,
				"sunset" : sunset.text,
				"moonrise" : moonrise.text,
				"moonset" : moonset.text,
				"humidity" : humidity.text,
				"rainfall" : rainfall.text,
				"wind" : wind.text,
				"sunshine" : sunshine.text,
			}

		},

		{
			"tide_info" : {

				"high1" : high1.text,
				"high1_time" : high1time.text,
				"high2" : high2.text,
				"high2_time" : high2time.text,
				"low1" : low1.text,
				"low1_time" : low1time.text,
				"low2" : low2.text,
				"low2_time" : low2time.text
			}
		},

		{
			"three_day_forecast" : [

				{
					"first_day" : {

						"date" : fDayDate.text,
						"condition" : fDayCond.text,
						"wind" : fDayWind.text,
						"sea" : fDaySea.text
					}

				},

				{
					"second_day" : {

						"date" : sDayDate.text,
						"condition" : sDayCond.text,
						"wind" : sDayWind.text,
						"sea" : sDaySea.text
					}

				},

				{
					"third_day" : {

						"date" : tDayDate.text,
						"condition" : tDayCond.text,
						"wind" : tDayWind.text,
						"sea" : tDaySea.text
					}

				}

			]
		}
	]

	infoJson = json.dumps(infoList, indent=4)

	return infoJson
