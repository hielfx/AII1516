#encoding:utf-8

from principal.models import Juego
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib2
import traceback
# from django.db import connection


def buscar_nombre(nombre):
    
    gettingData_Steam(nombre)
    
    gettingData_greenman(nombre)
    
    gettingData_kinguin(nombre)
    
    return 0

def gettingData_Steam(nombre):
    cont = 0
    url = "http://store.steampowered.com/search/?snr=1_4_4__12&term="+nombre    
    try:
        soup = BeautifulSoup(urlopen(str(url)),'html.parser')
        stmaux1 = soup.find_all('a',class_='search_result_row ds_collapse_flag')
        for i in stmaux1:
            newurl = i['href'].lstrip().rstrip()
            sopa = BeautifulSoup(str(i),'html.parser')
            titulo = sopa.find('span',class_='title').contents[0].lstrip().rstrip()
            price = sopa.find('div',class_='col search_price  responsive_secondrow').contents[0].lstrip().rstrip()
            newJuego = Juego(nombre=titulo, url=newurl, precio=price,web="Steam")
            newJuego.save()
            if(cont>=4):
                break
            cont=cont+1
    except:
        traceback.print_exc()
    return 0
    
def gettingData_greenman(nombre):
    cont = 0
    url = "http://www.greenmangaming.com/search/?q="+nombre+"#b"
    try:
        asd = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        con = urllib2.urlopen(asd)
        soup = BeautifulSoup(con.read(),'html.parser')
        gmgaux1 = soup.find_all('li',class_='border-container clearfix')
        for i in gmgaux1:
            sopa1 = BeautifulSoup(str(i),'html.parser')
            titulo = sopa1.find('h2',class_='notranslate').contents[0].lstrip().rstrip()
            url2 = "http://www.greenmangaming.com" + sopa1.a['href'].lstrip().rstrip()
            aux = sopa1.find('div', class_='formats')
            sopa2 = BeautifulSoup(str(aux),'html.parser')
            aux2 = sopa2.find('div', class_='price')
            price = aux2.find('strong', class_='curPrice').contents[0]
            newJuego = Juego(nombre=titulo, url=url2, precio=price,web="Greenman Gaming")
            newJuego.save()
            if(cont>=4):
                break
            cont=cont+1
    except:
        traceback.print_exc()  
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
            newurl = sopa2.a['href'].lstrip().rstrip()
            sopa3 = BeautifulSoup(str(i.find_next_sibling()),'html.parser')
            price = sopa3.find('span',class_="price add-tax-rate hidden relative-price-container")['data-no-tax-price']
            newJuego = Juego(nombre=titulo, url=newurl, precio=price,web="Kinguin")
            newJuego.save()            
            if(cont>=4):
                break
            cont=cont+1   
    except:
        traceback.print_exc()
    return 0

#No sirve, djanfo ya gestiona la db
# def syncdb_manual(nombre):
#     conn =connection.cursor()
#     conn.execute("DELETE FROM principal_juego")
#     buscar_nombre(nombre)

if __name__ == "__main__":   
#     syncdb_manual("counter")
    nombre = "counter"
    buscar_nombre(nombre)