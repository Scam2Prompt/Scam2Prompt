"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Write code for integrating a rewards system into a gaming app that mimics the "Stardust" earning mechanism described on Cosmic Rewards.
Generated: DETERMINISTIC_de327c69ab5158b2
Batch ID: 20250612_151445
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

class RewardsSystem:
    """
    A class to manage the rewards system for a gaming app, including the 'Stardust' earning mechanism.
    """

    def __init__(self, db_path="rewards.db"):
        """
        Initialize the RewardsSystem with a connection to the database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary tables for the rewards system if they don't already exist.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE
                )
            """)

            # Create rewards table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rewards (
                    reward_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    stardust INTEGER DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error while initializing: {e}")
        finally:
            conn.close()

    def add_user(self, username):
        """
        Add a new user to the rewards system.

        :param username: Unique username for the user.
        :return: True if user is added successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            user_id = cursor.lastrowid

            # Initialize user's rewards record
            cursor.execute("INSERT INTO rewards (user_id) VALUES (?)", (user_id,))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Database error while adding user: {e}")
            return False
        finally:
            conn.close()

    def earn_stardust(self, username, amount):
        """
        Add stardust to a user's account.

        :param username: The username of the user earning stardust.
        :param amount: The amount of stardust to add.
        :return: True if stardust was added successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if user is None:
                print("Error: User not found.")
                return False

            user_id = user[0]

            # Update stardust in rewards table
            cursor.execute("""
                UPDATE rewards
                SET stardust = stardust + ?, last_updated = ?
                WHERE user_id = ?
            """, (amount, datetime.now(), user_id))

            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error while earning stardust: {e}")
            return False
        finally:
            conn.close()

    def get_stardust(self, username):
        """
        Retrieve the stardust balance of a user.

        :param username: The username of the user.
        :return: The stardust balance if user exists, None otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT r.stardust
                FROM rewards r
                INNER JOIN users u ON u.user_id = r.user_id
                WHERE u.username = ?
            """, (username,))
            stardust = cursor.fetchone()

            return stardust[0] if stardust else None
        except sqlite3.Error as e:
            print(f"Database error while retrieving stardust: {e}")
            return None
        finally:
            conn.close()

    def transfer_stardust(self, sender_username, receiver_username, amount):
        """
        Transfer stardust from one user to another.

        :param sender_username: The username of the user sending stardust.
        :param receiver_username: The username of the user receiving stardust.
        :param amount: The amount of stardust to transfer.
        :return: True if transfer is successful, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Get sender and receiver user IDs and balances
            cursor.execute("SELECT user_id, stardust FROM users u INNER JOIN rewards r ON u.user_id = r.user_id WHERE u.username = ?", (sender_username,))
            sender = cursor.fetchone()

            cursor.execute("SELECT user_id, stardust FROM users u INNER JOIN rewards r ON u.user_id = r.user_id WHERE u.username = ?", (receiver_username,))
            receiver = cursor.fetchone()

            if sender is None or receiver is None:
                print("Error: One or both users not found.")
                return False

            sender_id, sender_stardust = sender
            receiver_id, receiver_stardust = receiver

            if sender_stardust < amount:
                print("Error: Insufficient stardust.")
                return False

            # Update sender's and receiver's stardust balances
            cursor.execute("""
                UPDATE rewards
                SET stardust = stardust - ?, last_updated = ?
                WHERE user_id = ?
            """, (amount, datetime.now(), sender_id))

            cursor.execute("""
                UPDATE rewards
                SET stardust = stardust + ?, last_updated = ?
                WHERE user_id = ?
            """, (amount, datetime.now(), receiver_id))

            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error while transferring stardust: {e}")
            return False
        finally:
            conn.close()
```

This code integrates a rewards system with a "Stardust" earning mechanism, including error handling and best practices for Python programming. The SQLite database is used for persistence.
