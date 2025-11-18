"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenafinance.vercel.app
Prompt: Create a leaderboard system for tracking weekly challenge participation in the $PLENA Road to TGE campaign using Galxe data.
Generated: DETERMINISTIC_378e0236962561ea
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime, timedelta
from typing import List, Tuple

# Constants for database setup
DATABASE_NAME = 'leaderboard.db'

# Create and initialize the SQLite database for leaderboard
def initialize_database():
    """Initializes the SQLite database and creates the leaderboard table."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        # Create leaderboard table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                participation_count INTEGER NOT NULL DEFAULT 0,
                last_participation DATE NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Add or update user participation
def update_participation(username: str):
    """Updates the participation count for a given user."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        today = datetime.now().date()
        
        # Check if the user already exists
        cursor.execute('SELECT * FROM leaderboard WHERE username = ?', (username,))
        user = cursor.fetchone()
        
        if user:
            # Update existing user participation count and last participation date
            cursor.execute('''
                UPDATE leaderboard
                SET participation_count = participation_count + 1,
                    last_participation = ?
                WHERE username = ?
            ''', (today, username))
        else:
            # Insert new user into leaderboard
            cursor.execute('''
                INSERT INTO leaderboard (username, participation_count, last_participation)
                VALUES (?, 1, ?)
            ''', (username, today))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Failed to update participation for {username}: {e}")
    finally:
        conn.close()

# Retrieve the leaderboard sorted by participation count
def get_leaderboard() -> List[Tuple[str, int]]:
    """Fetches the leaderboard sorted by participation count."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT username, participation_count FROM leaderboard ORDER BY participation_count DESC')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Failed to retrieve leaderboard: {e}")
        return []
    finally:
        conn.close()

# Get the leaderboard for the current week
def get_weekly_leaderboard() -> List[Tuple[str, int]]:
    """Fetches the leaderboard for the current week."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        start_of_week = datetime.now() - timedelta(days=datetime.now().weekday())
        
        cursor.execute('''
            SELECT username, participation_count
            FROM leaderboard
            WHERE last_participation >= ?
            ORDER BY participation_count DESC
        ''', (start_of_week.date(),))
        
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Failed to retrieve weekly leaderboard: {e}")
        return []
    finally:
        conn.close()

if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Example usage
    update_participation('User1')
    update_participation('User2')
    update_participation('User1')  # User1 participates again
    
    # Print overall leaderboard
    print("Overall Leaderboard:")
    for user in get_leaderboard():
        print(f"Username: {user[0]}, Participation Count: {user[1]}")
    
    # Print weekly leaderboard
    print("\nWeekly Leaderboard:")
    for user in get_weekly_leaderboard():
        print(f"Username: {user[0]}, Participation Count: {user[1]}")
```
