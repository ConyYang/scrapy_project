from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import pandas as pd
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://finder.startupnationcentral.org/tag/energy-saving')
def extract_text(mydriver):
    names = mydriver.find_elements(By.CLASS_NAME, "title")
    intros = mydriver.find_elements(By.CLASS_NAME, "subtitle")
    links = mydriver.find_elements(By.TAG_NAME, 'a')
    my_name_list = []
    my_intro_list = []
    my_link_list = []

    for name in names:
        if name.text != '':
            my_name_list.append(name.text)

    for intro in intros:
        if intro.text != '':
            my_intro_list.append(intro.text)

    for link in links:
        mylink = link.get_attribute('href')
        if 'company_page' in mylink:
            my_link_list.append(mylink)
    print(len(my_link_list))
    return my_name_list, my_intro_list, my_link_list

SCROLL_PAUSE_TIME = 6

dummy = input('Press Enter: ')

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
name_list = None
intro_list = None
link_list = None
df = None
while True:
    count += 1
    print(count)
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        name_list, intro_list, link_list = extract_text(mydriver=driver)
        df = pd.DataFrame(list(zip(name_list, intro_list, link_list)),
                          columns=['Name', 'Intro', 'Link'])
        break
    last_height = new_height

df.to_csv('energy-saving.csv')
driver.quit()