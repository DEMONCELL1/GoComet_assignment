import requests
from bs4 import BeautifulSoup    

def crawler(max_pages):
    page =1
    while page<= max_pages:
        url ="https://medium.com/" + str(page)
        source=requests.get(url)
        plain_text = source.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findall('a',{'class':''}):
            href = "https://medium.com/" + link.get('href')
            titles = link.string
            print(titles)
        page +=1
        
crawler(1)
