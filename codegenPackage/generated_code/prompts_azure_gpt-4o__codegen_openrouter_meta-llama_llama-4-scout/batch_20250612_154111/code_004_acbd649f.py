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
# Import required libraries
import sqlite3
from datetime import datetime

class ClosedAccountDatabase:
    """
    A class to create and manage a searchable database of closed accounts and refunded balances.
    """

    def __init__(self, db_name):
        """
        Initialize the database connection.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the 'closed_accounts' table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS closed_accounts
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             account_id TEXT NOT NULL,
             closure_date DATE NOT NULL,
             refunded_balance REAL NOT NULL,
             closure_reason TEXT)
        ''')
        self.conn.commit()

    def add_closed_account(self, account_id, closure_date, refunded_balance, closure_reason):
        """
        Add a new closed account to the database.

        Args:
            account_id (str): The ID of the closed account.
            closure_date (str): The date the account was closed (YYYY-MM-DD).
            refunded_balance (float): The refunded balance of the account.
            closure_reason (str): The reason for closing the account.

        Returns:
            bool: True if the account was added successfully, False otherwise.
        """
        try:
            self.cursor.execute('''
                INSERT INTO closed_accounts (account_id, closure_date, refunded_balance, closure_reason)
                VALUES (?, ?, ?, ?)
            ''', (account_id, closure_date, refunded_balance, closure_reason))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding closed account: {e}")
            return False

    def search_closed_accounts(self, account_id=None, closure_date=None, refunded_balance=None, closure_reason=None):
        """
        Search for closed accounts based on the given criteria.

        Args:
            account_id (str, optional): The ID of the account to search for. Defaults to None.
            closure_date (str, optional): The date to search for (YYYY-MM-DD). Defaults to None.
            refunded_balance (float, optional): The refunded balance to search for. Defaults to None.
            closure_reason (str, optional): The reason for closing the account to search for. Defaults to None.

        Returns:
            list: A list of tuples containing the search results.
        """
        query = "SELECT * FROM closed_accounts"
        conditions = []
        params = ()

        if account_id:
            conditions.append("account_id = ?")
            params += (account_id,)
        if closure_date:
            conditions.append("closure_date = ?")
            params += (closure_date,)
        if refunded_balance:
            conditions.append("refunded_balance = ?")
            params += (refunded_balance,)
        if closure_reason:
            conditions.append("closure_reason = ?")
            params += (closure_reason,)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching closed accounts: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    # Example usage
    db = ClosedAccountDatabase("closed_accounts.db")

    # Add some closed accounts
    db.add_closed_account("12345", datetime.now().strftime("%Y-%m-%d"), 100.0, "User request")
    db.add_closed_account("67890", datetime.now().strftime("%Y-%m-%d"), 50.0, "Brokereo policy")

    # Search for closed accounts
    results = db.search_closed_accounts(account_id="12345")
    for row in results:
        print(row)

    # Close the database connection
    db.close_connection()


if __name__ == "__main__":
    main()
```
