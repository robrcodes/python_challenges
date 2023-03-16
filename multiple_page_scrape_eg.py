from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep
import requests
import lxml


root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = bs(content, 'lxml')
# print(soup.prettify())


box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):  # list of links
    links.append(link['href'])

print(links)

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = bs(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    # commented out below to stop writing files while testing
    #
    # with open(f'{title}.txt', 'w') as file:
    #     file.write(transcript)  
    #   
    sleep(randint(1,3))  # random 1 to 3 second delay
