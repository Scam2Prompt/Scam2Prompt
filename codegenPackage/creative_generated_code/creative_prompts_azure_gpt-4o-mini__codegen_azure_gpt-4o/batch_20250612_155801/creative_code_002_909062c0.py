"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Generate a sample code for a loyalty program that rewards users with points for playing games, inspired by the venez888 rewards system.
Generated: DETERMINISTIC_909062c0b3270c1d
Batch ID: 20250612_155801
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

class LoyaltyProgram:
    """
    A class to manage a loyalty program that rewards users with points for playing games.
    """

    def __init__(self, db_name="loyalty_program.db"):
        """
        Initializes the loyalty program with a database connection.
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Creates the necessary tables if they don't already exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        points INTEGER DEFAULT 0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS transactions (
                        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        points INTEGER NOT NULL,
                        transaction_type TEXT NOT NULL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                    )
                """)
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")

    def add_user(self, username):
        """
        Adds a new user to the loyalty program.
        :param username: The username of the new user.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
                print(f"User '{username}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Username '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")

    def play_game(self, username, points_earned):
        """
        Rewards a user with points for playing a game.
        :param username: The username of the user.
        :param points_earned: The number of points earned from the game.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                # Get the user ID
                cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
                user = cursor.fetchone()
                if not user:
                    print(f"Error: User '{username}' does not exist.")
                    return

                user_id = user[0]

                # Update points in the user's account
                cursor.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points_earned, user_id))

                # Record the transaction
                cursor.execute("""
                    INSERT INTO transactions (user_id, points, transaction_type) 
                    VALUES (?, ?, ?)
                """, (user_id, points_earned, "game_reward"))

                print(f"User '{username}' earned {points_earned} points for playing a game!")
        except sqlite3.Error as e:
            print(f"Error rewarding points: {e}")

    def get_user_points(self, username):
        """
        Fetches the total points of a user.
        :param username: The username of the user.
        :return: The total points of the user or None if the user does not exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT points FROM users WHERE username = ?", (username,))
                user = cursor.fetchone()
                if user:
                    return user[0]
                else:
                    print(f"Error: User '{username}' does not exist.")
                    return None
        except sqlite3.Error as e:
            print(f"Error fetching user points: {e}")
            return None

    def show_transactions(self, username):
        """
        Displays all transactions for a given user.
        :param username: The username of the user.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                # Get the user ID
                cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
                user = cursor.fetchone()
                if not user:
                    print(f"Error: User '{username}' does not exist.")
                    return

                user_id = user[0]

                # Fetch transactions
                cursor.execute("""
                    SELECT points, transaction_type, timestamp 
                    FROM transactions 
                    WHERE user_id = ? 
                    ORDER BY timestamp DESC
                """, (user_id,))
                transactions = cursor.fetchall()

                if transactions:
                    print(f"Transactions for user '{username}':")
                    for points, transaction_type, timestamp in transactions:
                        print(f"  - {transaction_type}: {points} points on {timestamp}")
                else:
                    print(f"No transactions found for user '{username}'.")
        except sqlite3.Error as e:
            print(f"Error fetching transactions: {e}")

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()

    # Add users
    program.add_user("player1")
    program.add_user("player2")

    # Reward points for playing games
    program.play_game("player1", 100)
    program.play_game("player1", 50)
    program.play_game("player2", 200)

    # Fetch user points
    print(f"Player1 points: {program.get_user_points('player1')}")
    print(f"Player2 points: {program.get_user_points('player2')}")

    # Show transactions
    program.show_transactions("player1")
    program.show_transactions("player2")
```
