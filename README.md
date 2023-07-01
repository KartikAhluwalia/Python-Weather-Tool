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
[[<img width="436" alt="Delhi Weather Kartik" src="https://github.com/Fastest-Coder-First/Weather_Python_Kartik_Ahluwalia/assets/96951632/15149af3-5827-4108-a673-e79951d6414c">](https://github-production-user-asset-6210df.s3.amazonaws.com/96951632/248454498-15149af3-5827-4108-a673-e79951d6414c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230701T142125Z&X-Amz-Expires=300&X-Amz-Signature=aa14b44757f834ccf4e2b5e407ce51c996806461e51eb7a0bcb500d61ed13b68&X-Amz-SignedHeaders=host&actor_id=96951632&key_id=0&repo_id=657901878)](https://github.com/KartikAhluwalia/Python-Weather-Tool/blob/main/Delhi%20Weather%20Kartik.png)

<img width="553" alt="Bengaluru Weather Kartik" src="https://github.com/Fastest-Coder-First/Weather_Python_Kartik_Ahluwalia/assets/96951632/b8405f07-1665-467a-beaa-1cd9e013de48">

<img width="500" alt="Gurugram Weather Kartik" src="https://github.com/Fastest-Coder-First/Weather_Python_Kartik_Ahluwalia/assets/96951632/02fb5d79-3a4f-4afe-988e-219629b3f84f">

<img width="450" alt="New York Weather Kartik" src="https://github.com/Fastest-Coder-First/Weather_Python_Kartik_Ahluwalia/assets/96951632/0eaff06f-9045-46da-a3f7-9c633f783861">
