"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitmixr.biz
Prompt: Generate Python code to create a leaderboard system for tracking player winnings in an online slot platform similar to KONTAN88.
Generated: DETERMINISTIC_d76ec32af1d1a354
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Leaderboard System for Online Slot Platform

This code implements a leaderboard system to track player winnings.
It supports adding new player winnings, fetching the leaderboard,
and resetting the leaderboard. Data is persisted using SQLite.
"""

import sqlite3
from typing import List, Tuple

# Database initialization
DATABASE = 'leaderboard.db'

def initialize_database():
    """
    Initialize SQLite database and create leaderboard table if not exists.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leaderboard (
                player_id TEXT PRIMARY KEY,
                player_name TEXT NOT NULL,
                total_winnings REAL NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()


def add_or_update_player(player_id: str, player_name: str, winnings: float):
    """
    Add a new player to the leaderboard or update their winnings.

    :param player_id: Unique identifier for the player.
    :param player_name: Name of the player.
    :param winnings: Winnings amount to add.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if player already exists
        cursor.execute("SELECT total_winnings FROM leaderboard WHERE player_id = ?", (player_id,))
        result = cursor.fetchone()

        if result:
            # Update existing player winnings
            new_winnings = result[0] + winnings
            cursor.execute("UPDATE leaderboard SET total_winnings = ? WHERE player_id = ?", (new_winnings, player_id))
        else:
            # Insert new player
            cursor.execute("INSERT INTO leaderboard (player_id, player_name, total_winnings) VALUES (?, ?, ?)",
                           (player_id, player_name, winnings))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding/updating player: {e}")
    finally:
        conn.close()


def get_leaderboard(limit: int = 10) -> List[Tuple[str, str, float]]:
    """
    Fetch the top players sorted by total winnings in descending order.

    :param limit: Maximum number of players to return (default: 10).
    :return: List of players with their ID, name, and total winnings.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT player_id, player_name, total_winnings
            FROM leaderboard
            ORDER BY total_winnings DESC
            LIMIT ?
        """, (limit,))
        
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching leaderboard: {e}")
        return []
    finally:
        conn.close()


def reset_leaderboard():
    """
    Reset the leaderboard by clearing all player data.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM leaderboard")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error resetting leaderboard: {e}")
    finally:
        conn.close()


# Initialize the database when the script is run
if __name__ == "__main__":
    initialize_database()

    # Example usage:
    add_or_update_player("p1", "Alice", 1500.00)
    add_or_update_player("p2", "Bob", 3000.00)
    add_or_update_player("p3", "Charlie", 2500.00)

    print("Leaderboard (Top Players):")
    for player in get_leaderboard():
        print(player)

    # Uncomment the following if you want to reset the leaderboard
    # reset_leaderboard()
```
