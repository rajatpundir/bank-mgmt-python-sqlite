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
		self.conn.execute('''CREATE TABLE COMPANY
		       (ID INT PRIMARY KEY     NOT NULL,
		       NAME           TEXT    NOT NULL,
		       AGE            INT     NOT NULL,
		       ADDRESS        CHAR(50),
		       SALARY         REAL);''')
		print "Table created successfully";

	def create_customer_table(self):
		# CREATE CUSTOMER TABLE
		self.conn.execute('''CREATE TABLE CUSTOMER(
			CUSTOMER_ID		INTEGER 	PRIMARY KEY		AUTOINCREMENT,
			FIRST_NAME		TEXT,
			LAST_NAME		TEXT,
			PASSWORD		TEXT,
			ADDRESS1		CHAR(20),
			ADDRESS2		CHAR(20),
			ADDRESS3		CHAR(20),
			CITY			CHAR(20),
			STATE			CHAR(20),
			PINCODE			INTEGER(6)
			);''')
		print "Customer Table created successfully";

	def create_account_table(self):
		# CREATE ACOOUNT TABLE
		self.conn.execute('''CREATE TABLE AACOUNT(
			ACCOUNT_ID		INTEGER,
			FOREIGN KEY(ACCOUNT_ID)	REFERENCES CUSTOMER(CUSTOMER_ID),
			ACCOUNT_TYPE 	INTEGER,
			BALANCE			REAL,
			CLOSED			TEXT,
			CLOSED_TIME		TEXT
			);''')
		print "Account Table created successfully";

	def create_transaction_table(self):
		# CREATE ACOOUNT TABLE
		self.conn.execute('''CREATE TABLE AACOUNT(
			TRANSACTION_ID		INTEGER 	PRIMARY KEY		AUTOINCREMENT,
			ACCOUNT_ID			INTEGER,
			FOREIGN KEY(ACCOUNT_ID)	REFERENCES ACCOUNT(ACCOUNT_ID),
			TRANSACTION_TYPE 		TEXT,
			REMAINING_BALANCE	REAL,
			TRANSACTION_TIME	TEXT
			);''')
		print "Transaction Table created successfully";

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

class Customer:
	