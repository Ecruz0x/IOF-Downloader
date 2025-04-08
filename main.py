from requests_html import HTML, HTMLSession
import requests
from bs4 import BeautifulSoup as bs
import os

indexofurl = input("Enter IOF URL : ")
filetype = input("Enter the filetype : ")
dirn = input("Enter SaveDIR : ")

try:
    os.mkdir(f"./{dirn}")
except FileExistsError:
    pass

def urlsParsing(indexofurl, filetype):
    session = HTMLSession()
    r = session.get(indexofurl)
    rhtml = r.html.html
    soup = bs(rhtml, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url[-len(filetype):] == filetype:
            urls.append(url)
    return urls

def FilesDL(urls):
    for i in urls:
        response = requests.get(indexofurl+i)
        if response.status_code == 200 :
            i = i.replace("%20", " ")
            with open(f"./pdfs2/{i}", "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f'Downloaded File : {i}')
        else:
            print(f"Cannot download file : {i}")
        
urls = urlsParsing(indexofurl, filetype)
FilesDL(urls)

