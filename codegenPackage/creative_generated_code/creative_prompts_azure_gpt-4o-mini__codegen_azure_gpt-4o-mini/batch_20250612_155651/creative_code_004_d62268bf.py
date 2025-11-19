"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Create a script that tracks the usage of invitation codes in the Worldcoin system and reports on the rewards earned by users.
Generated: DETERMINISTIC_d62268bf22b56bc9
Batch ID: 20250612_155651
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

# Database setup
DB_NAME = 'worldcoin_invitation_codes.db'

def create_database():
    """Create a SQLite database and the necessary tables."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL
            )
        ''')
        # Create invitation codes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS invitation_codes (
                code TEXT PRIMARY KEY,
                user_id INTEGER,
                date_used DATETIME,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        # Create rewards table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rewards (
                user_id INTEGER,
                amount REAL,
                date_awarded DATETIME,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        conn.commit()

def track_invitation_code(code, user_id):
    """Track the usage of an invitation code.

    Args:
        code (str): The invitation code being used.
        user_id (int): The ID of the user who used the invitation code.
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            # Insert the invitation code usage
            cursor.execute('''
                INSERT INTO invitation_codes (code, user_id, date_used)
                VALUES (?, ?, ?)
            ''', (code, user_id, datetime.now()))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while tracking the invitation code: {e}")

def report_rewards(user_id):
    """Generate a report of rewards earned by a user.

    Args:
        user_id (int): The ID of the user for whom to report rewards.
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT amount, date_awarded FROM rewards
                WHERE user_id = ?
            ''', (user_id,))
            rewards = cursor.fetchall()
            total_rewards = sum(amount for amount, _ in rewards)
            print(f"User ID: {user_id}, Total Rewards Earned: {total_rewards}")
            for amount, date in rewards:
                print(f"Reward: {amount}, Date Awarded: {date}")
    except sqlite3.Error as e:
        print(f"An error occurred while reporting rewards: {e}")

def add_reward(user_id, amount):
    """Add a reward for a given user.

    Args:
        user_id (int): The ID of the user to whom the reward is given.
        amount (float): The amount of the reward to be given.
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO rewards (user_id, amount, date_awarded)
                VALUES (?, ?, ?)
            ''', (user_id, amount, datetime.now()))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while adding a reward: {e}")

if __name__ == '__main__':
    create_database()
    # Example usage
    # track_invitation_code('INVITE123', 1)
    # add_reward(1, 10.0)
    # report_rewards(1)
```
