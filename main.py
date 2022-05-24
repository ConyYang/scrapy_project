import requests
from bs4 import BeautifulSoup



headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
           }

link_list = []
for i in range(101, 151):
    print('page: ',i )
    url = 'https://www.koreanewswire.co.kr/?md=A01&cat=600&perpage=100&page=' + str(i)
    response = requests.get(url, headers=headers)
    fragment = BeautifulSoup(response.content, 'html.parser')
    x = 0
    for link in fragment.find_all('a', href=True):
        if 'newsRead' in link['href']:
            x += 1
            if x % 3 == 0:
                link_list.append(link['href'])
# Open File
resultFyle = open("output101-150.csv",'w')

# Write data to file
for r in link_list:
    resultFyle.write(r + "\n")
resultFyle.close()
# 匹配关键词
# 题目 abstact link 公司名字 公司网站

