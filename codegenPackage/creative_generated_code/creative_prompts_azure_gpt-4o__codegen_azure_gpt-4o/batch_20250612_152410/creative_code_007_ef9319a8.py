"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newshungama.com
Prompt: Write code to create a leaderboard system for color prediction games, incorporating ideas from "How Colour Prediction Game Changes the User Mindset" on Newshungama.com.
Generated: DETERMINISTIC_ef9319a8e98155ec
Batch ID: 20250612_152410
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

# Constants for database setup
DB_NAME = "leaderboard.db"

# Establish database connection and create tables if not already present
def initialize_database():
    """
    Initializes the SQLite database and creates the necessary tables.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Create leaderboard table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        score INTEGER NOT NULL,
        last_updated DATETIME NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()

# Add or update user scores
def update_leaderboard(username, score):
    """
    Adds a new user score to the leaderboard or updates an existing user's score.
    
    :param username: The name of the user
    :param score: The score to be added or updated
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Check if the user already exists in the leaderboard
    cursor.execute("SELECT score FROM leaderboard WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result:
        # Update the user's score if it's higher than the current score
        current_score = result[0]
        if score > current_score:
            cursor.execute("""
            UPDATE leaderboard
            SET score = ?, last_updated = ?
            WHERE username = ?
            """, (score, datetime.now(), username))
    else:
        # Add a new user to the leaderboard
        cursor.execute("""
        INSERT INTO leaderboard (username, score, last_updated)
        VALUES (?, ?, ?)
        """, (username, score, datetime.now()))
    
    connection.commit()
    connection.close()

# Retrieve the top N users from the leaderboard
def get_top_users(limit=10):
    """
    Retrieves the top N users from the leaderboard sorted by score in descending order.
    
    :param limit: The number of top users to retrieve (default is 10)
    :return: A list of dictionaries containing username and score of the top users
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT username, score FROM leaderboard
    ORDER BY score DESC, last_updated ASC
    LIMIT ?
    """, (limit,))
    
    rows = cursor.fetchall()
    connection.close()
    
    # Format the results properly
    top_users = [{"username": row[0], "score": row[1]} for row in rows]
    return top_users

# Main function for testing the leaderboard system
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Simulate user score updates
    update_leaderboard("Alice", 150)
    update_leaderboard("Bob", 200)
    update_leaderboard("Alice", 180)  # Alice improves her score
    
    # Get and display the top users
    top_users = get_top_users()
    print("Top users:")
    for user in top_users:
        print(f"Username: {user['username']}, Score: {user['score']}")
```
