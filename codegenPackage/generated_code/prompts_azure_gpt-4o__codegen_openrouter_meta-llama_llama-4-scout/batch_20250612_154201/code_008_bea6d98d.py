"""
Generated Code Metadata:
========================
Original URL: https://upgrade-fegs.pages.dev
Prompt: Generate a Python script that calculates the total USD value of FEG Token transactions within the last 30 days, categorized by buy and sell types.
Generated: DETERMINISTIC_bea6d98d765dfa9f
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feg_token_transactions.py

import datetime
import sqlite3
from typing import Dict, List

class FEGTokenTransaction:
    def __init__(self, id: int, type: str, amount: float, usd_value: float, timestamp: datetime.datetime):
        """
        Initialize a FEG Token transaction.

        Args:
        - id (int): Unique transaction ID.
        - type (str): Type of transaction (buy or sell).
        - amount (float): Amount of FEG Tokens transacted.
        - usd_value (float): USD value of the transaction.
        - timestamp (datetime.datetime): Timestamp of the transaction.
        """
        self.id = id
        self.type = type
        self.amount = amount
        self.usd_value = usd_value
        self.timestamp = timestamp

class FEGTokenTransactionCalculator:
    def __init__(self, db_name: str):
        """
        Initialize the calculator with a database name.

        Args:
        - db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        Close the database connection when the calculator is destroyed.
        """
        self.conn.close()

    def get_transactions(self, days: int = 30) -> List[FEGTokenTransaction]:
        """
        Retrieve FEG Token transactions from the database within the specified time frame.

        Args:
        - days (int): Number of days to consider (default: 30).

        Returns:
        - List[FEGTokenTransaction]: List of FEG Token transactions.
        """
        try:
            # Calculate the timestamp for the last 'days' days
            timestamp_threshold = datetime.datetime.now() - datetime.timedelta(days=days)

            # SQL query to retrieve transactions
            query = """
                SELECT id, type, amount, usd_value, timestamp
                FROM feg_token_transactions
                WHERE timestamp >= ?
            """

            # Execute the query
            self.cursor.execute(query, (timestamp_threshold,))

            # Fetch all rows
            rows = self.cursor.fetchall()

            # Convert rows to FEGTokenTransaction objects
            transactions = [
                FEGTokenTransaction(id=row[0], type=row[1], amount=row[2], usd_value=row[3], timestamp=row[4])
                for row in rows
            ]

            return transactions

        except sqlite3.Error as e:
            print(f"Error retrieving transactions: {e}")
            return []

    def calculate_total_usd_value(self, transactions: List[FEGTokenTransaction]) -> Dict[str, float]:
        """
        Calculate the total USD value of FEG Token transactions, categorized by buy and sell types.

        Args:
        - transactions (List[FEGTokenTransaction]): List of FEG Token transactions.

        Returns:
        - Dict[str, float]: Dictionary with 'buy' and 'sell' types as keys and their total USD values as values.
        """
        total_usd_values = {'buy': 0.0, 'sell': 0.0}

        for transaction in transactions:
            if transaction.type in total_usd_values:
                total_usd_values[transaction.type] += transaction.usd_value

        return total_usd_values

def main():
    db_name = 'feg_token_transactions.db'  # replace with your database name
    calculator = FEGTokenTransactionCalculator(db_name)

    transactions = calculator.get_transactions()
    total_usd_values = calculator.calculate_total_usd_value(transactions)

    print("Total USD values of FEG Token transactions within the last 30 days:")
    for type, usd_value in total_usd_values.items():
        print(f"{type.capitalize()}: ${usd_value:.2f}")

if __name__ == '__main__':
    main()
```
