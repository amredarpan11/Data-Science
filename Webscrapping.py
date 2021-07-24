# coding=utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
Text=[]

res = requests.get('https://en.wikipedia.org/wiki/Data_science')
soup = BeautifulSoup(res.text, 'html.parser')
soup.select('mw-headline')

for i in soup.select('.mw-headline'):
    print(i.text)

    Text.append(i.text)

df=pd.DataFrame({'Text':Text,})
df.to_csv('Web.csv', index=False, encoding='utf-8')
