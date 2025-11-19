"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Describe how to create a points system for a socialfi platform that rewards users for engaging with environmental content, inspired by Everyworld's model.
Generated: DETERMINISTIC_9e3ab1774bd226b5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

class SocialFiPointsSystem:
    """
    A class to manage a points system for a SocialFi platform that rewards users
    for engaging with environmental content.
    """

    def __init__(self, db_name="socialfi.db"):
        """
        Initialize the points system and connect to the database.
        If the database does not exist, it will be created.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary tables in the database if they do not already exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    points INTEGER DEFAULT 0
                )
            """)

            # Create engagement table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS engagements (
                    engagement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    content_id INTEGER NOT NULL,
                    engagement_type TEXT NOT NULL,
                    points_awarded INTEGER NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_user(self, username):
        """
        Add a new user to the platform.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()
            print(f"User '{username}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Username '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
        finally:
            conn.close()

    def award_points(self, username, content_id, engagement_type, points):
        """
        Award points to a user for engaging with content.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Get user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                print(f"Error: User '{username}' not found.")
                return

            user_id = user[0]

            # Update user's points
            cursor.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, user_id))

            # Log engagement
            cursor.execute("""
                INSERT INTO engagements (user_id, content_id, engagement_type, points_awarded)
                VALUES (?, ?, ?, ?)
            """, (user_id, content_id, engagement_type, points))

            conn.commit()
            print(f"{points} points awarded to '{username}' for {engagement_type} on content ID {content_id}.")
        except sqlite3.Error as e:
            print(f"Error awarding points: {e}")
        finally:
            conn.close()

    def get_user_points(self, username):
        """
        Retrieve the total points of a user.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("SELECT points FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                print(f"Error: User '{username}' not found.")
                return None

            return user[0]
        except sqlite3.Error as e:
            print(f"Error retrieving user points: {e}")
            return None
        finally:
            conn.close()

    def get_engagement_history(self, username):
        """
        Retrieve the engagement history of a user.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Get user ID
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                print(f"Error: User '{username}' not found.")
                return None

            user_id = user[0]

            # Retrieve engagement history
            cursor.execute("""
                SELECT content_id, engagement_type, points_awarded, timestamp
                FROM engagements
                WHERE user_id = ?
                ORDER BY timestamp DESC
            """, (user_id,))
            history = cursor.fetchall()

            return history
        except sqlite3.Error as e:
            print(f"Error retrieving engagement history: {e}")
            return None
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    # Initialize the points system
    points_system = SocialFiPointsSystem()

    # Add users
    points_system.add_user("alice")
    points_system.add_user("bob")

    # Award points for engagements
    points_system.award_points("alice", content_id=101, engagement_type="like", points=10)
    points_system.award_points("bob", content_id=102, engagement_type="comment", points=20)

    # Retrieve user points
    print("Alice's points:", points_system.get_user_points("alice"))
    print("Bob's points:", points_system.get_user_points("bob"))

    # Retrieve engagement history
    print("Alice's engagement history:", points_system.get_engagement_history("alice"))
    print("Bob's engagement history:", points_system.get_engagement_history("bob"))
```
