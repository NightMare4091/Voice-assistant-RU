import os
import webbrowser
import sys
import requests
import subprocess
from voice_v1 import speak
from num_to_text import num2text
import yagpt
from datetime import datetime
from bs4 import BeautifulSoup as BS

weather_api = "" # API-ключ openweather

def joke(*args):
    r = requests.get("https://nekdo.ru/random/")
    html = BS(r.content, "html.parser")

    for el in html.select(".content"):
        text = el.select(".text")
        speak(text[0].text)

def time(*args):
    now = datetime.now()
    current_time = now.strftime("%H %M")
    speak(f"Текущее время {str(current_time)}")

def chat(*args):
    pass

def ask(question):
    ans = yagpt.ask(question)
    print(ans)
    speak(ans)

def browse(*args):
    webbrowser.open("https://www.youtube.com", new=2)

def game(*args):
    subprocess.Popen("D:/tModLoader\start-tModLoader.bat")

def offpc(*args):
    os.system("shutdown")

def weather(*args):
    params = {'q': 'Ufa', 'units': 'metric', 'lang': 'ru', 'appid': weather_api}
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
    if not response:
        raise
    w = response.json()
    speak(f"На улице {w['weather'][0]['description']} {num2text(round(w['main']['temp']))} градусов")

def offBot(*args):
    sys.exit()

def passive(*args):
    pass
