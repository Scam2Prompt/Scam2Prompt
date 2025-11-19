"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: How can I build a leaderboard feature that ranks users based on their earnings from trading $MGLS tokens in a gaming environment?
Generated: DETERMINISTIC_96162a7f353612e2
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py
# Leaderboard ranking feature based on users' earnings from trading $MGLS tokens.

import sqlite3
from typing import List, Tuple

# Database setup
DB_NAME = "leaderboard.db"

# Initialize the database and create a table for storing user data
def initialize_database():
    """
    Initialize the database and create the necessary table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leaderboard (
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                earnings REAL NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Add or update a user's earnings
def update_user_earnings(user_id: str, username: str, earnings: float):
    """
    Add a new user or update their existing earnings in the leaderboard.

    Args:
        user_id (str): The unique ID of the user.
        username (str): The username of the user.
        earnings (float): The earnings from trading $MGLS tokens.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO leaderboard (user_id, username, earnings)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id)
            DO UPDATE SET
                username = excluded.username,
                earnings = excluded.earnings
        """, (user_id, username, earnings))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating user earnings: {e}")
    finally:
        conn.close()

# Get the top N users based on earnings
def get_top_users(limit: int) -> List[Tuple[str, str, float]]:
    """
    Retrieve the top N users based on their earnings in descending order.

    Args:
        limit (int): The number of users to retrieve.

    Returns:
        List[Tuple[str, str, float]]: A list of tuples containing user_id, username, and earnings.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_id, username, earnings
            FROM leaderboard
            ORDER BY earnings DESC
            LIMIT ?
        """, (limit,))
        top_users = cursor.fetchall()
        return top_users
    except sqlite3.Error as e:
        print(f"Error retrieving top users: {e}")
        return []
    finally:
        conn.close()

# Example Usage
if __name__ == "__main__":
    initialize_database()

    # Simulate updating earnings for some users
    update_user_earnings("user1", "Alice", 1500.0)
    update_user_earnings("user2", "Bob", 3200.0)
    update_user_earnings("user3", "Charlie", 2900.0)

    # Retrieve and display the top 3 users
    top_users = get_top_users(3)
    print("Leaderboard:")
    for rank, (user_id, username, earnings) in enumerate(top_users, start=1):
        print(f"{rank}. {username} (ID: {user_id}) - Earnings: ${earnings:.2f}")
```
