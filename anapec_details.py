
import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import chain
from urllib.parse import urlparse
import random

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
 
    return random.choice(uastrings)


def get_page_links(url):
    base_url = 'http://anapec.org/'
    r = requests.get(url)
    sp =BeautifulSoup(r.text, 'lxml')
    links = sp.select('a.nyroModal')
    return [base_url+link.attrs['href'] for link in links ]

def jobs_data(url): 
    r = requests.get(url)
    soup= BeautifulSoup(r.text, 'lxml')
    try : ref = soup.select_one('input#ref').attrs['value']
    except : ref='None'
    try :contrat= soup.select_one('div#oneofmine>p>span:-soup-contains("CI","CDD","CDI")').text.strip()
    except : contrat = "None"
    try: salaire = soup.select_one('div#oneofmine>p>span:-soup-contains("DHS")').text.strip() 
    except : salaire ="None"
    try: 
        Formation = soup.select_one('div#oneofmine>p>span:-soup-contains("BAC","Sans diplôme","Dernière année","Technicien","Formation ","Baccalauréat","Diplôme" )').text.replace('Ã©','é').replace('Ã¢','â').replace('Å\x93','oe').replace('Ã¨','è').strip()
    except : Formation ="None"
 
    
    
    
    jobs ={
            'ref': ref,
            'contrat': contrat,
            'salaire': salaire,
            'Formation': Formation,           
            
       
                  
    }

    
   
    return jobs
    
def main():
    results = []
    for x in range(0 ,3):
        urls=  get_page_links(f'http://anapec.org/sigec-app-rv/chercheurs/resultat_recherche/page:{x}/tout:all/language:fr')
        jobinfo = [jobs_data(url) for url in urls]
        results.append(jobinfo)
        print(f'page{x} completed. ')
        return results

df = pd.DataFrame(list(chain.from_iterable(main())))
df.to_csv('anapecdetails.csv', index=False)
print('saved to csv')
