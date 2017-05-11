##################################################################
# BEGIN Class Transaction
class Transaction:
	'Transaction class'
	##############################################################
	def __init__(self, database):
		# CONNECT TO DATABASE
		self.conn = sqlite3.connect(database)
	##############################################################
	def create_table(self):
		# CREATE TRANSACTION TABLE
		self.conn.execute('''CREATE TABLE TRANSACTION(
			TRANSACTION_ID		INTEGER 	PRIMARY KEY		AUTOINCREMENT,
			ACCOUNT_ID			INTEGER,
			TRANSACTION_TYPE 		TEXT,
			TRANSACTION_AMOUNT	REAL,
			REMAINING_BALANCE	REAL,
			TRANSACTION_TIME	TEXT
			FOREIGN KEY(ACCOUNT_ID)	REFERENCES ACCOUNT(ACCOUNT_ID),
			);''')
		print "Transaction Table created successfully";
	##############################################################
	def insert_account(self, account_id, transaction_type, transaction_amount, remaining_balance):
		# INSERT ROW
		self.conn.execute("INSERT INTO TRANSACTION (TRANSACTION_ID, ACCOUNT_ID, TRANSACTION_TYPE, TRANSACTION_AMOUNT, REMAINING_BALANCE, TRANSACTION_TIME) VALUES (NULL, :1, :2, :3, :4, CURRENT_TIMESTAMP)", (account_id, transaction_type, transaction_amount, remaining_balance));
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
		   print "CLOSED_TIME = ", row[4], "\n"
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
		self.conn.execute("UPDATE ACCOUNT set WITHDRAWALS = :1 where ACCOUNT_ID = :2", (withdrawals, account_id))
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
# END Class Transaction
##################################################################
