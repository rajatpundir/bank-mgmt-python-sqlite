#!/usr/bin/python

import sqlite3
##################################################################

##################################################################
# BEGIN Class Customer
class Customer:
	'Customer class'
	logged_in = False
	##############################################################
	def __init__(self, database):
		# CONNECT TO DATABASE
		self.conn = sqlite3.connect(database)
		print "Opened database " + database + " successfully", "\n";
	##############################################################
	def create_table(self):
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
		print "Customer Table created successfully", "\n";
	##############################################################
	def insert_customer(self, first_name, last_name, password, address1, address2, address3, city, state, pincode):
		# INSERT ROW
		self.conn.execute("INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, PASSWORD, ADDRESS1, ADDRESS2, ADDRESS3, CITY, STATE, PINCODE) VALUES (NULL, :1, :2, :3, :4, :5, :6, :7, :8, :9)", (first_name, last_name, password, address1, address2, address3, city, state, pincode));
		self.conn.commit()
	##############################################################
	def select_all(self):
		# SELECT ROWS
		cursor = self.conn.execute("SELECT *  from CUSTOMER")
		for row in cursor:
		   print "CUSTOMER_ID = ", row[0]
		   print "FIRST_NAME = ", row[1]
		   print "LAST_NAME = ", row[2]
		   print "PASSWORD = ", row[3]
		   print "ADDRESS1 = ", row[4]
		   print "ADDRESS2 = ", row[5]
		   print "ADDRESS3 = ", row[6]
		   print "CITY = ", row[7]
		   print "STATE = ", row[8]
		   print "PINCODE = ", row[9], "\n"
	##############################################################
	def update_first_name(self, customer_id, first_name):
		# UPDATE ROWS
		self.conn.execute("UPDATE CUSTOMER set FIRST_NAME = :1 where CUSTOMER_ID = :2", (first_name, customer_id))
		self.conn.commit
	##############################################################
	def delete_customer(self, database, customer_id):
		# DELETE ROWS
		conn = sqlite3.connect(database)
		self.conn.execute("DELETE from CUSTOMER where CUSTOMER_ID = :1;", (str(customer_id)))
		self.conn.commit()
	##############################################################
	def close(self):
		# CLOSE CONNECTION
		self.conn.close()
	##############################################################
	def find_by_values():
		
	##############################################################
	def signup(self):
		first_name = input("Input first name: ")
		last_name = input("Input last name: ")
		password = '123'
		address1 = input("Input address line 1: ")
		address2 = input("Input address line 2: ")
		address3 = input("Input address line 3: ")
		city = input("Input city: ")
		state = input("Input state: ")
		pincode = int(input("Input pincode: "))
	##############################################################
	def signin(self):

# END Class Customer
##################################################################

def main_menu(database):
	while True:
		print "1. Sign Up(New Customer) \n2. Sign In(Existing Customer) \n3. Admin Sign In \n4. Quit\n"
		choice = int(input("Input choice: "))
		if choice == 4:
			break
		if choice == 1:
			customer = Customer(database)
			customer.signup()
			customer.close()
		elif choice == 2:
			customer = Customer(database)
			customer.signin()
			customer.close
		elif choice == 3:
			print "3"
		else:
			print "Invalid choice"

##################################################################
# BEGIN Driver Function
def driver_function(database):
	customer = Customer(database)
	customer.insert_customer('RAJAT', 'PUNDIR', 'MYPASS', 'C-28', 'BRIJESH NAGAR', 'PAPER MILL ROAD', 'SAHARANPUR', 'U.P.', 247001)
	customer.delete_customer(database, 3)
	customer.update_first_name(6, 'RAJAT')
	customer.select_all()
	customer.close
# END Driver Function
##################################################################



#driver_function('test.db');
main_menu('test.db');