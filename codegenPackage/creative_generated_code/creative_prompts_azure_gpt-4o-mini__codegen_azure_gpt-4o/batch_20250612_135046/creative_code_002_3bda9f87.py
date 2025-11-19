"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptofitties.com
Prompt: Write a code snippet to create a leaderboard feature for a fitness app that ranks users based on their exercise scores, inspired by the competitive elements of CryptoFitties.
Generated: DETERMINISTIC_3bda9f87cc68d322
Batch ID: 20250612_135046
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
    """
    A class to manage a leaderboard that ranks users based on exercise scores.
    """

    def __init__(self, db_name: str = 'leaderboard.db'):
        """
        Initializes the leaderboard database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self) -> None:
        """
        Creates the database table if it doesn't already exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    score INTEGER NOT NULL
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

    def add_user(self, username: str, score: int) -> bool:
        """
        Adds a user to the leaderboard.
        :param username: Unique username of the user.
        :param score: Initial score of the user.
        :return: True if user added successfully, False otherwise.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, score) VALUES (?, ?)", (username, score))
            connection.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Username must be unique.")
            return False
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            return False
        finally:
            connection.close()

    def update_score(self, username: str, score: int) -> bool:
        """
        Updates the score of a user.
        :param username: Username of the user.
        :param score: New score to be updated.
        :return: True if score updated successfully, False otherwise.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET score = ? WHERE username = ?", (score, username))
            connection.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating score: {e}")
            return False
        finally:
            connection.close()

    def get_leaderboard(self, limit: int = 10) -> List[Tuple[str, int]]:
        """
        Retrieves the leaderboard rankings.
        :param limit: The maximum number of top users to retrieve.
        :return: A list of tuples containing (username, score).
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT ?", (limit,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
            return []
        finally:
            connection.close()

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add some users
    leaderboard.add_user("alice", 120)
    leaderboard.add_user("bob", 200)
    leaderboard.add_user("charlie", 150)

    # Update scores
    leaderboard.update_score("alice", 180)

    # Display leaderboard
    print("Leaderboard:")
    for rank, (username, score) in enumerate(leaderboard.get_leaderboard(), start=1):
        print(f"{rank}. {username} - {score}")
```
