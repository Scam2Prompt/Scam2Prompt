"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasnavi.pages.dev
Prompt: How can I implement a feature in my app that allows users to earn rewards for driving, similar to the Drive-to-Earn model used by Atlas Navi?
Generated: DETERMINISTIC_3b79f50c800d198d
Batch ID: 20250612_164305
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

class RewardSystem:
    def __init__(self, db_name='reward_system.db'):
        """Initialize the Reward System and set up the database."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.setup_database()

    def setup_database(self):
        """Create the rewards table if it does not exist."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS rewards (
                    user_id INTEGER PRIMARY KEY,
                    total_distance REAL DEFAULT 0,
                    total_rewards REAL DEFAULT 0
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def add_user(self, user_id):
        """Add a new user to the rewards system."""
        try:
            self.cursor.execute('INSERT INTO rewards (user_id) VALUES (?)', (user_id,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"User {user_id} already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user {user_id}: {e}")

    def log_trip(self, user_id, distance):
        """Record a trip for a user and calculate rewards."""
        if distance <= 0:
            print("Distance must be greater than 0.")
            return
        
        reward_per_km = 0.1  # Set reward rate
        reward = distance * reward_per_km
        
        try:
            self.cursor.execute('''
                UPDATE rewards
                SET total_distance = total_distance + ?,
                    total_rewards = total_rewards + ?
                WHERE user_id = ?
            ''', (distance, reward, user_id))
            self.connection.commit()
            print(f"Trip logged for user {user_id}: {distance} km, Reward: {reward}")
        except sqlite3.Error as e:
            print(f"Error logging trip for user {user_id}: {e}")

    def get_rewards(self, user_id):
        """Retrieve the total rewards for a given user."""
        try:
            self.cursor.execute('SELECT total_rewards FROM rewards WHERE user_id = ?', (user_id,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                print(f"No rewards found for user {user_id}.")
                return 0
        except sqlite3.Error as e:
            print(f"Error retrieving rewards for user {user_id}: {e}")
            return 0

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example of usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    reward_system.add_user(1)
    reward_system.log_trip(1, 50)  # User 1 drives 50 km
    rewards = reward_system.get_rewards(1)
    print(f"Total rewards for user 1: {rewards}")
    reward_system.close()
```
