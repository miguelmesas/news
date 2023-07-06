import yaml

from config import logging
from extract import extract
from transform import transform
from load import load


def scrape():
    logging.info('Start process')

    try:
        logging.info('Reading config file ...')
        config_file = open('./conf.yml')
        pages = yaml.load(config_file, Loader=yaml.FullLoader)
    except Exception as e:
        logging.error(f'An error has ocurred: {e}')

    for page in pages['pages']:
        extracted = extract(page)

        if 'error' in extracted:
            continue

        articles = transform(extracted, page)
        load(articles)
