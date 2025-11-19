"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bac-games.vercel.app
Prompt: Create a function that connects users to the BAC gaming clubs and tracks their rewards in a Play-2-Earn model.
Generated: DETERMINISTIC_744167cf764f2121
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class GamingClub:
    """
    A class to represent a BAC gaming club and track users' rewards in a Play-2-Earn model.
    """

    def __init__(self, db_file):
        """Initialize the GamingClub with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a SQLite database connection."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for users and rewards if they do not exist."""
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            total_rewards INTEGER DEFAULT 0
        );"""

        create_rewards_table = """
        CREATE TABLE IF NOT EXISTS rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(create_users_table)
            cursor.execute(create_rewards_table)
            self.connection.commit()
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_user(self, username):
        """Add a new user to the gaming club."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            self.connection.commit()
            print(f"User '{username}' added successfully.")
        except Error as e:
            print(f"Error adding user: {e}")

    def track_reward(self, username, amount):
        """Track rewards for a specified user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if user:
                user_id = user[0]
                cursor.execute("INSERT INTO rewards (user_id, amount) VALUES (?, ?)", (user_id, amount))
                cursor.execute("UPDATE users SET total_rewards = total_rewards + ? WHERE id = ?", (amount, user_id))
                self.connection.commit()
                print(f"Reward of {amount} tracked for user '{username}'.")
            else:
                print(f"User '{username}' not found.")
        except Error as e:
            print(f"Error tracking reward: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    gaming_club = GamingClub("gaming_club.db")
    gaming_club.add_user("player1")
    gaming_club.track_reward("player1", 100)
    gaming_club.close_connection()
```
