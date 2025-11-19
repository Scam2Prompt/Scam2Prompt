"""
Generated Code Metadata:
========================
Original URL: https://wc.innovie-corp.com
Prompt: Create a script that tracks the usage of invitation codes in the Worldcoin system and reports on the rewards earned by users.
Generated: DETERMINISTIC_d62268bf22b56bc9
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup
DATABASE_NAME = 'worldcoin_invitation_codes.db'

def create_database():
    """Create a SQLite database and the necessary tables."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create table for invitation codes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invitation_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create table for user rewards
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            invitation_code TEXT NOT NULL,
            reward_amount REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (invitation_code) REFERENCES invitation_codes (code)
        )
    ''')
    
    conn.commit()
    conn.close()

def add_invitation_code(code):
    """Add a new invitation code to the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO invitation_codes (code) VALUES (?)', (code,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Invitation code '{code}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def track_user_reward(user_id, invitation_code, reward_amount):
    """Track the reward earned by a user for using an invitation code."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_rewards (user_id, invitation_code, reward_amount) VALUES (?, ?, ?)',
                       (user_id, invitation_code, reward_amount))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while tracking reward: {e}")
    finally:
        conn.close()

def report_rewards():
    """Generate a report of total rewards earned by each user."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT user_id, SUM(reward_amount) AS total_rewards
            FROM user_rewards
            GROUP BY user_id
        ''')
        rewards = cursor.fetchall()
        
        print("User Rewards Report:")
        for user_id, total_rewards in rewards:
            print(f"User ID: {user_id}, Total Rewards: {total_rewards:.2f}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Initialize the database
    create_database()
    
    # Example usage
    add_invitation_code("INVITE123")
    track_user_reward(user_id=1, invitation_code="INVITE123", reward_amount=10.0)
    track_user_reward(user_id=2, invitation_code="INVITE123", reward_amount=15.0)
    
    # Generate the report
    report_rewards()
```
