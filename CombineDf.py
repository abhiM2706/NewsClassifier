import pandas as pd
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


dfNBC = pd.read_csv('textNBC.csv',usecols=['text'])
dfFox = pd.read_csv('textFox.csv',usecols=['text'])

dfNBC['label']='0'
dfFox['label']='1'

dfNew = pd.concat([dfNBC, dfFox],
          names=['Text', 'label'])
dfNew = dfNew.sample(frac=1)
dfNew = dfNew.dropna()
dfNew.to_csv('combinedText.csv')
