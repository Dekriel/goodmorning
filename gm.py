import requests
from bs4 import BeautifulSoup

query = 'https://www.bbc.com/news'
response = requests.get(query)

temp = []
scraped = BeautifulSoup(response.text, 'html.parser')
headlines = scraped.find('body').find_all('h3')
link = scraped.find('body').find_all('a')
for i in headlines:
    for j in link:
        temp.append(i.text.strip() + '         ')

print("good morning!")
print("=================================TOP STORIES TODAY=================================")
for _ in range(8):
    print(temp[_])
print("===================================================================================")
