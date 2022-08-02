from ast import keyword
from cgitb import text
from sys import getrecursionlimit
import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest

job_title = []
company = []
job_date = []
job_skill = []
link=[]
Metier = []
Secteur_dactivite = []
Contrat = []
Region = []
Ville = []
Experience = []
NEtude = []
Nposte = []

result = requests.get("https://www.emploi.ma/recherche-jobs-maroc?utm_source=site&utm_medium=link&utm_campaign=search_split&utm_term=all_jobs")
src =result.content

soup = BeautifulSoup(src,"lxml")

job_titles = soup.find_all("h5")
job_skills = soup.find_all("div", {"class":"badge"})
Links = soup.find_all("div", {"class":"job-description-wrapper"})

for i in range(len(job_titles)):  
    job_title.append(job_titles[i].text)
    job_skill.append(job_skills[i].text)
    link.append(Links[i].attrs['data-href'])



for link in Links : 
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    
    company = soup.find("a", { "href":"/recruteur/6710583"})[0].text
    Job_date = soup.find_all("div", {"job-ad-publication-date"})[0].text
    Metier = soup.find_all("div", {"field-item even"})[1].text
    Secteur_dactivite = soup.find_all("div", {"field-item even"})[2].text
    Contrat = soup.find_all("div", {"field-item even"})[3].text
    Region = soup.find_all("div", {"field-item even"})[4].text
    Ville = soup.find_all("td", {"style":"margin-left: 5px;"})[0].text
    Experience = soup.find_all("div", {"field-item even"})[5].text
    NEtude = soup.find_all("div", {"field-item even"})[6].text
    Nposte =soup.find_all("td", {"style":"margin-left: 5px;"})[1].text
    





file_list = [job_title,company,Job_date,Metier,Secteur_dactivite,Contrat,Region,Ville,Experience,NEtude,job_skill,Nposte]
exported = zip_longest(*file_list)

with open("Documents\jobs.csv","w+") as myfile: 
    wr = csv.writer(myfile)
    wr.writerow(['job_title','company','Job_date','Metier','Secteur_dactivite','Contrat','Region','Ville','Experience','NEtude','job_skill','Nposte'])
    wr.writerows(exported)