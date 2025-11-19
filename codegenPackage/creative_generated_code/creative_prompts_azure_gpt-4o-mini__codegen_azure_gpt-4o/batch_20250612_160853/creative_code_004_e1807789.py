"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Illustrate how to implement a rewards system for users in the Pudgy Penguins virtual home using a specific programming language.
Generated: DETERMINISTIC_e1807789c583e1ac
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Rewards System for Pudgy Penguins Virtual Home
- This script implements a rewards system where users can earn points based on their activity.
- Points can be redeemed for virtual items.
- Includes error handling and follows Python best practices.
"""

import sqlite3  # Using SQLite for simplicity
from datetime import datetime

# Database Setup
DB_FILE = "pudgy_penguins_rewards.db"

def initialize_database():
    """Initialize the database and create tables if they don't exist."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                points INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Create rewards history table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rewards_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                points INTEGER NOT NULL,
                activity TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        conn.close()

# User Management
def add_user(username):
    """Add a new user to the system."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Rewards System
def add_points(user_id, points, activity):
    """Add points to a user for a specific activity."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Update user points
        cursor.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, user_id))
        # Log activity in rewards history
        cursor.execute("""
            INSERT INTO rewards_history (user_id, points, activity)
            VALUES (?, ?, ?)
        """, (user_id, points, activity))
        conn.commit()
        print(f"Added {points} points to User ID {user_id} for activity: {activity}.")
    except sqlite3.Error as e:
        print(f"Error updating points: {e}")
    finally:
        conn.close()

def redeem_points(user_id, points):
    """Redeem points for a user."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Check if user has enough points
        cursor.execute("SELECT points FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result and result[0] >= points:
            # Deduct points
            cursor.execute("UPDATE users SET points = points - ? WHERE user_id = ?", (points, user_id))
            conn.commit()
            print(f"Redeemed {points} points for User ID {user_id}.")
        else:
            print(f"Error: Insufficient points for User ID {user_id}.")
    except sqlite3.Error as e:
        print(f"Error during points redemption: {e}")
    finally:
        conn.close()

# Utility Functions
def get_user_points(user_id):
    """Retrieve a user's current points."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            print(f"User ID {user_id} has {result[0]} points.")
            return result[0]
        else:
            print(f"No user found with ID {user_id}.")
            return None
    except sqlite3.Error as e:
        print(f"Error retrieving user points: {e}")
        return None
    finally:
        conn.close()

def view_rewards_history(user_id):
    """View the rewards history for a specific user."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT points, activity, timestamp
            FROM rewards_history
            WHERE user_id = ?
            ORDER BY timestamp DESC
        """, (user_id,))
        results = cursor.fetchall()
        if results:
            print(f"Rewards history for User ID {user_id}:")
            for row in results:
                print(f"Points: {row[0]}, Activity: {row[1]}, Timestamp: {row[2]}")
        else:
            print(f"No rewards history found for User ID {user_id}.")
    except sqlite3.Error as e:
        print(f"Error retrieving rewards history: {e}")
    finally:
        conn.close()

# Main Execution
if __name__ == "__main__":
    initialize_database()  # Ensure the database and tables are set up
    
    # Example usage
    add_user("penguin_lover")
    add_user("snowy_penguin")
    add_points(1, 50, "Completed daily quiz")
    add_points(2, 30, "Logged in for 7 days consecutively")
    redeem_points(1, 20)
    get_user_points(1)
    view_rewards_history(1)
```
