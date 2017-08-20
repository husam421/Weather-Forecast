from bs4 import BeautifulSoup as bs #exploring html documents
import requests #downloads files from internet
import pandas as pd #structure the downloaded data
import os
from os.path import join  #change directory
import schedule  #makes the code run ever x seconds/minutes/hours/days
import time      #makes the code run ever x seconds/minutes/hours/days



#Gets the weather from the weather channel
def forecast():
    page = requests.get('https://weather.com/weather/today/l/CAXX0051:1:CA')
    soup = bs(page.content, 'html.parser')
    weather = soup.find(id="APP")
    today_weather = weather.find(class_="today_nowcard-main")
    #location = today_weather.find(class_="loc-container").get_text()
    location = today_weather.find(class_="today_nowcard-location").get_text()
    time_stamp = today_weather.find(class_="today_nowcard-timestamp").get_text()
    temp = today_weather.find(class_="today_nowcard-temp").get_text()
    desc = today_weather.find(class_="today_nowcard-phrase").get_text()
    feels = today_weather.find(class_="today_nowcard-feels").get_text()
    high_and_low = today_weather.find(class_="today_nowcard-hilo").get_text()

    print (location + " " + time_stamp)
    print (temp)
    print (desc)
    print (feels)
    print (high_and_low)
    print ()

    #Stores the information in a file
    path = os.path.join('/Users/husammohammad/Desktop') #changes the directory to the desktop

    file1 = open(join(path, 'weather.txt'), 'w+')
    file1.write(location + " " + time_stamp + "\n")
    file1.write(temp + "\n")
    file1.write(desc + "\n")
    file1.write(feels + "\n")
    file1.write(high_and_low + "\n")
    file1.close()


#repeats the code every x seconds/minutes/hours/days
schedule.every(5).seconds.do(forecast)

while True:
    schedule.run_pending()
    time.sleep(1)
