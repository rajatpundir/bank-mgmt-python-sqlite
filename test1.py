#!/usr/bin/python

import sqlite3

class Db:
	'Common base class for all databases'

	def __init__(self, database):
		# CONNECT TO DATABASE
		self.conn = sqlite3.connect(database)
		print "Opened database " + database + " successfully";

	def create(self):
		# CREATE TABLE
		self.conn.execute('''CREATE TABLE CUSTOMER
		       (ID INT PRIMARY KEY     NOT NULL,
		       NAME           TEXT    NOT NULL,
		       AGE            INT     NOT NULL,
		       ADDRESS        CHAR(50),
		       SALARY         REAL);''')
		print "Table created successfully";

	def insert(self):
		# INSERT ROW
		self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
		self.conn.commit()

	def select(self):
		# SELECT ROWS
		cursor = self.conn.execute("SELECT id, name, address, salary  from COMPANY")
		for row in cursor:
		   print "ID = ", row[0]
		   print "NAME = ", row[1]
		   print "ADDRESS = ", row[2]
		   print "SALARY = ", row[3], "\n"
		print "Operation done successfully";

	def update(self):
		# UPDATE ROWS
		self.conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
		self.conn.commit
		print "Total number of rows updated :", conn.total_changes

	def delete(self):
		# DELETE ROWS
		self.conn.execute("DELETE from COMPANY where ID=2;")
		self.conn.commit()
		print "Total number of rows deleted :", conn.total_changes

	def close(self):
		# CLOSE CONNECTION
		self.conn.close()

customer = Db('test.db')
customer.select()