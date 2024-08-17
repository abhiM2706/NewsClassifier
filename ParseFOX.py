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
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

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

integer_array = np.random.randint(2, 10000, 400)
listFox = []
content_df = pd.read_csv('linksFox.csv')
for index in integer_array:

    link = content_df.iloc[index,1]
    print ("\n\n\n"+str(link)+"\n\n\n")
    # Target URL
    driver.get(link)
    # To load entire webpage
    time.sleep(1)
    check=True
    try:
        element = driver.find_element(By.CLASS_NAME, 'article-body')
        subelements = element.find_elements_by_css_selector("*")
        removeElement = element.find_element(By.CLASS_NAME, 'article-meta')
    except NoSuchElementException:
        check=False
    if(check==True):
        text=""

        for x in subelements:
            try:
                if(x.text != removeElement.text): 
                    text = text+x.text
            except(StaleElementReferenceException):
                text=""
        text = censor(text,removeElement.text)
        text = text.lower()
        text = censor(text,"fox")

        print(text)
        listFox.append(str(text))
    driver.delete_all_cookies()



dict = {'text': listFox}
df = pd.DataFrame(dict)
df.to_csv('textFox.csv')

