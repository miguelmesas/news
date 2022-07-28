import requests
from bs4 import BeautifulSoup


class Portal:
    def __init__(self, portal: str, url: str, links_selector: dict) -> None:
        self.portal = portal
        self.url = url
        self.links_selector = links_selector

    def get_soup(self) -> bool:
        response = requests.get(self.url)
        
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
            return True

        self.soup = None
        return False

    def get_links_to_articles(self) -> list:
        attr = self.links_selector['attr']

        if attr == 'class':
            articles = self.find_by_class()
        elif attr == 'href':
            articles = self.find_by_href()
        else:
            articles = self.find_by_attr()

        return articles
        
    def find_by_class(self) -> list:
        tag = self.links_selector['tag']
        value = self.links_selector['value']
        articles = self.soup.find_all(tag, class_=value)
        
        if not articles:
            return []
        
        links = []
        for a in articles:
            links.append(a.get('href', ''))

        return links

    def find_by_href(self) -> list:
        print('href')

    def find_by_attr(self) -> list:
        print('attr')
