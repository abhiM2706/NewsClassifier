# NewsClassifier

This project was my introduction to Web Scraping and Text Classification with Embeddings

The goal of my project was to be able to classify a piece of text/paragraph to be written by MSNBC News or FOX News which are both known to have different political views.

The first step of the project was to web scrape 10,000 links from both fox news and nbc. I used https://www.msnbc.com/archive/articles for NBC News to scrape links from 2018-2023 and https://www.foxnews.com/sitemap.xml?type=articles&page=2 to acces the sitemap of FOx News and iterated through all the pages by changing the url. After gathering the links and putting them into csv files, I accessed each of these links to scrape the text. For NBC news I scraped all the content within the "article-body" html class and for Fox News I scraped the content in the "article-body__content" class to only scrape the main text of the article. To prevent any bias or incorrect learning from my model, I censored out the words "NBC" ad "FOX" from all the scraped text.

The next step was the training. 
