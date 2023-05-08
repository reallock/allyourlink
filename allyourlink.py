import requests
from bs4 import BeautifulSoup
#Ask user for input
site = input('Site address:')
#Search site
url = 'https://'+site
#Pull all links from website then parse output
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
#List all links pulled from site
urls = []
#Use recursion to enumerate all sites
for link in soup.find_all('a'):
      print(link.get('href'))