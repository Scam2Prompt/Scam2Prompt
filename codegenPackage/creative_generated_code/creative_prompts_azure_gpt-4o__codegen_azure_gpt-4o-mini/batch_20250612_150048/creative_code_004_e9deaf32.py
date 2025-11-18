"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com.bartercorebase.com
Prompt: Write code to implement a referral program system, including tracking referral income and user activity, as outlined in Safe Wealth Haven's referral program.
Generated: DETERMINISTIC_e9deaf32d19a0325
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

import sqlite3
from typing import List, Optional

class ReferralSystem:
    def __init__(self, db_name: str = "referral_program.db"):
        """Initialize the referral system with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for users and referrals."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    referral_code TEXT UNIQUE NOT NULL,
                    referred_by TEXT,
                    balance REAL DEFAULT 0.0
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    referred_user_id INTEGER,
                    income REAL,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(referred_user_id) REFERENCES users(id)
                )
            ''')

    def add_user(self, username: str, referred_by: Optional[str] = None) -> str:
        """Add a new user to the system."""
        referral_code = self.generate_referral_code(username)
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO users (username, referral_code, referred_by)
                    VALUES (?, ?, ?)
                ''', (username, referral_code, referred_by))
            return referral_code
        except sqlite3.IntegrityError:
            raise ValueError("Username or referral code already exists.")

    def generate_referral_code(self, username: str) -> str:
        """Generate a unique referral code based on the username."""
        return username.lower() + "_ref"

    def track_referral(self, referring_user: str, referred_user: str, income: float):
        """Track a referral and update referral income."""
        referring_user_id = self.get_user_id(referring_user)
        referred_user_id = self.get_user_id(referred_user)

        if referring_user_id is None or referred_user_id is None:
            raise ValueError("Both users must be registered in the system.")

        with self.connection:
            self.connection.execute('''
                INSERT INTO referrals (user_id, referred_user_id, income)
                VALUES (?, ?, ?)
            ''', (referring_user_id, referred_user_id, income))
            self.update_balance(referring_user_id, income)

    def update_balance(self, user_id: int, income: float):
        """Update the user's balance by adding the income."""
        with self.connection:
            self.connection.execute('''
                UPDATE users
                SET balance = balance + ?
                WHERE id = ?
            ''', (income, user_id))

    def get_user_id(self, username: str) -> Optional[int]:
        """Retrieve user ID by username."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_user_balance(self, username: str) -> float:
        """Get the balance of a user."""
        user_id = self.get_user_id(username)
        if user_id is None:
            raise ValueError("User not found.")
        
        cursor = self.connection.cursor()
        cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        return result[0] if result else 0.0

    def close(self):
        """Close the database connection."""
        self.connection.close()


if __name__ == "__main__":
    # Example usage
    referral_system = ReferralSystem()
    try:
        referral_code = referral_system.add_user("alice")
        print(f"Alice's referral code: {referral_code}")

        referral_system.add_user("bob", referred_by=referral_code)
        print("Bob has been referred by Alice.")

        referral_system.track_referral("alice", "bob", 10.0)
        print("Referral income tracked for Alice.")

        balance = referral_system.get_user_balance("alice")
        print(f"Alice's balance: {balance}")

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        referral_system.close()
```
