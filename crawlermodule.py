import requests as req
from bs4 import BeautifulSoup as soup
import json



def crawl ():
    url = "https://www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=teclado&btnG=    "


    rs = req.get(url)
    content =rs.content 

    json = []



    page_soup = soup(content,'html.parser')
    containers = page_soup.findAll('div',{"class":"listagem-box"})


    for container in containers:



        nome=container.a.img['alt']

        preco = container.findAll('div',{"class":"listagem-precoavista"})
        preco = preco[0].text
        
        obj = {"nome":nome , "preco":preco}
        json.append(obj)

    return json
        
