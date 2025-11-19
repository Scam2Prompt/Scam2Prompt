"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Develop a script that automates the distribution of welcome bonuses for new users on a platform similar to venez888.
Generated: DETERMINISTIC_9186a540169edef3
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import sqlite3
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='welcome_bonus.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database configuration
DATABASE = 'platform.db'
WELCOME_BONUS_AMOUNT = 100  # Set the welcome bonus amount

def connect_to_database():
    """
    Establishes a connection to the SQLite database.
    Returns the connection object.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        logging.error(f"Failed to connect to the database: {e}")
        raise

def get_new_users(conn):
    """
    Fetches all new users who have not yet received their welcome bonus.
    Returns a list of user records.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_id, username
            FROM users
            WHERE welcome_bonus_given = 0
        """)
        return cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Failed to fetch new users: {e}")
        raise

def distribute_welcome_bonus(conn, user_id):
    """
    Assigns the welcome bonus to a user and updates the database.
    """
    try:
        cursor = conn.cursor()
        # Update user balance and mark bonus as given
        cursor.execute("""
            UPDATE users
            SET balance = balance + ?, welcome_bonus_given = 1, bonus_date = ?
            WHERE user_id = ?
        """, (WELCOME_BONUS_AMOUNT, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user_id))
        conn.commit()
        logging.info(f"Welcome bonus distributed to user_id: {user_id}")
    except sqlite3.Error as e:
        logging.error(f"Failed to distribute bonus to user_id {user_id}: {e}")
        raise

def main():
    """
    Main function to automate the distribution of welcome bonuses to new users.
    """
    try:
        # Connect to the database
        conn = connect_to_database()

        # Get list of new users
        new_users = get_new_users(conn)

        if not new_users:
            logging.info("No new users found for welcome bonus distribution.")
            return

        # Distribute bonus to each new user
        for user_id, username in new_users:
            logging.info(f"Processing welcome bonus for user_id: {user_id}, username: {username}")
            distribute_welcome_bonus(conn, user_id)

        logging.info("Welcome bonus distribution completed.")
    except Exception as e:
        logging.error(f"An error occurred during the welcome bonus distribution process: {e}")
    finally:
        # Ensure the database connection is closed
        try:
            conn.close()
        except NameError:
            # Connection was never established
            pass

if __name__ == '__main__':
    main()
```
