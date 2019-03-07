import requests
from bs4 import BeautifulSoup
import urllib2
import html5lib
import json
import sys

# print "total employees %d" % Employee.emptyCount


# https://www.adverts.ie/for-sale/price_0/sortby_start_date-desc

# https://www.adverts.ie/for-sale/computers/laptops-and-netbooks/127/sortby_start_date-desc/price_0/

# https://www.adverts.ie/for-sale/county-Cork/sortby_start_date-desc/price_0/

# https://www.adverts.ie/for-sale/diy-renovation/140/county-Cork/price_0/

# https://www.adverts.ie/for-sale/diy-renovation/140/county-Cork/sortby_start_date-desc/price_0/

class searchParameters:

	def __init__(self):
		self.root = "https://www.adverts.ie/for-sale/"
		self.category = ""
		self.subcategory = ""
		self.county = ""
		self.time = None
		self.price = "/price_0"

	def addCounty(self,county):
		self.county = "county-" + county

	def addCategory(self,category):
		self.category = category + "/"

	def addSubCategory(self,subcategory):
		self.subcategory = subcategory + "/"

cats = ["","home-garden","computers"]
subs = ["","kitchen-appliances/167","laptops-and-netbooks/127"]

l1 = searchParameters()
# l1.addCategory(cats[1])
# l1.addSubCategory(subs[1])
l1.addCounty("Cork")

fullLink = l1.root + l1.category + l1.subcategory + l1.county + l1.price

print fullLink

page = requests.get(fullLink)
contents = page.content
soup = BeautifulSoup(contents, 'html5lib')

times = soup.find_all('div', attrs={'class': 'sr-grid-cell quick-peek-container'})

# print(times)

for i in range(1,len(times)):
	print(i)
	a = times[i-1]
	link = a.div.div.a
	if 'href' in link.attrs:
		print 'link : https//www.adverts.ie/' + (link['href'])
		b = link['href']
		b = b.split('/')
		# print(b)
		# print(len(b))
		print 'category : ' + (b[1])
		print 'title : ' + (b[2])
	locObj = a.find_all('div', attrs={'class': 'location'})
	locTxt = locObj[0].text
	locTxt = locTxt.strip()
	print 'location : ' + locTxt


