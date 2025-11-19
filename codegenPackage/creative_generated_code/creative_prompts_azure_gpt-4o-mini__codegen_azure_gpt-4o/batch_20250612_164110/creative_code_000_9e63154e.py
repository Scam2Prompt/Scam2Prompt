"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: How can I implement an affiliate program similar to Cosmic Rewards that allows users to earn gift cards through gameplay?
Generated: DETERMINISTIC_9e63154e679a5c03
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean implementation for an affiliate program in Python. This is designed as a simplified version with core functionality for tracking user gameplay, rewards, and gift card redemption. It uses SQLite for database operations to ensure persistent data storage.

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "affiliate_program.db"


def initialize_database():
    """
    Initializes the SQLite database and creates tables if they do not already exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            affiliate_code TEXT UNIQUE NOT NULL,
            points INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS gameplay (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            points_earned INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rewards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            gift_card_code TEXT NOT NULL,
            redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()


# User management
def register_user(username, affiliate_code):
    """
    Registers a new user in the system.

    :param username: The user's username
    :param affiliate_code: A unique affiliate code for the user
    :return: Success or error message
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO users (username, affiliate_code) VALUES (?, ?)
        """, (username, affiliate_code))
        conn.commit()
        return f"User '{username}' registered successfully."
    except sqlite3.IntegrityError:
        return "Error: Username or affiliate code already exists."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()


def get_user_by_affiliate_code(affiliate_code):
    """
    Fetches user details using the affiliate code.

    :param affiliate_code: The affiliate code of the user
    :return: User details or None
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM users WHERE affiliate_code = ?
        """, (affiliate_code,))
        user = cursor.fetchone()
        return user
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()


# Gameplay tracking
def record_gameplay(affiliate_code, points_earned):
    """
    Records gameplay and adds points to the user's total.

    :param affiliate_code: The affiliate code of the user
    :param points_earned: Points earned during the gameplay session
    :return: Success or error message
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        user = get_user_by_affiliate_code(affiliate_code)
        if user:
            user_id = user[0]
            cursor.execute("""
            INSERT INTO gameplay (user_id, points_earned) VALUES (?, ?)
            """, (user_id, points_earned))
            cursor.execute("""
            UPDATE users SET points = points + ? WHERE id = ?
            """, (points_earned, user_id))
            conn.commit()
            return f"Gameplay recorded: {points_earned} points added to user '{user[1]}'."
        else:
            return "Error: User not found for the provided affiliate code."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()


# Rewards redemption
def redeem_points(affiliate_code, points_required, gift_card_code):
    """
    Redeems points for a gift card if the user has enough points.

    :param affiliate_code: The affiliate code of the user
    :param points_required: Points required to redeem the gift card
    :param gift_card_code: The code of the gift card to be redeemed
    :return: Success or error message
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        user = get_user_by_affiliate_code(affiliate_code)
        if user:
            user_id, username, _, points, _ = user
            if points >= points_required:
                cursor.execute("""
                INSERT INTO rewards (user_id, gift_card_code) VALUES (?, ?)
                """, (user_id, gift_card_code))
                cursor.execute("""
                UPDATE users SET points = points - ? WHERE id = ?
                """, (points_required, user_id))
                conn.commit()
                return f"Gift card '{gift_card_code}' redeemed successfully for user '{username}'."
            else:
                return f"Error: Insufficient points. User '{username}' has only {points} points."
        else:
            return "Error: User not found for the provided affiliate code."
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()


# Example usage
if __name__ == "__main__":
    initialize_database()
    print(register_user("player1", "AFF123"))
    print(record_gameplay("AFF123", 50))
    print(record_gameplay("AFF123", 30))
    print(redeem_points("AFF123", 70, "GIFT1234"))
    print(redeem_points("AFF123", 20, "GIFT5678"))
```

This code initializes an SQLite database, allows user registration, tracks gameplay to accumulate points, and enables users to redeem points for gift cards. It includes proper error handling and uses best practices.
