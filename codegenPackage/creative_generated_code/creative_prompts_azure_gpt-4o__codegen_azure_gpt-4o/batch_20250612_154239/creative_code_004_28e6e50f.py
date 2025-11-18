"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Write a script to track user activity and calculate rewards in a loyalty program for an online casino, including cashback on losses as described in BaxBet's features.
Generated: DETERMINISTIC_28e6e50fec360351
Batch ID: 20250612_154239
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
DB_FILE = 'casino_loyalty.db'

# Initialize database and table
def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            total_spent REAL DEFAULT 0,
            total_wins REAL DEFAULT 0,
            total_losses REAL DEFAULT 0,
            cashback_earned REAL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

# Function to add user activity
def record_activity(user_id, username, amount_spent, amount_won):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Check if user exists, if not, create a new entry
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("""
            INSERT INTO users (user_id, username, total_spent, total_wins, total_losses, cashback_earned)
            VALUES (?, ?, 0, 0, 0, 0)
        """, (user_id, username))
        conn.commit()

    # Calculate current loss and cashback (e.g., 10% cashback on losses)
    loss = max(amount_spent - amount_won, 0)
    cashback = loss * 0.10

    # Update user stats
    cursor.execute("""
        UPDATE users
        SET total_spent = total_spent + ?,
            total_wins = total_wins + ?,
            total_losses = total_losses + ?,
            cashback_earned = cashback_earned + ?
        WHERE user_id = ?
    """, (amount_spent, amount_won, loss, cashback, user_id))

    conn.commit()
    conn.close()

# Function to retrieve user stats
def get_user_stats(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    if user:
        return {
            'user_id': user[0],
            'username': user[1],
            'total_spent': user[2],
            'total_wins': user[3],
            'total_losses': user[4],
            'cashback_earned': user[5]
        }
    else:
        return None

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Simulated user activity
    record_activity(user_id=1, username="JohnDoe", amount_spent=100, amount_won=50)
    record_activity(user_id=1, username="JohnDoe", amount_spent=200, amount_won=150)

    # Retrieve and display user stats
    user_stats = get_user_stats(user_id=1)
    if user_stats:
        print(f"User Stats for {user_stats['username']}:")
        print(f"  Total Spent: ${user_stats['total_spent']:.2f}")
        print(f"  Total Wins: ${user_stats['total_wins']:.2f}")
        print(f"  Total Losses: ${user_stats['total_losses']:.2f}")
        print(f"  Cashback Earned: ${user_stats['cashback_earned']:.2f}")
    else:
        print("User not found.")
```
