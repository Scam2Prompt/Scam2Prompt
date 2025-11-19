"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Describe how to create a leaderboard feature for a coin-collecting game, inspired by the ranking system on minerinde.com.
Generated: DETERMINISTIC_d909e1bb1da5bc4e
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

# Database setup
DB_NAME = "leaderboard.db"

# Connect to the database and create the necessary table
def initialize_database():
    """
    Initialize the database by creating a table for storing leaderboard data.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            coins INTEGER NOT NULL DEFAULT 0
        )
        """)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        connection.close()

# Function to add or update a player in the leaderboard
def update_leaderboard(username: str, coins: int):
    """
    Add a new player to the leaderboard or update their coin count if they already exist.
    :param username: Name of the player.
    :param coins: Number of coins collected by the player.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        # Insert or update the player's data
        cursor.execute("""
        INSERT INTO leaderboard (username, coins)
        VALUES (?, ?)
        ON CONFLICT(username) DO UPDATE SET
        coins = coins + excluded.coins
        """, (username, coins))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error updating leaderboard: {e}")
    finally:
        connection.close()

# Function to retrieve the top players
def get_top_players(limit: int = 10) -> List[Tuple[str, int]]:
    """
    Retrieve the top players based on their coin count.
    :param limit: Number of top players to retrieve.
    :return: List of tuples containing player usernames and their coin counts.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT username, coins
        FROM leaderboard
        ORDER BY coins DESC
        LIMIT ?
        """, (limit,))
        top_players = cursor.fetchall()
        return top_players
    except sqlite3.Error as e:
        print(f"Error retrieving top players: {e}")
        return []
    finally:
        connection.close()

# Main function for testing the leaderboard feature
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add or update players
    update_leaderboard("player1", 150)
    update_leaderboard("player2", 300)
    update_leaderboard("player3", 200)
    update_leaderboard("player1", 50)  # Update player1's coins

    # Get the top players
    top_players = get_top_players(limit=3)
    print("Top Players:")
    for rank, (username, coins) in enumerate(top_players, start=1):
        print(f"{rank}. {username} - {coins} coins")
```
