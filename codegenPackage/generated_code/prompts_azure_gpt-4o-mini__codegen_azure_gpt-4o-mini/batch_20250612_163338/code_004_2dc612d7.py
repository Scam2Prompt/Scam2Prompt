"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Describe how to implement a leaderboard system for tracking player progress and $BIGTIME earnings in a game similar to Big Time.
Generated: DETERMINISTIC_2dc612d7dba1c8ee
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

class Leaderboard:
    def __init__(self, db_name: str = 'leaderboard.db'):
        """Initialize the leaderboard with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the leaderboard table if it doesn't exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS leaderboard (
                    player_id INTEGER PRIMARY KEY,
                    player_name TEXT NOT NULL,
                    progress INTEGER NOT NULL,
                    bigtime_earnings REAL NOT NULL
                )
            ''')

    def add_player(self, player_id: int, player_name: str, progress: int, bigtime_earnings: float):
        """Add a new player to the leaderboard."""
        with self.connection:
            try:
                self.connection.execute('''
                    INSERT INTO leaderboard (player_id, player_name, progress, bigtime_earnings)
                    VALUES (?, ?, ?, ?)
                ''', (player_id, player_name, progress, bigtime_earnings))
            except sqlite3.IntegrityError:
                print(f"Player ID {player_id} already exists. Use update_player to modify their data.")

    def update_player(self, player_id: int, progress: int, bigtime_earnings: float):
        """Update an existing player's progress and earnings."""
        with self.connection:
            self.connection.execute('''
                UPDATE leaderboard
                SET progress = ?, bigtime_earnings = ?
                WHERE player_id = ?
            ''', (progress, bigtime_earnings, player_id))

    def get_leaderboard(self) -> List[Tuple[int, str, int, float]]:
        """Retrieve the leaderboard sorted by progress and earnings."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT player_id, player_name, progress, bigtime_earnings
            FROM leaderboard
            ORDER BY progress DESC, bigtime_earnings DESC
        ''')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players
    leaderboard.add_player(1, 'PlayerOne', 100, 50.0)
    leaderboard.add_player(2, 'PlayerTwo', 150, 75.0)

    # Updating a player's progress and earnings
    leaderboard.update_player(1, 120, 60.0)

    # Fetching and displaying the leaderboard
    for entry in leaderboard.get_leaderboard():
        print(f"ID: {entry[0]}, Name: {entry[1]}, Progress: {entry[2]}, Earnings: {entry[3]}")

    # Closing the connection
    leaderboard.close()
```
