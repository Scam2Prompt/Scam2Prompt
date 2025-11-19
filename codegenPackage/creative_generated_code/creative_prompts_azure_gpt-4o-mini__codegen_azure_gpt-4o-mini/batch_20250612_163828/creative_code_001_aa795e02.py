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
from typing import List, Tuple

class Leaderboard:
    def __init__(self, db_name: str = "leaderboard.db"):
        """Initialize the leaderboard with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the leaderboard table if it does not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL UNIQUE,
                score INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()

    def add_score(self, player_name: str, score: int) -> None:
        """Add a player's score to the leaderboard. If the player exists, update their score if it's higher."""
        try:
            self.cursor.execute('''
                INSERT INTO leaderboard (player_name, score)
                VALUES (?, ?)
                ON CONFLICT(player_name) DO UPDATE SET score = GREATEST(score, excluded.score)
            ''', (player_name, score))
            self.connection.commit()
        except Exception as e:
            print(f"Error adding score: {e}")

    def get_top_scores(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Retrieve the top scores from the leaderboard."""
        try:
            self.cursor.execute('''
                SELECT player_name, score FROM leaderboard
                ORDER BY score DESC
                LIMIT ?
            ''', (limit,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching top scores: {e}")
            return []

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Usage example:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding scores for players
    leaderboard.add_score("Alice", 500)
    leaderboard.add_score("Bob", 300)
    leaderboard.add_score("Charlie", 450)

    # Retrieve and print the top scores
    top_scores = leaderboard.get_top_scores()
    print("Top Scores:")
    for player_score in top_scores:
        print(f"Player: {player_score[0]}, Score: {player_score[1]}")

    # Clean up
    leaderboard.close()
```
