import json
from filter_bot import filtra
import time
import os
req = input('DIGITE SUA REQUISIÇÃO')

filtra(req)
 


f = open('home.json','r')
jso = f.read()
json_str = json.loads(jso)
a=0
for linha in json_str:
    print(linha['nome'])
    print(linha['preco'])
    

