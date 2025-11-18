"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Develop a leaderboard system for tracking top traders, inspired by the "Leaderboard" functionality on the Deeptrade UI platform.
Generated: DETERMINISTIC_3fffe97085709cb9
Batch ID: 20250612_153758
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
    def __init__(self, db_name: str = 'traders.db'):
        """Initialize the leaderboard with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the traders table if it doesn't exist."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS traders (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    score INTEGER NOT NULL DEFAULT 0
                )
            ''')

    def add_trader(self, name: str) -> None:
        """Add a new trader to the leaderboard."""
        try:
            with self.conn:
                self.conn.execute('INSERT INTO traders (name) VALUES (?)', (name,))
        except sqlite3.IntegrityError:
            print(f"Trader '{name}' already exists.")

    def update_score(self, name: str, score: int) -> None:
        """Update the score of a trader."""
        with self.conn:
            self.conn.execute('''
                UPDATE traders
                SET score = score + ?
                WHERE name = ?
            ''', (score, name))

    def get_leaderboard(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Retrieve the top traders sorted by their scores."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT name, score
            FROM traders
            ORDER BY score DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

if __name__ == "__main__":
    # Example usage of the Leaderboard class
    leaderboard = Leaderboard()

    # Adding traders
    leaderboard.add_trader("Alice")
    leaderboard.add_trader("Bob")

    # Update scores
    leaderboard.update_score("Alice", 50)
    leaderboard.update_score("Bob", 30)

    # Retrieve and print the leaderboard
    top_traders = leaderboard.get_leaderboard()
    print("Leaderboard:")
    for trader, score in top_traders:
        print(f"{trader}: {score}")

    # Close the connection when done
    leaderboard.close()
```
