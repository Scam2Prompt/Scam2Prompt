"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbabak.info
Prompt: How can I implement a bonus system for new members in a gaming site like PANSOS4D, ensuring secure transactions?
Generated: DETERMINISTIC_5d6cf0ca4cf64b74
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BonusSystem:
    """
    Bonus System for new members in a gaming site.
    Ensures secure transactions for bonus allocation.
    """

    def __init__(self, database="gaming_site.db"):
        """
        Initialize the bonus system and set up the database connection.

        Args:
            database (str): Path to the SQLite database file.
        """
        self.database = database
        self._setup_database()

    def _setup_database(self):
        """
        Set up the database tables if they don't exist.
        """
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            # Create members table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    join_date TEXT NOT NULL,
                    received_bonus INTEGER DEFAULT 0
                )
            """)

            # Create transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    bonus_amount REAL NOT NULL,
                    transaction_date TEXT NOT NULL,
                    FOREIGN KEY(member_id) REFERENCES members(id)
                )
            """)

            connection.commit()
        except sqlite3.Error as e:
            logging.error(f"Database setup failed: {e}")
        finally:
            connection.close()

    def add_new_member(self, username):
        """
        Add a new member to the database.

        Args:
            username (str): Username of the new member.
        """
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("INSERT INTO members (username, join_date) VALUES (?, ?)", (username, join_date))
            connection.commit()
            logging.info(f"New member '{username}' added successfully.")
        except sqlite3.IntegrityError:
            logging.warning(f"Username '{username}' already exists.")
        except sqlite3.Error as e:
            logging.error(f"Failed to add new member: {e}")
        finally:
            connection.close()

    def allocate_bonus(self, username, bonus_amount):
        """
        Allocate a bonus to a new member securely.

        Args:
            username (str): Username of the member.
            bonus_amount (float): Bonus amount to be allocated.
        """
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            # Check if the member exists and hasn't received a bonus
            cursor.execute("SELECT id, received_bonus FROM members WHERE username = ?", (username,))
            member = cursor.fetchone()

            if not member:
                logging.warning(f"Member '{username}' not found.")
                return
            if member[1] == 1:
                logging.warning(f"Member '{username}' already received a bonus.")
                return

            member_id = member[0]
            transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create a transaction and update the member's bonus status
            cursor.execute("""
                INSERT INTO transactions (member_id, bonus_amount, transaction_date) 
                VALUES (?, ?, ?)
            """, (member_id, bonus_amount, transaction_date))

            cursor.execute("""
                UPDATE members 
                SET received_bonus = 1 
                WHERE id = ?
            """, (member_id,))

            connection.commit()
            logging.info(f"Bonus of {bonus_amount} allocated to '{username}' successfully.")
        except sqlite3.Error as e:
            logging.error(f"Failed to allocate bonus: {e}")
        finally:
            connection.close()

    def get_member_info(self, username):
        """
        Retrieve information about a member.

        Args:
            username (str): Username of the member.

        Returns:
            dict: Member information or None if the member doesn't exist.
        """
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT members.username, members.join_date, members.received_bonus, 
                       transactions.bonus_amount, transactions.transaction_date
                FROM members
                LEFT JOIN transactions ON members.id = transactions.member_id
                WHERE members.username = ?
            """, (username,))
            member_info = cursor.fetchone()

            if member_info:
                return {
                    "username": member_info[0],
                    "join_date": member_info[1],
                    "received_bonus": bool(member_info[2]),
                    "bonus_amount": member_info[3],
                    "transaction_date": member_info[4]
                }
            else:
                logging.warning(f"Member '{username}' not found.")
                return None
        except sqlite3.Error as e:
            logging.error(f"Failed to retrieve member info: {e}")
            return None
        finally:
            connection.close()


# Example usage:
if __name__ == "__main__":
    bonus_system = BonusSystem()

    # Add new members
    bonus_system.add_new_member("player1")
    bonus_system.add_new_member("player2")

    # Allocate bonus
    bonus_system.allocate_bonus("player1", 100.0)

    # Retrieve member info
    member_info = bonus_system.get_member_info("player1")
    if member_info:
        print("Member Info:", member_info)
```

This Python code is production-ready, properly documented, uses error handling, and adheres to best practices for secure transactions in the bonus system.
