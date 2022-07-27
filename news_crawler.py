import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def fetch_google_news_data():
    result = []
    url = 'https://news.google.com/search?q=%EB%88%84%EC%88%98&hl=ko&gl=KR&ceid=KR%3Ako'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    root_link = 'https://www.google.com/'

    print(soup)

    # tag, attribues
    list_items = soup.find_all('div', 'NiLAwe')

    for item in list_items:
        # title
        title = item.find('a', 'DY5T1d RZIKme').text

        # link
        page_raw_link = root_link + item.find('a', 'VDXfz')['href']
        page_part_links = urlparse(page_raw_link)
        normalized_page_link = page_part_links.scheme + '://' + page_part_links.hostname + page_part_links.path

        # id
        news_id = page_part_links.path.split('/')[-1]
        link_obj = {
            'title': title,
            'link': normalized_page_link,
            'news_id': news_id
        }

        print(title)
        result.append(link_obj)
    return result


if __name__ == '__main__':
    fetch_google_news_data()
