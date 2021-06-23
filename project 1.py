import requests
#import os
from datetime import datetime

api_key = '1a9c3ff6579e3062b1e68a66fd9c7d6a'
location = input("Enter the city name :")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q=KOTTAYAM&appid=1a9c3ff6579e3062b1e68a66fd9c7d6a"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data[ 'main' ]['temp']) - 273.15)
weather_desc = api_data[ 'weather'][0]['description']
hmdt = api_data[ 'main']['humidity']
wind_spd = api_data['wind' ]['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("--------------------------------------------------------------")
print ("Weather Stats for - {} || {}".format(location.upper(), date_time))
print ("--------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :", hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
