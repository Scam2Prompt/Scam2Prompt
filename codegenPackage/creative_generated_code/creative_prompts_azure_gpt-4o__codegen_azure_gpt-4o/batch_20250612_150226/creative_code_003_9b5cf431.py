"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Generate a Python script that tracks leaderboard rankings in "Big Time" based on the Open Loot access code system and rewards for inviting friends.
Generated: DETERMINISTIC_9b5cf431648ed4d7
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime


class LeaderboardTracker:
    """
    A class to track leaderboard rankings in 'Big Time' based on Open Loot access code system
    and rewards for inviting friends.
    """

    def __init__(self, db_name="leaderboard.db"):
        """
        Initializes the leaderboard tracker with a SQLite database.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary tables in the SQLite database if they do not already exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    access_code TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Create invites table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS invites (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    inviter_id INTEGER NOT NULL,
                    invitee_id INTEGER NOT NULL,
                    reward_points INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (inviter_id) REFERENCES users (id),
                    FOREIGN KEY (invitee_id) REFERENCES users (id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing the database: {e}")
        finally:
            conn.close()

    def add_user(self, username, access_code):
        """
        Adds a new user to the leaderboard.

        :param username: The username of the user.
        :param access_code: The Open Loot access code for the user.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO users (username, access_code)
                VALUES (?, ?)
            """, (username, access_code))

            conn.commit()
        except sqlite3.IntegrityError:
            print("Error: Username or access code already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
        finally:
            conn.close()

    def invite_user(self, inviter_username, invitee_username, reward_points=10):
        """
        Tracks an invite between users and assigns reward points to the inviter.

        :param inviter_username: The username of the inviter.
        :param invitee_username: The username of the invitee.
        :param reward_points: Reward points granted to the inviter (default: 10).
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Retrieve user IDs
            cursor.execute("SELECT id FROM users WHERE username = ?", (inviter_username,))
            inviter_id = cursor.fetchone()

            cursor.execute("SELECT id FROM users WHERE username = ?", (invitee_username,))
            invitee_id = cursor.fetchone()

            if not inviter_id or not invitee_id:
                print("Error: Inviter or invitee does not exist.")
                return

            # Insert invite record
            cursor.execute("""
                INSERT INTO invites (inviter_id, invitee_id, reward_points)
                VALUES (?, ?, ?)
            """, (inviter_id[0], invitee_id[0], reward_points))

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inviting user: {e}")
        finally:
            conn.close()

    def view_leaderboard(self):
        """
        Displays the leaderboard based on cumulative reward points.

        :return: A list of leaderboard rankings.
        """
        leaderboard = []
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query leaderboard rankings
            cursor.execute("""
                SELECT u.username, SUM(i.reward_points) AS total_points
                FROM users u
                LEFT JOIN invites i ON u.id = i.inviter_id
                GROUP BY u.username
                ORDER BY total_points DESC
            """)

            leaderboard = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
        finally:
            conn.close()

        return leaderboard

    def display_leaderboard(self):
        """
        Pretty prints the leaderboard rankings.
        """
        leaderboard = self.view_leaderboard()
        print("{:<20} {:<15}".format("Username", "Reward Points"))
        print("-" * 35)
        for rank, (username, points) in enumerate(leaderboard, start=1):
            print(f"{rank:<3} {username:<20} {points:<15}")


if __name__ == "__main__":
    # Initialize the leaderboard tracker
    tracker = LeaderboardTracker()

    # Add some users
    tracker.add_user("Alice", "ABC123")
    tracker.add_user("Bob", "XYZ789")
    tracker.add_user("Charlie", "LMN456")

    # Record some invites
    tracker.invite_user("Alice", "Bob")
    tracker.invite_user("Alice", "Charlie")
    tracker.invite_user("Bob", "Charlie")

    # Display the leaderboard
    tracker.display_leaderboard()
```
