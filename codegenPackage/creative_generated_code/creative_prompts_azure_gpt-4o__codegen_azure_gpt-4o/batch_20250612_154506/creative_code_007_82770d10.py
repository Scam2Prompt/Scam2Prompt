"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a Python program to track and update user loyalty points based on their betting activity, as described in VZ99's VIP rewards system.
Generated: DETERMINISTIC_82770d100369b475
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class LoyaltyPointsSystem:
    """
    A class to manage user loyalty points based on betting activity.
    """

    def __init__(self, db_name="loyalty_points.db"):
        """
        Initialize the LoyaltyPointsSystem with a database connection.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary database table if it doesn't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Create users table with columns for user ID and loyalty points
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    loyalty_points INTEGER NOT NULL DEFAULT 0
                )
            """)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")

    def add_user(self, user_id):
        """
        Add a new user to the system.
        :param user_id: Unique identifier for the user.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error adding user {user_id}: {e}")

    def update_loyalty_points(self, user_id, points):
        """
        Update loyalty points for a user.
        :param user_id: Unique identifier for the user.
        :param points: Points to be added or subtracted.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET loyalty_points = loyalty_points + ? WHERE user_id = ?", (points, user_id))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error updating loyalty points for user {user_id}: {e}")

    def get_loyalty_points(self, user_id):
        """
        Retrieve loyalty points for a user.
        :param user_id: Unique identifier for the user.
        :return: Loyalty points of the user or None if the user doesn't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT loyalty_points FROM users WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Error retrieving loyalty points for user {user_id}: {e}")
            return None

    def delete_user(self, user_id):
        """
        Remove a user from the system.
        :param user_id: Unique identifier for the user.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error deleting user {user_id}: {e}")


# Example usage:
if __name__ == "__main__":
    # Initialize the loyalty points system
    system = LoyaltyPointsSystem()

    # Add a new user
    system.add_user("user123")

    # Update loyalty points
    system.update_loyalty_points("user123", 50)

    # Retrieve loyalty points
    points = system.get_loyalty_points("user123")
    print(f"User 'user123' has {points} loyalty points.")

    # Delete user
    system.delete_user("user123")
```
