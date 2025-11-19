"""
Generated Code Metadata:
========================
Original URL: https://qna3ai.web.app
Prompt: How can I create a rewards system for users who participate in voting, inspired by the QnA3 credits system?
Generated: DETERMINISTIC_a6a1e3893e836975
Batch ID: 20250612_161224
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

# Database setup
DB_NAME = "rewards_system.db"

def initialize_database():
    """
    Initializes the database with necessary tables if they don't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            credits INTEGER DEFAULT 0
        )
        """)
        
        # Create votes table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            vote_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_user(username):
    """
    Adds a new user to the system.
    :param username: The username of the new user.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding user: {e}")
    finally:
        conn.close()

def record_vote(username):
    """
    Records a vote for a user and rewards them with credits.
    :param username: The username of the user who voted.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Fetch user ID and current credits
        cursor.execute("SELECT user_id, credits FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        
        if user is None:
            print(f"Error: User '{username}' not found.")
            return
        
        user_id, current_credits = user
        
        # Record the vote
        vote_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO votes (user_id, vote_date) VALUES (?, ?)", (user_id, vote_date))
        
        # Update user credits
        new_credits = current_credits + 10  # Reward 10 credits per vote
        cursor.execute("UPDATE users SET credits = ? WHERE user_id = ?", (new_credits, user_id))
        
        conn.commit()
        print(f"Vote recorded for '{username}'. Credits updated to {new_credits}.")
    except sqlite3.Error as e:
        print(f"Error recording vote: {e}")
    finally:
        conn.close()

def get_user_credits(username):
    """
    Retrieves the current credits of a user.
    :param username: The username of the user.
    :return: The number of credits the user has.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT credits FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        
        if user is None:
            print(f"Error: User '{username}' not found.")
            return None
        
        return user[0]
    except sqlite3.Error as e:
        print(f"Error fetching user credits: {e}")
        return None
    finally:
        conn.close()

# Main program (example usage)
if __name__ == "__main__":
    initialize_database()
    
    # Add users
    add_user("Alice")
    add_user("Bob")
    
    # Record votes
    record_vote("Alice")
    record_vote("Bob")
    record_vote("Alice")
    
    # Get user credits
    print(f"Alice's credits: {get_user_credits('Alice')}")
    print(f"Bob's credits: {get_user_credits('Bob')}")
```

This code implements a rewards system for users who participate in voting. It uses SQLite for data storage, includes error handling, and follows best practices for Python programming.
