#from db_executer import Db_executer
from CustomLogger import logger
import datetime

'''db_name = r"C:\Users\Kasia\PycharmProjects\W1_cwiczenia\Project\clinic.db"
db = Db_executer(db_name)'''

logger.info(f'Start{datetime.datetime.now()}')



#db.create_analysis_table()
#db.close_conn()


def send_sms(msg,phone_num):
    log.info(f"We sent message: {msg} to: {phone_num}")

'''with open(r"C:\Users\Kasia\PycharmProjects\W1_cwiczenia\Project\Antarctica.csv", encoding='UTF-8-sig') as csv_file3:
    all_row = csv.reader(csv_file3, delimiter=';')
    dane = db.select_all_tasks(table_name='patients')
    for row in all_row:
        if row[4] != 'collection_time':
            row[4] = str(datetime.strptime(row[4], "%d.%m.%Y %H:%M"))
        if row[5] == 'T':
           row[5] = 'True'
        else:
            row[5] = 'False'

        if row[2] != 'pesel':
            #print(row[2])
            znajdz = int(row[2])
            for i in dane:
                if (i[3]) == znajdz:
                    row[2] = i[0]
                    #print(row[2])

        if row[0] != "id":
            #print(row[1], row[3], row[2], row[4], row[5])
            db.insert_analysis(
            probe_number=row[1],
            analysis_id=row[3],
            patient_id=row[2],
            collection_time=row[4],
            result=row[5])
'''
        '''if row[5] == "False":
            week_days = ["Poniedzialek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
            obj_datetime = datetime.strptime(row[4], "%d.%m.%Y %H:%M")
            week_number = obj_datetime.weekday()
            msg = f'Dzień dobry, ' \
                  f'Zapraszamy na wizytę kontrolną w {week_days[week_number]} dokładna data ' \
                  f'{row[4]} o godzinie {obj_datetime.time()}'
            print(msg)
            send_sms(msg, row[7])'''






r'''with open(r"C:\Users\Kasia\PycharmProjects\W1_cwiczenia\Project\new_patients.csv", encoding="UTF-8") as csv_file:
    all_rows = csv.reader(csv_file, delimiter=',')
    print(all_rows)
    for row in all_rows:
        print(row)
        db.insert_new_patient(id=row[0], name=row[1], surname=row[2], pesel=row[3])'''



'''sql = """
    INSERT INTO analysis
    (probe_number, analysis_id, patient_id, collection_time, result)
    VALUES (?,?,?,?,?)
    """

analysis_data = [3423, 1, 18, "09.10.2021 19:00", "True"]
try:
    db.execute_sql(sql, analysis_data)
except Exception as e:
    print(f"Something went wrong {e}")'''


db.close_conn()


r'''db = db_handler.Database(r"C:\Users\Kasia\PycharmProjects\W1_cwiczenia\Project\patients.db")
db.execute_sql(sql_create_table)
print("DB created")

sql_insert = """
    INSERT INTO patients
    (id,name,surname,pesel)
    VALUES(?,?,?,?)

"""


with open (r"C:\Users\Kasia\PycharmProjects\W1_cwiczenia\Project\project-data.txt") as in_file:
    for line in in_file.readlines():
        patient_data = line.strip().split(sep=",")
        print(patient_data)
        db.execute_sql(sql_insert, patient_data)


db.close_conn()'''