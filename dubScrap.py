import requests
from bs4 import BeautifulSoup
import urllib2
import html5lib
import json

fullList = list()
showData = dict()

page = requests.get('http://dublab.com/schedule/')
print('Received data')
contents = page.content
soup = BeautifulSoup(contents, 'html5lib')
print 'Data souped'
# print(soup.prettify)

#Look for table with schedule
table = soup.find( "table", {"class":"eme-calendar-table fullcalendar"} ) 

month = soup.find( "td", {"class":"month_name"} )
month = (month.text).strip('<> ')

n = 1
records = [] # store all of the records in this list
for row in table.findAll('tr'):
    col = row.findAll('td')
    print n
    n = n+1
    for i in range(0,len(col)):
	    if 'eventful' in col[i]['class']:
	    	print col[i]
	    	weekStart = col[i].findAll('li')
	    	for show in weekStart:
	    		showData = dict()
	    		print 'Time: ' + show.find('p').contents[2] + ', Show: ' + show.find('a').text + ', Link: ' + show.find('a').get('href')
	    		# # lst = [node['class'] for node in col[i] if node.has_attr('class')]
	    		# # print lst
	    		# # for ana in col[i]:
	    		# # 	if ana.parent.name == 'td':
	    		# # 		print ana

	    		dayNum = col[i]['class'][2][-2:]
	    		dayNum = dayNum.strip('-')
	    		showData['title'] = show.find('a').text
	    		showData['time'] = show.find('p').contents[2]
	    		showData['link'] = show.find('a').get('href')
	    		showData['day'] = col[i]['class'][0]
	    		showData['date'] = dayNum
	    		showData['month'] = month
	    		fullList.append(showData)		

#Write to JSON
with open('scheduleDUB.json', 'w') as fp:
            json.dump(fullList, fp)

print(fullList[15])




