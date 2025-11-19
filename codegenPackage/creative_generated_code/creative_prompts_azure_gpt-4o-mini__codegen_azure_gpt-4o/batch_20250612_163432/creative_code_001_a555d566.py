"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pandas-dsp.pages.dev
Prompt: Write code to create a leaderboard system for tracking NFT Panda stakers and their rewards, inspired by the PandaVerse platform.
Generated: DETERMINISTIC_a555d5668dfc2eb1
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py
import sqlite3
from datetime import datetime

# Constants
DATABASE_NAME = "leaderboard.db"

# SQL Queries
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS leaderboard (
    user_id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    total_stake REAL NOT NULL DEFAULT 0.0,
    total_rewards REAL NOT NULL DEFAULT 0.0,
    last_updated TIMESTAMP NOT NULL
);
"""

INSERT_OR_UPDATE_USER_QUERY = """
INSERT INTO leaderboard (user_id, username, total_stake, total_rewards, last_updated)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(user_id)
DO UPDATE SET
    total_stake = leaderboard.total_stake + excluded.total_stake,
    total_rewards = leaderboard.total_rewards + excluded.total_rewards,
    last_updated = excluded.last_updated;
"""

GET_LEADERBOARD_QUERY = """
SELECT username, total_stake, total_rewards, last_updated 
FROM leaderboard 
ORDER BY total_rewards DESC, total_stake DESC 
LIMIT ?;
"""

# Initialize Database
def initialize_database():
    """Creates the leaderboard table if not already present."""
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        connection.close()

# Update User Data
def update_user(user_id, username, stake, rewards):
    """
    Updates or inserts user data into the leaderboard.

    Args:
        user_id (str): Unique ID of the user.
        username (str): Username of the user.
        stake (float): Amount staked by the user.
        rewards (float): Rewards earned by the user.

    Raises:
        ValueError: If stake or rewards are negative.
    """
    if stake < 0 or rewards < 0:
        raise ValueError("Stake and rewards must be non-negative.")

    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        last_updated = datetime.now()
        cursor.execute(INSERT_OR_UPDATE_USER_QUERY, (user_id, username, stake, rewards, last_updated))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error updating user data: {e}")
    finally:
        connection.close()

# Get Leaderboard
def get_leaderboard(limit=10):
    """
    Retrieves the top users from the leaderboard.

    Args:
        limit (int): Number of top users to retrieve. Default is 10.

    Returns:
        list of dict: List containing user data sorted by rewards and stake.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute(GET_LEADERBOARD_QUERY, (limit,))
        rows = cursor.fetchall()
        leaderboard = [
            {
                "username": row[0],
                "total_stake": row[1],
                "total_rewards": row[2],
                "last_updated": row[3]
            }
            for row in rows
        ]
        return leaderboard
    except sqlite3.Error as e:
        print(f"Error retrieving leaderboard: {e}")
        return []
    finally:
        connection.close()

# Main Execution (for testing purposes)
if __name__ == "__main__":
    # Initialize database
    initialize_database()
    
    # Example user updates
    try:
        update_user("user1", "PandaLover", 150.0, 20.5)
        update_user("user2", "CryptoKing", 200.0, 35.0)
        update_user("user3", "NFTQueen", 120.0, 18.0)
    except ValueError as ve:
        print(ve)
    
    # Retrieve and display leaderboard
    print("Top Users:")
    leaderboard = get_leaderboard(limit=5)
    for idx, user in enumerate(leaderboard, start=1):
        print(f"{idx}. {user['username']} - Stake: {user['total_stake']}, Rewards: {user['total_rewards']}")
```
