from bs4 import BeautifulSoup as bs #exploring html documents
import requests #downloads files from internet
import pandas as pd #structure the downloaded data

result = requests.get('https://www.theweathernetwork.com/ca/weather/british-columbia/burnaby')
soup = bs(result.content, 'html.parser')
print('hello')
