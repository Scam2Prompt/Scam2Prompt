"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Generate code to facilitate a referral mission system that rewards users for inviting others, inspired by KAYEN's community engagement strategies.
Generated: DETERMINISTIC_ee0bfef9efd6ed15
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import Tuple, List, Optional

class ReferralSystem:
    def __init__(self, db_name: str = 'referral_system.db'):
        """Initialize the Referral System with a database connection."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for the referral system."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    referral_code TEXT UNIQUE NOT NULL,
                    referred_count INTEGER DEFAULT 0,
                    rewards INTEGER DEFAULT 0
                )
            ''')

    def add_user(self, username: str) -> Optional[str]:
        """Add a new user to the system with a unique referral code.

        Args:
            username (str): The username of the new user.

        Returns:
            Optional[str]: The referral code for the user or None if the user already exists.
        """
        referral_code = f"{username}_{hash(username)}"
        try:
            with self.conn:
                self.conn.execute('INSERT INTO users (username, referral_code) VALUES (?, ?)', (username, referral_code))
            return referral_code
        except sqlite3.IntegrityError:
            # User already exists
            return None

    def refer_user(self, referrer_code: str, new_username: str) -> bool:
        """Refer a new user through an existing user's referral code.

        Args:
            referrer_code (str): The referral code of the referrer.
            new_username (str): The username of the new user.

        Returns:
            bool: True if the referral was successful, False otherwise.
        """
        referrer = self.get_user_by_referral_code(referrer_code)
        if referrer is None or referrer['username'] == new_username:
            return False  # Invalid referral or self-referral

        # Add new user
        if self.add_user(new_username):
            self.update_referral_count(referrer['id'])
            return True
        return False

    def get_user_by_referral_code(self, referral_code: str) -> Optional[dict]:
        """Retrieve user details by referral code.

        Args:
            referral_code (str): The referral code to search for.

        Returns:
            Optional[dict]: User details or None if the user is not found.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE referral_code = ?', (referral_code,))
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'username': row[1],
                'referral_code': row[2],
                'referred_count': row[3],
                'rewards': row[4]
            }
        return None

    def update_referral_count(self, user_id: int):
        """Increase the referred count for a user and update rewards.

        Args:
            user_id (int): The ID of the user whose referral count is updated.
        """
        with self.conn:
            self.conn.execute('UPDATE users SET referred_count = referred_count + 1, rewards = rewards + 10 WHERE id = ?', (user_id,))
    
    def get_user_rewards(self, username: str) -> Optional[int]:
        """Get the current rewards for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[int]: User's rewards or None if the user does not exist.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT rewards FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        return row[0] if row else None

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


# Example of usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    referral_code = referral_system.add_user('Alice')
    print(f"Alice's referral code: {referral_code}")
    
    # Referring another user
    success = referral_system.refer_user(referral_code, 'Bob')
    print(f"Referral successful: {success}")
    
    # Get Bob's rewards
    rewards = referral_system.get_user_rewards('Alice')
    print(f"Alice's rewards: {rewards}")
    
    referral_system.close()
```
