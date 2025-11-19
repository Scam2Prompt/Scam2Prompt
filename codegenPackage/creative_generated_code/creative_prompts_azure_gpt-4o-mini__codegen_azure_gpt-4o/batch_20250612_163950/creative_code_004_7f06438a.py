"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoons.web.app
Prompt: Explain how to implement a leaderboard feature for the Kangamoon community, rewarding users based on their participation and $KANG earnings.
Generated: DETERMINISTIC_7f06438a8c293889
Batch ID: 20250612_163950
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = 'kangamoon_leaderboard.db'

def create_database():
    """
    Initialize the SQLite database and create the required tables.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        participation_score INTEGER DEFAULT 0,
        kang_earnings REAL DEFAULT 0
    )
    """)

    # Create leaderboard table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        rank INTEGER NOT NULL,
        last_updated TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    """)

    conn.commit()
    conn.close()

def add_user(username):
    """
    Add a new user to the database.

    :param username: The username of the new user.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    finally:
        conn.close()

def update_user_stats(user_id, participation_score, kang_earnings):
    """
    Update a user's participation score and $KANG earnings.

    :param user_id: The ID of the user whose stats are being updated.
    :param participation_score: The new participation score to add.
    :param kang_earnings: The new $KANG earnings to add.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users 
    SET participation_score = participation_score + ?, 
        kang_earnings = kang_earnings + ?
    WHERE user_id = ?
    """, (participation_score, kang_earnings, user_id))

    conn.commit()
    conn.close()

def generate_leaderboard():
    """
    Generate the leaderboard based on user stats.
    Ranks users based on participation score and $KANG earnings.

    :return: A list of leaderboard entries.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Retrieve users sorted by participation score and kang_earnings
    cursor.execute("""
    SELECT user_id, username, participation_score, kang_earnings
    FROM users
    ORDER BY participation_score DESC, kang_earnings DESC
    """)

    users = cursor.fetchall()

    # Update leaderboard table with ranks
    cursor.execute("DELETE FROM leaderboard")  # Clear previous leaderboard data
    for rank, user in enumerate(users, start=1):
        cursor.execute("""
        INSERT INTO leaderboard (user_id, rank, last_updated)
        VALUES (?, ?, ?)
        """, (user[0], rank, datetime.now()))

    conn.commit()

    # Fetch updated leaderboard for display
    cursor.execute("""
    SELECT l.rank, u.username, u.participation_score, u.kang_earnings, l.last_updated
    FROM leaderboard l
    JOIN users u ON l.user_id = u.user_id
    ORDER BY l.rank
    """)

    leaderboard = cursor.fetchall()
    conn.close()

    return leaderboard

def display_leaderboard():
    """
    Display the leaderboard in a readable format.
    """
    leaderboard = generate_leaderboard()

    print("Leaderboard:")
    print(f"{'Rank':<5} {'Username':<15} {'Participation Score':<20} {'$KANG Earnings':<15} {'Last Updated':<25}")
    print("-" * 80)
    for entry in leaderboard:
        rank, username, participation_score, kang_earnings, last_updated = entry
        print(f"{rank:<5} {username:<15} {participation_score:<20} {kang_earnings:<15.2f} {last_updated:<25}")

# Main program logic
if __name__ == "__main__":
    create_database()

    # Add sample users
    add_user("Alice")
    add_user("Bob")
    add_user("Charlie")

    # Update user stats
    update_user_stats(1, participation_score=100, kang_earnings=50.5)
    update_user_stats(2, participation_score=200, kang_earnings=70.2)
    update_user_stats(3, participation_score=150, kang_earnings=60.0)

    # Display leaderboard
    display_leaderboard()
```
