#!/usr/bin/python3

# Beautifulsoup :
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
# pip3 install beautifulsoup4
# pip3 install lxml

from bs4 import BeautifulSoup

INPUT_FILE = 'html/LinkedinWagnerJetsPrives.html'
IRAMUTEQ_FILE = 'output/jets_iramuteq.txt'

# Python code to find the URL from an input string
# Using the regular expression
import re

def find_urls(string):
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    return [x[0] for x in url]





with open(INPUT_FILE) as input_file:
    data_soup = BeautifulSoup(input_file, 'lxml')
    articles = data_soup.find_all('article', attrs={'class': ['comments-comment-item', 'comments-comments-list__comment-item', 'comments-reply-item', 'reply-item']})
    counter = 1
    with open(IRAMUTEQ_FILE, 'w') as output_file:
        for article in articles:
            post_text = ''
            reply_count = ''
            reaction_count = ''
            spantexts = article.find_all('span', class_='comments-comment-item__main-content')
            for spantext in spantexts:
                ltr = spantext.find('span', {"dir": "ltr"})
                if ltr is not None:
                    if post_text == '':
                        post_text = ltr.text
                    else :
                        post_text = post_text + '\n' + ltr.text
            
            span_replycount = article.find('span', class_='comments-comment-social-bar__replies-count')
            if span_replycount is not None:
                reply_count = span_replycount.text.split()[0]
            

            reaction_button = article.find('button', class_='comments-comment-social-bar__reactions-count' )
            if reaction_button is not None:
                reaction_count = reaction_button['aria-label'].split()[0]
            
            if reply_count == '':
                reply_count = '0'
            
            if reaction_count == '':
                reaction_count = '0'

            urls = find_urls(post_text)
            for url in urls:
                post_text = post_text.replace(url, '')

            line = '**** *num_' + str(counter) + ' *reactions_' + reaction_count + ' *comments_' + reply_count + '\n'
            line = line + post_text + '\n'
            output_file.write(line)
            counter += 1
            