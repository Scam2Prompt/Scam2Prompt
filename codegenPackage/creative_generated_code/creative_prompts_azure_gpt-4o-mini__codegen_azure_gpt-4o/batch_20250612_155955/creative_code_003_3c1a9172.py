"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: What are the best practices for integrating a referral system in a mobile game that rewards users for inviting friends?
Generated: DETERMINISTIC_3c1a917297a5be73
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for integrating a referral system in a mobile game. The referral system allows users to invite friends and rewards them based on successful referrals.

```python
import uuid
import sqlite3
from typing import Optional

# Database setup: Initialize a SQLite database for storing user and referral information
DB_NAME = "referral_system.db"

def setup_database():
    """
    Sets up the database tables for users and referrals.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Table for user information
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        username TEXT NOT NULL,
        referral_code TEXT UNIQUE NOT NULL,
        rewards INTEGER DEFAULT 0
    )
    """)
    # Table for tracking referrals
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referrals (
        referrer_id TEXT NOT NULL,
        referred_id TEXT NOT NULL,
        reward_status TEXT DEFAULT 'pending',
        FOREIGN KEY (referrer_id) REFERENCES users(user_id),
        FOREIGN KEY (referred_id) REFERENCES users(user_id)
    )
    """)
    conn.commit()
    conn.close()

# Utility Functions
def generate_referral_code() -> str:
    """
    Generates a unique referral code for a user.
    """
    return str(uuid.uuid4())[:8]

# User Registration
def register_user(username: str, referral_code: Optional[str] = None) -> str:
    """
    Registers a new user. Optionally, a referral code can be provided to associate the user with a referrer.

    Args:
        username (str): The username of the new user.
        referral_code (Optional[str]): Referral code of the referrer (if applicable).

    Returns:
        str: The user ID of the newly registered user.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Generate a unique user ID and referral code for the new user
    user_id = str(uuid.uuid4())
    user_referral_code = generate_referral_code()

    try:
        # Insert new user into the users table
        cursor.execute("""
        INSERT INTO users (user_id, username, referral_code)
        VALUES (?, ?, ?)
        """, (user_id, username, user_referral_code))

        # If a referral code is provided, link the new user to the referrer
        if referral_code:
            cursor.execute("""
            SELECT user_id FROM users WHERE referral_code = ?
            """, (referral_code,))
            referrer = cursor.fetchone()
            if referrer:
                referrer_id = referrer[0]
                # Add referral record
                cursor.execute("""
                INSERT INTO referrals (referrer_id, referred_id)
                VALUES (?, ?)
                """, (referrer_id, user_id))
            else:
                print("Invalid referral code provided. No rewards will be granted.")
        
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error during registration: {e}")
        user_id = None
    finally:
        conn.close()

    return user_id

# Reward Distribution
def distribute_rewards():
    """
    Distributes rewards to users whose referrals have been successfully registered.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        # Fetch pending referrals
        cursor.execute("""
        SELECT referrer_id, referred_id FROM referrals WHERE reward_status = 'pending'
        """)
        pending_referrals = cursor.fetchall()

        for referrer_id, referred_id in pending_referrals:
            # Check if referred user exists (basic validation for successful referral)
            cursor.execute("""
            SELECT user_id FROM users WHERE user_id = ?
            """, (referred_id,))
            referred_user = cursor.fetchone()

            if referred_user:
                # Update rewards for the referrer
                cursor.execute("""
                UPDATE users SET rewards = rewards + 1 WHERE user_id = ?
                """, (referrer_id,))
                # Mark referral as rewarded
                cursor.execute("""
                UPDATE referrals SET reward_status = 'rewarded' WHERE referrer_id = ? AND referred_id = ?
                """, (referrer_id, referred_id))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error during reward distribution: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Set up the database
    setup_database()

    # Register users and simulate referrals
    user1_id = register_user("PlayerOne")
    user2_id = register_user("PlayerTwo", referral_code="1234abcd")  # Replace with the actual referral code of user1

    # Distribute rewards
    distribute_rewards()

    print("Referral system executed successfully.")
```

This code provides a simple and scalable framework for a referral system in a mobile game, complete with user registration, referral tracking, and reward distribution.
