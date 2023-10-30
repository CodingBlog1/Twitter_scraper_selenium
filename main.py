from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
import pandas
from collections import defaultdict

load_dotenv()
username = os.getenv("USERNAME001")
password = os.getenv("PASSWORD")

print(username, password)

my_dict = defaultdict(list)

url = f"https://twitter.com"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(5)

#
WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div',
        )
    )
).click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
    )
).send_keys(username)
time.sleep(4)
WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div",
        )
    )
).click()
time.sleep(4)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
    )
).send_keys(password)
time.sleep(2)
WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div",
        )
    )
).click()
time.sleep(2)


# SEARCH
WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div.css-1dbjc4n.r-1habvwh > div.css-1dbjc4n.r-15zivkp.r-1bymd8e.r-13qz1uu > nav > a:nth-child(2) > div",
        )
    )
).click()
time.sleep(2)
input_field_Xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, input_field_Xpath))
).send_keys("salman khan")
time.sleep(3)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, input_field_Xpath))
).send_keys(Keys.RETURN)
time.sleep(2)
people_search_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div'

WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, people_search_button_xpath))
).click()


time.sleep(3)

people_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div[1]'
WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, people_xpath))
).click()

time.sleep(2)


location_user_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[1]/span/span'
location = (
    WebDriverWait(driver, 60)
    .until(EC.presence_of_element_located((By.XPATH, location_user_xpath)))
    .text
)
print(location)

joined_date_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[2]/span'
joined_date = (
    WebDriverWait(driver, 60)
    .until(EC.presence_of_element_located((By.XPATH, joined_date_xpath)))
    .text
)
print(joined_date)

following_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span'
following_count = (
    WebDriverWait(driver, 60)
    .until(EC.presence_of_element_located((By.XPATH, following_xpath)))
    .text
)
print("following", following_count)

followers_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span'
followers_count = (
    WebDriverWait(driver, 60)
    .until(EC.presence_of_element_located((By.XPATH, followers_xpath)))
    .text
)
print("followers", followers_count)


last_height = driver.execute_script("return document.body.scrollHeight")

post_count = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    tweet_elements = driver.find_elements(
        By.CSS_SELECTOR, 'article[data-testid="tweet"]'
    )

    post_count += len(tweet_elements)
    print("tweet_elements", len(tweet_elements))
    for tweet_element in tweet_elements:
        try:
            video_div = driver.find_element(
                By.CSS_SELECTOR, 'div[data-testid="videoComponent"]'
            )
            post_src = video_div.find_element(By.TAG_NAME, "video").get_attribute("src")

        except:
            post_src = ""

        comments = tweet_element.find_element(
            By.CSS_SELECTOR, 'div[data-testid="reply"]'
        )
        like = tweet_element.find_element(By.CSS_SELECTOR, 'div[data-testid="like"]')

        print("linkes", like.text)
        print("post_count", post_count)
        print("post_src", post_src)

        my_dict["Likes"].append(like.text)
        my_dict["Number of Comments"].append(comments.text)
        my_dict["Post Source URL"].append(post_src)

    if post_count >= 100:
        break
    if new_height == last_height:
        break

    last_height = new_height


df = dict(my_dict)
print(df)
data_df = pandas.DataFrame.from_dict(df)
print(data_df)
data_df.to_excel(f"{username}.xlsx", index=False)

time.sleep(4)
driver.quit()
