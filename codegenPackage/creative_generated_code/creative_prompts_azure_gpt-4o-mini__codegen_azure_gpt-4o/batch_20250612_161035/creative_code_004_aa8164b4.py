"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blum-airdrop.pages.dev
Prompt: Explain how to utilize Blum's rewarding point system in a crypto trading application to enhance user engagement.
Generated: DETERMINISTIC_aa8164b42a32e06c
Batch ID: 20250612_161035
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

# Constants for the Reward System
REWARD_THRESHOLD = 1000  # Minimum trade amount to qualify for points
POINTS_PER_TRADE = 10    # Points awarded per qualifying trade
BONUS_POINTS = 50        # Bonus points for exceeding high trade volume
HIGH_VOLUME_THRESHOLD = 5000  # Threshold for high trade volume

# Database setup for storing user data and points
def initialize_database():
    """Initialize the database with user points table if it doesn't exist."""
    conn = sqlite3.connect("crypto_trading.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_points (
        user_id TEXT PRIMARY KEY,
        points INTEGER DEFAULT 0,
        last_updated TEXT
    )
    """)
    conn.commit()
    conn.close()

# Function to update points for a user based on trade volume
def update_user_points(user_id, trade_amount):
    """
    Updates the user's points based on trade amount.

    Args:
        user_id (str): Unique identifier for the user.
        trade_amount (float): Amount of the trade in USD.

    Returns:
        dict: A summary of the updated points.
    """
    conn = sqlite3.connect("crypto_trading.db")
    cursor = conn.cursor()

    # Check if user exists in the database
    cursor.execute("SELECT points FROM user_points WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    # If user does not exist, initialize their record
    if result is None:
        cursor.execute("INSERT INTO user_points (user_id, points, last_updated) VALUES (?, ?, ?)", 
                       (user_id, 0, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()

    # Calculate points based on trade volume
    points_earned = 0
    if trade_amount >= REWARD_THRESHOLD:
        points_earned = POINTS_PER_TRADE
        if trade_amount > HIGH_VOLUME_THRESHOLD:
            points_earned += BONUS_POINTS

    # Update the user's points
    cursor.execute("UPDATE user_points SET points = points + ?, last_updated = ? WHERE user_id = ?", 
                   (points_earned, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_id))
    conn.commit()

    # Fetch the updated points for the user
    cursor.execute("SELECT points FROM user_points WHERE user_id = ?", (user_id,))
    updated_points = cursor.fetchone()[0]

    conn.close()

    # Return summary
    return {
        "user_id": user_id,
        "trade_amount": trade_amount,
        "points_earned": points_earned,
        "total_points": updated_points
    }

# Function to retrieve user points
def get_user_points(user_id):
    """
    Fetches the total points for a user.

    Args:
        user_id (str): Unique identifier for the user.

    Returns:
        dict: The user's total points and last updated timestamp.
    """
    conn = sqlite3.connect("crypto_trading.db")
    cursor = conn.cursor()

    cursor.execute("SELECT points, last_updated FROM user_points WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            "user_id": user_id,
            "points": result[0],
            "last_updated": result[1]
        }
    else:
        return {
            "user_id": user_id,
            "points": 0,
            "last_updated": None
        }

# Example usage
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Simulate trade actions
    user_trade = update_user_points("user123", 2000)
    print(f"Trade Summary: {user_trade}")

    # Fetch user points
    user_data = get_user_points("user123")
    print(f"User Points: {user_data}")
```
