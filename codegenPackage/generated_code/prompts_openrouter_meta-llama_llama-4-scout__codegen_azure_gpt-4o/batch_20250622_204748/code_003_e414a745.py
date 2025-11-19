"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Design a system for leaderboards and rankings in an online casino, where users can accumulate XP and receive bonuses, such as rakebacks and exclusive drops.
Generated: DETERMINISTIC_e414a745e96fdad5
Batch ID: 20250622_204748
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
XP_THRESHOLD_FOR_BONUS = 1000  # XP required for bonuses
RAKEBACK_PERCENTAGE = 0.05     # Rakeback percentage
EXCLUSIVE_DROP_XP = 5000       # XP required for exclusive drops

# Database setup
DB_NAME = "casino_leaderboard.db"

def initialize_database():
    """
    Initialize the database and create necessary tables if they don't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        xp INTEGER DEFAULT 0,
        rakeback REAL DEFAULT 0,
        exclusive_drop BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create leaderboard table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        rank INTEGER NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_user(username):
    """
    Add a new user to the database.
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

def update_xp(username, xp_gained):
    """
    Update the XP of a user and calculate bonuses.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Fetch user data
    cursor.execute("SELECT id, xp FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if not user:
        print(f"Error: User '{username}' not found.")
        conn.close()
        return
    
    user_id, current_xp = user
    new_xp = current_xp + xp_gained
    
    # Calculate bonuses
    rakeback = 0
    exclusive_drop = False
    if new_xp >= XP_THRESHOLD_FOR_BONUS:
        rakeback = new_xp * RAKEBACK_PERCENTAGE
    if new_xp >= EXCLUSIVE_DROP_XP:
        exclusive_drop = True
    
    # Update user data
    cursor.execute("""
    UPDATE users
    SET xp = ?, rakeback = ?, exclusive_drop = ?
    WHERE id = ?
    """, (new_xp, rakeback, exclusive_drop, user_id))
    
    conn.commit()
    conn.close()

def update_leaderboard():
    """
    Update the leaderboard rankings based on user XP.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Fetch all users sorted by XP in descending order
    cursor.execute("SELECT id, xp FROM users ORDER BY xp DESC")
    users = cursor.fetchall()
    
    # Update leaderboard rankings
    for rank, (user_id, _) in enumerate(users, start=1):
        cursor.execute("""
        INSERT INTO leaderboard (user_id, rank, updated_at)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
        rank = excluded.rank,
        updated_at = excluded.updated_at
        """, (user_id, rank, datetime.now()))
    
    conn.commit()
    conn.close()

def get_leaderboard():
    """
    Retrieve the current leaderboard.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT u.username, l.rank, u.xp
    FROM leaderboard l
    JOIN users u ON l.user_id = u.id
    ORDER BY l.rank ASC
    """)
    leaderboard = cursor.fetchall()
    
    conn.close()
    return leaderboard

# Main execution
if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    add_user("Alice")
    add_user("Bob")
    update_xp("Alice", 1200)
    update_xp("Bob", 800)
    update_leaderboard()
    
    leaderboard = get_leaderboard()
    print("Leaderboard:")
    for username, rank, xp in leaderboard:
        print(f"Rank {rank}: {username} - {xp} XP")
```
