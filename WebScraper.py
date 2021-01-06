
def GenTxt(records):
    Doc = open('Libros.txt','w')
    Doc.write('Titulo - Autor -  Precio(UYU)\n')
    for record in records:
        line = record[0]+' - '+record[1]+' - '+record[2]+'\n'
        Doc.write(line)
    Doc.close()
    
def GenCSV():
    import pandas as pd
    df = pd.DataFrame(records,columns=['Titulo','Autor','Precio'])
    df.to_csv('Libros.csv',index=False,encoding='utf-8')
    
import requests
from bs4 import BeautifulSoup as b

base_url = 'https://www.isadoralibros.com.uy/sitio/libros/buscar/q/'
author_many=['seneca','epicteto','marco aurelio']
records = []
for author in author_many:
    url=base_url+author
    html = requests.get(url)
    content = html.content
    soup = b(content,"html.parser")

    for post in soup.find_all('article',attrs={'class':'boxLibro'}):
        title = post.find('p', attrs={'class':'titulo'}).text
        author_book = post.find('p', attrs={'class':'autor'}).text
        price = post.find('p', attrs={'class':'precio'}).text
        records.append((title,author_book,price))
    records.append(('Books of',author,url))
GenTxt(records)



