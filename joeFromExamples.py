from bs4 import BeautifulSoup
import urllib2
import codecs

response = urllib2.urlopen('http://www.reality.sk/zakazka/0747-003578/predaj/1-izb-byt/kosice-mestska-cast-sever-sladkovicova-kosice-sever/art-real-1-izb-byt-sladkovicova-ul-kosice-sever')
html = response.read()
soup = BeautifulSoup(html)
print(soup.prettify)