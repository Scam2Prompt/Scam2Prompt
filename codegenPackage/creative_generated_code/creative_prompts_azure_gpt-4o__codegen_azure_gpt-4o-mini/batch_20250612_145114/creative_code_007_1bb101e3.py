"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Implement a feature to track user purchases and link them to cashback rewards, inspired by Shoppiday's tools for earning money with purchases.
Generated: DETERMINISTIC_1bb101e382a7fd02
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

class CashbackTracker:
    def __init__(self, db_name='cashback.db'):
        """Initialize the database connection and create tables if they do not exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create tables for users and purchases if they do not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                purchase_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                amount REAL NOT NULL,
                purchase_date TEXT NOT NULL,
                cashback REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        self.connection.commit()

    def add_user(self, name, email):
        """Add a new user to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO users (name, email)
                VALUES (?, ?)
            ''', (name, email))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Error: User with this email already exists.")

    def track_purchase(self, user_id, amount, cashback_rate):
        """
        Track a user's purchase and calculate cashback.
        
        :param user_id: ID of the user making the purchase
        :param amount: Amount of the purchase
        :param cashback_rate: Cashback percentage in decimal form (e.g., 0.1 for 10%)
        """
        # Calculate cashback based on the purchase amount and the cashback rate
        cashback = amount * cashback_rate
        purchase_date = datetime.now().isoformat()

        try:
            self.cursor.execute('''
                INSERT INTO purchases (user_id, amount, purchase_date, cashback)
                VALUES (?, ?, ?, ?)
            ''', (user_id, amount, purchase_date, cashback))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error tracking purchase: {e}")

    def get_user_cashback(self, user_id):
        """
        Retrieve total cashback earned by a user.
        
        :param user_id: ID of the user
        :return: Total cashback earned by the user
        """
        self.cursor.execute('''
            SELECT SUM(cashback) FROM purchases
            WHERE user_id = ?
        ''', (user_id,))
        total_cashback = self.cursor.fetchone()[0]
        return total_cashback if total_cashback is not None else 0.0

    def close(self):
        """Close the database connection."""
        self.connection.close()


# Example usage
if __name__ == "__main__":
    tracker = CashbackTracker()
    tracker.add_user('John Doe', 'john.doe@example.com')
    tracker.track_purchase(1, 100.0, 0.1)  # Track a $100 purchase with 10% cashback
    total_cashback = tracker.get_user_cashback(1)
    print(f'Total cashback for user 1: ${total_cashback:.2f}')
    tracker.close()
```
