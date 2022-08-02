from ast import keyword
from cgitb import strong, text
from sys import getrecursionlimit
import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest

job_title = []
company = []
job_date = []
Job_skill = []
link=[]
Metier=[]

result = requests.get("https://www.emploi.ma/recherche-jobs-maroc?utm_source=site&utm_medium=link&utm_campaign=search_split&utm_term=all_jobs")
src =result.content
soup = BeautifulSoup(src,"lxml")
Links = soup.find_all("div", {"class":"job-description-wrapper"})

for i in range(len(Links)):  
    link.append(Links[i].attrs['data-href'])

    result = requests.get("link")
    src =result.content
    soup = BeautifulSoup(src,"lxml")
    Job_title=soup.find_all("strong")[0].text
    company = soup.find_all("a", { "href":"/recruteur/6710583"})[0].
    Job_date = soup.find_all("div", {"job-ad-publication-date"})[0].text
    Metier = soup.find_all("div", {"field-item even"})[1].text
    Secteur_dactivite = soup.find_all("div", {"field-item even"})[2].text
    Contart = soup.find_all("div", {"field-item even"})[3].text
    Region = soup.find_all("div", {"field-item even"})[4].text
    Experience = soup.find_all("div", {"field-item even"})[5].text
    NEtude = soup.find_all("div", {"field-item even"})[6].text
    Ville = soup.find_all("td", {"style":"margin-left: 5px;"})[0].text
    Nposte =soup.find_all("td", {"style":"margin-left: 5px;"})[1].text
