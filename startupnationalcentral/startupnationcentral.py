import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'finder.startupnationcentral.org',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
url = 'https://finder.startupnationcentral.org/startups/search?inu=True&li_type=GO&list_1_action=and&list_1_tag=artificial-intelligence'
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.content)

# find all ref
fragment = BeautifulSoup(response.content, 'html.parser')
link_list = []
for link in fragment.find_all('a', href=True):
    if 'company_page' in link['href']:
        if link['href'] not in link_list:
            link_list.append(link['href'])
print(link_list)