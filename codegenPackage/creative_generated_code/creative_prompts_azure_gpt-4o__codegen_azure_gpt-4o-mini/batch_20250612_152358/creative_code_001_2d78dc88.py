"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-lab.pages.dev
Prompt: Develop a leaderboard system that tracks user progress in completing quests, similar to the functionality described on Memes Lab.
Generated: DETERMINISTIC_2d78dc8869e10076
Batch ID: 20250612_152358
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
        """Initialize the leaderboard with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the leaderboard table in the database if it doesn't exist."""
        with self.conn:
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS user_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                quests_completed INTEGER DEFAULT 0
            )
            ''')

    def add_user(self, username: str):
        """Add a new user to the leaderboard."""
        try:
            with self.conn:
                self.conn.execute('INSERT INTO user_progress (username) VALUES (?)', (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")

    def update_progress(self, username: str):
        """Increment the quest completion count for a user."""
        with self.conn:
            result = self.conn.execute('UPDATE user_progress SET quests_completed = quests_completed + 1 WHERE username = ?', (username,))
            if result.rowcount == 0:
                print(f"User '{username}' not found. Please add the user first.")

    def get_leaderboard(self) -> List[Tuple[str, int]]:
        """Return the leaderboard sorted by quests completed in descending order."""
        cursor = self.conn.execute('SELECT username, quests_completed FROM user_progress ORDER BY quests_completed DESC')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()

if __name__ == "__main__":
    lb = Leaderboard()

    # Example usage
    lb.add_user('Alice')
    lb.add_user('Bob')

    lb.update_progress('Alice')
    lb.update_progress('Alice')
    lb.update_progress('Bob')

    # Display the leaderboard
    leaderboard = lb.get_leaderboard()
    for position, (username, quests_completed) in enumerate(leaderboard, start=1):
        print(f"{position}. {username}: {quests_completed} quests completed")
    
    # Close the leaderboard to free up resources
    lb.close()
```
