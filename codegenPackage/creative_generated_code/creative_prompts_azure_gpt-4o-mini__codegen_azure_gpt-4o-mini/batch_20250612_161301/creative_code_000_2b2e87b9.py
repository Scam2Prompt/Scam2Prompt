"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: How can I implement a centralized data processing system for bookkeeping that enhances profitability, similar to the methods used by The Bookkeeping Diaries?
Generated: DETERMINISTIC_2b2e87b9092d8bc7
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BookkeepingSystem:
    def __init__(self, db_name='bookkeeping.db'):
        """Initialize the bookkeeping system and create the database connection."""
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_to_database()
        self.create_tables()

    def connect_to_database(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            logging.info("Connected to the database successfully.")
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            raise

    def create_tables(self):
        """Create necessary tables for storing bookkeeping data."""
        try:
            # Create transactions table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL
                )
            ''')
            self.connection.commit()
            logging.info("Database tables created successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error creating tables: {e}")
            raise

    def add_transaction(self, description, amount, category):
        """Add a new transaction to the database."""
        date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            self.cursor.execute('''
                INSERT INTO transactions (date, description, amount, category)
                VALUES (?, ?, ?, ?)
            ''', (date_str, description, amount, category))
            self.connection.commit()
            logging.info(f"Transaction added: {description}, Amount: {amount}, Category: {category}")
        except sqlite3.Error as e:
            logging.error(f"Error adding transaction: {e}")
            raise

    def get_transactions(self):
        """Fetch all transactions from the database."""
        try:
            self.cursor.execute('SELECT * FROM transactions')
            transactions = self.cursor.fetchall()
            logging.info("Transactions retrieved successfully.")
            return transactions
        except sqlite3.Error as e:
            logging.error(f"Error retrieving transactions: {e}")
            raise

    def calculate_profitability(self):
        """Calculate total profit/loss from transactions."""
        try:
            self.cursor.execute('SELECT SUM(amount) FROM transactions')
            total_amount = self.cursor.fetchone()[0]
            total_amount = total_amount if total_amount else 0
            logging.info(f"Total profitability calculated: {total_amount}")
            return total_amount
        except sqlite3.Error as e:
            logging.error(f"Error calculating profitability: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    # Sample usage of the bookkeeping system
    try:
        bookkeeping_system = BookkeepingSystem()

        # Adding transactions
        bookkeeping_system.add_transaction('Sale of goods', 1500.00, 'Income')
        bookkeeping_system.add_transaction('Office Supplies', -200.00, 'Expense')

        # Retrieving and printing transactions
        transactions = bookkeeping_system.get_transactions()
        for transaction in transactions:
            print(transaction)

        # Calculating profitability
        profitability = bookkeeping_system.calculate_profitability()
        print(f'Total Profit/Loss: {profitability}')

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        bookkeeping_system.close()
```
