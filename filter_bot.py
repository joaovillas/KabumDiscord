import json
from crawlerhome import crawlhome
from crawlermodule import crawl
import time


def filtra(req):
    f = open('home.json','w')


    req = req.upper()

    if (req == "!KABUM"):
        
        json_response = crawlhome()
        json_str = json.dumps(json_response,ensure_ascii=False,sort_keys=True,indent=4)
        f.write(json_str)
    if (req == "!TECLADO"):
        json_response = crawl()
        json_str = json.dumps(json_response,ensure_ascii=False,sort_keys=True,indent=4)
        f.write(json_str)
    f.close()