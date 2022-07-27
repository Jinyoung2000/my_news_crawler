import os
import requests
from bs4 import BeautifulSoup
import django

from urllib.parse import urlparse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_news_crawler.settings")
django.setup()
from main.models import NewsData


def fetch_google_news_data():
    result = []
    url = 'https://news.google.com/search?q=%EB%88%84%EC%88%98%ED%83%90%EC%A7%80&hl=ko&gl=KR&ceid=KR%3Ako'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    root_link = 'https://news.google.com/'

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
        try:
            NewsData(title=title, link=normalized_page_link, news_id=news_id).save()
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    fetch_google_news_data()
