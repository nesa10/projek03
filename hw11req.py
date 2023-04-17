
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import requests



driver = webdriver.Chrome('.\chromedriver.exe')
url = "https://www.spacex.com/launches/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

req = data.text



soup = BeautifulSoup(req, 'html.parser')
item = soup.find_all('div', {'class': ['item', 'row']})
for item in item:
     tanggal = item.select_one('date')
     if not tanggal:
          continue
    

nama_tujuan = item.select_one ('.label').text.strip()
tanggal = tanggal.text.strip()
print(nama_tujuan,tanggal)
     
     
     






