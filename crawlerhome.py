import requests as req
from bs4 import BeautifulSoup as soup
import json



def crawlhome():
    url = "https://www.kabum.com.br/"


    rs = req.get(url)
    content =rs.content 

    json = []



    page_soup = soup(content,'html.parser')
    containers = page_soup.findAll('div',{"class":"H-box"})


    for container in containers:


    # 
        nome=preco = container.findAll('span',{"class":"H-titulo"})
        nome= nome[0].text
        nome = nome.replace('..','')
        preco = container.findAll('div',{"class":"H-preco"})
        preco = preco[0].text
        obj = {"nome":nome , "preco":preco}
        json.append(obj)

    return json
        
