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
    """
    A class to manage a leaderboard system tracking user progress in completing quests.
    """
    
    def __init__(self, db_name: str = "leaderboard.db"):
        """
        Initialize the leaderboard system with a SQLite database.

        :param db_name: Name of the database file to use (default: "leaderboard.db").
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Create the necessary database tables if they do not already exist."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Create users table to store user data
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL
                    )
                """)
                # Create quests table to store quests data
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS quests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        quest_name TEXT NOT NULL,
                        completion_status BOOLEAN NOT NULL DEFAULT 0,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                    )
                """)
                # Create leaderboard view to aggregate user progress
                cursor.execute("""
                    CREATE VIEW IF NOT EXISTS leaderboard AS
                    SELECT 
                        u.username, 
                        COUNT(q.id) AS quests_completed
                    FROM 
                        users u
                    LEFT JOIN 
                        quests q
                    ON 
                        u.id = q.user_id AND q.completion_status = 1
                    GROUP BY 
                        u.id
                    ORDER BY 
                        quests_completed DESC, u.username ASC
                """)
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")

    def add_user(self, username: str):
        """
        Add a new user to the leaderboard.

        :param username: The username of the new user.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (username) VALUES (?)
                """, (username,))
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user '{username}': {e}")

    def add_quest(self, username: str, quest_name: str):
        """
        Assign a new quest to a user.

        :param username: The username of the user.
        :param quest_name: The name of the quest.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Get user ID
                cursor.execute("""
                    SELECT id FROM users WHERE username = ?
                """, (username,))
                user = cursor.fetchone()
                if not user:
                    print(f"User '{username}' not found.")
                    return

                user_id = user[0]

                # Add quest for the user
                cursor.execute("""
                    INSERT INTO quests (user_id, quest_name, completion_status) 
                    VALUES (?, ?, 0)
                """, (user_id, quest_name))
        except sqlite3.Error as e:
            print(f"Error adding quest '{quest_name}' for user '{username}': {e}")

    def complete_quest(self, username: str, quest_name: str):
        """
        Mark a quest as completed for a user.

        :param username: The username of the user.
        :param quest_name: The name of the quest.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Get user ID
                cursor.execute("""
                    SELECT id FROM users WHERE username = ?
                """, (username,))
                user = cursor.fetchone()
                if not user:
                    print(f"User '{username}' not found.")
                    return

                user_id = user[0]

                # Mark the quest as completed
                cursor.execute("""
                    UPDATE quests 
                    SET completion_status = 1 
                    WHERE user_id = ? AND quest_name = ?
                """, (user_id, quest_name))
                if cursor.rowcount == 0:
                    print(f"Quest '{quest_name}' not found for user '{username}'.")
        except sqlite3.Error as e:
            print(f"Error completing quest '{quest_name}' for user '{username}': {e}")

    def get_leaderboard(self) -> List[Tuple[str, int]]:
        """
        Retrieve the leaderboard data.

        :return: A list of tuples containing usernames and their completed quest counts.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT username, quests_completed FROM leaderboard
                """)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
            return []

# Example usage (for testing purposes):
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add users
    leaderboard.add_user("Alice")
    leaderboard.add_user("Bob")

    # Add quests
    leaderboard.add_quest("Alice", "Quest 1")
    leaderboard.add_quest("Alice", "Quest 2")
    leaderboard.add_quest("Bob", "Quest 1")

    # Complete quests
    leaderboard.complete_quest("Alice", "Quest 1")

    # Get leaderboard
    for username, quests_completed in leaderboard.get_leaderboard():
        print(f"{username}: {quests_completed} quests completed")
```
