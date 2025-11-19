"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: How can I implement a leaderboard system for a play-to-earn game using the mechanics described on ev.io?
Generated: DETERMINISTIC_aa795e02d36cbb08
Batch ID: 20250612_163828
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
DATABASE_NAME = "leaderboard.db"

# Initialize the database and create the necessary table
def initialize_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create a table for storing player scores
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            player_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            score INTEGER NOT NULL DEFAULT 0,
            last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()


# Function to add or update a player's score
def update_player_score(player_id, username, score):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO leaderboard (player_id, username, score, last_updated)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(player_id) DO UPDATE SET
            username = excluded.username,
            score = excluded.score,
            last_updated = excluded.last_updated
        """, (player_id, username, score, datetime.now()))
        conn.commit()
        print(f"Score updated for player {username} (ID: {player_id}).")
    except sqlite3.Error as e:
        print(f"Error updating player score: {e}")
    finally:
        conn.close()


# Function to retrieve the top N players from the leaderboard
def get_top_players(limit=10):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT username, score, last_updated
        FROM leaderboard
        ORDER BY score DESC, last_updated ASC
        LIMIT ?
        """, (limit,))
        top_players = cursor.fetchall()

        return top_players
    except sqlite3.Error as e:
        print(f"Error retrieving top players: {e}")
        return []
    finally:
        conn.close()


# Function to delete a player from the leaderboard
def remove_player(player_id):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM leaderboard
        WHERE player_id = ?
        """, (player_id,))
        conn.commit()
        print(f"Player with ID {player_id} removed from leaderboard.")
    except sqlite3.Error as e:
        print(f"Error removing player: {e}")
    finally:
        conn.close()


# Initialize the database (run this once before using the leaderboard)
initialize_database()

# Example usage
if __name__ == "__main__":
    # Add or update player scores
    update_player_score("1", "PlayerOne", 1500)
    update_player_score("2", "PlayerTwo", 1800)
    update_player_score("3", "PlayerThree", 1200)

    # Get top players
    print("Top Players:")
    top_players = get_top_players(5)
    for rank, player in enumerate(top_players, start=1):
        username, score, last_updated = player
        print(f"{rank}. {username} - {score} points (Last Updated: {last_updated})")

    # Remove a player
    remove_player("3")
```
