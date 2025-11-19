"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Explain how to design a leaderboard system for tracking user progress in an NFT evolution game based on the HV-MTL mechanics.
Generated: DETERMINISTIC_727e25df183a196f
Batch ID: 20250612_135528
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
                    user_id TEXT PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    score INTEGER NOT NULL DEFAULT 0,
                    evolution_level INTEGER NOT NULL DEFAULT 0
                )
            ''')

    def add_user(self, user_id: str, user_name: str):
        """Add a new user to the leaderboard."""
        with self.connection:
            try:
                self.connection.execute('''
                    INSERT INTO leaderboard (user_id, user_name)
                    VALUES (?, ?)
                ''', (user_id, user_name))
            except sqlite3.IntegrityError:
                print(f"User {user_name} already exists in the leaderboard.")

    def update_score(self, user_id: str, score: int, evolution_level: int):
        """Update the user's score and evolution level."""
        with self.connection:
            self.connection.execute('''
                UPDATE leaderboard
                SET score = score + ?, evolution_level = ?
                WHERE user_id = ?
            ''', (score, evolution_level, user_id))

    def get_leaderboard(self) -> List[Tuple[str, str, int, int]]:
        """Retrieve the leaderboard sorted by score."""
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT user_id, user_name, score, evolution_level
            FROM leaderboard
            ORDER BY score DESC
        ''')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding users
    leaderboard.add_user("1", "Alice")
    leaderboard.add_user("2", "Bob")

    # Updating scores
    leaderboard.update_score("1", 100, 1)
    leaderboard.update_score("2", 150, 2)

    # Fetching and displaying the leaderboard
    for entry in leaderboard.get_leaderboard():
        print(f"User ID: {entry[0]}, Name: {entry[1]}, Score: {entry[2]}, Evolution Level: {entry[3]}")

    # Closing the connection
    leaderboard.close()
```
