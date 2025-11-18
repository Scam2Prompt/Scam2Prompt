"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtclaim.com
Prompt: Generate code to implement a referral tracking system for a cryptocurrency faucet platform, adhering to the rules outlined by USDT Claim regarding referral limits and inactivity.
Generated: DETERMINISTIC_52a1da570d828859
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_tracking.py
import sqlite3
from datetime import datetime, timedelta

class ReferralTrackingSystem:
    def __init__(self, db_name='referrals.db'):
        """Initialize the referral tracking system with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for tracking referrals."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS referrals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    referrer_id INTEGER NOT NULL,
                    referred_id INTEGER NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    active BOOLEAN DEFAULT TRUE,
                    FOREIGN KEY (referrer_id) REFERENCES users (id),
                    FOREIGN KEY (referred_id) REFERENCES users (id)
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    last_claim DATETIME,
                    claim_count INTEGER DEFAULT 0
                )
            ''')

    def add_user(self, username):
        """Add a new user to the system."""
        try:
            with self.connection:
                self.connection.execute('INSERT INTO users (username) VALUES (?)', (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")

    def add_referral(self, referrer_id, referred_id):
        """Add a referral relationship."""
        try:
            with self.connection:
                self.connection.execute('INSERT INTO referrals (referrer_id, referred_id) VALUES (?, ?)', 
                                        (referrer_id, referred_id))
        except sqlite3.IntegrityError:
            print(f"Referral from user {referrer_id} to user {referred_id} already exists.")

    def get_referrals(self, user_id):
        """Retrieve all referrals for a given user."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT referred_id, created_at FROM referrals WHERE referrer_id = ?', (user_id,))
        return cursor.fetchall()

    def check_inactivity(self, user_id):
        """Check if a user has been inactive for more than 30 days."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT last_claim FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            last_claim = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            return datetime.now() - last_claim > timedelta(days=30)
        return True  # Treat as inactive if user doesn't exist

    def update_user_claim(self, user_id):
        """Update the user's claim time and increment the claim count."""
        if self.check_inactivity(user_id):
            print(f"User {user_id} is inactive and cannot claim.")
            return

        with self.connection:
            self.connection.execute('''
                UPDATE users 
                SET last_claim = CURRENT_TIMESTAMP, claim_count = claim_count + 1 
                WHERE id = ?
            ''', (user_id,))
    
    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example of using the referral tracking system
if __name__ == "__main__":
    referral_system = ReferralTrackingSystem()
    referral_system.add_user('Alice')
    referral_system.add_user('Bob')
    referral_system.add_referral(1, 2)  # Alice refers Bob
    print(referral_system.get_referrals(1))  # Get referrals for Alice
    referral_system.update_user_claim(1)  # Update claim for Alice
    referral_system.close()
```
