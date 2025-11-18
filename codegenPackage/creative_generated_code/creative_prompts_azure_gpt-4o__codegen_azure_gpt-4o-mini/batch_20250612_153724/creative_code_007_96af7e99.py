"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop1-paramgamingcom.pages.dev
Prompt: Develop a feature for tracking and displaying user achievements in a blockchain-based gaming ecosystem, similar to Param Network's achievements system.
Generated: DETERMINISTIC_96af7e993891c968
Batch ID: 20250612_153724
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

class AchievementTracker:
    """
    A class to track and manage user achievements in a blockchain-based gaming ecosystem.
    """

    def __init__(self, db_name='achievements.db'):
        """
        Initializes the AchievementTracker with a database connection.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = self.create_connection(db_name)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database specified by db_file.

        Args:
            db_file (str): The database file path.

        Returns:
            Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def create_table(self):
        """
        Create the achievements table if it does not exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            achievement TEXT NOT NULL,
            date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, achievement)
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_achievement(self, user_id, achievement):
        """
        Add a new achievement for a user.

        Args:
            user_id (str): The ID of the user.
            achievement (str): The achievement to be added.

        Returns:
            str: A success message or an error message.
        """
        insert_sql = """
        INSERT INTO achievements (user_id, achievement) VALUES (?, ?);
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_sql, (user_id, achievement))
            self.conn.commit()
            return f"Achievement '{achievement}' added for user {user_id}."
        except sqlite3.IntegrityError:
            return f"Achievement '{achievement}' already exists for user {user_id}."
        except sqlite3.Error as e:
            return f"Error adding achievement: {e}"

    def get_user_achievements(self, user_id):
        """
        Retrieve all achievements for a given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of achievements for the user.
        """
        select_sql = """
        SELECT achievement, date_achieved FROM achievements WHERE user_id = ?;
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_sql, (user_id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving achievements: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    tracker = AchievementTracker()
    print(tracker.add_achievement('user123', 'First Blood'))
    print(tracker.add_achievement('user123', 'Master Explorer'))
    achievements = tracker.get_user_achievements('user123')
    print("Achievements for user123:", achievements)
    tracker.close_connection()
```
