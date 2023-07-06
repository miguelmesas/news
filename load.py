import os
import pymongo

from config import logging


def _check_existing(articles):
    collection = _db_connection()
    articles = articles
    articles_to_save = []

    for article in articles:
        query = list(collection.find({'link': article['link']}))
        if query:
            continue
        else:
            articles_to_save.append(article)
    
    return articles_to_save


def _db_connection():
    _db = os.getenv('MONGO_INITDB_DATABASE')
    _db_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    _db_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

    mongo_client = pymongo.MongoClient(f'mongodb://{_db_user}:{_db_password}@mongo:27017')
    db = mongo_client[_db]
    collection = db['articles']

    return collection 


def load(articles):
    logging.info('Saving articles ...')

    articles = _check_existing(articles)
    try:
        collection = _db_connection()
        collection.insert_many(articles)
    except Exception as e:
        logging.error(f'An error as ocurred: {e}')
    
    logging.info('Articles saved')
