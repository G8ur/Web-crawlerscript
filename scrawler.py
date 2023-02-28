from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re

score=urlopen("https://www.livescore.com/en/")
goal=soup(score.read())

for link in goal.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs('href')) # if href present in the url
    print("No Href")      #if no href in the url     