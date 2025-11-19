"""
Generated Code Metadata:
========================
Original URL: https://changelly.ws
Prompt: Generate code for a referral program system that tracks user referrals and calculates passive income based on exchange transactions, inspired by Changelly's referral program.
Generated: DETERMINISTIC_82d4451280fdb3c5
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from decimal import Decimal, InvalidOperation

class ReferralProgram:
    def __init__(self, db_name='referral_program.db'):
        """Initialize the referral program with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for users and transactions."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    referral_code TEXT UNIQUE NOT NULL,
                    referred_by TEXT,
                    balance DECIMAL(10, 2) DEFAULT 0.00
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    amount DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

    def add_user(self, username, referred_by=None):
        """Add a new user to the system."""
        referral_code = self.generate_referral_code(username)
        with self.connection:
            try:
                self.connection.execute('''
                    INSERT INTO users (username, referral_code, referred_by)
                    VALUES (?, ?, ?)
                ''', (username, referral_code, referred_by))
            except sqlite3.IntegrityError:
                raise ValueError("Username or referral code already exists.")

    def generate_referral_code(self, username):
        """Generate a unique referral code based on the username."""
        return username.lower() + '_ref'

    def record_transaction(self, username, amount):
        """Record a transaction for a user and calculate passive income for referrals."""
        user_id = self.get_user_id(username)
        if user_id is None:
            raise ValueError("User not found.")

        amount = self.validate_amount(amount)
        with self.connection:
            self.connection.execute('''
                INSERT INTO transactions (user_id, amount)
                VALUES (?, ?)
            ''', (user_id, amount))
            self.update_referral_income(user_id, amount)

    def validate_amount(self, amount):
        """Validate the transaction amount."""
        try:
            amount = Decimal(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            return amount
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid amount provided.")

    def update_referral_income(self, user_id, amount):
        """Update the balance of the referrer based on the transaction amount."""
        referrer = self.get_referrer(user_id)
        if referrer:
            passive_income = amount * Decimal('0.05')  # 5% referral income
            with self.connection:
                self.connection.execute('''
                    UPDATE users
                    SET balance = balance + ?
                    WHERE referral_code = ?
                ''', (passive_income, referrer))

    def get_user_id(self, username):
        """Retrieve the user ID based on the username."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_referrer(self, user_id):
        """Get the referral code of the user who referred the current user."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT referred_by FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_user_balance(self, username):
        """Retrieve the balance of a user."""
        user_id = self.get_user_id(username)
        if user_id is None:
            raise ValueError("User not found.")
        cursor = self.connection.cursor()
        cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        return result[0] if result else 0.00

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage:
if __name__ == "__main__":
    referral_program = ReferralProgram()
    try:
        referral_program.add_user('alice')
        referral_program.add_user('bob', 'alice_ref')
        referral_program.record_transaction('bob', 100)
        print(f"Alice's balance: {referral_program.get_user_balance('alice')}")
        print(f"Bob's balance: {referral_program.get_user_balance('bob')}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        referral_program.close()
```
