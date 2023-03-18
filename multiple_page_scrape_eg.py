from bs4 import BeautifulSoup as bs
from numpy.random import default_rng
from time import sleep
import requests
import lxml


root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = bs(content, 'lxml')
t_count = 1

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):  # list of links
    links.append(link['href'])

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
    rng = default_rng()
    sleep_delay = rng.uniform(1,3)
    print(t_count,title)
    print('delaying for : ', sleep_delay, ' seconds')
    sleep(sleep_delay)  # random 1 to 3 second delay
    print('sleep delay finished')

    # stop after 5 while testing
    if t_count == 2:
        break
    t_count += 1
