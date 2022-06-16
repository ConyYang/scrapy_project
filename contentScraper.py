import re
import requests
import pandas as pd
import numpy as np

def extract_info(text):
    # title
    s = '(?s)(?<=<h1>)(.+?)(?=</h1>)'
    title = re.search(s, text)
    if title:
        my_title = title.group(0)
    else:
        my_title = 'No title'

    # abstact
    s1 = '(?s)(?<=<p class="sub-title fs-md">)(.+?)(?=</p>)'
    result = re.search(s1, text)
    if result:
        mystring = result.group(0)
        abstract = re.sub(r'r<br>', ' ', mystring)[20:-18]
    else:
        abstract = 'No abstract'
    # company name
    s2 = '(?s)(?<=target="_blank">)(.+?)(?=</a>)'
    company = re.findall(s2, text)
    if company:
        my_company = company[1]
    else:
        my_company = 'No company'
    # website
    s3 = '(?s)(?<=<div class="corp-website"><a href=")(.+?)(?=")'
    website = re.search(s3, text)
    if website:
        my_web = website.group(0)
    else:
        my_web = 'no website link'

    return  my_title, my_company, my_web, abstract


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    arr_info = []
    url_list = pd.read_csv('koreanNewsWire50_100/output51-100.csv')['URL_Links']
    i = 0
    j = 1
    for url in url_list:
        print(i)
        i+=1

        response = requests.get(url, headers=headers)
        text_ = str(response.content)
        title, company, website, abstract = extract_info(text_)
        print(title, company, website, abstract)
        arr_info.append([title, abstract, company, website, url])

        if i % 1000 == 0:
            j += 1
            df = pd.DataFrame(np.array(arr_info),
                           columns=['title', 'abstract', 'company', 'website', 'link'])

            df.to_excel('KoreanNewsWire51_100_' + str(j) + '.xlsx')
            arr_info = []
            i = 0
    j += 1
    df = pd.DataFrame(np.array(arr_info),
                      columns=['title', 'abstract', 'company', 'website', 'link'])
    df.to_excel('KoreanNewsWire51_100_' + str(j) + '.xlsx')




