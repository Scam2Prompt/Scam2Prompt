"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihoc2exgdukcfgx2odn2mrsfomsily2pdvuxrl2n64fq42owgngji.ipfs.dweb.link
Prompt: Create a program to monitor and manage analytics for user activity on Avalon Finance's BTC Layer2 lending protocol.
Generated: DETERMINISTIC_cb30810a40ed8fea
Batch ID: 20250612_152358
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

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityMonitor:
    """Class to monitor and manage user activity analytics for Avalon Finance's BTC Layer2 lending protocol."""
    
    def __init__(self, db_name='user_activity.db'):
        """Initialize the database connection and create the required table if it doesn't exist."""
        self.connection = self.create_connection(db_name)
        self.create_table()

    def create_connection(self, db_name):
        """Create a database connection to the SQLite database."""
        try:
            conn = sqlite3.connect(db_name)
            logging.info("Database connection established.")
            return conn
        except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise

    def create_table(self):
        """Create the user_activity table if it does not already exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS user_activity (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id TEXT NOT NULL,
                                activity_type TEXT NOT NULL,
                                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                             );''')
            self.connection.commit()
            logging.info("User activity table created or already exists.")
        except sqlite3.Error as e:
            logging.error(f"Error creating table: {e}")
            raise

    def log_activity(self, user_id, activity_type):
        """Log user activity into the database.

        Args:
            user_id (str): The ID of the user.
            activity_type (str): The type of activity being logged.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''INSERT INTO user_activity (user_id, activity_type)
                              VALUES (?, ?)''', (user_id, activity_type))
            self.connection.commit()
            logging.info(f"Logged activity for user {user_id}: {activity_type}")
        except sqlite3.Error as e:
            logging.error(f"Error logging activity: {e}")
            raise

    def get_activity_report(self):
        """Retrieve activity report from the database.

        Returns:
            list: A list of user activities.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''SELECT * FROM user_activity ORDER BY timestamp DESC;''')
            activities = cursor.fetchall()
            logging.info("Activity report retrieved successfully.")
            return activities
        except sqlite3.Error as e:
            logging.error(f"Error retrieving activity report: {e}")
            raise

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

# Example usage
if __name__ == "__main__":
    monitor = UserActivityMonitor()

    # Log some sample activities
    monitor.log_activity('user123', 'Lend BTC')
    monitor.log_activity('user456', 'Withdraw BTC')

    # Retrieve and print the activity report
    activities = monitor.get_activity_report()
    for activity in activities:
        print(f"User ID: {activity[1]}, Activity Type: {activity[2]}, Timestamp: {activity[3]}")

    # Close the connection to the database
    monitor.close_connection()
```
