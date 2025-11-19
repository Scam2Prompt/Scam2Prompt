"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: How can I implement a loyalty rewards program in a casino gaming application similar to BaxBet?
Generated: DETERMINISTIC_cb295a27f7e6487c
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# loyalty_rewards.py

import sqlite3
from datetime import datetime

# Constants for reward tiers
REWARD_TIERS = {
    "Bronze": {"points_threshold": 0, "multiplier": 1.0},
    "Silver": {"points_threshold": 1000, "multiplier": 1.1},
    "Gold": {"points_threshold": 5000, "multiplier": 1.2},
    "Platinum": {"points_threshold": 10000, "multiplier": 1.5},
}

# Initialize SQLite database connection (In production, use a robust database)
DATABASE_FILE = "casino_rewards.db"


class LoyaltyRewards:
    def __init__(self, db_file=DATABASE_FILE):
        self.connection = sqlite3.connect(db_file)
        self._initialize_database()

    def _initialize_database(self):
        """Initialize the database schema if not exists."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    points INTEGER DEFAULT 0,
                    tier TEXT DEFAULT 'Bronze',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

    def add_user(self, username):
        """Add a new user to the system."""
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO users (username) VALUES (?)",
                    (username,)
                )
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Username '{username}' already exists.") from e

    def get_user_info(self, username):
        """Retrieve user information."""
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT username, points, tier, created_at FROM users WHERE username = ?",
            (username,),
        )
        user = cursor.fetchone()
        if not user:
            raise ValueError(f"User '{username}' not found.")
        return {
            "username": user[0],
            "points": user[1],
            "tier": user[2],
            "created_at": user[3],
        }

    def update_points(self, username, points_earned):
        """Update loyalty points for a user."""
        user_info = self.get_user_info(username)
        new_points = user_info["points"] + points_earned

        # Determine new tier based on updated points
        new_tier = self._calculate_tier(new_points)

        with self.connection:
            self.connection.execute(
                "UPDATE users SET points = ?, tier = ? WHERE username = ?",
                (new_points, new_tier, username),
            )

    def _calculate_tier(self, points):
        """Calculate the loyalty tier based on points."""
        for tier, details in sorted(REWARD_TIERS.items(), key=lambda x: x[1]["points_threshold"], reverse=True):
            if points >= details["points_threshold"]:
                return tier
        return "Bronze"

    def apply_rewards_multiplier(self, username, base_reward):
        """Calculate the reward based on user's tier multiplier."""
        user_info = self.get_user_info(username)
        tier = user_info["tier"]
        multiplier = REWARD_TIERS[tier]["multiplier"]
        return base_reward * multiplier

    def close(self):
        """Close the database connection."""
        self.connection.close()


# Example Usage
if __name__ == "__main__":
    # Initialize the rewards system
    rewards = LoyaltyRewards()

    # Add users
    try:
        rewards.add_user("player1")
        rewards.add_user("player2")
    except ValueError as e:
        print(e)

    # Update points and check tiers
    rewards.update_points("player1", 1200)  # Player1 earned points
    print(rewards.get_user_info("player1"))

    # Apply a reward multiplier
    base_reward = 100
    final_reward = rewards.apply_rewards_multiplier("player1", base_reward)
    print(f"Final reward for player1: {final_reward}")

    # Close connection
    rewards.close()
```
