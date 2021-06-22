# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:27:01 2021

@author: HP
"""

import requests

from datetime import datetime

api_key='f428d9c55fa9a956cfc250ffa8054c6b'
location = input("Enter the city name : ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %y | %I:%M%S %p")

print("-------------------------------------------------------")
print("Weather status for - {} || {}".format(location.upper(),date_time))
print("-------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_speed ,'kmph')

f = open("weather.txt", "w")
f.write("-------------------------------------------------------\n")
f.write("Weather status for - {} || {}".format(location.upper(),date_time))
f.write("\n-------------------------------------------------------\n")
f.write("Current temperature is: {:.2f} deg C".format(temp_city))
f.write("\n")
f.write("Current weather desc is :{}".format(weather_desc))
f.write("\n")
f.write("Current Humidity is (in perentage)   :{}".format(hmdt))
f.write("\n")
f.write("Current wind speed is (in kmph) is  :{}".format(wind_speed))
f.close()