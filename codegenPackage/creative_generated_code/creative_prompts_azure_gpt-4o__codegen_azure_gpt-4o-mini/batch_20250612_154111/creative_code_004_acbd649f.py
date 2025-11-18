"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokereo.com
Prompt: Generate code to create a searchable database of closed accounts and refunded balances, based on the procedures described in Brokereo's Terms and Conditions.
Generated: DETERMINISTIC_acbd649f249abe30
Batch ID: 20250612_154111
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

# Database handler class
class DatabaseHandler:
    def __init__(self, db_file):
        """Initialize the database handler with the given database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def create_table(self):
        """Create a table for storing closed accounts and refunded balances."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS closed_accounts (
            account_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            refund_balance REAL NOT NULL,
            closed_date TEXT NOT NULL,
            UNIQUE(account_id)
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_closed_account(self, account_id, user_id, refund_balance, closed_date):
        """Insert a closed account record into the closed_accounts table."""
        insert_sql = """
        INSERT INTO closed_accounts (account_id, user_id, refund_balance, closed_date)
        VALUES (?, ?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (account_id, user_id, refund_balance, closed_date))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Account ID {account_id} already exists.")
        except Error as e:
            print(f"Error inserting record: {e}")

    def search_closed_accounts(self, user_id):
        """Search for closed accounts by user_id."""
        search_sql = "SELECT * FROM closed_accounts WHERE user_id = ?;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(search_sql, (user_id,))
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error searching records: {e}")
            return []

# Example usage
if __name__ == "__main__":
    db_handler = DatabaseHandler("closed_accounts.db")
    db_handler.create_table()

    # Sample data for demonstration
    db_handler.insert_closed_account(1, 101, 150.00, '2023-10-01')
    db_handler.insert_closed_account(2, 102, 200.50, '2023-10-02')

    # Searching for closed accounts
    results = db_handler.search_closed_accounts(101)
    for record in results:
        print(record)

    # Close the database connection on exit
    db_handler.close_connection()
```
