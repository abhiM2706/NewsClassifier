from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re 

from chromedriver_py import binary_path

#path = r"C:\Users\abhi2\OneDrive\Desktop\chrome-win64.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())

mainLink = "https://www.msnbc.com/archive/articles/"
MONTHS = ['january','february','march','april','may','june','july', 'august','september','october','november','december']
COLUMN_NAMES=['Links']


def getLinks(startLink):
    linkList = []
    regexnbc = r"^https://www.msnbc.com/.*" 
    pattern = re.compile(regexnbc)
    
    for i in range(2021,2023):
        for j in range (3,11):  
            newLink = mainLink+str(i)+"/"+str(MONTHS[j])
            driver.get(newLink)
            time.sleep(5)
            links = driver.find_elements_by_tag_name("a")
            for link in links:
                list = pattern.findall(str(link.get_attribute("href")))
                if(len(list)!=0):
                    print(str(link.get_attribute("href")))
                    linkList.append(str(link.get_attribute("href")))

    driver.quit()
    return linkList


list = getLinks(mainLink)
dict = {'Links': list}
df = pd.DataFrame(dict)
df = df.drop_duplicates('Links')
df.to_csv('linksNBC.csv')