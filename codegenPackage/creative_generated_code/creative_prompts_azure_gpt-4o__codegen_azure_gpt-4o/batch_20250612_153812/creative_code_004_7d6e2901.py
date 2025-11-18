"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-neurongate.xyz
Prompt: Write code to implement a leaderboard system for casino games, inspired by the community-driven features of Zeus Fortune.
Generated: DETERMINISTIC_7d6e2901842c302e
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing


class Leaderboard:
    """
    Leaderboard system for managing casino game scores.
    Inspired by community-driven features of Zeus Fortune.
    """

    def __init__(self, db_name="leaderboard.db"):
        """
        Initialize the leaderboard system.

        Args:
            db_name (str): SQLite database filename.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the database table if it does not exist.
        """
        with closing(self._connect_db()) as conn:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS leaderboard (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        score INTEGER NOT NULL,
                        game_name TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)

    def _connect_db(self):
        """
        Establish a connection to the database.

        Returns:
            sqlite3.Connection: Database connection object.
        """
        return sqlite3.connect(self.db_name)

    def add_score(self, username, score, game_name):
        """
        Add a score entry to the leaderboard.

        Args:
            username (str): Player's username.
            score (int): Player's score.
            game_name (str): Name of the casino game.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        try:
            with closing(self._connect_db()) as conn:
                with conn:
                    conn.execute("""
                        INSERT INTO leaderboard (username, score, game_name)
                        VALUES (?, ?, ?)
                    """, (username, score, game_name))
            return True
        except Exception as e:
            print(f"Error adding score: {e}")
            return False

    def get_top_scores(self, game_name, limit=10):
        """
        Retrieve the top scores for a specific game.

        Args:
            game_name (str): Name of the casino game.
            limit (int): Maximum number of scores to retrieve.

        Returns:
            list[dict]: List of top scores as dictionaries.
        """
        try:
            with closing(self._connect_db()) as conn:
                cursor = conn.execute("""
                    SELECT username, score, timestamp
                    FROM leaderboard
                    WHERE game_name = ?
                    ORDER BY score DESC
                    LIMIT ?
                """, (game_name, limit))
                return [
                    {"username": row[0], "score": row[1], "timestamp": row[2]}
                    for row in cursor.fetchall()
                ]
        except Exception as e:
            print(f"Error retrieving top scores: {e}")
            return []

    def reset_leaderboard(self, game_name):
        """
        Clear all scores for a specific game.

        Args:
            game_name (str): Name of the casino game.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        try:
            with closing(self._connect_db()) as conn:
                with conn:
                    conn.execute("""
                        DELETE FROM leaderboard
                        WHERE game_name = ?
                    """, (game_name,))
            return True
        except Exception as e:
            print(f"Error resetting leaderboard: {e}")
            return False


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add scores
    leaderboard.add_score("Player1", 1200, "Zeus Fortune")
    leaderboard.add_score("Player2", 1500, "Zeus Fortune")

    # Get top scores
    print("Top Scores for Zeus Fortune:")
    for score in leaderboard.get_top_scores("Zeus Fortune"):
        print(score)

    # Reset leaderboard for a specific game
    leaderboard.reset_leaderboard("Zeus Fortune")
```
