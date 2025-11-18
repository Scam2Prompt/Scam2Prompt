"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-web.pages.dev
Prompt: Create a script to display tournament leaderboards for a gaming platform, similar to Metacade's competitive gaming features.
Generated: DETERMINISTIC_741a399bf7466587
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sqlite3
from typing import List, Tuple

# SQLite database file name
DB_FILE = "gaming_tournament.db"

# Connect to SQLite database (create it if it doesn't exist)
def connect_to_db():
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        exit(1)

# Function to initialize the database schema
def initialize_db(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
        exit(1)

# Function to add a new player
def add_player(conn: sqlite3.Connection, username: str, score: int):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO players (username, score) VALUES (?, ?)", (username, score))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding player: {e}")

# Function to update a player's score
def update_score(conn: sqlite3.Connection, username: str, score: int):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE players SET score = ? WHERE username = ?", (score, username))
        if cursor.rowcount == 0:
            print(f"Error: Username '{username}' not found.")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating score: {e}")

# Function to fetch leaderboard data
def fetch_leaderboard(conn: sqlite3.Connection) -> List[Tuple[str, int]]:
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT username, score FROM players ORDER BY score DESC")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching leaderboard: {e}")
        return []

# Function to display the leaderboard
def display_leaderboard(leaderboard: List[Tuple[str, int]]):
    print("\nTournament Leaderboard")
    print("-----------------------")
    print("{:<20} {:<10}".format("Username", "Score"))
    print("-----------------------")
    for username, score in leaderboard:
        print("{:<20} {:<10}".format(username, score))
    print("-----------------------")

# Main function to drive the script
def main():
    # Connect to the database
    conn = connect_to_db()
    
    # Initialize database schema
    initialize_db(conn)
    
    # Example: Add or update players
    add_player(conn, "PlayerOne", 1500)
    add_player(conn, "PlayerTwo", 1200)
    add_player(conn, "PlayerThree", 1800)
    update_score(conn, "PlayerTwo", 2000)
    
    # Fetch and display the leaderboard
    leaderboard = fetch_leaderboard(conn)
    display_leaderboard(leaderboard)
    
    # Close database connection
    conn.close()

# Entry point of the script
if __name__ == "__main__":
    main()
```
