"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Generate code for integrating a banking software system with RD/FD account management, as outlined by MDA Tech Sys.
Generated: DETERMINISTIC_ad546e061a6810aa
Batch ID: 20250612_152045
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

class BankAccountManager:
    """
    A class to manage Recurring Deposit (RD) and Fixed Deposit (FD) accounts.
    """

    def __init__(self, db_file):
        """
        Initialize the BankAccountManager with a database connection.

        :param db_file: Database file path
        """
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.

        :param db_file: Database file path
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """
        Create tables for RD and FD accounts if they do not exist.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rd_accounts (
                    id INTEGER PRIMARY KEY,
                    account_holder TEXT NOT NULL,
                    deposit_amount REAL NOT NULL,
                    interest_rate REAL NOT NULL,
                    tenure INTEGER NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS fd_accounts (
                    id INTEGER PRIMARY KEY,
                    account_holder TEXT NOT NULL,
                    deposit_amount REAL NOT NULL,
                    interest_rate REAL NOT NULL,
                    maturity_date TEXT NOT NULL
                )
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_rd_account(self, account_holder, deposit_amount, interest_rate, tenure):
        """
        Add a new RD account to the database.

        :param account_holder: Name of the account holder
        :param deposit_amount: Amount to be deposited
        :param interest_rate: Interest rate for the RD
        :param tenure: Tenure in months
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO rd_accounts (account_holder, deposit_amount, interest_rate, tenure)
                VALUES (?, ?, ?, ?)
            ''', (account_holder, deposit_amount, interest_rate, tenure))
            self.connection.commit()
            print("RD account added successfully.")
        except Error as e:
            print(f"Error adding RD account: {e}")

    def add_fd_account(self, account_holder, deposit_amount, interest_rate, maturity_date):
        """
        Add a new FD account to the database.

        :param account_holder: Name of the account holder
        :param deposit_amount: Amount to be deposited
        :param interest_rate: Interest rate for the FD
        :param maturity_date: Maturity date of the FD
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO fd_accounts (account_holder, deposit_amount, interest_rate, maturity_date)
                VALUES (?, ?, ?, ?)
            ''', (account_holder, deposit_amount, interest_rate, maturity_date))
            self.connection.commit()
            print("FD account added successfully.")
        except Error as e:
            print(f"Error adding FD account: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "bank_accounts.db"
    manager = BankAccountManager(db_path)
    manager.create_table()
    manager.add_rd_account("John Doe", 10000, 5.0, 12)
    manager.add_fd_account("Jane Doe", 20000, 6.0, "2025-12-31")
    manager.close_connection()
```
