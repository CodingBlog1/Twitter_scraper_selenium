from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('USERNAME001')
password = os.getenv('PASSWORD')

print(username,password)


url = f"https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(6)


WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))).send_keys(username)
time.sleep(5)
WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div'))).click()
time.sleep(5)
WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(password)
time.sleep(5)
WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div'))).click()
time.sleep(10)


#SEARCH
WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div.css-1dbjc4n.r-1habvwh > div.css-1dbjc4n.r-15zivkp.r-1bymd8e.r-13qz1uu > nav > a:nth-child(2) > div'))).click()
time.sleep(5)

WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input'))).send_keys('salman khan')
time.sleep(3)

#sarch list
# input = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="typeaheadDropdown-4"]/div[6]/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/span/svg/g/path'))).text
# print(input)
# if input:
    
    
WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="typeaheadDropdown-3"]/div[6]/div'))).click()


time.sleep(4)
