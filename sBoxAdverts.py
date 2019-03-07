import requests
from bs4 import BeautifulSoup
import urllib2
import html5lib
import json
import sys

fullList = list()


#Retrieve data from AJAX request page
# page = requests.get('https://www.nts.live/schedule/listing_xhr/1?ajax=true&timezone=Europe/Dublin')
page = requests.get('https://www.adverts.ie/free-stuff?utm_source=homepage&utm_medium=link&utm_campaign=Free+Stuff')

page = requests.get('https://www.adverts.ie/for-sale/price_0/sortby_start_date-desc')

# print(page)


contents = page.content
# print(contents)
# exit()
soup = BeautifulSoup(contents, 'html5lib')

# print(soup)

with open('/Users/josef/gitHub/radSched/outputfile.txt', 'w') as f:
    sys.stdout = f
    # print "test"
    print soup

f.close()

times = soup.find_all('div', attrs={'class': 'sr-grid-cell quick-peek-container'})

with open('/Users/josef/gitHub/radSched/outputfile1.txt', 'w') as f:
    sys.stdout = f
    # print "test"
    for i in range(1,len(times)):
	    print(i)
	    a = times[i-1]
	    # #### TODO GET IMAGE LINK 
	    # bb = a.find_all('a', attrs={'class': 'main-image'})
	    # if 'src' in bb.attrs:
	    # 	print(bb['src'])
	    # print bb
	    # print(bb)

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
f.close()
# print('%s: at : %s @ %s' % (shows[0].text, times[0].text, 'blah'))