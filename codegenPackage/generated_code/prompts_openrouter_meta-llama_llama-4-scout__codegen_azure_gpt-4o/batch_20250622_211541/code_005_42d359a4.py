"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Create a system to track and manage user bonuses and rewards on a platform similar to Coin Rush, focusing on cashback, rake back, and VIP benefits.
Generated: DETERMINISTIC_42d359a4e9147cb1
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: rewards_system.py

import sqlite3
from datetime import datetime

# Constants for reward types
REWARD_TYPES = ["cashback", "rakeback", "vip"]

# Database setup
DB_NAME = "rewards.db"

def initialize_database():
    """
    Initialize the SQLite database and create necessary tables.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        vip_level INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create rewards table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rewards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        reward_type TEXT NOT NULL,
        amount REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_user(username, vip_level=0):
    """
    Add a new user to the platform.
    :param username: The username of the user.
    :param vip_level: The VIP level of the user (default is 0).
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, vip_level) VALUES (?, ?)", (username, vip_level))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    finally:
        conn.close()

def add_reward(user_id, reward_type, amount):
    """
    Add a reward for a user.
    :param user_id: The ID of the user receiving the reward.
    :param reward_type: The type of reward (cashback, rakeback, vip).
    :param amount: The amount of the reward.
    """
    if reward_type not in REWARD_TYPES:
        print(f"Error: Invalid reward type '{reward_type}'. Must be one of {REWARD_TYPES}.")
        return
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rewards (user_id, reward_type, amount) VALUES (?, ?, ?)", (user_id, reward_type, amount))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: User ID '{user_id}' does not exist.")
    finally:
        conn.close()

def get_user_rewards(user_id):
    """
    Retrieve all rewards for a specific user.
    :param user_id: The ID of the user.
    :return: A list of rewards for the user.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT reward_type, amount, created_at FROM rewards WHERE user_id = ?", (user_id,))
    rewards = cursor.fetchall()
    conn.close()
    return rewards

def get_user_details(username):
    """
    Retrieve user details by username.
    :param username: The username of the user.
    :return: User details including ID, VIP level, and creation date.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, vip_level, created_at FROM users WHERE username = ?", (username,))
    user_details = cursor.fetchone()
    conn.close()
    return user_details

def update_vip_level(user_id, new_vip_level):
    """
    Update the VIP level of a user.
    :param user_id: The ID of the user.
    :param new_vip_level: The new VIP level to set.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET vip_level = ? WHERE id = ?", (new_vip_level, user_id))
        conn.commit()
    finally:
        conn.close()

# Main execution for testing purposes
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Add sample users
    add_user("john_doe", vip_level=1)
    add_user("jane_smith", vip_level=2)
    
    # Add rewards
    user_details = get_user_details("john_doe")
    if user_details:
        user_id = user_details[0]
        add_reward(user_id, "cashback", 50.0)
        add_reward(user_id, "rakeback", 20.0)
    
    # Retrieve and display rewards
    if user_details:
        rewards = get_user_rewards(user_id)
        print(f"Rewards for user 'john_doe': {rewards}")
    
    # Update VIP level
    if user_details:
        update_vip_level(user_id, 3)
        print(f"Updated VIP level for 'john_doe' to 3.")
```

This code is a complete, production-ready implementation of a rewards system for tracking user bonuses and rewards. It includes database initialization, user management, reward tracking, and VIP level updates.
