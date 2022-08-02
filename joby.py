from ast import Return
from ssl import HAS_TLSv1_1
from timeit import repeat
from matplotlib.pyplot import text
from numpy import r_
import requests
from bs4 import BeautifulSoup
import soupsieve
import pandas as pd
from itertools import chain


def get_page_links(url):

    r = requests.get(url)
    sp =BeautifulSoup(r.text, 'lxml')
    links = sp.select('div.job-description-wrapper')

    return [link.attrs['data-href'] for link in links ]

def jobs_data(url): 
    r = requests.get(url)
    sp= BeautifulSoup(r.text, 'lxml')
    title = sp.select_one('h1.title').text.strip().replace('\n', '')
    date = sp.select_one('div.job-ad-publication-date').text.strip().replace('Publiée le ', '')       
    companys= getattr(sp.select_one('div.company-title a'), 'text', 'None')
    Metier= sp.find("div", {"field field-name-field-offre-metiers field-type-taxonomy-term-reference field-label-hidden"},{'field-item even'}).text
    Secteur= sp.find("div", {"field field-name-field-offre-secteur field-type-taxonomy-term-reference field-label-hidden"},{'field-item even'}).text
    Contrat= sp.find("div", {'field field-name-field-offre-contrat-type field-type-taxonomy-term-reference field-label-hidden'},{"field-item even"}).text
    Region=sp.find("div", {'field field-name-field-offre-region field-type-taxonomy-term-reference field-label-hidden'},{"field-item even"}).text
    Experience=sp.find("div", {'field field-name-field-offre-niveau-experience field-type-taxonomy-term-reference field-label-hidden'}, {"field-item even"}).text
    NEtude= sp.find("div",{'field field-name-field-offre-niveau-etude field-type-taxonomy-term-reference field-label-hidden'}, {"field-item even"}).text
    try :
        skills= sp.find("div", {"field field-name-field-offre-tags field-type-taxonomy-term-reference field-label-hidden"},{'field-item even'}).text
    except : 
        skills = "None"
    try :
        Ville= sp.select('table.job-ad-criteria > tr>td[style="margin-left: 5px;"]')[0].text
    except:
        Ville = "None"
    try :
        Nposte= sp.select('table.job-ad-criteria > tr>td[style="margin-left: 5px;"]')[1].text
    except :
     Nposte="None"

    jobs ={
            'title' : title,
            'date': date,    
            'companys' :companys,
            'Metier':  Metier,
            'Secteur' : Secteur,
            'Contart' : Contrat, 
            'Region': Region,
            'Experience' :Experience,
            'NEtude' : NEtude,
            'skills' : skills,
            'Ville' : Ville,
            'Nposte' :  Nposte,
                 
                    
                  
    }

    
   
    return jobs
    
def main():
    results = []
    for x in range(0 ,50):
       urls=  get_page_links(f'https://www.emploi.ma/recherche-jobs-maroc?utm_source=site&utm_medium=link&utm_campaign=search_split&utm_term=all_jobs&page={x}')
       jobinfo = [jobs_data(url) for url in urls]
       results.append(jobinfo)
    print(f'page{x} completed. ')
    return results

df = pd.DataFrame(list(chain.from_iterable(main())))
df.to_csv('offreEmploi.csv', index=False)
print('saved to csv')


