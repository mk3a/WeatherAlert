#!/usr/bin/env python3
# Sends Weather Alerts to cellphone
# To Do List
#   Test to see if precipitation bound is a good bound
import requests
import json
import texting


def weatherInfoToAlert(temp_c, precip, windSpeed):
    minTempWarning = -15  # Canada doesn't need MaxTempWarning
    minComfortTemp = 0
    maxComfortTemp = 27
    precipLowBound_mm = 5
    windLowBound_kmh = 25
    curWeatherAlerts = []
    if temp_c!=None:
        if temp_c < minTempWarning:
            curWeatherAlerts.append('You should stay at home')
        elif temp_c < minComfortTemp:
            curWeatherAlerts.append('Really Cold(%s)! Don\'t forget your coat' %str(temp_c))
        elif temp_c > maxComfortTemp:
            curWeatherAlerts.append('Dress Light,Warm Day')
    if precip!=None :
        if precip > precipLowBound_mm:
            if windSpeed!=None and windSpeed > windLowBound_kmh:
                curWeatherAlerts.append('Rainy but too windy for an umbrealla.\
                                 Take a raincoat. Its in the third drawer')
            else:
                curWeatherAlerts.append('Don\'t forget your umbrella')
        return curWeatherAlerts


def getWeatherAlerts():
    watWeatherURL = 'https://api.uwaterloo.ca/v2/weather/current.json'
    weatherRes = requests.get(watWeatherURL)
    weatherRes.raise_for_status()
    weatherJSON = json.loads(weatherRes.text)
    temp_c = weatherJSON['data']['temperature_current_c']
    precip = weatherJSON['data']['precipitation_24hr_mm']
    windSpeed = weatherJSON['data']['wind_speed_kph']
    curWeatherAlerts = weatherInfoToAlert(temp_c, precip, windSpeed)
    if curWeatherAlerts==None :
        print('All is well')
    else :
        for alert in curWeatherAlerts:
            texting.textme(alert)

getWeatherAlerts()
