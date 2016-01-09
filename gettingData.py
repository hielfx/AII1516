#encoding:utf-8

import datetime
#from principal.models import Juego
from django.db import connection
from bs4 import BeautifulSoup
from urllib2 import urlopen


def buscar_nombre(nombre):
    
    result_steam = gettingData_Steam(nombre)
    
    #result_humble = gettingData_humble(nombre)
    
    result_kinguin = gettingData_kinguin(nombre)
    
    return 0

def gettingData_Steam(nombre):
    cont = 0
    url = "http://store.steampowered.com/search/?snr=1_4_4__12&term="+nombre    
    try:
        soup = BeautifulSoup(urlopen(str(url)),'html.parser')
        stmaux1 = soup.find_all('a',class_='search_result_row ds_collapse_flag')
        for i in stmaux1:
            #newJuego = Juego()
            url = i['href'].lstrip().rstrip()
            sopa = BeautifulSoup(str(i),'html.parser')
            titulo = sopa.find('span',class_='title').contents[0].lstrip().rstrip()
            precio = sopa.find('div',class_='col search_price  responsive_secondrow').contents[0].lstrip().rstrip()
            #newJuego.titulo = titulo
            #newJuego.url = url
            #newJuego.precio = precio
            print titulo +" ("+ precio +")" + url
            
            print "--------------------"
            if(cont>=4):
                break
            cont=cont+1
    except:
        pass
    return 0
    
def gettingData_cdkeys(nombre):
    cont = 0
    url = "http://www.cdkeys.com/catalogsearch/result/?q="+nombre
    
    try:
        soup = BeautifulSoup(urlopen(str(url)),'html.parser')
        hmblaux1 = soup.find_all('div',class_='js-search-results-holder search-results-holder')
        print hmblaux1
        for i in hmblaux1:
            
            sopa1 = BeautifulSoup(str(i),'html.parser')
            aux = sopa1.find('h4',itemprop='name').contents[0]
            sopa2 = BeautifulSoup(str(aux),'html.parser')
            titulo = sopa2['a'].contents[0]
            
            print "--------------------"
            if(cont>=4):
                break
            cont=cont+1
    except:
        pass    
    return 0

def gettingData_kinguin(nombre):
    cont = 0
    url = "http://www.kinguin.net/es/catalogsearch/result/index/?q="+nombre
    try:
        soup = BeautifulSoup(urlopen(str(url)),'html.parser')
        stmaux1 = soup.find_all('div',class_='product-name')
        for i in stmaux1:
            
            sopa1 = BeautifulSoup(str(i),'html.parser')
            aux = sopa1.find('h4',itemprop='name')
            sopa2 = BeautifulSoup(str(aux),'html.parser')
            titulo = sopa2.a.contents[0].lstrip().rstrip()
            url = sopa2.a['href'].lstrip().rstrip()
            sopa3 = BeautifulSoup(str(i.find_next_sibling()),'html.parser')
            price = sopa3.find('span',class_="price add-tax-rate hidden relative-price-container")['data-no-tax-price']
            print titulo +" (" +price+ ") "+url
            
            print "--------------------"
            if(cont>=4):
                break
            cont=cont+1   
    except:
        pass
    return 0
buscar_nombre("fifa")
    
