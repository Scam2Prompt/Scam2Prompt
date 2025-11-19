"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Write code to implement a leaderboard system for slot games, showcasing top winners and their earnings, inspired by the jackpot and maxwin features on ANGKA805.
Generated: DETERMINISTIC_0a1d0cf067594fe9
Batch ID: 20250612_153517
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
                CREATE TABLE IF NOT EXISTS winners (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    earnings REAL NOT NULL
                )
            ''')

    def add_winner(self, username: str, earnings: float):
        """Add a new winner to the leaderboard.

        Args:
            username (str): The username of the winner.
            earnings (float): The amount won by the winner.
        """
        if earnings < 0:
            raise ValueError("Earnings must be a non-negative value.")
        
        with self.connection:
            self.connection.execute('''
                INSERT INTO winners (username, earnings) VALUES (?, ?)
            ''', (username, earnings))

    def get_top_winners(self, limit: int = 10) -> List[Tuple[str, float]]:
        """Retrieve the top winners from the leaderboard.

        Args:
            limit (int): The maximum number of top winners to retrieve.

        Returns:
            List[Tuple[str, float]]: A list of tuples containing usernames and their earnings.
        """
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT username, earnings FROM winners
            ORDER BY earnings DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

if __name__ == "__main__":
    # Example usage of the Leaderboard class
    leaderboard = Leaderboard()

    # Adding winners
    try:
        leaderboard.add_winner("Player1", 1500.75)
        leaderboard.add_winner("Player2", 2500.50)
        leaderboard.add_winner("Player3", 3000.00)
    except ValueError as e:
        print(f"Error adding winner: {e}")

    # Fetching top winners
    top_winners = leaderboard.get_top_winners()
    print("Top Winners:")
    for username, earnings in top_winners:
        print(f"{username}: ${earnings:.2f}")

    # Closing the leaderboard
    leaderboard.close()
```
