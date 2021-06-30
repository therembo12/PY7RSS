# from feedparser import *
# from bs4 import BeautifulSoup
# import lxml
# from pprint import pprint
# from datetime import datetime
# from time import mktime
# import json
# import EP_parsing.parser_1 as parser
# import EP_parsing.parser_2 as parser_2

# RSS_URL = 'https://www.pravda.com.ua/rss/view_news/'


# feed = parse(RSS_URL)

# # print(feed)
# urls = [
#     'pravda.com.ua',
#     'eurointegration.com.ua',
#     'life.pravda.com.ua',
#     'epravda.com.ua'
# ]

# news = []

# for item in feed.entries:
#     data = {}
#     data['title'] = item.title
#     data['desc'] = item.summary
#     data['url'] = item.link
#     data['date'] = f'{item.published_parsed[2]}-{item.published_parsed[1]}-{item.published_parsed[0]}  {item.published_parsed[3]}:{item.published_parsed[4]}:{item.published_parsed[5]}'
#     if data['url'].split('/')[2][4:] == 'pravda.com.ua':
#         data.update(parser(data['url']))

# news.append(data)

# elif data['url'].split('/')[2][4:] == 'epravda.com.ua':
#     data['content'] = parser_2.parse(data['url'])

# with open('news.json', 'w') as file:
#     json.dump(news, file, indent=4)
#     file.close()
from feedparser import *
from pprint import pprint
from datetime import datetime
from time import mktime
import json
from EP_parsing.parser_1 import parse as parser1
from EP_parsing.parser_2 import parse as parser2
from EP_parsing.parser_3 import parse as parser3
from EP_parsing.parser_4 import parse as parser4


RSS_URL = 'https://www.pravda.com.ua/rss/view_news/'
feed = parse(RSS_URL)
urls = [
    'pravda.com.ua',
    'eurointegration.com.ua',
    'life.pravda.com.ua',
    'epravda.com.ua'
]
news = []
for item in feed.entries:
    data = {}
    data['title'] = item.title
    data['description'] = item.summary
    data['url'] = item.link
    data['date'] = f'{item.published_parsed[2]}-{item.published_parsed[1]}-{item.published_parsed[0]}  {item.published_parsed[3]}:{item.published_parsed[4]}:{item.published_parsed[5]}'
    if data['url'].split('/')[2][4:] == 'pravda.com.ua':
        data.update(parser1(data['url']))
    elif data['url'].split('/')[2][4:] == 'epravda.com.ua':
        data.update(parser2(data['url']))
    elif data['url'].split('/')[2][0:] == 'life.pravda.com.ua':
        data.update(parser3(data['url']))
    elif data['url'].split('/')[2][0:] == 'eurointegration.com.ua':
        data.update(parser4(data['url']))
    news.append(data)

with open('news.json', 'w', encoding='utf8') as file:
    json.dump(news, file, indent=4, ensure_ascii=False)
    file.close()
