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
       
    # test print to screen instead of file
    print(transcript)
    # with open(f'{title}.txt', 'w') as file:
    #     file.write(transcript)

    # random 1 to 5 second delay
    sleep(randint(1,5))
