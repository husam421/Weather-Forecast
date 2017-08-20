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




"""
#Gets prayer times
def prayer_times():
    website = requests.get('https://www.islamicfinder.org/world/canada/6173331/vancouver-prayer-times/')
    soup1 = bs(website.content, 'html.parser')
    times = soup1.find(id="prayerTimeFilter")
    prayers = times.find_all(class_="todayPrayer")

    isDate = soup1.find(id="main-column")
    storeDate = isDate.find_all(class_="large-6")
    islamicDate = storeDate[1]
    hijriDate = islamicDate.find(class_="dateToday").get_text()
    print (hijriDate)

    fajr = prayers[0]
    fajrName = fajr.find(class_="todayPrayerName").get_text()
    fajrTime = fajr.find(class_="todayPrayerTime").get_text()
    fajrToday = fajrName + ":" + fajrTime
    print (fajrName,":" ,fajrTime)

    duhr = prayers[2]
    duhrName = duhr.find(class_="todayPrayerName").get_text()
    duhrTime = duhr.find(class_="todayPrayerTime").get_text()
    duhrToday = duhrName + ":" + duhrTime
    print (duhrName,":" ,duhrTime)

    asr = prayers[3]
    asrName = asr.find(class_="todayPrayerName").get_text()
    asrTime = asr.find(class_="todayPrayerTime").get_text()
    asrToday = asrName + ":" + asrTime
    print (asrName,":" ,asrTime)

    maghrib = prayers[4]
    maghName = maghrib.find(class_="todayPrayerName").get_text()
    maghTime = maghrib.find(class_="todayPrayerTime").get_text()
    maghToday = maghName + ":" + maghTime
    print (maghName,":" ,maghTime)

    isha = prayers[5]
    ishaName = isha.find(class_="todayPrayerName").get_text()
    ishaTime = isha.find(class_="todayPrayerTime").get_text()
    ishaToday = ishaName + ":" + ishaTime
    print (ishaName,":" ,ishaTime)
    print()
"""

""" #Stores information in a file
    path = os.path.join('/Users/husammohammad/Desktop') #changes the directory to the desktop

    file1 = open(join(path, 'prayers.txt'), 'w+')
    file1.write(hijriDate + "\n")
    file1.write(fajrToday + "\n")
    file1.write(duhrToday + "\n")
    file1.write(asrToday + "\n")
    file1.write(maghToday + "\n")
    file1.write(ishaToday)
    file1.close()
"""


#repeats the code every x seconds/minutes/hours/days
schedule.every(5).seconds.do(forecast)

while True:
    schedule.run_pending()
    time.sleep(1)
