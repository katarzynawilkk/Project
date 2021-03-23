import os
import time

from db_executer import Db_executer
from CustomLogger import logger
import datetime


logger.info(f"Start {datetime.datetime.now()}")

path_to_watch = '.'
before = dict([(f, None) for f in os.listdir(path_to_watch)])

while 1:
    db_name = r'C:\Users\Kasia\PycharmProjects\W1_cwiczenia\Project\clinic.db'
    db = Db_executer(db_name)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])

    added = []
    for name in after: #sprawdzamy czy pojawil sie nowy plik
        if not name in before: # porownanie
            added.append(name)#jesli nie a tej nazwy to znaczy ze zostal dodany

    removed = []
    for name in before:
        if not name in after:
            removed.append(name)

    if added: # jesli lista nie jest pusta to wchodze do tego bloku
        logger.info(f'Added:{added}')
        for added_file in added: # dla kazdego pliku
            if 'patients' in  added_file:
                with open(added_file, 'r') as file:  #otwieramy
                    rows = file.readlines() # odczytaj wiersz po wierszu
                    for row in rows:
                        row = row.split(',')
                        print(row)
                        db.insert_new_patient(row[0],row[1],row[2],row[3])
            if 'antarctica' in added_file:
                for name in added_file:
                    db.antarctica_analysis(name)
    else:
        logger.info('Nothing was added')

    if removed:
        logger.info(f'Removed {removed}')
    else:
        logger.info('Nothing was removed')

    before = after
    db.close_conn()
    time.sleep(10)




