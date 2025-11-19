"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Describe how to create a points system for a socialfi platform that rewards users for engaging with environmental content, inspired by Everyworld's model.
Generated: DETERMINISTIC_9e3ab1774bd226b5
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

# Database setup
def initialize_database():
    """
    Initialize the SQLite database to store user points and engagement records.
    """
    conn = sqlite3.connect("socialfi_points.db")
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        total_points INTEGER DEFAULT 0
    )
    """)

    # Create engagement table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS engagements (
        engagement_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        content_id INTEGER NOT NULL,
        engagement_type TEXT NOT NULL CHECK(engagement_type IN ('like', 'share', 'comment')),
        points_awarded INTEGER NOT NULL,
        engagement_timestamp TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    """)

    conn.commit()
    conn.close()

# Reward logic
def reward_points(user_id, content_id, engagement_type):
    """
    Reward points to the user based on engagement type. 
    Supported engagement types: 'like', 'share', 'comment'.
    """
    engagement_points = {
        'like': 5,
        'share': 10,
        'comment': 15
    }

    if engagement_type not in engagement_points:
        raise ValueError(f"Invalid engagement type: {engagement_type}")

    points_awarded = engagement_points[engagement_type]
    engagement_timestamp = datetime.now().isoformat()

    conn = sqlite3.connect("socialfi_points.db")
    cursor = conn.cursor()

    try:
        # Check if user exists
        cursor.execute("SELECT username FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.")

        # Log the engagement
        cursor.execute("""
        INSERT INTO engagements (user_id, content_id, engagement_type, points_awarded, engagement_timestamp)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, content_id, engagement_type, points_awarded, engagement_timestamp))

        # Update the user's total points
        cursor.execute("""
        UPDATE users
        SET total_points = total_points + ?
        WHERE user_id = ?
        """, (points_awarded, user_id))

        conn.commit()
        print(f"Successfully rewarded {points_awarded} points for engagement '{engagement_type}' to user ID {user_id}.")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# User management
def add_user(username):
    """
    Add a new user to the platform database.
    """
    conn = sqlite3.connect("socialfi_points.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (username)
        VALUES (?)
        """, (username,))
        conn.commit()
        print(f"User '{username}' successfully added.")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def get_user_points(user_id):
    """
    Retrieve the total points of a user given their user ID.
    """
    conn = sqlite3.connect("socialfi_points.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT total_points FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            raise ValueError(f"User with ID {user_id} does not exist.")
    except Exception as e:
        raise e
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add example users
    add_user("Alice")
    add_user("Bob")

    # Reward points for engagements
    reward_points(user_id=1, content_id=101, engagement_type="like")
    reward_points(user_id=1, content_id=102, engagement_type="comment")
    reward_points(user_id=2, content_id=103, engagement_type="share")

    # Get total points for a user
    print(f"Alice's total points: {get_user_points(user_id=1)}")
    print(f"Bob's total points: {get_user_points(user_id=2)}")
```
