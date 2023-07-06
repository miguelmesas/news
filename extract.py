import requests

from config import logging


def extract(page):
    page_name = page['name']
    page_url = page['url']

    logging.info(f'Extracting from: {page_name}')

    response = requests.get(page_url)
    if response.status_code == 200:
        return {
            'content': response.text,
            'status_code': response.status_code
        }
    else:
        logging.error(f'Request error on {page_name}: {response.status_code}')
        return {
            'error': 'An error as ocurred',
            'status_code': response.status_code
        }
