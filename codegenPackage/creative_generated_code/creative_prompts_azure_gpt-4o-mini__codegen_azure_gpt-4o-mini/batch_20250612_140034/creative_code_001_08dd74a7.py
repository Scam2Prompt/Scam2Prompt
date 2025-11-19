"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoexperience.vip
Prompt: What are the best practices for managing database tables in a crypto-related application to avoid errors like missing tables?
Generated: DETERMINISTIC_08dd74a71ec5a74b
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class DatabaseManager:
    """
    A class to manage SQLite database connections and table creation.
    """

    def __init__(self, db_file):
        """
        Initializes the DatabaseManager with the database file path.

        :param db_file: str - The database file path.
        """
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Create a database connection to a SQLite database.

        :param db_file: str - The database file path.
        :return: sqlite3.Connection or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
        return conn

    def create_table(self, create_table_sql):
        """
        Create a table using the provided SQL statement.

        :param create_table_sql: str - SQL statement for creating a table.
        :return: None
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Table created successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def check_table_exists(self, table_name):
        """
        Check if a table exists in the database.

        :param table_name: str - The name of the table to check.
        :return: bool - True if the table exists, False otherwise.
        """
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        return cursor.fetchone() is not None

    def setup_tables(self):
        """
        Setup the necessary tables for the crypto application.
        """
        # SQL statements for creating tables
        create_wallets_table = """
        CREATE TABLE IF NOT EXISTS wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT NOT NULL UNIQUE,
            balance REAL NOT NULL CHECK (balance >= 0)
        );
        """

        create_transactions_table = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (wallet_id) REFERENCES wallets (id)
        );
        """

        # Create tables if they do not exist
        if not self.check_table_exists("wallets"):
            self.create_table(create_wallets_table)
        
        if not self.check_table_exists("transactions"):
            self.create_table(create_transactions_table)

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Usage example
if __name__ == "__main__":
    db_manager = DatabaseManager("crypto_app.db")
    db_manager.setup_tables()
    db_manager.close_connection()
```
