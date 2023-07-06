import re

from datetime import datetime
from bs4 import BeautifulSoup

from config import logging


def _get_title(title):
    if title is None:
        return None

    return title.text.strip()


def _get_link(link, base_url):
    if not link:
        return None

    uri = link.get('href')
    if re.match('^http.', uri):
        return uri
    else:
        return base_url + uri


def _get_epigraph(epigraph, title):
    if epigraph is None:
        return title
    
    return epigraph.text.strip()


def transform(extracted, page):
    content = extracted['content']
    page_name = page['name']
    page_url = page['url']
    article_tag = page['article']['tag']
    article_class = page['article']['class']

    logging.info(f'Cleaning data for: {page_name} ...')

    html = BeautifulSoup(content, 'html.parser')
    articles = html.find_all(article_tag, class_=article_class)

    data = []
    for article in articles:
        logging.info(f'Getting articles from: {page_name}')
        
        title_tag = page['title']['tag']
        title_class = page['title']['class']
        link_tag = page['link']['tag']
        link_class = page['link']['class']
        epigraph_tag = page['epigraph']['tag']
        epigraph_class = page['epigraph']['class']

        _title = article.find(title_tag, class_=title_class)
        _link = article.find(link_tag, class_=link_class)
        _epigraph = article.find(epigraph_tag, class_=epigraph_class)

        title = _get_title(_title)
        if title is None:
            continue

        link = _get_link(_link, page_url)
        epigraph = _get_epigraph(_epigraph, title)

        _article = {
            'page': page_name,
            'page_url': page_url,
            'title': title,
            'link': link,
            'epigraph': epigraph,
            'date': datetime.utcnow()
        }

        data.append(_article)
    
    return data
