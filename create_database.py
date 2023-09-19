#this python file will load Crime_Incidents.cvs and create a database from the data. You must move the csv
#file into the same directory in order to run this properly


import csv
import sqlite3
from sqlite3 import Error

case_num = []
date = []
time = []
weekday = []
incident_type = []
address = []
location = []
latitude = []
longitude = []
neighborhood = []
with open('Crime_Incidents.csv') as f:
    reader = csv.reader(f)
    next(reader)
    i = 0
    for row in reader:
        temp_date = row[1].split()
        try:
            if int(temp_date[0][6:10]) <= 2009:
                pass
            else:

                date.append(temp_date[0])
                if temp_date[2] == 'AM':
                    time.append(temp_date[1])
                else:
                    time.append(str(int(temp_date[1][0:2])+12)+temp_date[1][2:8])
                case_num.append(row[0])
                incident_type.append(row[3])
                weekday.append(row[7])
                address.append(row[8])
                location.append(row[11])
                latitude.append(row[12])
                longitude.append(row[13])
                neighborhood.append(row[22])
        except IndexError:
            pass
print(time[0:10])
print(temp_date)
data = list(zip(case_num,date,time,weekday,incident_type,address,location,latitude,longitude,neighborhood))



def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql, drop_table_name=None):
    
    if drop_table_name: 
        try:
            c = conn.cursor()
            c.execute("""DROP TABLE IF EXISTS %s""" % (drop_table_name))
        except Error as e:
            print(e)
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

conn = create_connection('normalized.db')
data_table = """
        CREATE TABLE IF NOT EXISTS Crime(
        CaseNumber text not null primary key,
        Date text,
        Time text,
        Weekday text,
        IncidentType text,
        Address text,
        Location text,
        Latitude real,
        Longitude real,
        Neighborhood text
    );
    """
with conn:
        create_table(conn, data_table, 'Crime')

        cur = conn.cursor()
        cur.executemany("INSERT INTO Crime VALUES(?,?,?,?,?,?,?,?,?,?)",data)