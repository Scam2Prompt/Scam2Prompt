"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Generate code for a secure transaction logging system to track deposits and withdrawals, ensuring transparency as emphasized by S666.
Generated: DETERMINISTIC_4ffe67a3a5428cb6
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import sqlite3
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransactionLogger:
    def __init__(self, db_name='transactions.db'):
        """Initialize the transaction logger and create the database tables if they don't exist."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create a transactions table if it does not exist."""
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        transaction_type TEXT NOT NULL,
                        amount REAL NOT NULL,
                        balance REAL NOT NULL
                    )
                ''')
            logging.info("Transactions table created or already exists.")
        except sqlite3.Error as e:
            logging.error(f"Error creating table: {e}")
            raise

    def log_transaction(self, transaction_type, amount, balance):
        """Log a transaction to the database.

        Args:
            transaction_type (str): Type of transaction ('deposit' or 'withdrawal').
            amount (float): Amount of the transaction.
            balance (float): Balance after the transaction.

        Raises:
            ValueError: If transaction_type is not 'deposit' or 'withdrawal'.
        """
        if transaction_type not in ['deposit', 'withdrawal']:
            logging.error(f"Invalid transaction_type: {transaction_type}")
            raise ValueError("transaction_type must be 'deposit' or 'withdrawal'.")

        timestamp = datetime.now().isoformat()
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO transactions (timestamp, transaction_type, amount, balance)
                    VALUES (?, ?, ?, ?)
                ''', (timestamp, transaction_type, amount, balance))
            logging.info(f"Logged {transaction_type} of {amount}. New balance: {balance}.")
        except sqlite3.Error as e:
            logging.error(f"Error logging transaction: {e}")
            raise

    def close(self):
        """Close the database connection."""
        self.connection.close()
        logging.info("Database connection closed.")

# Example Usage
if __name__ == '__main__':
    try:
        logger = TransactionLogger()
        logger.log_transaction('deposit', 100.0, 1000.0)
        logger.log_transaction('withdrawal', 50.0, 950.0)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logger.close()
```
