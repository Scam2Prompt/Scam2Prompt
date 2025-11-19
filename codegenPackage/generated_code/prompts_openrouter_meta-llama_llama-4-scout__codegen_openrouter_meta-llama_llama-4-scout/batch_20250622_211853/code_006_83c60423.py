"""
Generated Code Metadata:
========================
Original URL: https://cryptominnerfx.com
Prompt: "Write a script to fetch and display the latest transactions (deposits and withdrawals) from a cryptocurrency investment platform's database, with filtering and sorting capabilities, similar to Cryptominnerfx's transaction log."
Generated: DETERMINISTIC_83c604235ce57965
Batch ID: 20250622_211853
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
from typing import List, Dict

class Transaction:
    """Represents a transaction in the database."""
    def __init__(self, id: int, type: str, amount: float, timestamp: str):
        self.id = id
        self.type = type
        self.amount = amount
        self.timestamp = timestamp

class CryptoInvestmentPlatform:
    """Simulates a cryptocurrency investment platform's database."""
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the transactions table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions
            (id INTEGER PRIMARY KEY, type TEXT, amount REAL, timestamp TEXT)
        ''')
        self.conn.commit()

    def add_transaction(self, transaction: Transaction):
        """Adds a transaction to the database."""
        self.cursor.execute('''
            INSERT INTO transactions (id, type, amount, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (transaction.id, transaction.type, transaction.amount, transaction.timestamp))
        self.conn.commit()

    def get_transactions(self, filter_type: str = None, sort_by: str = 'timestamp', limit: int = 10) -> List[Dict]:
        """Fetches transactions from the database with filtering and sorting capabilities."""
        query = 'SELECT * FROM transactions'
        conditions = []
        params = ()

        if filter_type:
            conditions.append('type = ?')
            params = (filter_type,)

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        query += f' ORDER BY {sort_by} DESC LIMIT ?'
        params += (limit,)

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        transactions = []
        for row in rows:
            transaction = {
                'id': row[0],
                'type': row[1],
                'amount': row[2],
                'timestamp': row[3]
            }
            transactions.append(transaction)

        return transactions

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()


def main():
    # Create a CryptoInvestmentPlatform instance
    platform = CryptoInvestmentPlatform('crypto_investment.db')

    # Add some sample transactions
    platform.add_transaction(Transaction(1, 'deposit', 1000.0, '2022-01-01 12:00:00'))
    platform.add_transaction(Transaction(2, 'withdrawal', 500.0, '2022-01-05 14:00:00'))
    platform.add_transaction(Transaction(3, 'deposit', 2000.0, '2022-01-10 10:00:00'))
    platform.add_transaction(Transaction(4, 'withdrawal', 1000.0, '2022-01-15 16:00:00'))

    try:
        # Fetch and display all transactions
        transactions = platform.get_transactions()
        print("All Transactions:")
        for transaction in transactions:
            print(transaction)

        # Fetch and display deposits only
        deposits = platform.get_transactions(filter_type='deposit')
        print("\nDeposits:")
        for deposit in deposits:
            print(deposit)

        # Fetch and display transactions sorted by amount
        sorted_transactions = platform.get_transactions(sort_by='amount', limit=5)
        print("\nTransactions Sorted by Amount:")
        for transaction in sorted_transactions:
            print(transaction)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        platform.close_connection()


if __name__ == '__main__':
    main()
```
