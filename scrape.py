import os
import logging
from turtle import pd

from yaml import load
from yaml.loader import SafeLoader

from extract import Portal


BASEDIR = os.path.abspath(os.path.dirname(__file__))


logging.basicConfig(
    filename = os.path.join(BASEDIR, 'logs.log'), level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s')


def _get_portals_conf() -> dict:
    """
    Returns the configuration of the portals for data extraction.
    """
    logging.info('obteniendo información de los portales.')
    conf_file = os.path.join(BASEDIR, 'conf.yml')
    with open(conf_file) as f:
        data = load(f, Loader=SafeLoader)
    
    return data


def _get_links_to_articles(portal_info: dict) -> list:
    logging.info(f'obteniendo links de los articulos para: {portal_info["name"]}')
    
    name = portal_info['name']
    url = portal_info['url']
    selector = portal_info['home_selector']
    portal = Portal(name, url, selector)
    
    if not portal.get_soup():
        logging.warning(f'no se pudo obtener el soup del home.')
        return []
    
    articles = portal.get_links_to_articles()
    return articles


def _get_articles_info(links: list, portal_info: dict):
    logging.info(f'obteniendo articulos para: {portal_info["name"]}')
    
    base_url = portal_info['url']

    articles = []
    for link in links:
        pass


if __name__ == '__main__':
    _portals = _get_portals_conf()

    for _portal in _portals:

        _links = _get_links_to_articles(_portal)
        if not _links:
            logging.warning('no se encontraron articulos.')
            continue
        
        _articles = _get_articles_info(_links, _portal)
        if not _articles:
            logging.warning('no se pudo extraer la información de los articulos')

        # Save articles
