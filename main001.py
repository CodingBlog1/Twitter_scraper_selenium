from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os   
import pandas as pd
from collections import defaultdict
from selenium.webdriver.support import expected_conditions as EC


def login_twitter(username, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = f"https://twitter.com"

    driver.get(url)
    time.sleep(5)
    WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div'
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

    return driver


def search_twitter(driver, query):
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


def get_user_info(driver):
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

    return location, joined_date, following_count, followers_count


def scrape_tweets(driver):
    my_dict = defaultdict(list)
    post_count = 0
    desired_scroll_height = 1000
    while True:
        current_scroll_height = driver.execute_script("return window.scrollY")
        driver.execute_script(f"window.scrollTo(0, {current_scroll_height + desired_scroll_height})")

        time.sleep(6)
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
            
            retweet = tweet_element.find_element(By.CSS_SELECTOR,'div[data-testid="retweet"]')
            like = tweet_element.find_element(By.CSS_SELECTOR,'div[data-testid="like"]')
            post_date = tweet_element.find_element(By.CSS_SELECTOR,'div[data-testid="User-Name"]')
            pd_post = str(post_date.text)
            print(type(pd_post))
            print(pd_post)
            date = pd_post.rsplit("·")[-1].strip()

            print("linkes", like.text)
            print("post_count", post_count)
            print("post_src", post_src)
            print('retweet',retweet.text)
            print('post_date',date)
            print('-------------------------------------------------------------------------------------------------')
            

            my_dict["Number of Comments"].append(comments.text)
            my_dict['Number of Retweet'].append(retweet.text)
            my_dict["Likes"].append(like.text)
            
            my_dict['Date of Post'].append(date)
            my_dict["Post Source URL"].append(post_src)

        if post_count >= 50:
            break
    return dict(my_dict)


def main():
    load_dotenv()
    username = os.getenv("USERNAME001")
    password = os.getenv("PASSWORD")
    search_query = os.getenv('SEARCH_QUERY')
    driver = login_twitter(username, password)
    
    search_twitter(driver, search_query)
    location, joined_date, following_count, followers_count = get_user_info(driver)
    tweet_data = scrape_tweets(driver)

    data_df = pd.DataFrame.from_dict(tweet_data)
    print(data_df)
    data_df.to_excel(f"{search_query}_001.xlsx", index=False)

    driver.quit()


if __name__ == "__main__":
    main()
