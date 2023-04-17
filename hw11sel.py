from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import requests



driver = webdriver.Chrome('.\chromedriver.exe')
url = "https://www.spacex.com/launches/"
driver.get(url)
sleep(5)
req = driver.page_source
driver.quit()



soup = BeautifulSoup(req, 'html.parser')
item = soup.find_all('div', {'class': ['item', 'row']})
for item in item:
     tanggal = item.select_one('date')
     if not tanggal:
          continue
    

nama_tujuan = item.select_one ('.starship').text.strip()
tanggal = tanggal.text.strip()
print(nama_tujuan,tanggal)
     
     
     






