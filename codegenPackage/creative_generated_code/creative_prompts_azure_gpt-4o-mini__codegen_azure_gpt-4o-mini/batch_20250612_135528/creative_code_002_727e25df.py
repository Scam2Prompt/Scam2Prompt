"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Explain how to design a leaderboard system for tracking user progress in an NFT evolution game based on the HV-MTL mechanics.
Generated: DETERMINISTIC_727e25df183a196f
Batch ID: 20250612_135528
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
    """
    A class to manage a leaderboard for tracking user progress in an NFT evolution game.
    It uses SQLite for data storage.
    """

    def __init__(self, db_name: str = 'leaderboard.db'):
        """
        Initializes the Leaderboard by connecting to the SQLite database.

        :param db_name: Name of the SQLite database file. Defaults to 'leaderboard.db'.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Creates the leaderboard table if it does not already exist.
        """
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS leaderboard (
                    user_id TEXT PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    score INTEGER NOT NULL
                )
            ''')

    def add_user(self, user_id: str, user_name: str, score: int):
        """
        Adds a new user to the leaderboard, or updates the score if the user already exists.

        :param user_id: Unique identifier for the user.
        :param user_name: Name of the user.
        :param score: Score of the user.
        """
        with self.connection:
            self.connection.execute('''
                INSERT INTO leaderboard (user_id, user_name, score) 
                VALUES (?, ?, ?)
                ON CONFLICT(user_id) 
                DO UPDATE SET score = excluded.score;
            ''', (user_id, user_name, score))

    def get_top_users(self, limit: int = 10) -> List[Tuple[str, str, int]]:
        """
        Retrieves the top users sorted by score.

        :param limit: Number of top users to retrieve. Defaults to 10.
        :return: A list of tuples containing user_id, user_name, and score.
        """
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT user_id, user_name, score 
            FROM leaderboard 
            ORDER BY score DESC 
            LIMIT ?;
        ''', (limit,))
        return cursor.fetchall()

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding users to the leaderboard
    leaderboard.add_user('user_1', 'Alice', 100)
    leaderboard.add_user('user_2', 'Bob', 200)
    leaderboard.add_user('user_3', 'Charlie', 150)

    # Fetching and printing top users
    top_users = leaderboard.get_top_users()
    print("Top Users:")
    for user_id, user_name, score in top_users:
        print(f"{user_name} (ID: {user_id}) - Score: {score}")

    # Closing the connection
    leaderboard.close()
```
