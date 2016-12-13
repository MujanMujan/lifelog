#!/usr/bin/python3.5

## import required module

import time;
import sqlite3;
import os;
import sys;

## get localtime of system
localtime = time.asctime( time.localtime(time.time()) )

## just print welcome message
#print("welcome to lifelog application\nthe current time is :", localtime, "\n\n\n")


## database connection and table creation
conn = sqlite3.connect('lldb.db')
conn.execute('''CREATE TABLE IF NOT EXISTS LOGS
       (ID INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
       DATE           TEXT    NOT NULL,
       DETAIL            TEXT     NOT NULL);''')

## main of program :
try:
	if sys.argv[1] == "m":
		log = sys.argv[2]
		conn.execute('insert into LOGS(DATE,DETAIL)values ("%s","%s")'%(localtime,log))
		conn.commit()
		print("Log added !")
		conn.close()
	elif sys.argv[1] == "h":
		if len(sys.argv) >= 3:
			number_of_record = sys.argv[2]
		else:
			number_of_record = str(10)
		cu = conn.execute('select * from (select * from LOGS order by ID DESC limit ' + number_of_record + ') order by ID ASC;')
		for row in cu:
			print(str(row[0]) +  "| " + row[1] + "| log: "+ row[2])


except:
	print("\nhelp!")
	print("to add a log use '-m' flag\nexmp: lifelog m 'message want to save'")
	print("to see history of logs use '-h' flag\nexmp: lifelog h <number of lastest record>\ndefualt value is 10")

	sys.exit(0)






