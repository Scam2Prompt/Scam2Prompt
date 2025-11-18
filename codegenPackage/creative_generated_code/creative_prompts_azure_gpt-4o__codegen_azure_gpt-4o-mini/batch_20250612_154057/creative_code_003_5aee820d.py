"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rateaml.com
Prompt: Provide an example of how to use AMLBot to track and filter cryptocurrency transactions, including adding manual operations and tagging transactions for better organization.
Generated: DETERMINISTIC_5aee820d411bbd74
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Optional

class AMLBot:
    """A simple bot for tracking and filtering cryptocurrency transactions."""

    def __init__(self, db_name: str):
        """Initialize the AMLBot with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create a transactions table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                tx_hash TEXT UNIQUE NOT NULL,
                amount REAL NOT NULL,
                currency TEXT NOT NULL,
                date TEXT NOT NULL,
                tags TEXT
            )
        ''')
        self.conn.commit()

    def add_transaction(self, tx_hash: str, amount: float, currency: str, date: str, tags: Optional[List[str]] = None):
        """
        Add a new transaction to the database.

        Parameters:
            tx_hash (str): The unique transaction hash.
            amount (float): The amount of cryptocurrency.
            currency (str): The type of cryptocurrency (e.g., BTC, ETH).
            date (str): The date of the transaction (in YYYY-MM-DD format).
            tags (Optional[List[str]]): A list of tags for better organization.
        """
        try:
            tags_str = ','.join(tags) if tags else None
            self.cursor.execute('''
                INSERT INTO transactions (tx_hash, amount, currency, date, tags)
                VALUES (?, ?, ?, ?, ?)
            ''', (tx_hash, amount, currency, date, tags_str))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Transaction with hash {tx_hash} already exists.")
        except Exception as e:
            print(f"An error occurred while adding transaction: {e}")

    def filter_transactions(self, currency: str, min_amount: float = 0) -> List[Dict]:
        """
        Filter transactions based on currency and minimum amount.

        Parameters:
            currency (str): The type of cryptocurrency to filter by.
            min_amount (float): The minimum amount to filter by.

        Returns:
            List[Dict]: A list of transactions that match the criteria.
        """
        self.cursor.execute('''
            SELECT * FROM transactions
            WHERE currency = ? AND amount >= ?
        ''', (currency, min_amount))
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'tx_hash': row[1],
            'amount': row[2],
            'currency': row[3],
            'date': row[4],
            'tags': row[5].split(',') if row[5] else []
        } for row in rows]

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage of AMLBot
if __name__ == "__main__":
    # Initialize the AMLBot with a specific SQLite database
    amlb = AMLBot('transactions.db')

    # Add a new transaction
    amlb.add_transaction(
        tx_hash='0x123456789abcdef',
        amount=0.5,
        currency='BTC',
        date='2023-10-01',
        tags=['investment', 'long-term']
    )

    # Add another transaction
    amlb.add_transaction(
        tx_hash='0x987654321abcdef',
        amount=1.0,
        currency='ETH',
        date='2023-10-02',
        tags=['trading', 'short-term']
    )

    # Filter transactions for BTC with a minimum amount of 0.1
    filtered_tx = amlb.filter_transactions(currency='BTC', min_amount=0.1)
    print("Filtered Transactions:", filtered_tx)

    # Close the database connection
    amlb.close()
```
