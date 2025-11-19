"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-st.pages.dev
Prompt: Explain how to implement a leaderboard system for the Kangamoon community, focusing on tracking user participation in challenges and rewards.
Generated: DETERMINISTIC_bdb4e847b97394c1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Leaderboard System for Kangamoon Community
# This script tracks user participation in challenges and rewards.
# The system stores user data and calculates rankings based on performance.
# Technology: Python with SQLite for database management.

import sqlite3
from datetime import datetime

class LeaderboardSystem:
    def __init__(self, db_name="kangamoon_leaderboard.db"):
        """
        Initialize the leaderboard system with a SQLite database.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary tables if they do not exist in the database.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Users table: Stores user information.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    joined_date TEXT NOT NULL
                )
            """)

            # Challenges table: Stores information about challenges.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS challenges (
                    challenge_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL
                )
            """)

            # Participation table: Tracks user participation in challenges.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS participation (
                    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    challenge_id INTEGER NOT NULL,
                    score INTEGER NOT NULL DEFAULT 0,
                    FOREIGN KEY(user_id) REFERENCES users(user_id),
                    FOREIGN KEY(challenge_id) REFERENCES challenges(challenge_id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def add_user(self, username):
        """
        Adds a new user to the leaderboard.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            joined_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO users (username, joined_date) VALUES (?, ?)", (username, joined_date))

            conn.commit()
            print(f"User '{username}' successfully added.")
        except sqlite3.IntegrityError:
            print(f"Error: User '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def add_challenge(self, name, description, start_date, end_date):
        """
        Adds a new challenge to the leaderboard.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO challenges (name, description, start_date, end_date) 
                VALUES (?, ?, ?, ?)
            """, (name, description, start_date, end_date))

            conn.commit()
            print(f"Challenge '{name}' successfully added.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def record_participation(self, username, challenge_name, score):
        """
        Records a user's participation in a challenge with their score.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Get user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                print(f"Error: User '{username}' does not exist.")
                return
            user_id = user[0]

            # Get challenge ID
            cursor.execute("SELECT challenge_id FROM challenges WHERE name = ?", (challenge_name,))
            challenge = cursor.fetchone()
            if not challenge:
                print(f"Error: Challenge '{challenge_name}' does not exist.")
                return
            challenge_id = challenge[0]

            # Record participation
            cursor.execute("""
                INSERT INTO participation (user_id, challenge_id, score) 
                VALUES (?, ?, ?)
            """, (user_id, challenge_id, score))

            conn.commit()
            print(f"Participation recorded: {username} in '{challenge_name}' with score {score}.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def get_leaderboard(self, challenge_name):
        """
        Retrieves and prints the leaderboard for a specific challenge, sorted by score.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Get challenge ID
            cursor.execute("SELECT challenge_id FROM challenges WHERE name = ?", (challenge_name,))
            challenge = cursor.fetchone()
            if not challenge:
                print(f"Error: Challenge '{challenge_name}' does not exist.")
                return
            challenge_id = challenge[0]

            # Get leaderboard data
            cursor.execute("""
                SELECT u.username, p.score
                FROM participation p
                JOIN users u ON p.user_id = u.user_id
                WHERE p.challenge_id = ?
                ORDER BY p.score DESC
            """, (challenge_id,))
            leaderboard = cursor.fetchall()

            print(f"Leaderboard for '{challenge_name}':")
            for rank, (username, score) in enumerate(leaderboard, start=1):
                print(f"{rank}. {username} - {score} points")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()


# Example usage of the LeaderboardSystem class
if __name__ == "__main__":
    system = LeaderboardSystem()

    # Adding users
    system.add_user("Alice")
    system.add_user("Bob")

    # Adding a challenge
    system.add_challenge(
        name="Challenge 1",
        description="Complete the coding task.",
        start_date="2023-10-01",
        end_date="2023-10-10"
    )

    # Recording participation
    system.record_participation("Alice", "Challenge 1", 95)
    system.record_participation("Bob", "Challenge 1", 85)

    # Retrieving leaderboard
    system.get_leaderboard("Challenge 1")
```
