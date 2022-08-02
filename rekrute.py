from ast import Return
from ssl import HAS_TLSv1_1
from timeit import repeat
from matplotlib.pyplot import text, title
from numpy import r_
import requests
from bs4 import BeautifulSoup
import soupsieve
import pandas as pd
from itertools import chain

def get_page_links(url):
    urlbase = 'https://www.rekrute.com'
    r = requests.get(url)
    sp =BeautifulSoup(r.text, 'lxml')
    links = sp.select('div.col-sm-10 col-xs-12 a')
    return [urlbase + link.attrs['data-href'] for link in links ]




def jobs_data(url): 
    r = requests.get(url)
    sp= BeautifulSoup(r.text, 'lxml')

    Jobs= {

    'titre' : sp.find("title").text.strip().replace('    ', ''),
    'MetierS' :sp.find("h2", {"h2italic"}).text.strip().replace('    ', ''),
    #'company': titre.split()[-1],
    'Experience' :sp.find("li",{"title":"Expérience requise"}).text.strip().replace('    ', ''),
    'RegionT' :sp.find("li",{"title":"Région"}, {"b"}).text.strip().replace('   ', ''),
    #'Region' :RegionT.split("sur")[1].strip().replace('   ', ''),
    #'Nposte' :RegionT.split()[0].strip().replace('   ', ''),
    #'Ville' : titre.split(" - ")[2].strip().replace('   ', ''),
    'formation':sp.find("li",{"title":"Niveau d'étude et formation"}).text.strip().replace('    ', ''),
    'contrat' : sp.find("span",{"title":"Type de contrat"}).text.strip().replace('    ', ''),
    'teletravail' : sp.find("span",{"title":"Télétravail"}).text.strip().replace('    ', ''),
    'Management' : getattr(sp.find("span",{"class":"tagmanagement"}).text.strip().replace('    ', ''), 'text', None)

}

    return Jobs

    
def main():
    
    results = []

    for x in range(0 ,2):
       urls= (f'https://www.rekrute.com/offres.html?p={x}')
       jobinfo = [jobs_data(url) for url in urls]
       results.append(jobinfo)
    print(f'page{x} completed. ')
    return results

df = pd.DataFrame(list(chain.from_iterable(main())))
df.to_csv('offreRekrute.csv', index=False)
print('saved to csv')
