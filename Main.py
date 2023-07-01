import requests
import json
from termcolor import colored, cprint
from pyfiglet import Figlet
import os
import time 
from datetime import date

os.system('cls')

print_red=lambda x: cprint(x,'red') 
print_green=lambda x: cprint(x,'green') 
print_yellow=lambda x: cprint(x,'yellow')   
print_blue=lambda x: cprint(x,'blue')   
print_magenta=lambda x: cprint(x,'magenta') 
print_cyan=lambda x: cprint(x,'cyan')   
print_white=lambda x: cprint(x,'white') 

today=date.today()
d2=today.strftime("%B %d, %Y")  

f=Figlet(font='banner3-D',width=200)
f1=Figlet(font='standard',width=200)
f2=Figlet(font='slant',width=200)

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

CITY = input('Enter city name: ')
API_KEY="0b3d0531d0f60dbfd371c2edfe3068fd"
URL=BASE_URL+"q="+CITY+"&appid="+API_KEY
response=requests.get(URL)
if response.status_code==200:
    data=response.json()
    main=data['main']
    temperature=main['temp']
    min_temp=main['temp_min']
    max_temp=main['temp_max']
    humidity=main['humidity']
    pressure=main['pressure']
    wind=data['wind']
    wind_speed=wind['speed']
    report=data['weather']
    print_yellow(f1.renderText(f"Weather Report"))
    print_blue(f1.renderText(f"{d2}"))
    time.sleep(2)
    print_green(f.renderText(f"{CITY}"))
    time.sleep(1)
    print_red(f"Temperature in Kelvin: {temperature}")
    print_red(f"Minimum Temperature in Kevin: {min_temp}")
    print_red(f"Maximum Temperature in Kelvin: {max_temp}")
    print_blue(f"Humidity: {humidity}%")
    print_magenta(f"Pressure: {pressure}")
    print_cyan(f"Wind Speed: {wind_speed}")
    time.sleep(2)
    #Weather Report:
    print_white(f2.renderText(f"{report[0]['description']}"))

else:
    print("Error in the HTTP request")
