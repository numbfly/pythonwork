## test selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options = chrome_options)



method = input("需要翻译的英文是：")
url = f"https://fanyi.baidu.com/?aldtype=16047#en/zh/{method}"

browser.get(url)
browser.implicitly_wait(10)

html = browser.page_source
browser.close()

soup = BeautifulSoup(html, 'lxml')
word = soup.find('p',{'class':'ordinary-output target-output clearfix'})

print (f"{method} 的翻译是：")
