
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.sumitomocorp.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
url = 'https://www.sumitomocorp.com/en/jp/news/release/2022'
response = requests.get(url, headers=headers)
print(response.content)