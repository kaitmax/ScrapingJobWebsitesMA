from ast import Return
from re import I, X
from ssl import HAS_TLSv1_1
from timeit import repeat
from attr import attrs
from matplotlib.pyplot import text, title
from numpy import append, r_
import requests
from bs4 import BeautifulSoup
import soupsieve
import pandas as pd




link =[]
job_title =[]
ville =[]
poste_date =[]
Nposte= []
sector =[]
fonction =[]
experience =[]
niveau =[]
Contrat =[]
Company= []



x = 1  
while True : 
    r = requests.get(f"https://www.rekrute.com/offres.html?p={x}")
    sp =BeautifulSoup(r.text, 'lxml')
    x_max = int(sp.select_one("span.jobs").text.split("sur")[1].strip())
    if(x > x_max) : 
        print("baraka")
        break
    job_titles = sp.select('div>div>h2>a[href*="/offre-emploi-"]')
    dates = sp.select("em > span:nth-of-type(1)")  
    npostes = sp.select("em > span:nth-of-type(3)")
    sectors = sp.select('div> ul >li > a[href*=".html?sectorId"] ')
    fonctions = sp.select('div> ul >li > a[href*=".html?positionId"] ')
    experiences = sp.select('div> ul >li > a[href*=".html?workExperienceId"] ')
    niveaux = sp.select('div> ul >li > a[href*=".html?studyLevelId"] ') 
    Contrats = sp.select('div> ul >li > a[href*=".html?contractType"] ')  
    companys = sp.select('ul >li >div>div>a>img')

    for i in range(len(job_titles)): 

            job_title.append(job_titles[i].text.split("|")[0].strip().replace('    ', ''))
            ville.append(job_titles[i].text.split("|")[1].strip().replace('(Maroc)', ''),)
            poste_date.append(dates[i].text.strip().replace('    ', ''))
            try :
                Nposte.append(npostes[i].text.strip().replace('    ', '')) 
            except :
                Nposte.append('None')
            sector.append(sectors[i].text.strip().replace('    ', ''),)
            fonction.append(fonctions[i].text.strip().replace('    ', ''),)
            experience.append(experiences[I].text.strip().replace('    ', ''),)
            niveau.append(niveaux[i].text.strip().replace('    ', ''),)
            Contrat.append(Contrats[i].text.strip().replace('    ', ''),)
            try :
                Company.append(companys[i].attrs['alt'] )
            except : 
                Company.append('None')

    x +=1 
    print("page switched")
jobs ={

                        'job_title': job_title,
                        'ville' : ville,
                        'poste_date':poste_date,
                        'Nposte' :Nposte,
                        'sector' : sector,
                        'fonction':fonction,
                        'experience': experience,
                        'niveau': niveau,
                        'Contrat':Contrat,
                        'Company': Company,
    }

                

df = pd.DataFrame(jobs)
df.to_csv('Rekrutejobs.csv', index=False)                       
print('saved to csv')

