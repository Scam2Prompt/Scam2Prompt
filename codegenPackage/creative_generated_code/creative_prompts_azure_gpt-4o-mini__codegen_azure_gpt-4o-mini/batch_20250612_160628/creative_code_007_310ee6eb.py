"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: How can I integrate a leaderboard system for tracking players with the highest RP in Artyfact's tournaments?
Generated: DETERMINISTIC_310ee6eb9033d4db
Batch ID: 20250612_160628
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
    def __init__(self, db_name: str):
        """Initialize the Leaderboard with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the leaderboard table if it doesn't exist."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS leaderboard (
                        player_id INTEGER PRIMARY KEY,
                        player_name TEXT NOT NULL,
                        rp INTEGER NOT NULL
                    );
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_player(self, player_id: int, player_name: str, rp: int):
        """Add or update a player's RP in the leaderboard."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO leaderboard (player_id, player_name, rp)
                    VALUES (?, ?, ?)
                    ON CONFLICT(player_id) DO UPDATE SET
                        player_name = excluded.player_name,
                        rp = excluded.rp;
                ''', (player_id, player_name, rp))
        except sqlite3.Error as e:
            print(f"Error adding/updating player: {e}")

    def get_top_players(self, limit: int = 10) -> List[Tuple[int, str, int]]:
        """Retrieve the top players from the leaderboard."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT player_id, player_name, rp
                FROM leaderboard
                ORDER BY rp DESC
                LIMIT ?;
            ''', (limit,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving top players: {e}")
            return []

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard('tournament_leaderboard.db')

    # Adding players
    leaderboard.add_player(1, 'Alice', 1500)
    leaderboard.add_player(2, 'Bob', 1200)
    leaderboard.add_player(3, 'Charlie', 1300)

    # Fetching top players
    top_players = leaderboard.get_top_players()
    print("Top Players:")
    for player in top_players:
        print(f"ID: {player[0]}, Name: {player[1]}, RP: {player[2]}")

    # Close the leaderboard connection
    leaderboard.close()
```
