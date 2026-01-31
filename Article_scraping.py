# Task 1 : web Scraping : use libraries like requests and BeautifulSoup to scrape data from a website [Welcome to pyton .org ]
import requests
from bs4 import BeautifulSoup
from collections import Counter
url='https://www.python.org'
def python_latest_articles():
    response=requests.get(url)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        latest_article=[]
        for articles in soup.select('.blog-widget li'):
            title=articles.a.text.strip()
            latest_article.append(title)
        return latest_article
if __name__=='__main__':
    python_articles=python_latest_articles()
    if python_articles:
        print('latest articles in python sections are :')
        for index,articles in enumerate(python_articles,1):
            print(f'{index} : {articles}')
# Task 2 : Word frequency create a programme that reads a created text file from task 1 and counts the frequency of the each word.
all_title=''.join(python_articles)
words=all_title.split()
word_count=Counter(words)
for word in words:
    word=word.strip().lower()
    if word:
        word_count[word]=word_count[word]+1
# sort the words by decending order
word_count=word_count.most_common()
for word,count in word_count:
    print(f'{word} : {count}')