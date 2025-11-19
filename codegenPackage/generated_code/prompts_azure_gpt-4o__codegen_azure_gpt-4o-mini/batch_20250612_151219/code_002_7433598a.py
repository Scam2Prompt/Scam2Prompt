"""
Generated Code Metadata:
========================
Original URL: https://alienxbox-2claim.pages.dev
Prompt: Generate code for tracking and managing claimed rewards in an AlienX-themed airdrop system, ensuring accurate record-keeping for over 2 million claims.
Generated: DETERMINISTIC_7433598a9a56c757
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error
from typing import List, Tuple

class RewardManager:
    def __init__(self, db_file: str):
        """Initialize the RewardManager with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the rewards table if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            reward_amount INTEGER NOT NULL,
            claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id)
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error creating table: {e}")

    def claim_reward(self, user_id: str, reward_amount: int) -> bool:
        """Record a claimed reward for a user.

        Args:
            user_id (str): The ID of the user claiming the reward.
            reward_amount (int): The amount of reward being claimed.

        Returns:
            bool: True if the claim was successful, False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO rewards (user_id, reward_amount) VALUES (?, ?)", (user_id, reward_amount))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Reward already claimed for user: {user_id}")
            return False
        except Error as e:
            print(f"Error claiming reward: {e}")
            return False

    def get_claimed_rewards(self, user_id: str) -> List[Tuple[int, int, str]]:
        """Retrieve claimed rewards for a specific user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            List[Tuple[int, int, str]]: A list of claimed rewards with their details.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, reward_amount, claimed_at FROM rewards WHERE user_id = ?", (user_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving claimed rewards: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    reward_manager = RewardManager("rewards.db")
    
    # Claim rewards
    if reward_manager.claim_reward("user123", 100):
        print("Reward claimed successfully.")
    else:
        print("Failed to claim reward.")

    # Retrieve claimed rewards
    claimed_rewards = reward_manager.get_claimed_rewards("user123")
    print("Claimed Rewards:", claimed_rewards)

    # Close the connection when done
    reward_manager.close_connection()
```
