"""
Generated Code Metadata:
========================
Original URL: https://ggew.pages.dev
Prompt: "Design a rewarding point system for a cryptocurrency trading platform, incorporating leaderboards and social interactions, inspired by Blum's features."
Generated: DETERMINISTIC_12bd8a354ba6bcbf
Batch ID: 20250622_204646
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
from typing import List, Dict

# Constants
DATABASE_FILE = "trading_platform.db"
POINTS_PER_TRADE = 10
BONUS_POINTS_FOR_TOP_TRADER = 50

# Database setup
def initialize_database():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        points INTEGER DEFAULT 0,
        last_trade TIMESTAMP
    )
    """)
    
    # Create trades table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        trade_amount REAL NOT NULL,
        trade_time TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    conn.commit()
    conn.close()

# User management
def add_user(username: str):
    """Add a new user to the platform."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    finally:
        conn.close()

# Trade management
def record_trade(username: str, trade_amount: float):
    """Record a trade and update user points."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Get user ID
    cursor.execute("SELECT id, points FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        print(f"Error: User '{username}' not found.")
        conn.close()
        return
    
    user_id, current_points = user
    
    # Record trade
    trade_time = datetime.now()
    cursor.execute("""
    INSERT INTO trades (user_id, trade_amount, trade_time)
    VALUES (?, ?, ?)
    """, (user_id, trade_amount, trade_time))
    
    # Update points
    new_points = current_points + POINTS_PER_TRADE
    cursor.execute("""
    UPDATE users
    SET points = ?, last_trade = ?
    WHERE id = ?
    """, (new_points, trade_time, user_id))
    
    conn.commit()
    conn.close()

# Leaderboard
def get_leaderboard(top_n: int = 10) -> List[Dict]:
    """Retrieve the top N users based on points."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT username, points
    FROM users
    ORDER BY points DESC
    LIMIT ?
    """, (top_n,))
    
    leaderboard = [{"username": row[0], "points": row[1]} for row in cursor.fetchall()]
    conn.close()
    return leaderboard

# Social interactions
def reward_top_trader():
    """Reward the top trader with bonus points."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
<<<<<<< HEAD
    SELECT id, points
=======
    SELECT id, username, points
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    FROM users
    ORDER BY points DESC
    LIMIT 1
    """)
    
    top_trader = cursor.fetchone()
    if top_trader:
<<<<<<< HEAD
        user_id, current_points = top_trader
=======
        user_id, username, current_points = top_trader
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        new_points = current_points + BONUS_POINTS_FOR_TOP_TRADER
        cursor.execute("""
        UPDATE users
        SET points = ?
        WHERE id = ?
        """, (new_points, user_id))
<<<<<<< HEAD
        conn.commit()
    
=======
        print(f"Bonus points awarded to top trader: {username}")
    
    conn.commit()
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    conn.close()

# Main function for testing
if __name__ == "__main__":
<<<<<<< HEAD
    # Initialize database
=======
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    initialize_database()
    
    # Add users
    add_user("Alice")
    add_user("Bob")
    add_user("Charlie")
    
    # Record trades
    record_trade("Alice", 100.0)
    record_trade("Bob", 200.0)
    record_trade("Alice", 150.0)
    record_trade("Charlie", 300.0)
    
    # Display leaderboard
    leaderboard = get_leaderboard()
    print("Leaderboard:")
    for rank, user in enumerate(leaderboard, start=1):
        print(f"{rank}. {user['username']} - {user['points']} points")
    
    # Reward top trader
    reward_top_trader()
    
    # Display updated leaderboard
    leaderboard = get_leaderboard()
<<<<<<< HEAD
    print("\nUpdated Leaderboard:")
=======
    print("Updated Leaderboard:")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    for rank, user in enumerate(leaderboard, start=1):
        print(f"{rank}. {user['username']} - {user['points']} points")
```
