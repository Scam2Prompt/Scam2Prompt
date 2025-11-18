"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Develop a leaderboard system for tracking user points in the XSwap ecosystem, referencing the features mentioned on the webpage.
Generated: DETERMINISTIC_8bb68121877dbb7e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: leaderboard_system.py

import sqlite3
from typing import List, Dict, Optional

# Database setup
DB_NAME = "xswap_leaderboard.db"

def initialize_database():
    """
    Initialize the database by creating the necessary table for the leaderboard.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create the leaderboard table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            points INTEGER NOT NULL DEFAULT 0
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_or_update_user(user_id: str, username: str, points: int):
    """
    Add a new user to the leaderboard or update their points if they already exist.

    :param user_id: Unique identifier for the user
    :param username: Username of the user
    :param points: Points to add or set for the user
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if the user already exists
        cursor.execute("SELECT user_id FROM leaderboard WHERE user_id = ?", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Update points for existing user
            cursor.execute("""
                UPDATE leaderboard
                SET points = points + ?, username = ?
                WHERE user_id = ?
            """, (points, username, user_id))
        else:
            # Insert new user
            cursor.execute("""
                INSERT INTO leaderboard (user_id, username, points)
                VALUES (?, ?, ?)
            """, (user_id, username, points))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding or updating user: {e}")
    finally:
        conn.close()

def get_top_users(limit: int = 10) -> List[Dict[str, Optional[str]]]:
    """
    Retrieve the top users from the leaderboard sorted by points in descending order.

    :param limit: Number of top users to retrieve (default is 10)
    :return: List of dictionaries containing user data
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT user_id, username, points
            FROM leaderboard
            ORDER BY points DESC
            LIMIT ?
        """, (limit,))
        
        rows = cursor.fetchall()

        # Transform rows into a list of dictionaries
        top_users = [
            {"user_id": row[0], "username": row[1], "points": row[2]}
            for row in rows
        ]

        return top_users
    except sqlite3.Error as e:
        print(f"Error retrieving top users: {e}")
        return []
    finally:
        conn.close()

def delete_user(user_id: str):
    """
    Remove a user from the leaderboard.

    :param user_id: Unique identifier for the user to delete
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM leaderboard WHERE user_id = ?", (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")
    finally:
        conn.close()

# Initialize the database when the script is run
if __name__ == "__main__":
    initialize_database()
```

This script provides a leaderboard system with essential features such as adding/updating users, retrieving top users, and deleting a user. It uses SQLite for persistence and includes proper error handling and documentation.
