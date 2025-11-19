"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halo-social.pages.dev
Prompt: How can I implement a system to track social influence and reward users with Halo XP based on their contributions, following the guidelines provided by halo.social?
Generated: DETERMINISTIC_2fbf64e838007754
Batch ID: 20250612_162504
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

# Constants
DATABASE_NAME = 'halo_social.db'
REWARD_PER_CONTRIBUTION = 10  # Halo XP reward per contribution

class HaloSocialTracker:
    def __init__(self):
        """Initialize the HaloSocialTracker and create the database if it doesn't exist."""
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.create_tables()

    def create_tables(self):
        """Create tables for users and contributions if they don't exist."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        halo_xp INTEGER DEFAULT 0
                    )
                ''')
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS contributions (
                        contribution_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        contribution_text TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def add_user(self, username):
        """Add a new user to the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO users (username) VALUES (?)
                ''', (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user '{username}': {e}")

    def record_contribution(self, username, contribution_text):
        """Record a user's contribution and reward them with Halo XP."""
        try:
            cursor = self.conn.execute('''
                SELECT user_id FROM users WHERE username = ?
            ''', (username,))
            user = cursor.fetchone()
            if user:
                user_id = user[0]
                with self.conn:
                    # Insert the contribution
                    self.conn.execute('''
                        INSERT INTO contributions (user_id, contribution_text) VALUES (?, ?)
                    ''', (user_id, contribution_text))
                    # Update the user's Halo XP
                    self.conn.execute('''
                        UPDATE users SET halo_xp = halo_xp + ? WHERE user_id = ?
                    ''', (REWARD_PER_CONTRIBUTION, user_id))
                print(f"Contribution recorded and {REWARD_PER_CONTRIBUTION} Halo XP awarded to {username}.")
            else:
                print(f"User '{username}' not found.")
        except sqlite3.Error as e:
            print(f"Error recording contribution for '{username}': {e}")

    def get_user_halo_xp(self, username):
        """Retrieve the Halo XP for a specified user."""
        try:
            cursor = self.conn.execute('''
                SELECT halo_xp FROM users WHERE username = ?
            ''', (username,))
            user = cursor.fetchone()
            if user:
                return user[0]
            else:
                print(f"User '{username}' not found.")
                return None
        except sqlite3.Error as e:
            print(f"Error retrieving Halo XP for '{username}': {e}")
            return None

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    tracker = HaloSocialTracker()
    tracker.add_user('Alice')
    tracker.add_user('Bob')
    tracker.record_contribution('Alice', 'I shared an article about climate change.')
    print(f"Alice's Halo XP: {tracker.get_user_halo_xp('Alice')}")
    tracker.close()
```
