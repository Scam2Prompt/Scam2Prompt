"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Can you provide a code example for tracking user earnings and activity statistics for a platform like AUTOBUX?
Generated: DETERMINISTIC_15b50c745d0bfe31
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

class UserActivityTracker:
    """
    A class to track user earnings and activity statistics for a platform.
    """

    def __init__(self, db_name='user_activity.db'):
        """
        Initializes the database connection and creates the table if it doesn't exist.

        :param db_name: Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates a table for storing user activity and earnings if it doesn't already exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_activity (
                user_id INTEGER NOT NULL,
                activity_date TEXT NOT NULL,
                earnings REAL NOT NULL,
                PRIMARY KEY (user_id, activity_date)
            )
        ''')
        self.connection.commit()

    def log_activity(self, user_id, earnings):
        """
        Logs user activity and earnings into the database.

        :param user_id: ID of the user.
        :param earnings: Earnings amount for the given activity.
        """
        activity_date = datetime.now().strftime("%Y-%m-%d")
        try:
            self.cursor.execute('''
                INSERT INTO user_activity (user_id, activity_date, earnings)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id, activity_date) DO UPDATE SET
                    earnings = earnings + excluded.earnings
            ''', (user_id, activity_date, earnings))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while logging activity: {e}")

    def get_user_statistics(self, user_id):
        """
        Retrieves the total earnings for a user.

        :param user_id: ID of the user.
        :return: Total earnings and the number of activity records.
        """
        try:
            self.cursor.execute('''
                SELECT SUM(earnings), COUNT(*)
                FROM user_activity
                WHERE user_id = ?
            ''', (user_id,))
            return self.cursor.fetchone()  # Returns (total_earnings, activity_count)
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving user statistics: {e}")
            return None

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()


# Example usage:
if __name__ == "__main__":
    tracker = UserActivityTracker()

    # Log some activities
    tracker.log_activity(user_id=1, earnings=100.50)
    tracker.log_activity(user_id=1, earnings=50.75)

    # Retrieve statistics for the user
    earnings, activity_count = tracker.get_user_statistics(user_id=1)
    print(f"User 1 Total Earnings: {earnings}, Activity Count: {activity_count}")

    # Close the database connection
    tracker.close()
```
