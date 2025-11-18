"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gam3searly.pages.dev
Prompt: Recommend APIs or libraries for implementing a leaderboard system like the one on GAM3S.GG, where users can earn XP and track rankings.
Generated: DETERMINISTIC_c981a632cc8692ed
Batch ID: 20250612_153400
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
from typing import List, Dict, Optional


class Leaderboard:
    """
    A class to manage a leaderboard system that tracks user XP and rankings.
    """

    def __init__(self, db_name: str = 'leaderboard.db'):
        """
        Initializes the Leaderboard with a SQLite database.

        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_table()

    def create_connection(self) -> sqlite3.Connection:
        """
        Creates a database connection to the SQLite database.

        :return: SQLite Connection object.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def create_table(self):
        """
        Creates the leaderboard table if it does not already exist.
        """
        try:
            with self.connection:
                self.connection.execute("""
                CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    xp INTEGER NOT NULL DEFAULT 0
                )
                """)
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            raise

    def add_user(self, username: str) -> None:
        """
        Adds a new user to the leaderboard.

        :param username: The username of the new user.
        :raises sqlite3.IntegrityError: If the user already exists.
        """
        try:
            with self.connection:
                self.connection.execute("INSERT INTO leaderboard (username) VALUES (?)", (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
            raise

    def update_xp(self, username: str, xp: int) -> None:
        """
        Updates the XP for a user.

        :param username: The username of the user.
        :param xp: The amount of XP to add.
        :raises ValueError: If the XP is negative.
        :raises sqlite3.Error: If the user does not exist.
        """
        if xp < 0:
            raise ValueError("XP cannot be negative.")
        
        try:
            with self.connection:
                self.connection.execute("""
                UPDATE leaderboard
                SET xp = xp + ?
                WHERE username = ?
                """, (xp, username))
        except sqlite3.Error as e:
            print(f"Error updating XP for user '{username}': {e}")
            raise

    def get_leaderboard(self) -> List[Dict[str, Optional[int]]]:
        """
        Retrieves the leaderboard sorted by XP in descending order.

        :return: A list of dictionaries containing usernames and XP.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT username, xp FROM leaderboard ORDER BY xp DESC")
            rows = cursor.fetchall()
            return [{"username": row[0], "xp": row[1]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
            raise

    def close(self) -> None:
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add users to the leaderboard
    leaderboard.add_user("Alice")
    leaderboard.add_user("Bob")

    # Update XP for users
    leaderboard.update_xp("Alice", 50)
    leaderboard.update_xp("Bob", 30)

    # Retrieve and print the current leaderboard
    print(leaderboard.get_leaderboard())

    # Close the database connection
    leaderboard.close()
```
