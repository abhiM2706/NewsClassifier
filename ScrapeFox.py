from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re 
from selenium.webdriver.common.by import By

from chromedriver_py import binary_path
import feedparser

import xml.etree.ElementTree as ET
import requests

link = "https://www.foxnews.com/sitemap.xml?type=articles&page="
urls = []

for i in range(2,3):
    mainLink = link+str(i)
    response = requests.get(mainLink)
    xml_content = response.content

    root = ET.fromstring(xml_content)

    namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    for url in root.findall('sitemap:url', namespace):
        loc = url.find('sitemap:loc', namespace).text
        urls.append(loc)
        print(loc)

dict = {'Links': urls}
df = pd.DataFrame(dict)
df = df.drop_duplicates('Links')
df.to_csv('linksFox.csv')