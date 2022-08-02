from tkinter.tix import TEXT
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.sarouty.ma/fr/recherche?c=1&ob=mr&page=1")
src =result.content
title = []
sp = BeautifulSoup(src,"lxml")
for titles in sp.select('h2.card-title__title'):
for adresses in sp.select('span.card__location-text'):
print(adresses.text)
