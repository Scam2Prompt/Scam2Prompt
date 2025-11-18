"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonswaps.com
Prompt: Write code to implement a user reputation system for a blockchain-based escrow service, inspired by Elon Swaps' self-regulation mechanisms.
Generated: DETERMINISTIC_d42b85c07454331e
Batch ID: 20250612_154322
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

# Define constants for reputation system
MAX_RATING = 5  # Maximum rating a user can give
MIN_RATING = 0  # Minimum rating a user can give
DEFAULT_REPUTATION_SCORE = 3  # Default reputation score for new users

# Database setup
DB_FILE = 'user_reputation.db'


def initialize_database():
    """
    Initializes the SQLite database.
    Creates tables for users and reputation scores if they do not exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create reputation table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reputation (
            user_id INTEGER NOT NULL,
            score REAL NOT NULL DEFAULT ?,
            ratings_count INTEGER NOT NULL DEFAULT 0,
            last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''', (DEFAULT_REPUTATION_SCORE,))

    conn.commit()
    conn.close()


def add_user(username):
    """
    Adds a new user to the system.
    :param username: The username of the new user.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Insert into users table
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        user_id = cursor.lastrowid

        # Initialize reputation for the new user
        cursor.execute('INSERT INTO reputation (user_id) VALUES (?)', (user_id,))

        conn.commit()
        print(f"User '{username}' added successfully with user_id {user_id}.")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    finally:
        conn.close()


def rate_user(rater_username, target_username, rating):
    """
    Rates a user in the system.
    :param rater_username: The username of the rater.
    :param target_username: The username of the user being rated.
    :param rating: The rating score given by the rater (must be between MIN_RATING and MAX_RATING).
    """
    if not (MIN_RATING <= rating <= MAX_RATING):
        print(f"Error: Rating must be between {MIN_RATING} and {MAX_RATING}.")
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Fetch user IDs
        cursor.execute('SELECT user_id FROM users WHERE username = ?', (rater_username,))
        rater = cursor.fetchone()
        cursor.execute('SELECT user_id FROM users WHERE username = ?', (target_username,))
        target = cursor.fetchone()

        if not rater:
            print(f"Error: Rater '{rater_username}' does not exist.")
            return
        if not target:
            print(f"Error: Target user '{target_username}' does not exist.")
            return

        target_id = target[0]

        # Update reputation score for the target user
        cursor.execute('''
            SELECT score, ratings_count
            FROM reputation WHERE user_id = ?
        ''', (target_id,))
        reputation = cursor.fetchone()

        if reputation:
            current_score, ratings_count = reputation
            new_score = ((current_score * ratings_count) + rating) / (ratings_count + 1)
            new_ratings_count = ratings_count + 1

            cursor.execute('''
                UPDATE reputation
                SET score = ?, ratings_count = ?, last_updated = ?
                WHERE user_id = ?
            ''', (new_score, new_ratings_count, datetime.now(), target_id))

            conn.commit()
            print(f"User '{target_username}' rated successfully. New score: {new_score:.2f}")
        else:
            print(f"Error: Reputation data for '{target_username}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()


def get_reputation(username):
    """
    Retrieves the reputation score for a given user.
    :param username: The username of the user whose reputation score will be fetched.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT r.score, r.ratings_count
            FROM users u
            JOIN reputation r ON u.user_id = r.user_id
            WHERE u.username = ?
        ''', (username,))
        result = cursor.fetchone()

        if result:
            score, ratings_count = result
            print(f"User '{username}' has a reputation score of {score:.2f} based on {ratings_count} rating(s).")
        else:
            print(f"Error: Reputation data for '{username}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()


# Example usage:
if __name__ == "__main__":
    initialize_database()

    add_user("alice")
    add_user("bob")
    rate_user("alice", "bob", 4)
    rate_user("alice", "bob", 5)
    get_reputation("bob")
```
