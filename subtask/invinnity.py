
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'invinity.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
url = 'https://invinity.com/investors/announcements/'
response = requests.get(url, headers=headers)
