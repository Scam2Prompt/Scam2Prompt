"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3ai.web.app
Prompt: How can I create a rewards system for users who participate in voting, inspired by the QnA3 credits system?
Generated: DETERMINISTIC_a6a1e3893e836975
Batch ID: 20250612_161224
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

class RewardsSystem:
    """
    A rewards system for users who participate in voting.
    Users earn points for each vote they cast, which can later be redeemed for rewards.
    """

    def __init__(self, db_name="rewards_system.db"):
        """
        Initializes the rewards system and sets up the database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the database by creating necessary tables if they do not exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            # Create Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    points INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Create Votes table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Votes (
                    vote_id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES Users (user_id)
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Database setup error: {e}")
        finally:
            connection.close()

    def add_user(self, username):
        """
        Adds a new user to the system.
        :param username: The username of the new user.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Users (username) VALUES (?)", (username,))
            connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: Username '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

    def cast_vote(self, username):
        """
        Records a vote cast by a user and rewards them with points.
        :param username: The username of the user casting the vote.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Verify the user exists
            cursor.execute("SELECT user_id, points FROM Users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                print(f"Error: User '{username}' does not exist.")
                return

            user_id, current_points = user

            # Insert a new vote record
            cursor.execute("INSERT INTO Votes (user_id) VALUES (?)", (user_id,))
            
            # Update the user's points
            updated_points = current_points + 10  # Award 10 points per vote
            cursor.execute("UPDATE Users SET points = ? WHERE user_id = ?", (updated_points, user_id))
            
            connection.commit()
            print(f"Vote recorded! '{username}' now has {updated_points} points.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

    def get_user_points(self, username):
        """
        Retrieves the number of points a user has earned.
        :param username: The username of the user.
        :return: The number of points the user has, or None if the user does not exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT points FROM Users WHERE username = ?", (username,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                print(f"Error: User '{username}' does not exist.")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            connection.close()

    def redeem_points(self, username, points_to_redeem):
        """
        Allows a user to redeem their points for rewards.
        :param username: The username of the user redeeming points.
        :param points_to_redeem: The number of points to redeem.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Verify the user exists and has enough points
            cursor.execute("SELECT user_id, points FROM Users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                print(f"Error: User '{username}' does not exist.")
                return
            
            user_id, current_points = user
            if current_points < points_to_redeem:
                print(f"Error: Insufficient points. '{username}' only has {current_points} points.")
                return
            
            # Deduct the points
            updated_points = current_points - points_to_redeem
            cursor.execute("UPDATE Users SET points = ? WHERE user_id = ?", (updated_points, user_id))
            connection.commit()
            print(f"'{username}' redeemed {points_to_redeem} points. Remaining points: {updated_points}.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Adding users
    rewards_system.add_user("Alice")
    rewards_system.add_user("Bob")

    # Casting votes
    rewards_system.cast_vote("Alice")
    rewards_system.cast_vote("Bob")
    rewards_system.cast_vote("Alice")

    # Checking user points
    print("Alice's points:", rewards_system.get_user_points("Alice"))
    print("Bob's points:", rewards_system.get_user_points("Bob"))

    # Redeeming points
    rewards_system.redeem_points("Alice", 15)
    print("Alice's points after redemption:", rewards_system.get_user_points("Alice"))
```
