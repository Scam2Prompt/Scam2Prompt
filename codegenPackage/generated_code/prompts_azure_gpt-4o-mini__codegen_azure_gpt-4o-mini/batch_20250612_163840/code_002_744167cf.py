"""
Generated Code Metadata:
========================
Original URL: https://bac-games.vercel.app
Prompt: Create a function that connects users to the BAC gaming clubs and tracks their rewards in a Play-2-Earn model.
Generated: DETERMINISTIC_744167cf764f2121
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, Tuple

class BACGamingClub:
    def __init__(self, db_name: str):
        """Initialize the BACGamingClub with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for users and rewards if they do not exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    total_rewards INTEGER DEFAULT 0
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS rewards (
                    reward_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    amount INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')

    def connect_user(self, username: str) -> Optional[int]:
        """Connect a user to the BAC gaming club and return their user ID.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[int]: The user ID if the user is successfully connected, None otherwise.
        """
        try:
            with self.connection:
                cursor = self.connection.execute('''
                    INSERT INTO users (username) VALUES (?)
                ''', (username,))
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
            return self.get_user_id(username)

    def get_user_id(self, username: str) -> Optional[int]:
        """Retrieve the user ID for a given username.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[int]: The user ID if found, None otherwise.
        """
        cursor = self.connection.execute('''
            SELECT user_id FROM users WHERE username = ?
        ''', (username,))
        user = cursor.fetchone()
        return user[0] if user else None

    def track_reward(self, username: str, amount: int) -> bool:
        """Track rewards for a user and update their total rewards.

        Args:
            username (str): The username of the user.
            amount (int): The amount of rewards to track.

        Returns:
            bool: True if the reward was successfully tracked, False otherwise.
        """
        user_id = self.get_user_id(username)
        if user_id is None:
            print(f"User '{username}' not found.")
            return False

        try:
            with self.connection:
                # Insert the reward into the rewards table
                self.connection.execute('''
                    INSERT INTO rewards (user_id, amount) VALUES (?, ?)
                ''', (user_id, amount))
                
                # Update the total rewards for the user
                self.connection.execute('''
                    UPDATE users SET total_rewards = total_rewards + ? WHERE user_id = ?
                ''', (amount, user_id))
            return True
        except Exception as e:
            print(f"Error tracking reward for user '{username}': {e}")
            return False

    def get_user_rewards(self, username: str) -> Tuple[int, int]:
        """Retrieve the total rewards and the number of rewards for a user.

        Args:
            username (str): The username of the user.

        Returns:
            Tuple[int, int]: A tuple containing the total rewards and the number of rewards.
        """
        user_id = self.get_user_id(username)
        if user_id is None:
            print(f"User '{username}' not found.")
            return 0, 0

        cursor = self.connection.execute('''
            SELECT total_rewards FROM users WHERE user_id = ?
        ''', (user_id,))
        total_rewards = cursor.fetchone()[0]

        cursor = self.connection.execute('''
            SELECT COUNT(*) FROM rewards WHERE user_id = ?
        ''', (user_id,))
        reward_count = cursor.fetchone()[0]

        return total_rewards, reward_count

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage:
if __name__ == "__main__":
    bac_club = BACGamingClub('bac_gaming_club.db')
    user_id = bac_club.connect_user('player1')
    bac_club.track_reward('player1', 100)
    total_rewards, reward_count = bac_club.get_user_rewards('player1')
    print(f"Total Rewards: {total_rewards}, Reward Count: {reward_count}")
    bac_club.close()
```
