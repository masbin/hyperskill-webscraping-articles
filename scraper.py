import requests
import os
from bs4 import BeautifulSoup
import string

def get_articles(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.findAll("article")
        print(len(articles))
        found_list =[]
        for article in articles:
            category = article.findChild("span",  {"data-test":"article.type"}).text.strip()
            headline = article.findChild("a").get_text()
            link_url = article.findChild("a").get('href')
            found = {'cat':category, 'link': link_url, 'title': headline}
            found_list.append(found)
        print(found_list)
        return found_list

def createFileName(sentence):
    return sentence.translate(str.maketrans(' ', '_', string.punctuation))

def save_article(article_list, root_url, category, page_number):
    os.mkdir(f'Page_{page_number}')
    for article in article_list:
        if article['cat'] == category:
            article_url = root_url + article['link']
            filename = createFileName(article['title']) + '.txt'
            print(f"Getting article {article_url} for page {page_number}")
            r = requests.get(article_url)
            if r.status_code == 200:
                file = open(f'Page_{page_number}\\{filename}', 'wb')
                soup = BeautifulSoup(r.content, 'html.parser')
                if soup.find("div",  {"class":"article__body cleared"}):
                    article_body = soup.find("div",  {"class":"article__body cleared"}).get_text()
                    print("found content in article__body cleared")
                elif soup.find("div",  {"class":"c-article-section"}):
                    article_body = soup.find("div",  {"class":"c-article-section"}).get_text()
                    print("found content in c-article-section")
                elif soup.find("div",  {"class":"article-item__body"}):
                    article_body = soup.find("div",  {"class":"article-item__body"}).get_text()
                    print("found content in article-item__body")
                print(f"writing file to Page_{page_number}\\{filename}")
                file.write(bytes(article_body, encoding='utf-8'))
                file.close()
    return "Articles downloaded successfully"

no_of_pages = int(input())
find_category = input()
root_url = "https://nature.com"
print(no_of_pages)
print(find_category)

for i in range(1, no_of_pages + 1):
    print(f"get page {i}")
    url_input = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i}"
    new_article = (get_articles(url_input))
    print(save_article(new_article, root_url, find_category, i))
