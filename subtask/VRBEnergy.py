import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'vrbenergy.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
url = 'https://vrbenergy.com/news/'
response = requests.get(url, headers=headers)
fragment = BeautifulSoup(response.content, 'html.parser')
link_list = []
for link in fragment.find_all('a', href=True):
    if 'vrbenergy.com' in link['href']:
        if link['href'] not in link_list:
            link_list.append(link['href'])
print(link_list)