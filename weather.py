from pprint import pprint
import requests
from creds import weather_key

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)

	except:
		final_str = 'There was a problem retrieving that information\nas no such place exists'
	
	return final_str

def get_weather(city):
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params = params)
	weather_json = response.json()

	#print(weather['name'])
	#print(weather['weather'][0]['description'])
	#print(weather['main']['temp'])

	weather_str = format_response(weather_json)
	return weather_str

if __name__ == "__main__":
	city = input("Enter city: ")
	weather = get_weather(city)
	pprint(weather)