"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: How can I build a leaderboard for trade swaps that mimics the functionality of Deeptrade?
Generated: DETERMINISTIC_78729ca26bc15699
Batch ID: 20250612_155643
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

# Constants
DATABASE_NAME = "leaderboard.db"

# Initialize the database
def initialize_database():
    """
    Creates the leaderboard table if it doesn't exist.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            swaps INTEGER NOT NULL DEFAULT 0,
            last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

# Add or update a user in the leaderboard
def update_leaderboard(username, swaps):
    """
    Adds a new user to the leaderboard or updates their swap count.
    :param username: The username of the trader.
    :param swaps: The number of swaps to add to the user's total.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Check if the user already exists
        cursor.execute("SELECT swaps FROM leaderboard WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result:
            # Update existing user's swap count
            new_swaps = result[0] + swaps
            cursor.execute("""
                UPDATE leaderboard
                SET swaps = ?, last_updated = ?
                WHERE username = ?
            """, (new_swaps, datetime.now(), username))
        else:
            # Insert new user into the leaderboard
            cursor.execute("""
                INSERT INTO leaderboard (username, swaps, last_updated)
                VALUES (?, ?, ?)
            """, (username, swaps, datetime.now()))

        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        connection.close()

# Retrieve the top N users from the leaderboard
def get_top_users(limit=10):
    """
    Retrieves the top N users from the leaderboard based on swap count.
    :param limit: The number of top users to retrieve.
    :return: A list of dictionaries containing user data.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT username, swaps, last_updated
            FROM leaderboard
            ORDER BY swaps DESC, last_updated ASC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        top_users = [
            {"username": row[0], "swaps": row[1], "last_updated": row[2]}
            for row in rows
        ]
        return top_users
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    finally:
        connection.close()

# Main function for demonstration
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    update_leaderboard("trader1", 5)
    update_leaderboard("trader2", 10)
    update_leaderboard("trader1", 3)  # Update existing user

    # Get top users
    top_users = get_top_users(limit=5)
    print("Top Users:")
    for user in top_users:
        print(user)
```

This code creates a SQLite-based leaderboard for trade swaps, allowing you to add/update users and retrieve the top performers. It includes error handling, adheres to best practices, and is production-ready.
