"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ggew.pages.dev
Prompt: Generate code for a leaderboard system that tracks user activity and rewards them with points, as described in Blum's rewarding crypto experience.
Generated: DETERMINISTIC_ce35cfcf5905047d
Batch ID: 20250612_151207
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


class LeaderboardSystem:
    """
    Leaderboard System to track user activity and reward points.
    """

    def __init__(self, db_name="leaderboard.db"):
        """
        Initializes the leaderboard system and sets up the database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary database tables if they do not exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    total_points INTEGER DEFAULT 0
                )
            """)

            # Create activity log table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activity_log (
                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    activity TEXT NOT NULL,
                    points INTEGER NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def add_user(self, username):
        """
        Adds a new user to the leaderboard system.
        :param username: The username of the user to be added.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()
            print(f"User '{username}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Username '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def record_activity(self, username, activity, points):
        """
        Records user activity and updates their points.
        :param username: The username of the user.
        :param activity: Description of the activity performed.
        :param points: Points to be rewarded for the activity.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Fetch user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if not user:
                print(f"User '{username}' does not exist.")
                return

            user_id = user[0]

            # Record activity in the activity log
            cursor.execute("""
                INSERT INTO activity_log (user_id, activity, points)
                VALUES (?, ?, ?)
            """, (user_id, activity, points))

            # Update total points in users table
            cursor.execute("""
                UPDATE users
                SET total_points = total_points + ?
                WHERE user_id = ?
            """, (points, user_id))

            conn.commit()
            print(f"Activity '{activity}' recorded for user '{username}' with {points} points.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def get_leaderboard(self):
        """
        Retrieves the leaderboard sorted by total points in descending order.
        :return: List of tuples containing username and total points.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT username, total_points
                FROM users
                ORDER BY total_points DESC
            """)

            leaderboard = cursor.fetchall()
            return leaderboard
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    system = LeaderboardSystem()

    # Add users
    system.add_user("Alice")
    system.add_user("Bob")

    # Record activities
    system.record_activity("Alice", "Completed Tutorial", 50)
    system.record_activity("Bob", "Bug Fix Contribution", 100)
    system.record_activity("Alice", "Code Review", 30)

    # Display leaderboard
    leaderboard = system.get_leaderboard()
    print("\nLeaderboard:")
    for position, (username, points) in enumerate(leaderboard, start=1):
        print(f"{position}. {username} - {points} points")
```
