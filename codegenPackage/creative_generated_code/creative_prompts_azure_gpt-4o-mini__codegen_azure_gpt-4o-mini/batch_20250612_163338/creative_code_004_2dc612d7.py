"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Describe how to implement a leaderboard system for tracking player progress and $BIGTIME earnings in a game similar to Big Time.
Generated: DETERMINISTIC_2dc612d7dba1c8ee
Batch ID: 20250612_163338
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

class Leaderboard:
    def __init__(self, db_name: str = 'leaderboard.db'):
        """
        Initialize the leaderboard system and create the database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_table()

    def create_connection(self) -> sqlite3.Connection:
        """
        Create a database connection to the SQLite database.
        :return: Connection object.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the leaderboard table if it does not exist."""
        try:
            with self.connection:
                self.connection.execute('''
                CREATE TABLE IF NOT EXISTS leaderboard (
                    player_id INTEGER PRIMARY KEY,
                    player_name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    bigtime_earnings REAL NOT NULL
                )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_player(self, player_id: int, player_name: str, score: int, bigtime_earnings: float):
        """
        Add a new player to the leaderboard.
        :param player_id: Unique identifier for the player.
        :param player_name: Name of the player.
        :param score: Player's score.
        :param bigtime_earnings: Amount of $BIGTIME earned by the player.
        """
        try:
            with self.connection:
                self.connection.execute('''
                INSERT INTO leaderboard (player_id, player_name, score, bigtime_earnings) 
                VALUES (?, ?, ?, ?)
                ''', (player_id, player_name, score, bigtime_earnings))
        except sqlite3.IntegrityError:
            print(f"Player with ID {player_id} already exists.")
        except sqlite3.Error as e:
            print(f"Error adding player: {e}")

    def update_player(self, player_id: int, score: int, bigtime_earnings: float):
        """
        Update an existing player's score and $BIGTIME earnings.
        :param player_id: Unique identifier for the player.
        :param score: New score for the player.
        :param bigtime_earnings: New amount of $BIGTIME earned by the player.
        """
        try:
            with self.connection:
                self.connection.execute('''
                UPDATE leaderboard 
                SET score = ?, bigtime_earnings = ?
                WHERE player_id = ?
                ''', (score, bigtime_earnings, player_id))
        except sqlite3.Error as e:
            print(f"Error updating player: {e}")

    def get_leaderboard(self) -> List[Tuple[int, str, int, float]]:
        """
        Retrieve the leaderboard, sorted by score and $BIGTIME earnings.
        :return: List of players in leaderboard format.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
            SELECT player_id, player_name, score, bigtime_earnings
            FROM leaderboard
            ORDER BY score DESC, bigtime_earnings DESC
            ''')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example of usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_player(1, 'PlayerOne', 100, 50.0)
    leaderboard.add_player(2, 'PlayerTwo', 150, 75.0)
    
    print("Current Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(player)

    leaderboard.update_player(1, 200, 100.0)
    
    print("\nUpdated Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(player)

    leaderboard.close_connection()
```
