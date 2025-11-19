"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Generate code to facilitate a referral mission system that rewards users for inviting others, inspired by KAYEN's community engagement strategies.
Generated: DETERMINISTIC_ee0bfef9efd6ed15
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import sqlite3
from datetime import datetime

# Database initialization
DB_NAME = "referral_system.db"

def initialize_database():
    """
    Initialize the database with necessary tables for the referral system.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            referred_by TEXT,
            reward_points INTEGER DEFAULT 0,
            join_date TEXT NOT NULL
        )
    """)

    # Create referrals table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            referrer_id TEXT NOT NULL,
            referred_id TEXT NOT NULL,
            referral_date TEXT NOT NULL,
            PRIMARY KEY (referrer_id, referred_id),
            FOREIGN KEY (referrer_id) REFERENCES users(id),
            FOREIGN KEY (referred_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()

# User Registration
def register_user(username, referred_by=None):
    """
    Register a new user in the system.
    :param username: The username of the new user.
    :param referred_by: The ID of the referrer, if applicable.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())
    join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Insert new user into the database
        cursor.execute("""
            INSERT INTO users (id, username, referred_by, join_date)
            VALUES (?, ?, ?, ?)
        """, (user_id, username, referred_by, join_date))

        # If referred by someone, record the referral
        if referred_by:
            cursor.execute("SELECT * FROM users WHERE id = ?", (referred_by,))
            referrer = cursor.fetchone()

            if referrer:
                referral_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("""
                    INSERT INTO referrals (referrer_id, referred_id, referral_date)
                    VALUES (?, ?, ?)
                """, (referred_by, user_id, referral_date))

                # Reward the referrer with points
                reward_points = 10  # Points for each successful referral
                cursor.execute("""
                    UPDATE users
                    SET reward_points = reward_points + ?
                    WHERE id = ?
                """, (reward_points, referred_by))
            else:
                print("Referrer ID not found. No referral recorded.")
        conn.commit()
        print(f"User '{username}' registered successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# View User Information
def view_user_info(user_id):
    """
    View the details of a user including their referral history.
    :param user_id: The ID of the user to view.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        # Fetch user details
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if user:
            print(f"User ID: {user[0]}")
            print(f"Username: {user[1]}")
            print(f"Referred By: {user[2]}")
            print(f"Reward Points: {user[3]}")
            print(f"Join Date: {user[4]}")
            print("\nReferral History:")
            
            # Fetch referral history
            cursor.execute("""
                SELECT referred_id, referral_date
                FROM referrals
                WHERE referrer_id = ?
            """, (user_id,))
            referrals = cursor.fetchall()
            if referrals:
                for referral in referrals:
                    print(f"- Referred User ID: {referral[0]}, Referral Date: {referral[1]}")
            else:
                print("No referrals made.")
        else:
            print("User not found.")
    finally:
        conn.close()

# Main execution (example usage)
if __name__ == "__main__":
    initialize_database()
    
    # Register some users
    register_user("Alice")
    register_user("Bob")
    
    # Example: Bob refers Charlie
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = 'Bob'")
    bob_id = cursor.fetchone()[0]
    conn.close()
    register_user("Charlie", referred_by=bob_id)

    # View Bob's info and referral history
    view_user_info(bob_id)
```
