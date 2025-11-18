"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alienxbox-2claim.pages.dev
Prompt: Generate code for tracking and managing claimed rewards in an AlienX-themed airdrop system, ensuring accurate record-keeping for over 2 million claims.
Generated: DETERMINISTIC_7433598a9a56c757
Batch ID: 20250612_151219
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
from typing import List, Tuple

class RewardTracker:
    def __init__(self, db_file: str):
        """Initialize RewardTracker with a SQLite database file."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file: str):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful.")
        except Error as e:
            print(f"Error '{e}' occurred when connecting to the database.")
        return conn

    def create_table(self):
        """Create a table for storing claimed rewards if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            reward_amount REAL NOT NULL,
            claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id)
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
            print("Rewards table created successfully.")
        except Error as e:
            print(f"Error '{e}' occurred when creating the table.")

    def claim_reward(self, user_id: str, reward_amount: float) -> str:
        """Claim a reward for a user and store it in the database.

        Args:
            user_id (str): The identifier for the user claiming the reward.
            reward_amount (float): The amount of reward being claimed.

        Returns:
            str: Success message or error message.
        """
        if reward_amount <= 0:
            return "Reward amount must be greater than 0."

        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO rewards (user_id, reward_amount) VALUES (?, ?);", (user_id, reward_amount))
            self.connection.commit()
            return f"Reward of {reward_amount} claimed successfully for user {user_id}."
        except sqlite3.IntegrityError:
            return f"User {user_id} has already claimed their reward."
        except Error as e:
            return f"Error '{e}' occurred when claiming reward."

    def get_all_claims(self) -> List[Tuple[str, float, str]]:
        """Retrieve all claimed rewards from the database.

        Returns:
            List[Tuple[str, float, str]]: A list of claimed rewards.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT user_id, reward_amount, claimed_at FROM rewards;")
            return cursor.fetchall()
        except Error as e:
            print(f"Error '{e}' occurred when retrieving claims.")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    tracker = RewardTracker("alienx_rewards.db")

    # Example to claim rewards
    print(tracker.claim_reward("user123", 10.0))
    print(tracker.claim_reward("user456", 15.5))

    # Retrieve and print all claims
    claims = tracker.get_all_claims()
    for claim in claims:
        print(claim)

    # Close the database connection
    tracker.close_connection()
```
