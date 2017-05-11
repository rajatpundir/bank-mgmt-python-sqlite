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
		cursor = self.conn.execute("SELECT *  from ACCOUNT")
		for row in cursor:
		   self.delete_customer(database, row[0])
	##############################################################
	def update_balance(self, account_id, balance):
		# UPDATE PASSWORD
		self.conn.execute("UPDATE ACCOUNT set BALANCE = :1 where ACCOUNT_ID = :2", (balance, account_id))
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