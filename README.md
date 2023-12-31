# Python-Weather-Tool

The Weather Forecast Tool is a Python command-line application that provides users with up-to-date weather information for any city they specify for the current date. By leveraging APIs and the user's input, the tool fetches the current weather data and displays it in a user-friendly format.

Upon running the program, the user is prompted to enter the name of the city for which they desire the weather forecast. Once the city name is entered, the tool initiates a request to a weather API (such as OpenWeatherMap) to retrieve the relevant weather data.

To enhance the user experience, the program uses various fonts to stylize the output. The weather information is presented in a visually appealing format, making it easy for users to read and understand. For example, different font styles for the temperature, humidity, pressure, and overall weather condition, allowing each piece of information to stand out.

To further improve the user experience, the program utilizes the time.sleep function to introduce a pause between retrieving the weather data and displaying it on the screen. This delay enhances the perceived responsiveness of the application, giving users a brief moment to anticipate the results.

Additionally, before each code execution, the program employs a screen-clearing mechanism to ensure a clean and clutter-free display. By clearing the command-line interface before presenting the weather forecast, the tool offers users a neat and organized view of the information.

The weather forecast tool provides essential weather details such as temperature, humidity, pressure, and an overall description of the weather condition (e.g., sunny, cloudy, rainy) for the specified city. This enables users to stay informed about the current weather conditions in any location of their interest.

Overall, this Python project combines functionality, aesthetics, and user experience enhancements to create a user-friendly weather forecast tool in the command line.

# Pre-Requisites

import requests

import json

from termcolor import colored, cprint

from pyfiglet import Figlet

import os

import time 

Download and Install the above packages for before running the code.

# Screenshots

<img width="436" alt="Delhi Weather Kartik" src="https://github.com/KartikAhluwalia/Python-Weather-Tool/assets/96951632/50f6d2da-d701-4f1b-8517-6af2726b2d3e">

<img width="553" alt="Bengaluru Weather Kartik" src="https://github.com/KartikAhluwalia/Python-Weather-Tool/assets/96951632/26f138cc-a6b7-48ff-b67f-221f2af0c6c5">

<img width="500" alt="Gurugram Weather Kartik" src="https://github.com/KartikAhluwalia/Python-Weather-Tool/assets/96951632/1c22057f-82ee-417c-8b97-37cfea4a1463">

<img width="450" alt="New York Weather Kartik" src="https://github.com/KartikAhluwalia/Python-Weather-Tool/assets/96951632/3eadb931-fb89-495a-b0b3-b76513cb47ee">

