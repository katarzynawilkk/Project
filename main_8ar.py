from db_executer import Db_executer
import csv
from datetime import datetime

from send_sms import send_sms

db_name = r"C:\Users\cp24\Desktop\Akademia Kodu\Project\clinic.db"
db = Db_executer(db_name)

#wstawianie zadziała tylko raz, ponieważ gdy na bazie bedą już dane id wywoła się bład Uniqe error
csv_file = r'C:\Users\cp24\Desktop\Akademia Kodu\Project\Antarctica.csv'
all_db_patients = db.select_all_tasks("patients")
print(all_db_patients)

def antarctica_analysis(csv_file):
    with open(csv_file, encoding="utf-8-sig") as an_file:
        all_rows = csv.reader(an_file, delimiter=';')
        for one_row in all_rows:
            #print(one_row)
            for one_patient in all_db_patients:
                #print(type(one_row[2]), one_row[2], type(one_patient[3]), one_patient[3])
                if one_row[0] != 'id':
                    if one_row[2] == str(one_patient[3]): #porównuje pesele aby dostać id
                        one_row[4] = str(datetime.strptime(one_row[4], "%d.%m.%Y %H:%M"))
                        if one_row[5] == 'T':
                            one_row[5] = 'True'
                        else:
                            one_row[5] = 'False'
                        db.insert_analysis(
                            probe_number=one_row[1],
                            analysis_id=one_row[3],
                            patient_id=one_patient[0], #odnosimy się do bazy danych do tablicy patients i wyciągamy id
                            collection_time=one_row[4],
                            result=one_row[5]
                        )
                        if one_row[5] == "False":
                            week_days = ["Poniedzialek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
                            obj_datetime = datetime.strptime(one_row[6], "%d.%m.%Y %H:%M")
                            week_number = obj_datetime.weekday()
                            msg = f'Dzień dobry, ' \
                                  f'Zapraszamy na wizytę kontrolną w {week_days[week_number]} dokładna data ' \
                                  f'{one_row[6]} o godzinie {obj_datetime.time()}'

                            send_sms(msg, one_row[7])

db.close_conn()




