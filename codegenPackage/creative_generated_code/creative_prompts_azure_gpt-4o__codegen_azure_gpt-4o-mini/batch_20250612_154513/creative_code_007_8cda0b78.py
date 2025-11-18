"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Develop a function to calculate and display the leaderboard for Bet88 users based on their betting performance and winnings.
Generated: DETERMINISTIC_8cda0b7868a5de93
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

# Database configuration
DATABASE_NAME = 'bet88_users.db'

def initialize_database():
    """Initialize the SQLite database and create the necessary table if it doesn't exist."""
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    total_bets INTEGER DEFAULT 0,
                    total_winnings REAL DEFAULT 0.0
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def add_user(user_id: int, username: str):
    """Add a new user to the database."""
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding user: {e}")

def update_user_betting_performance(user_id: int, bet_amount: int, winnings: float):
    """Update the user's betting performance."""
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users 
                SET total_bets = total_bets + ?, 
                    total_winnings = total_winnings + ? 
                WHERE user_id = ?
            ''', (bet_amount, winnings, user_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating user performance: {e}")

def get_leaderboard() -> List[Tuple[str, int, float]]:
    """Retrieve the leaderboard sorted by total winnings."""
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, total_bets, total_winnings 
                FROM users 
                ORDER BY total_winnings DESC
            ''')
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving leaderboard: {e}")
        return []

def display_leaderboard():
    """Display the leaderboard to the console."""
    leaderboard = get_leaderboard()
    if not leaderboard:
        print("No users found in the leaderboard.")
        return
    
    print("Leaderboard:")
    print("{:<20} {:<15} {:<15}".format("Username", "Total Bets", "Total Winnings"))
    print("-" * 50)
    for username, total_bets, total_winnings in leaderboard:
        print("{:<20} {:<15} ${:<14.2f}".format(username, total_bets, total_winnings))

# Initialize the database (should be called once in the application)
initialize_database()

# Example usage:
# add_user(1, 'Alice')
# update_user_betting_performance(1, 5, 150.00)
# add_user(2, 'Bob')
# update_user_betting_performance(2, 3, 200.00)
# display_leaderboard()
```
