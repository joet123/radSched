import requests
from bs4 import BeautifulSoup
import urllib2
import html5lib
import json

fullList = list()


#Retrieve data from AJAX request page
page = requests.get('https://www.nts.live/schedule/listing_xhr/1?ajax=true&timezone=Europe/Dublin')
contents = page.content
soup = BeautifulSoup(contents, 'html5lib')

#Look for times and show objects (could be reduced to one object)
times = soup.find_all('span', attrs={'class': 'time'})
shows = soup.find_all('a')
print(shows)
# print(soup.prettify)

#Extract individual shows/times/links
for i in range(0,len(shows)):
	showData = dict()
	linkStr = 'https://www.nts.live' + shows[i].get('href')
	# print('%s: at : %s @ %s' % (shows[i].text, times[i].text, linkStr))
	showData['title'] = shows[i].text
	showData['time'] = times[i].text
	showData['link'] = linkStr
	fullList.append(showData)

#Write to JSON
with open('scheduleNTS.json', 'w') as fp:
            json.dump(fullList, fp)

print(fullList[15])

