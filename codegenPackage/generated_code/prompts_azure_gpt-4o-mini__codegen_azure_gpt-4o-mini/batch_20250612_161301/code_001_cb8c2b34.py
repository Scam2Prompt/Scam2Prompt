"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: How can I implement a system to track and manage user bonuses and VIP rewards in a gaming application like Betpanda?
Generated: DETERMINISTIC_cb8c2b3499103d19
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class BonusManager:
    """
    A class to manage user bonuses and VIP rewards in a gaming application.
    """

    def __init__(self, db_name: str):
        """
        Initializes the BonusManager with a SQLite database.

        :param db_name: The name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables for tracking user bonuses and VIP rewards.
        """
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    vip_level INTEGER DEFAULT 0
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS bonuses (
                    bonus_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    amount REAL NOT NULL,
                    description TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')

    def add_user(self, username: str) -> int:
        """
        Adds a new user to the system.

        :param username: The username of the new user.
        :return: The user ID of the newly created user.
        """
        with self.connection:
            cursor = self.connection.execute('''
                INSERT INTO users (username) VALUES (?)
            ''', (username,))
            return cursor.lastrowid

    def add_bonus(self, user_id: int, amount: float, description: str) -> None:
        """
        Adds a bonus for a specific user.

        :param user_id: The ID of the user receiving the bonus.
        :param amount: The amount of the bonus.
        :param description: A description of the bonus.
        """
        with self.connection:
            self.connection.execute('''
                INSERT INTO bonuses (user_id, amount, description) VALUES (?, ?, ?)
            ''', (user_id, amount, description))

    def get_user_bonuses(self, user_id: int) -> List[Dict[str, Optional[float]]]:
        """
        Retrieves all bonuses for a specific user.

        :param user_id: The ID of the user.
        :return: A list of bonuses associated with the user.
        """
        cursor = self.connection.execute('''
            SELECT bonus_id, amount, description FROM bonuses WHERE user_id = ?
        ''', (user_id,))
        return [{'bonus_id': row[0], 'amount': row[1], 'description': row[2]} for row in cursor.fetchall()]

    def update_vip_level(self, user_id: int, new_level: int) -> None:
        """
        Updates the VIP level of a user.

        :param user_id: The ID of the user.
        :param new_level: The new VIP level to set.
        """
        with self.connection:
            self.connection.execute('''
                UPDATE users SET vip_level = ? WHERE user_id = ?
            ''', (new_level, user_id))

    def get_user_info(self, user_id: int) -> Optional[Dict[str, Optional[int]]]:
        """
        Retrieves user information including VIP level.

        :param user_id: The ID of the user.
        :return: A dictionary containing user information or None if not found.
        """
        cursor = self.connection.execute('''
            SELECT username, vip_level FROM users WHERE user_id = ?
        ''', (user_id,))
        row = cursor.fetchone()
        if row:
            return {'username': row[0], 'vip_level': row[1]}
        return None

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()

# Example usage
if __name__ == "__main__":
    try:
        bonus_manager = BonusManager('gaming_app.db')
        user_id = bonus_manager.add_user('player1')
        bonus_manager.add_bonus(user_id, 100.0, 'Welcome Bonus')
        bonuses = bonus_manager.get_user_bonuses(user_id)
        print(f"Bonuses for user {user_id}: {bonuses}")
        bonus_manager.update_vip_level(user_id, 1)
        user_info = bonus_manager.get_user_info(user_id)
        print(f"User info: {user_info}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        bonus_manager.close()
```
