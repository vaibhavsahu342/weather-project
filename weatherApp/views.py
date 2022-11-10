from django.shortcuts import render

# Create your views here.

import urllib.request
import json
import datetime

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&appid=d1eb9bdaf572046a5445eec09a1414f3&units=metric').read()
        list_of_weather_data = json.loads(source)
        data = {
             "country_code": str(list_of_weather_data['sys']['country']),
             "coordinate": str(list_of_weather_data['coord']['lon']) + ' ,' + str(list_of_weather_data['coord']['lat']),
             "temp": str(list_of_weather_data['main']['temp']) + ' ℃',
             "pressure": str(list_of_weather_data['main']['pressure']) + ' hpa',
             "humidity": str(list_of_weather_data['main']['humidity']) + ' %',
             "main": str(list_of_weather_data['weather'][0]['main']),
             "description": str(list_of_weather_data['weather'][0]['description']),
             "icon": list_of_weather_data['weather'][0]['icon'],
             "timezone": list_of_weather_data['timezone'],
             "name": list_of_weather_data['name'],


        }

        print(data)

    else:
        data = {}


    return render(request, "index.html", data )




