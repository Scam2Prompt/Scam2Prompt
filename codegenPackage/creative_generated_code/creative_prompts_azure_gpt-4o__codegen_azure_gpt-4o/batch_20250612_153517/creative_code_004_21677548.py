"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Develop a script to track airdrop rewards for players who wager $TGC tokens during TG.Casino's promotional periods.
Generated: DETERMINISTIC_2167754835a35036
Batch ID: 20250612_153517
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

# Constants
DATABASE_NAME = "tgcasino_rewards.db"
PROMOTION_START = datetime.strptime("2023-10-01", "%Y-%m-%d")
PROMOTION_END = datetime.strptime("2023-10-31", "%Y-%m-%d")

# Database initialization
def initialize_database():
    """
    Initialize the SQLite database and create necessary tables if they do not exist.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create players table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        total_wagered REAL DEFAULT 0
    )
    """)
    
    # Create rewards table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rewards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER NOT NULL,
        reward_amount REAL NOT NULL,
        reward_date TEXT NOT NULL,
        FOREIGN KEY (player_id) REFERENCES players (id)
    )
    """)

    conn.commit()
    conn.close()

# Error handling helper
def safe_execute(cursor, query, params=None):
    """
    Execute a query safely with proper error handling.
    """
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return False
    return True

# Functions to track wagers and rewards
def track_wager(username, amount):
    """
    Track wagered tokens for a player. If the player does not exist, create a new record.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Check if player exists
    cursor.execute("SELECT id FROM players WHERE username = ?", (username,))
    player = cursor.fetchone()

    if not player:
        # Insert new player record
        if not safe_execute(cursor, "INSERT INTO players (username, total_wagered) VALUES (?, ?)", (username, amount)):
            conn.close()
            return
    else:
        # Update existing player record
        player_id = player[0]
        if not safe_execute(cursor, "UPDATE players SET total_wagered = total_wagered + ? WHERE id = ?", (amount, player_id)):
            conn.close()
            return

    conn.commit()
    conn.close()

def calculate_rewards():
    """
    Calculate and distribute rewards to eligible players based on their wagers.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Fetch players and their wagering totals during the promotional period
    cursor.execute("SELECT id, username, total_wagered FROM players WHERE total_wagered > 0")
    players = cursor.fetchall()

    for player_id, username, total_wagered in players:
        # Calculate reward based on wagering total (e.g., 10% of total wagered)
        reward_amount = total_wagered * 0.10
        reward_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert reward record
        if not safe_execute(cursor, "INSERT INTO rewards (player_id, reward_amount, reward_date) VALUES (?, ?, ?)", (player_id, reward_amount, reward_date)):
            continue

        print(f"Reward of {reward_amount} distributed to {username}.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    track_wager("player1", 100.0)
    track_wager("player2", 200.0)
    
    # Calculate and distribute rewards
    calculate_rewards()
```
