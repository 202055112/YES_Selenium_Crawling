import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
url= 'http://www.yes24.com/main/default.aspx'
driver.get(url)

time.sleep(5)

search=driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/div[1]/form/fieldset/span[1]/label/input')
search.click()
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/div[1]/form/fieldset/span[1]/label/input').send_keys('파이썬')
search.send_keys(Keys.ENTER)

res=[]
for _ in range(1):
    time.sleep(10)
    for j in range(1,24):
        try:
            name=driver.find_element_by_xpath(f'/html/body/div/div[4]/div/div[2]/section[2]/div[3]/ul/li[{j}]/div/div[2]/div[2]/a[1]').text
            print(f'{name}')
        except:
            name = "NAN"
            pass
        try:
            author=driver.find_element_by_xpath(f'/html/body/div/div[4]/div/div[2]/section[2]/div[3]/ul/li[{j}]/div/div[2]/div[3]/span[1]/a').text
            print(f'{author}')  
        except:
            author= 'NAN'
            pass
        try:
            price=driver.find_element_by_xpath(f'//*[@id="yesSchList"]/li[{j}]/div/div[2]/div[4]/strong').text
            print(f'{price} 원')
        except:
            price= 'NAN'
            pass
        res.append((name, author, price))
print(res)
driver.quit()

data = pd.DataFrame(res)
data.to_csv('./data.csv')