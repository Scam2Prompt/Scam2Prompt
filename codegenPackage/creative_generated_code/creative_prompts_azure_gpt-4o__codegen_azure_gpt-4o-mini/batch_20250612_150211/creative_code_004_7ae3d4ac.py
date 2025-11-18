"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Write code to automate referral program tracking for an investment platform, including features to calculate referral income as described on the 10x Investment website.
Generated: DETERMINISTIC_7ae3d4ac65545232
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import Optional, Tuple

class ReferralProgram:
    def __init__(self, db_name: str):
        """Initialize the referral program with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for tracking referrals and earnings."""
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                referral_code TEXT UNIQUE
            )
            """)
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS referrals (
                referral_id INTEGER PRIMARY KEY,
                referrer_id INTEGER,
                referred_id INTEGER,
                amount_earned REAL,
                FOREIGN KEY(referrer_id) REFERENCES users(user_id),
                FOREIGN KEY(referred_id) REFERENCES users(user_id)
            )
            """)

    def add_user(self, name: str, referral_code: str) -> int:
        """Add a new user to the database."""
        try:
            with self.connection:
                cursor = self.connection.execute("""
                INSERT INTO users (name, referral_code) VALUES (?, ?)
                """, (name, referral_code))
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Referral code must be unique.")

    def track_referral(self, referrer_code: str, referred_name: str, earned_amount: float) -> Optional[int]:
        """Track a referral when a new user is referred."""
        try:
            referrer_id = self.get_user_id_by_referral_code(referrer_code)
            referred_id = self.add_user(referred_name, self.generate_referral_code(referred_name))

            with self.connection:
                self.connection.execute("""
                INSERT INTO referrals (referrer_id, referred_id, amount_earned) VALUES (?, ?, ?)
                """, (referrer_id, referred_id, earned_amount))

            return referred_id
        except ValueError as e:
            print(f"Error tracking referral: {e}")
            return None

    def get_user_id_by_referral_code(self, referral_code: str) -> int:
        """Get user ID by referral code."""
        cursor = self.connection.execute("""
        SELECT user_id FROM users WHERE referral_code = ?
        """, (referral_code,))
        user = cursor.fetchone()
        if user:
            return user[0]
        else:
            raise ValueError("Referral code not found.")

    def generate_referral_code(self, name: str) -> str:
        """Generate a simple referral code based on the user's name."""
        return name.lower().replace(" ", "_")

    def calculate_referral_income(self, referrer_id: int) -> float:
        """Calculate total income earned through referrals for a given user."""
        cursor = self.connection.execute("""
        SELECT SUM(amount_earned) FROM referrals WHERE referrer_id = ?
        """, (referrer_id,))
        total_income = cursor.fetchone()[0]
        return total_income if total_income else 0.0

    def close(self):
        """Close the database connection."""
        self.connection.close()


# Usage Example
if __name__ == "__main__":
    referral_program = ReferralProgram('referral_program.db')
    try:
        user1_id = referral_program.add_user('Alice Smith', 'alice_smith')
        user2_id = referral_program.track_referral('alice_smith', 'Bob Johnson', 100.0)
        total_income = referral_program.calculate_referral_income(user1_id)
        print(f"Alice's total referral income: ${total_income:.2f}")
    finally:
        referral_program.close()
```
