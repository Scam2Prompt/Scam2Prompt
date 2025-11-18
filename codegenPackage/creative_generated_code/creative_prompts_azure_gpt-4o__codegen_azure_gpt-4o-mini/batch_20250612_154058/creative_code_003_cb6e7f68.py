"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Generate a Python script to calculate referral bonuses based on a referral code system, where users earn a percentage of their referrals' earnings.
Generated: DETERMINISTIC_cb6e7f688e5f3431
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import Dict, Tuple

# Database handler class
class ReferralDatabase:
    """Handles database operations for user referrals."""
    
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables if they do not exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    earnings REAL NOT NULL DEFAULT 0.0,
                    referral_code TEXT UNIQUE NOT NULL,
                    referred_by TEXT
                )
            ''')

    def add_user(self, name: str, referral_code: str, referred_by: str = None) -> int:
        """Add a new user to the database."""
        with self.connection:
            cursor = self.connection.execute('''
                INSERT INTO users (name, referral_code, referred_by) 
                VALUES (?, ?, ?)
            ''', (name, referral_code, referred_by))
            return cursor.lastrowid

    def update_earnings(self, user_id: int, amount: float) -> None:
        """Update a user's earnings in the database."""
        with self.connection:
            self.connection.execute('''
                UPDATE users 
                SET earnings = earnings + ? 
                WHERE id = ?
            ''', (amount, user_id))

    def get_user(self, referral_code: str) -> Tuple[int, str, float, str]:
        """Retrieve a user by their referral code."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT id, name, earnings, referred_by 
            FROM users 
            WHERE referral_code = ?
        ''', (referral_code,))
        return cursor.fetchone()

    def close(self):
        """Close the database connection."""
        self.connection.close()

class ReferralSystem:
    """Calculates referral bonuses based on user earnings."""
    
    def __init__(self, db: ReferralDatabase, bonus_percentage: float):
        """Initialize the referral system."""
        self.db = db
        self.bonus_percentage = bonus_percentage

    def refer_user(self, name: str, referral_code: str, referred_by_code: str = None) -> int:
        """Register a new user and process their referral."""
        referred_by_user = self.db.get_user(referred_by_code) if referred_by_code else None
        
        if referred_by_user:
            referred_by_id = referred_by_user[0]
            self.db.add_user(name, referral_code, referred_by=referred_by_code)
            return referred_by_id
        else:
            return self.db.add_user(name, referral_code)

    def calculate_bonus(self, referrer_code: str, earnings: float) -> float:
        """Calculate the bonus for a referrer based on their referral's earnings."""
        return earnings * self.bonus_percentage / 100

    def distribute_bonus(self, referral_code: str, earnings: float) -> None:
        """Distribute referral bonuses to the referrer."""
        user = self.db.get_user(referral_code)
        if user:
            user_id = user[0]
            referrer_code = user[3]
            bonus = self.calculate_bonus(referrer_code, earnings)
            self.db.update_earnings(user_id, bonus)

def main():
    # Initialize the referral database
    db = ReferralDatabase('referral_system.db')
    
    # Initialize the referral system with a bonus percentage
    referral_system = ReferralSystem(db, bonus_percentage=10.0)

    # Example usage
    try:
        referrer_code = 'ABC123'
        referral_system.refer_user('John Doe', 'XYZ987', referrer_code)
        referral_system.update_earnings(referrer_code, 100.0)
        referral_system.distribute_bonus('XYZ987', 100.0)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == '__main__':
    main()
```
