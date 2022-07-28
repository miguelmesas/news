import os
import logging
from yaml import load
from yaml.loader import SafeLoader


BASEDIR = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(
    filename = os.path.join(BASEDIR, 'logs.log'),
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def _config():
    conf_file = os.path.join(BASEDIR, 'conf.yml')
    with open(conf_file) as f:
        data = load(f, Loader=SafeLoader)
    
    return data


def run():
    print('From run()')


if __name__ == '__main__':
    run()
