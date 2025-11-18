"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Develop a Python script to generate a referral program tracker, inspired by the referral program mentioned on RapidCoinTrades, including features for tracking referrals and calculating earnings.
Generated: DETERMINISTIC_13b5c11e820d54db
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class ReferralProgramTracker:
    """A class to manage a referral program, tracking referrals and calculating earnings."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database successful.")
        except Error as e:
            print(f"Error: {e}")
        return conn

    def create_tables(self):
        """Create necessary tables for tracking referrals and earnings."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    referral_code TEXT UNIQUE NOT NULL
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY,
                    referrer_id INTEGER NOT NULL,
                    referee_id INTEGER NOT NULL,
                    FOREIGN KEY (referrer_id) REFERENCES users (id),
                    FOREIGN KEY (referee_id) REFERENCES users (id)
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS earnings (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                );
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error: {e}")

    def add_user(self, name, referral_code):
        """Add a new user to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO users (name, referral_code) VALUES (?, ?)
            ''', (name, referral_code))
            self.connection.commit()
            print(f"User '{name}' added successfully.")
        except Error as e:
            print(f"Error adding user: {e}")

    def add_referral(self, referrer_code, referee_code):
        """Record a referral relationship between two users."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referrer_code,))
            referrer = cursor.fetchone()
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referee_code,))
            referee = cursor.fetchone()
            if referrer and referee:
                cursor.execute('''
                    INSERT INTO referrals (referrer_id, referee_id)
                    VALUES (?, ?)
                ''', (referrer[0], referee[0]))
                self.connection.commit()
                print(f"Referral from '{referrer_code}' to '{referee_code}' added successfully.")
            else:
                print("Invalid referral codes.")
        except Error as e:
            print(f"Error adding referral: {e}")

    def calculate_earnings(self, referral_code, amount):
        """Calculate earnings for a user based on referrals."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referral_code,))
            user = cursor.fetchone()
            if user:
                cursor.execute('''
                    INSERT INTO earnings (user_id, amount)
                    VALUES (?, ?)
                ''', (user[0], amount))
                self.connection.commit()
                print(f"Earnings of {amount} added for user '{referral_code}'.")
            else:
                print("Invalid referral code.")
        except Error as e:
            print(f"Error calculating earnings: {e}")

    def get_user_earnings(self, referral_code):
        """Retrieve total earnings for a user based on their referral code."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT id FROM users WHERE referral_code = ?', (referral_code,))
            user = cursor.fetchone()
            if user:
                cursor.execute('''
                    SELECT SUM(amount) FROM earnings WHERE user_id = ?
                ''', (user[0],))
                total_earnings = cursor.fetchone()[0]
                return total_earnings if total_earnings else 0
            else:
                print("Invalid referral code.")
                return 0
        except Error as e:
            print(f"Error retrieving earnings: {e}")
            return 0

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


# Example usage
if __name__ == "__main__":
    db_file = "referral_program.db"
    tracker = ReferralProgramTracker(db_file)

    # Adding users
    tracker.add_user("Alice", "ALICE123")
    tracker.add_user("Bob", "BOB456")

    # Adding referrals
    tracker.add_referral("ALICE123", "BOB456")

    # Calculating earnings
    tracker.calculate_earnings("ALICE123", 50.0)

    # Retrieving total earnings
    earnings = tracker.get_user_earnings("ALICE123")
    print(f"Total earnings for Alice: {earnings}")

    # Closing the connection
    tracker.close_connection()
```
