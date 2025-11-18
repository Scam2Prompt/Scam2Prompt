"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "What are the best practices for implementing a slot game leaderboard that tracks high payouts and frequent wins, as seen on สล็อตเว็บตรง?"
Generated: DETERMINISTIC_8bda98b6ab95dccd
Batch ID: 20250612_145526
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
from datetime import datetime


class Leaderboard:
    """
    A class to manage a slot game leaderboard tracking high payouts and frequent wins.
    """

    def __init__(self, db_path: str = "leaderboard.db"):
        """
        Initialize the leaderboard with a SQLite database connection.
        :param db_path: File path for the SQLite database.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the database schema for the leaderboard.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Create players table to store user stats
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        total_payout REAL NOT NULL DEFAULT 0.0,
                        wins INTEGER NOT NULL DEFAULT 0,
                        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise

    def add_or_update_player(self, username: str, payout: float, win: bool):
        """
        Add a new player or update an existing player's stats.
        :param username: The username of the player.
        :param payout: The amount of payout to add.
        :param win: Whether the player had a win.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Check if the player already exists
                cursor.execute("SELECT * FROM players WHERE username = ?", (username,))
                player = cursor.fetchone()
                if player:
                    # Update existing player stats
                    cursor.execute("""
                        UPDATE players
                        SET total_payout = total_payout + ?,
                            wins = wins + ?,
                            last_updated = ?
                        WHERE username = ?
                    """, (payout, 1 if win else 0, datetime.now(), username))
                else:
                    # Insert new player
                    cursor.execute("""
                        INSERT INTO players (username, total_payout, wins, last_updated)
                        VALUES (?, ?, ?, ?)
                    """, (username, payout, 1 if win else 0, datetime.now()))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating player stats: {e}")
            raise

    def get_top_players_by_payout(self, limit: int = 10) -> List[Tuple]:
        """
        Retrieve the top players sorted by total payout.
        :param limit: The number of players to retrieve.
        :return: A list of tuples representing the top players.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT username, total_payout, wins
                    FROM players
                    ORDER BY total_payout DESC
                    LIMIT ?
                """, (limit,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving top players by payout: {e}")
            raise

    def get_top_players_by_wins(self, limit: int = 10) -> List[Tuple]:
        """
        Retrieve the top players sorted by number of wins.
        :param limit: The number of players to retrieve.
        :return: A list of tuples representing the top players.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT username, total_payout, wins
                    FROM players
                    ORDER BY wins DESC
                    LIMIT ?
                """, (limit,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving top players by wins: {e}")
            raise

    def reset_leaderboard(self):
        """
        Reset the leaderboard by clearing all player data.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM players")
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error resetting leaderboard: {e}")
            raise


# Example usage:
# leaderboard = Leaderboard()
# leaderboard.add_or_update_player("player1", payout=500, win=True)
# leaderboard.add_or_update_player("player2", payout=300, win=False)
# print(leaderboard.get_top_players_by_payout())
# print(leaderboard.get_top_players_by_wins())
# leaderboard.reset_leaderboard()
```
