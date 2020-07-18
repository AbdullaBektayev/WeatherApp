from django.shortcuts import render, get_object_or_404, redirect
from .models import City
from .forms import CityForm
import requests
def index(request):
    appid = 'fc9244307c069cb0fc31243b8dc7a2ad' # my app id form site openweathermap.org
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid # api url
    if(request.method == 'POST' and requests.get(url.format(request.POST['name'])).json()['cod'] != '404'): # check method of request and correctness input info
        temp = City.objects.filter(name=request.POST['name']) # if city name exist on our database get this object
        if temp: # if we have already have object with same city name
            temp.delete() # then delete
        form = CityForm(request.POST) # creating object with form
        form.save() # save object

    form = CityForm() # empty form for context

    all_cities = [] # for store all information about city from database

    for city in City.objects.all().order_by('-id')[:5]: # loop for last 5 song object from database
        res = requests.get(url.format(city.name)).json() # get info from openweathermap.org with api and convert json to dictionary
        city_info = {  # dictionary for storing information on City object
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'id': city.id,
            'min': res['main']['temp_min'],
            'max': res['main']['temp_max'],
            'wind': res['wind']['speed'],
            'pressure': res['main']['pressure']
        }
        all_cities.append(city_info) # adding info about current city

    geo_loc = requests.get('https://ipinfo.io/').json() # get info about geolocation from ipinfo.io and convert json to dictionary


    context = {'all_info': all_cities, 'form': form,'geo_loc': geo_loc['city']}  # context dictionary for get information by keys on html page

    return render(request,'weather/index.html',context)

def city_delete(request,pk): # function for deleting object form database City
    city = get_object_or_404(City,pk=pk) # get object by primary key

    if request.method == 'POST': # check method
        city.delete() # delete object
        return redirect('/')

    return render(request,'weather/index.html',{'city': city})

def city_delete_all(request):  # function for deleting all object form database Song
    city = City.objects.all() # get all objects from database Song
    city.delete() # delete all objects
    return redirect('/')