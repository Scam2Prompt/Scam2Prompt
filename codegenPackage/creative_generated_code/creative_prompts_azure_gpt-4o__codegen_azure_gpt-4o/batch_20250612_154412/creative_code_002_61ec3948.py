"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: Develop a leaderboard system for tracking top players in a crypto-based casino platform, inspired by the leaderboard functionality on Jups.io.
Generated: DETERMINISTIC_61ec3948bf055cc4
Batch ID: 20250612_154412
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
DB_NAME = "leaderboard.db"
TOP_PLAYERS_LIMIT = 10


class Leaderboard:
    """
    Leaderboard class for tracking top players in a crypto-based casino platform.
    """

    def __init__(self, db_name):
        """
        Initialize the leaderboard system.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the SQLite database with the necessary table if it doesn't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    score INTEGER NOT NULL,
                    last_updated TIMESTAMP NOT NULL
                )
                """
            )
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization failed: {e}")
        finally:
            conn.close()

    def add_or_update_player(self, username, score):
        """
        Add a new player or update an existing player's score.

        :param username: The username of the player.
        :param score: The score of the player.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Check if the player already exists
            cursor.execute(
                "SELECT score FROM players WHERE username = ?", (username,)
            )
            existing_player = cursor.fetchone()

            if existing_player:
                # Update the player's score if they already exist
                cursor.execute(
                    """
                    UPDATE players
                    SET score = ?, last_updated = ?
                    WHERE username = ?
                    """,
                    (score, datetime.now(), username),
                )
            else:
                # Add the player if they don't exist
                cursor.execute(
                    """
                    INSERT INTO players (username, score, last_updated)
                    VALUES (?, ?, ?)
                    """,
                    (username, score, datetime.now()),
                )
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding or updating player: {e}")
        finally:
            conn.close()

    def get_top_players(self, limit=TOP_PLAYERS_LIMIT):
        """
        Retrieve the top players based on their scores.

        :param limit: The maximum number of top players to retrieve. Defaults to TOP_PLAYERS_LIMIT.
        :return: A list of dictionaries containing top player data.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT username, score, last_updated
                FROM players
                ORDER BY score DESC, last_updated ASC
                LIMIT ?
                """,
                (limit,),
            )
            rows = cursor.fetchall()

            # Transform data into a list of dictionaries
            top_players = [
                {"username": row[0], "score": row[1], "last_updated": row[2]}
                for row in rows
            ]
            return top_players
        except sqlite3.Error as e:
            print(f"Error retrieving top players: {e}")
            return []
        finally:
            conn.close()

    def delete_player(self, username):
        """
        Delete a player from the leaderboard.

        :param username: The username of the player to delete.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM players WHERE username = ?", (username,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting player: {e}")
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard(DB_NAME)

    # Add or update players
    leaderboard.add_or_update_player("Alice", 1200)
    leaderboard.add_or_update_player("Bob", 1500)
    leaderboard.add_or_update_player("Charlie", 900)

    # Get top players
    print("Top Players:", leaderboard.get_top_players())

    # Delete a player
    leaderboard.delete_player("Charlie")

    # Get updated leaderboard
    print("Updated Leaderboard:", leaderboard.get_top_players())
```
