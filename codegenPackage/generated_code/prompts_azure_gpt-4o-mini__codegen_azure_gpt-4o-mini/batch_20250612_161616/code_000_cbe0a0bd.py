"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: How can I implement a cashless payment system for school meals similar to the NO CASH initiative described on the It's Cool website?
Generated: DETERMINISTIC_cbe0a0bd470358aa
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cashless_payment_system.py

import sqlite3
from datetime import datetime

class CashlessPaymentSystem:
    def __init__(self, db_name='school_meals.db'):
        """Initialize the cashless payment system with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for users and transactions."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    balance REAL NOT NULL DEFAULT 0.0
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    amount REAL,
                    timestamp TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')

    def add_user(self, name, initial_balance=0.0):
        """Add a new user to the system."""
        with self.connection:
            self.connection.execute('''
                INSERT INTO users (name, balance) VALUES (?, ?)
            ''', (name, initial_balance))

    def load_user(self, user_id):
        """Load user details by user ID."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        return cursor.fetchone()

    def update_balance(self, user_id, amount):
        """Update the user's balance and record the transaction."""
        user = self.load_user(user_id)
        if user is None:
            raise ValueError("User not found.")

        new_balance = user[2] + amount
        if new_balance < 0:
            raise ValueError("Insufficient balance.")

        with self.connection:
            self.connection.execute('''
                UPDATE users SET balance = ? WHERE user_id = ?
            ''', (new_balance, user_id))
            self.record_transaction(user_id, amount)

    def record_transaction(self, user_id, amount):
        """Record a transaction in the database."""
        timestamp = datetime.now().isoformat()
        with self.connection:
            self.connection.execute('''
                INSERT INTO transactions (user_id, amount, timestamp) VALUES (?, ?, ?)
            ''', (user_id, amount, timestamp))

    def get_balance(self, user_id):
        """Get the current balance of the user."""
        user = self.load_user(user_id)
        if user is None:
            raise ValueError("User not found.")
        return user[2]

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    try:
        payment_system = CashlessPaymentSystem()
        payment_system.add_user("John Doe", 50.0)  # Add a user with an initial balance
        user_id = 1  # Assuming John Doe is user_id 1
        print(f"Initial Balance: {payment_system.get_balance(user_id)}")
        
        payment_system.update_balance(user_id, -10.0)  # Deduct 10.0 for a meal
        print(f"Updated Balance: {payment_system.get_balance(user_id)}")
        
        payment_system.close()
    except Exception as e:
        print(f"An error occurred: {e}")
```
