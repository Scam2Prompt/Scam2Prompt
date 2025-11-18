"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Write code to implement a leaderboard system for slot games, showcasing top winners and their earnings, inspired by the jackpot and maxwin features on ANGKA805.
Generated: DETERMINISTIC_0a1d0cf067594fe9
Batch ID: 20250612_153517
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
from typing import List, Tuple

class Leaderboard:
    """A class to represent a leaderboard for slot games."""

    def __init__(self, db_name: str = 'leaderboard.db'):
        """Initialize the database connection and create the leaderboard table."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the leaderboard table if it doesn't exist."""
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS leaderboard (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        player_name TEXT NOT NULL,
                        earnings REAL NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_winner(self, player_name: str, earnings: float):
        """Add a winner to the leaderboard."""
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO leaderboard (player_name, earnings) 
                    VALUES (?, ?)
                ''', (player_name, earnings))
        except sqlite3.Error as e:
            print(f"Error adding winner: {e}")

    def get_top_winners(self, limit: int = 10) -> List[Tuple[str, float]]:
        """Retrieve the top winners sorted by earnings."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT player_name, earnings 
                FROM leaderboard 
                ORDER BY earnings DESC 
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving top winners: {e}")
            return []

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == '__main__':
    leaderboard = Leaderboard()
    leaderboard.add_winner('Alice', 1500.00)
    leaderboard.add_winner('Bob', 2500.50)
    leaderboard.add_winner('Charlie', 1000.75)

    top_winners = leaderboard.get_top_winners()
    print("Top Winners:")
    for player_name, earnings in top_winners:
        print(f"{player_name}: ${earnings:.2f}")

    leaderboard.close()
```
