"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playember-57a.pages.dev
Prompt: Generate code to implement a leaderboard system for a blockchain-based mobile game, considering PlayEmber's experience with hit IP games and global brands.
Generated: DETERMINISTIC_77a0b512b536cdca
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard_system.py

import sqlite3
from typing import List, Dict

# Constants for database
DB_NAME = "leaderboard.db"
TABLE_NAME = "leaderboard"

# Initialize the database and create the leaderboard table
def initialize_database():
    """Initializes the database and creates a leaderboard table if it does not exist."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Create leaderboard table
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                player_id TEXT PRIMARY KEY,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Add or update player score
def update_score(player_id: str, player_name: str, score: int):
    """
    Updates the score for a player. If the player does not exist, they are added.
    :param player_id: Unique player identifier (e.g., blockchain wallet address)
    :param player_name: Player's name
    :param score: Player's score
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Check if the player already exists
        cursor.execute(f"SELECT score FROM {TABLE_NAME} WHERE player_id = ?", (player_id,))
        row = cursor.fetchone()

        if row:
            # Update score if it's higher than the existing score
            if score > row[0]:
                cursor.execute(
                    f"UPDATE {TABLE_NAME} SET score = ?, timestamp = CURRENT_TIMESTAMP WHERE player_id = ?",
                    (score, player_id)
                )
        else:
            # Insert new player
            cursor.execute(
                f"INSERT INTO {TABLE_NAME} (player_id, player_name, score) VALUES (?, ?, ?)",
                (player_id, player_name, score)
            )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating score: {e}")
    finally:
        conn.close()

# Retrieve top N players
def get_top_players(limit: int = 10) -> List[Dict[str, str]]:
    """
    Retrieves the top N players based on their scores.
    :param limit: Number of top players to fetch
    :return: List of dictionaries containing player details
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT player_id, player_name, score FROM {TABLE_NAME} ORDER BY score DESC, timestamp ASC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        return [{"player_id": row[0], "player_name": row[1], "score": row[2]} for row in rows]
    except sqlite3.Error as e:
        print(f"Error retrieving top players: {e}")
        return []
    finally:
        conn.close()

# Remove player from leaderboard
def remove_player(player_id: str):
    """
    Removes a player from the leaderboard.
    :param player_id: Unique player identifier
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE player_id = ?", (player_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error removing player: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()

    # Add or update player scores
    update_score("wallet_123", "Alice", 1500)
    update_score("wallet_456", "Bob", 2000)
    update_score("wallet_789", "Charlie", 1800)

    # Retrieve top players
    top_players = get_top_players(5)
    print("Top Players:")
    for player in top_players:
        print(player)

    # Remove a player
    remove_player("wallet_123")
```
