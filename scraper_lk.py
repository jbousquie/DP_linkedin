#!/usr/bin/python3

# Beautifulsoup :
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
# pip3 install beautifulsoup4
# pip3 install lxml

from bs4 import BeautifulSoup

INPUT_FILE = 'html/LinkedinWagnerJetsPrives.html'
CSV_FILE = 'output/jets_iramuteq.txt'

with open(INPUT_FILE) as input_file:
    data_soup = BeautifulSoup(input_file, 'lxml')
    articles = data_soup.find_all('article', class_='comments-comment-item')
    counter = 1
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

        line = '**** *num_' + str(counter) + ' *reactions_' + reaction_count + ' *comments_' + reply_count + '\n'
        line = line + post_text + '\n'
        counter += 1
        print(line)