#!/usr/bin/python3.5

import time;
import sqlite3;
import os;
import sys;


localtime = time.asctime( time.localtime(time.time()) )

print("welcome to lifelog application\nthe current time is :", localtime)
print("type your log then press return")

if sys.argv[1] == "-m":
	matn = sys.argv[2]



localtime = time.asctime( time.localtime(time.time()) )


conn = sqlite3.connect('test3.db')

print("Opened database successfully")
#CREATE TABLE IF NOT EXISTS

conn.execute('''CREATE TABLE IF NOT EXISTS LOGS
       (ID INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
       DATE           TEXT    NOT NULL,
       DETAIL            TEXT     NOT NULL);''')

print("table created successfully")


test = "alaki"

conn.execute('insert into LOGS(DATE,DETAIL)values ("%s","%s")'%(localtime,matn))
conn.commit()


cu = conn.execute('SELECT * FROM LOGS')
for row in cu:
	print(str(row[0]) +  "| " + row[1] + "| log: "+ row[2])




conn.close()
