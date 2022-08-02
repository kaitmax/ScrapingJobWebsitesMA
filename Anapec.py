from datetime import date
from re import I, X
from ssl import HAS_TLSv1_1
from time import sleep
from timeit import repeat
from weakref import ref
from attr import attrs
from matplotlib.pyplot import get, table, text, title
from numpy import append, r_
import requests
from bs4 import BeautifulSoup
import soupsieve
import pandas as pd

base_url = 'http://anapec.org/'
links =[]
ref =[]
date_poste =[]
Nbre_poste =[]
poste_title = []
lieu =[]
contrat =[]
salaire =[]
formation =[]
secteur =[]


x=1   
while True :
    r = requests.get('http://anapec.org/sigec-app-rv/chercheurs/resultat_recherche/page:{x}/tout:all/language:fr')
    sp = BeautifulSoup(r.text , 'lxml')
    offres =int(sp.select_one('p.sul > span>strong').text)
    x_max =int(offres // 15)
    if (x > 100): 
        print('barak')
        break
    url = sp.select('a.nyroModal')
    refs = sp.select('table.tablesorter>tbody>tr>td:nth-of-type(2)')
    date_postes = sp.select('table.tablesorter>tbody>tr>td:nth-of-type(3)')
    poste_titles = sp.select('table.tablesorter>tbody>tr>td:nth-of-type(4)')
    Nbre_postes = sp.select('table.tablesorter>tbody>tr>td:nth-of-type(5)')
    lieux = sp.select('table.tablesorter>tbody>tr>td:nth-of-type(7)')
  
    for i in range(len(refs)):
        ref.append(refs[i].text)
        date_poste.append(date_postes[i].text)
        Nbre_poste.append(Nbre_postes[i].text)
        poste_title.append(poste_titles[i].text.replace('Ã©','é').replace('Ã¢','â').replace('Å\x93','oe').replace('Ã¨','è'))
        lieu.append(lieux[i].text.replace('Ã©','é').replace('Ã¢','â').replace('Å\x93','oe').replace('Ã¨','è').strip())
        links.append(base_url + url[i].attrs['href'])


   
    x +=1
    
    print("page switched")

     
  



jobs = { 
        'ref': ref,
        'date_poste':date_poste,
        'nbre_poste' : Nbre_poste,
        'poste_title' : poste_title,
        'lieu' : lieu,
    
             }

df =pd.DataFrame(jobs)
df.to_csv('anapec1.csv', index=False)
print('saved to csv')