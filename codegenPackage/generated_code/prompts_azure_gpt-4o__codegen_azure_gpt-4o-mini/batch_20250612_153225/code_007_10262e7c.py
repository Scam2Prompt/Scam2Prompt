"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Develop a tool for tracking updates on sound system installations and events, similar to the "Actualités" section of the Sound Source website.
Generated: DETERMINISTIC_10262e7c7913b888
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

class SoundSystemTracker:
    """
    A class to track updates on sound system installations and events.
    """

    def __init__(self, db_name='sound_system_tracker.db'):
        """
        Initializes the database connection and creates the necessary table if it doesn't exist.

        :param db_name: Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Creates the updates table if it does not already exist.
        """
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS updates (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        event_date TEXT NOT NULL,
                        created_at TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_update(self, title, description, event_date):
        """
        Adds a new update to the database.

        :param title: Title of the update.
        :param description: Description of the update.
        :param event_date: Date of the event in YYYY-MM-DD format.
        """
        created_at = datetime.now().isoformat()
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO updates (title, description, event_date, created_at)
                    VALUES (?, ?, ?, ?)
                ''', (title, description, event_date, created_at))
        except sqlite3.Error as e:
            print(f"Error adding update: {e}")

    def get_updates(self):
        """
        Retrieves all updates from the database.

        :return: A list of updates.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM updates ORDER BY event_date DESC')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving updates: {e}")
            return []

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    # Example usage of the SoundSystemTracker class
    tracker = SoundSystemTracker()

    # Adding a new update
    tracker.add_update(
        title="New Sound System Installation",
        description="Installed a new sound system at the downtown venue.",
        event_date="2023-10-15"
    )

    # Retrieving and printing all updates
    updates = tracker.get_updates()
    for update in updates:
        print(f"ID: {update[0]}, Title: {update[1]}, Description: {update[2]}, Event Date: {update[3]}, Created At: {update[4]}")

    # Closing the tracker
    tracker.close()
```
