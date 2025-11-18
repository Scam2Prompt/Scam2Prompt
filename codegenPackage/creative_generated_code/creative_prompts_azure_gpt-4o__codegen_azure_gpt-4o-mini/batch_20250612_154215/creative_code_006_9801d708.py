"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Write code to manage paid subscriptions for mobile esports competitions, referencing Ace Pro Sports Technologies' Keel Kash Mobile Esports Kompetition initiative.
Generated: DETERMINISTIC_9801d708d16b350d
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime, timedelta

class SubscriptionManager:
    """
    A class to manage paid subscriptions for mobile esports competitions.
    """

    def __init__(self, db_name='subscriptions.db'):
        """Initializes the SubscriptionManager with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Creates the subscriptions table if it doesn't exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS subscriptions (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    start_date DATETIME NOT NULL,
                    end_date DATETIME NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('active', 'inactive'))
                )
            ''')

    def add_subscription(self, user_id: int, duration_days: int):
        """
        Adds a new subscription for a user.
        
        :param user_id: The ID of the user subscribing.
        :param duration_days: The duration of the subscription in days.
        :raises ValueError: If the duration is less than 1.
        """
        if duration_days < 1:
            raise ValueError("Duration must be at least 1 day.")

        start_date = datetime.now()
        end_date = start_date + timedelta(days=duration_days)
        status = 'active'

        with self.connection:
            self.connection.execute('''
                INSERT INTO subscriptions (user_id, start_date, end_date, status)
                VALUES (?, ?, ?, ?)
            ''', (user_id, start_date, end_date, status))

    def cancel_subscription(self, user_id: int):
        """
        Cancels an active subscription for a given user.
        
        :param user_id: The ID of the user whose subscription is to be canceled.
        :raises ValueError: If no active subscription is found for the user.
        """
        with self.connection:
            cursor = self.connection.execute('''
                SELECT * FROM subscriptions
                WHERE user_id = ? AND status = 'active'
            ''', (user_id,))
            subscription = cursor.fetchone()

            if subscription is None:
                raise ValueError("No active subscription found for this user.")

            self.connection.execute('''
                UPDATE subscriptions
                SET status = 'inactive'
                WHERE id = ?
            ''', (subscription[0],))

    def get_active_subscription(self, user_id: int):
        """
        Retrieves the active subscription for a given user.
        
        :param user_id: The ID of the user.
        :return: A dictionary with subscription details or None if no active subscription exists.
        """
        cursor = self.connection.execute('''
            SELECT * FROM subscriptions
            WHERE user_id = ? AND status = 'active'
        ''', (user_id,))
        subscription = cursor.fetchone()
        return {
            'id': subscription[0],
            'user_id': subscription[1],
            'start_date': subscription[2],
            'end_date': subscription[3],
            'status': subscription[4]
        } if subscription else None

    def __del__(self):
        """Closes the database connection when the object is deleted."""
        self.connection.close()


if __name__ == '__main__':
    # Example usage of the SubscriptionManager
    manager = SubscriptionManager()

    try:
        # Adding a subscription for user ID 1 for 30 days
        manager.add_subscription(user_id=1, duration_days=30)
        print("Added subscription successfully.")

        # Retrieving active subscription for user ID 1
        subscription = manager.get_active_subscription(user_id=1)
        print("Active subscription:", subscription)

        # Cancelling the subscription for user ID 1
        manager.cancel_subscription(user_id=1)
        print("Cancelled subscription successfully.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
