#piszemy nasz dekorator
import os
import sqlite3
from CustomLogger import logger
import time


def connection_retry(func):
    def wrapper(**kwargs):
        tries = kwargs['tries']
        delay = kwargs['delay']
        db_name = kwargs['db_name']
        for i in range(int(tries)):
            logger.info(f'It is y {i} try to connect')
            conn = None
            if os.path.isfile(db_name):
                try:
                    conn = sqlite3.connect(db_name)
                except Exception as e:
                    logger.error(f' The {i} attempt failed', exc_info=True)
                    time.sleep(delay)
                else:
                    logger.error
                return conn
            else:
                logger.error(f'No database {db_name}')

    return wrapper
