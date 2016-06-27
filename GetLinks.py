from BeautifulSoup import BeautifulSoup
import urllib2
import numpy
import re

html_page = urllib2.urlopen("http://slashdot.org")
soup = BeautifulSoup(html_page)
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)
