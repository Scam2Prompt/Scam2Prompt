"""
Generated Code Metadata:
========================
Original URL: https://brokereo.com
Prompt: Generate code to create a searchable database of closed accounts and refunded balances, based on the procedures described in Brokereo's Terms and Conditions.
Generated: DETERMINISTIC_acbd649f249abe30
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class ClosedAccountsDatabase:
    """
    A class to manage a SQLite database for closed accounts and refunded balances.
    """

    def __init__(self, db_file):
        """
        Initialize the database connection.
        
        :param db_file: Database file path
        """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.
        
        :param db_file: Database file path
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """
        Create a table for closed accounts if it doesn't exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS closed_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number TEXT NOT NULL,
            refund_amount REAL NOT NULL,
            closure_date TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Closed accounts table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_closed_account(self, account_number, refund_amount, closure_date):
        """
        Insert a new closed account into the database.
        
        :param account_number: The account number of the closed account
        :param refund_amount: The refunded balance
        :param closure_date: The date the account was closed
        """
        insert_sql = """
        INSERT INTO closed_accounts (account_number, refund_amount, closure_date)
        VALUES (?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (account_number, refund_amount, closure_date))
            self.connection.commit()
            print(f"Inserted closed account: {account_number}")
        except Error as e:
            print(f"Error inserting closed account: {e}")

    def search_closed_accounts(self, account_number):
        """
        Search for closed accounts by account number.
        
        :param account_number: The account number to search for
        :return: List of matching closed accounts
        """
        search_sql = """
        SELECT * FROM closed_accounts WHERE account_number = ?;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(search_sql, (account_number,))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error searching closed accounts: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = ClosedAccountsDatabase("closed_accounts.db")
    db.insert_closed_account("123456789", 150.75, "2023-10-01")
    accounts = db.search_closed_accounts("123456789")
    print("Search results:", accounts)
    db.close_connection()
```
