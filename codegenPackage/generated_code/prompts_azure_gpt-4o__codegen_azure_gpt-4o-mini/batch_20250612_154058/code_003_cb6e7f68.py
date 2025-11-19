"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: Generate a Python script to calculate referral bonuses based on a referral code system, where users earn a percentage of their referrals' earnings.
Generated: DETERMINISTIC_cb6e7f688e5f3431
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

# Constants
DATABASE_NAME = 'referral_system.db'
REFERRAL_BONUS_PERCENTAGE = 0.1  # 10% bonus for referrals

# Database setup
def setup_database():
    """Sets up the database and creates the necessary tables."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                referral_code TEXT UNIQUE NOT NULL,
                earnings REAL DEFAULT 0.0,
                referred_by TEXT
            )
        ''')
        conn.commit()

# Function to add a new user
def add_user(name: str, referral_code: str, referred_by: str = None) -> None:
    """Adds a new user to the database.

    Args:
        name (str): The name of the user.
        referral_code (str): The unique referral code for the user.
        referred_by (str): The referral code of the user who referred this user.
    """
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, referral_code, referred_by)
                VALUES (?, ?, ?)
            ''', (name, referral_code, referred_by))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Referral code '{referral_code}' already exists.")
    except Exception as e:
        print(f"An error occurred while adding user: {e}")

# Function to update user earnings
def update_user_earnings(referral_code: str, earnings: float) -> None:
    """Updates the earnings of a user and calculates referral bonuses.

    Args:
        referral_code (str): The referral code of the user whose earnings are updated.
        earnings (float): The amount of earnings to add.
    """
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            # Update the user's earnings
            cursor.execute('''
                UPDATE users
                SET earnings = earnings + ?
                WHERE referral_code = ?
            ''', (earnings, referral_code))
            conn.commit()

            # Calculate and distribute referral bonuses
            cursor.execute('''
                SELECT referred_by FROM users WHERE referral_code = ?
            ''', (referral_code,))
            referred_by = cursor.fetchone()

            if referred_by and referred_by[0]:
                bonus = earnings * REFERRAL_BONUS_PERCENTAGE
                cursor.execute('''
                    UPDATE users
                    SET earnings = earnings + ?
                    WHERE referral_code = ?
                ''', (bonus, referred_by[0]))
                conn.commit()
    except Exception as e:
        print(f"An error occurred while updating earnings: {e}")

# Function to get user earnings
def get_user_earnings(referral_code: str) -> float:
    """Retrieves the earnings of a user.

    Args:
        referral_code (str): The referral code of the user.

    Returns:
        float: The earnings of the user.
    """
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT earnings FROM users WHERE referral_code = ?
            ''', (referral_code,))
            result = cursor.fetchone()
            return result[0] if result else 0.0
    except Exception as e:
        print(f"An error occurred while retrieving earnings: {e}")
        return 0.0

# Main execution
if __name__ == "__main__":
    setup_database()
    # Example usage
    add_user("Alice", "ALICE123")
    add_user("Bob", "BOB456", "ALICE123")
    update_user_earnings("BOB456", 100.0)

    print(f"Alice's earnings: {get_user_earnings('ALICE123')}")
    print(f"Bob's earnings: {get_user_earnings('BOB456')}")
```
