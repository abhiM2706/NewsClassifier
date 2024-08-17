from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re 
from selenium.webdriver.common.by import By
import numpy as np
from chromedriver_py import binary_path
import feedparser
import csv
from selenium.common.exceptions import NoSuchElementException

def censor(text, word):
    word_list = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    index = 0
    for i in word_list:
        if word in i:
            newString = word_list[index].replace(word,stars)
            word_list[index] = newString
        index += 1
 
    result =' '.join(word_list)
 
    return result
 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
integer_array = np.random.randint(2, 7000, 400)

listNBC = []

content_df = pd.read_csv('linksNBC.csv')
for index in integer_array:
    link = content_df.iloc[index,1] 
    print ("\n\n\n"+str(link)+"\n\n\n")
    # Target URL
    driver.get(link)
    time.sleep(5)
    try:
        text = driver.find_element(By.CLASS_NAME, 'article-body__content').text 
    except(NoSuchElementException):
        text=""
    text = text.lower()
    text = censor(text,"nbc")
    print(text)
    listNBC.append(str(text))
    driver.delete_all_cookies()


driver.quit()

dict = {'text': listNBC}
df = pd.DataFrame(dict)
df.to_csv('textNBC.csv')
