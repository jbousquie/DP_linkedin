#!/usr/bin/python3

# Beautifulsoup :
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
# pip3 install beautifulsoup4
# pip3 install lxml

from bs4 import BeautifulSoup

INPUT_FILE = 'html/LinkedinWagnerJetsPrives.html'
CSV_FILE = 'output/jets.csv'

with open(INPUT_FILE) as input_file:
    data_soup = BeautifulSoup(input_file, 'lxml')
    #articles = data_soup.find_all('article', class_='comments-comment-item comments-reply-item reply-item')
    articles = data_soup.find_all('article')
    for article in articles:
        spantexts = article.find_all('span', class_='comments-comment-item__main-content')
        for spantext in spantexts:
            ltr = spantext.find('span', {"dir": "ltr"})
            print(ltr.text)
        
        span_replycount = article.find('span', class_='comments-comment-social-bar__replies-count')
        print(span_replycount)