import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',

    handlers=[
        logging.FileHandler(filename='log.txt', mode='w'),
        logging.StreamHandler(sys.stdout)
    ]
)