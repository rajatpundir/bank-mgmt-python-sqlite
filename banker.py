#!/usr/bin/python

import sqlite3
##################################################################

##################################################################
# BEGIN Class Account
class Account:
	'Account class'
	##############################################################
	def __init__(self, database):
		# CONNECT TO DATABASE
		self.conn = sqlite3.connect(database)
	##############################################################
	def create_table(self):
		# CREATE ACOOUNT TABLE
		self.conn.execute('''CREATE TABLE ACCOUNT(
			ACCOUNT_ID		INTEGER,
			ACCOUNT_TYPE 	TEXT,
			BALANCE			REAL,
			WITHDRAWALS		INTEGER,
			LAST_WITHDRAWAL_TIME	TEXT,
			CLOSED_TIME		TEXT,
			FOREIGN KEY(ACCOUNT_ID)	REFERENCES CUSTOMER(CUSTOMER_ID)
			);''')
	##############################################################
	def insert_account(self, account_id, account_type, balance):
		# INSERT ROW
		self.conn.execute("INSERT INTO ACCOUNT (ACCOUNT_ID, ACCOUNT_TYPE, BALANCE, WITHDRAWALS, LAST_WITHDRAWAL_TIME, CLOSED_TIME) VALUES (:1, :2, :3, 0, NULL, NULL)", (account_id, account_type, balance));
		self.conn.commit()
	##############################################################
	def select_all(self):
		# SELECT ROWS
		cursor = self.conn.execute("SELECT *  from ACCOUNT")
		for row in cursor:
		   print "ACCOUNT_ID = ", row[0]
		   print "ACCOUNT_TYPE = ", row[1]
		   print "BALANCE = ", row[2]
		   print "WITHDRAWALS = ", row[3]
		   print "LAST_WITHDRAWAL_TIME = ", row[4]
		   print "CLOSED_TIME = ", row[5], "\n"
	##############################################################
	def get_balance(self, account_id):
		cursor = self.conn.execute("SELECT * from ACCOUNT where ACCOUNT_ID = :1", (str(account_id),))
		for row in cursor:
			return row[2]
	##############################################################
	def get_withdrawals(self, account_id):
		cursor = self.conn.execute("SELECT * from ACCOUNT where ACCOUNT_ID = :1", (str(account_id),))
		for row in cursor:
			return row[3]
	##############################################################
	def delete_all(self, database):
		# DELETE ROWS
		cursor = self.conn.execute("SELECT *  from ACCOUNT")
		for row in cursor:
		   self.delete_customer(database, row[0])
	##############################################################
	def update_balance(self, account_id, balance):
		# UPDATE PASSWORD
		self.conn.execute("UPDATE ACCOUNT set BALANCE = :1 where ACCOUNT_ID = :2", (balance, account_id))
		self.conn.commit
	##############################################################
	def update_withdrawals(self, account_id, withdrawals):
		# UPDATE PASSWORD
		self.conn.execute("UPDATE ACCOUNT set WITHDRAWALS = :1, LAST_WITHDRAWAL_TIME = CURRENT_TIMESTAMP where ACCOUNT_ID = :2", (withdrawals, account_id))
		self.conn.commit
	##############################################################
	def delete_account(self, database, account_id):
		# DELETE ROWS
		conn = sqlite3.connect(database)
		self.conn.execute("DELETE from ACCOUNT where ACCOUNT_ID = :1;", (str(account_id),))
		self.conn.commit()
	##############################################################
	def close(self):
		# CLOSE CONNECTION
		self.conn.close()
# END Class Account
##################################################################

##################################################################
# BEGIN Class Customer
class Customer:
	'Customer class'
	##############################################################
	def __init__(self, database):
		# CONNECT TO DATABASE
		self.conn = sqlite3.connect(database)
		# print "Opened database " + database + " successfully", "\n";
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
	def delete_all(self, database):
		# DELETE ROWS
		cursor = self.conn.execute("SELECT *  from CUSTOMER")
		for row in cursor:
		   self.delete_customer(database, row[0])
	##############################################################
	def update_password(self, customer_id, password):
		# UPDATE PASSWORD
		self.conn.execute("UPDATE CUSTOMER set PASSWORD = :1 where CUSTOMER_ID = :2", (password, customer_id))
		self.conn.commit
	##############################################################
	def get_password(self, customer_id):
		cursor = self.conn.execute("SELECT * from CUSTOMER where CUSTOMER_ID = :1", (str(customer_id),))
		for row in cursor:
			return row[3]
	##############################################################
	def delete_customer(self, database, customer_id):
		# DELETE ROWS
		conn = sqlite3.connect(database)
		self.conn.execute("DELETE from CUSTOMER where CUSTOMER_ID = :1;", (str(customer_id),))
		self.conn.commit()
	##############################################################
	def close(self):
		# CLOSE CONNECTION
		self.conn.close()
	##############################################################
	def find_by_values(self, first_name, last_name, password, address1, address2, address3, city, state, pincode):
		cursor = self.conn.execute("SELECT CUSTOMER_ID  from CUSTOMER WHERE FIRST_NAME = :1 AND LAST_NAME = :2 AND PASSWORD = :3 AND ADDRESS1 = :4 AND ADDRESS2 = :5 AND ADDRESS3 = :6 AND CITY = :7 AND STATE = :8 AND PINCODE = :9 ORDER BY CUSTOMER_ID DESC", (first_name, last_name, password, address1, address2, address3, city, state, pincode))
		for row in cursor:
		   return row[0]
	##############################################################
	def signup(self, database):
		first_name = raw_input("Input first name: ")
		last_name = raw_input("Input last name: ")
		address1 = raw_input("Input address line 1: ")
		address2 = raw_input("Input address line 2: ")
		address3 = raw_input("Input address line 3: ")
		city = raw_input("Input city: ")
		state = raw_input("Input state: ")
		pincode = int(input("Input pincode: "))
		self.insert_customer(first_name, last_name, 'NULL', address1, address2, address3, city, state, pincode)
		customer_id = self.find_by_values(first_name, last_name, 'NULL', address1, address2, address3, city, state, pincode)
		password = raw_input("\nYour Customer-ID is " + str(customer_id) + "\nPlease enter password for your account: ")
		print password
		self.update_password(customer_id, str(password))
		self.conn.commit()
		balance = float(input("Input balance: "))
		account_type = 's'
		if balance > 5000:
			account_type = raw_input("Input account type(s for savings, c for current): ")
		account = Account(database)
		account.insert_account(customer_id, account_type, balance)
		account.close()
	##############################################################
	def signin(self, database):
		logged_in = False
		if not logged_in:
			customer_id = raw_input("\nInput Customer ID: ")
			password = raw_input("Input password: ")
			if password == self.get_password(customer_id):
				logged_in = True
				print "You have successfully logged in !"
			else:
				print "Invalid Customer ID or password"

		while logged_in:
			print "\n1. Address Change \n2. Money Deposit \n3. Money Withdrawal \n4. Print Statement \n5. Transfer Money \n6. Account Closure \n7. Customer Logout\n"
			choice = int(input("Input choice: "))
			if choice == 7:
				# CUSTOMER LOGOUT
				logged_in = False
				break
			if choice == 1:
				# ADDRESS CHANGE
				address1 = raw_input("Input address line 1: ")
				address2 = raw_input("Input address line 2: ")
				address3 = raw_input("Input address line 3: ")
				city = raw_input("Input city: ")
				state = raw_input("Input state: ")
				pincode = int(input("Input pincode: "))
				self.conn.execute("UPDATE CUSTOMER set ADDRESS1 = :1, ADDRESS2 = :2, ADDRESS3 = :3, CITY = :4, STATE = :5, PINCODE = :6 where CUSTOMER_ID = :7", (address1, address2, address3, city, state, pincode, customer_id))
				self.conn.commit()
			elif choice == 2:
				# MONEY DEPOSIT
				money = float(input("Input amount to deposit: "))
				if(money > 0):
					account = Account(database)
					balance = float(account.get_balance(customer_id))
					account.update_balance(customer_id, balance + money)
					account.conn.commit()
					account.close
			elif choice == 3:
				# MONEY WITHDRAWAL
				account = Account(database)
				withdrawals = account.get_withdrawals(customer_id)
				if withdrawals < 10:
					money = float(input("Input amount to withdraw: "))
					balance = float(account.get_balance(customer_id))
					if money <= balance:
						account.update_balance(customer_id, balance - money)
						account.update_withdrawals(customer_id, withdrawals + 1)
					else:
						print "You cannot withdraw more money than you own!\n"
				else:
					print "You have already withdrawn money 10 times for this month\n"
				account.conn.commit()
				account.close
			elif choice == 4:
				# PRINT STATEMENT
				print "x4x"
			elif choice == 5:
				# TRANSFER MONEY
				print "x5x"
			elif choice == 6:
				# TRANSFER MONEY
				print "x6x"
			elif choice == 8:
				customer = Customer(database)
				customer.select_all()
				customer.close
			else:
				account = Account(database)
				account.select_all()
				account.close
# END Class Customer
##################################################################

##################################################################
# BEGIN MAIN MENU
def main_menu(database):
	while True:
		print "1. Sign Up(New Customer) \n2. Sign In(Existing Customer) \n3. Admin Sign In \n4. Quit\n"
		choice = int(input("Input choice: "))
		if choice == 4:
			break
		if choice == 1:
			customer = Customer(database)
			customer.signup(database)
			customer.close()
		elif choice == 2:
			customer = Customer(database)
			customer.signin(database)
			customer.close
		elif choice == 3:
			print "3"
		else:
			print "Invalid choice"
# END MAIN MENU
##################################################################

##################################################################
# BEGIN Driver Program
database = 'test.db'
try:
	customer = Customer(database)
	customer.create_table()
	customer.close()
	account = Account(database)
	account.create_table()
	account.select_all()
	account.close
except:
	pass
main_menu(database);
# END Driver Program
##################################################################
