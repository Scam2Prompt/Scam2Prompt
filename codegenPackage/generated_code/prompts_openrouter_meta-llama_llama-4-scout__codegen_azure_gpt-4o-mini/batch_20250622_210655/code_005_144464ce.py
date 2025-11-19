"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Develop a system for tracking event attendance and member engagement for an organization like IBCAJ, suggesting relevant software or tools."
Generated: DETERMINISTIC_144464ce5364da7d
Batch ID: 20250622_210655
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

class AttendanceTracker:
    """
    A class to track event attendance and member engagement for an organization.
    """

    def __init__(self, db_name='attendance.db'):
        """
        Initializes the AttendanceTracker with a SQLite database.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_tables()

    def create_connection(self):
        """
        Creates a database connection to the SQLite database.

        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """
        Creates the necessary tables for tracking attendance and members.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_name TEXT NOT NULL,
                    event_date TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER,
                    event_id INTEGER,
                    attendance_date TEXT NOT NULL,
                    FOREIGN KEY (member_id) REFERENCES members (id),
                    FOREIGN KEY (event_id) REFERENCES events (id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_member(self, name, email):
        """
        Adds a new member to the database.

        :param name: Name of the member.
        :param email: Email of the member.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO members (name, email) VALUES (?, ?)', (name, email))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding member: {e}")

    def add_event(self, event_name, event_date):
        """
        Adds a new event to the database.

        :param event_name: Name of the event.
        :param event_date: Date of the event in YYYY-MM-DD format.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO events (event_name, event_date) VALUES (?, ?)', (event_name, event_date))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding event: {e}")

    def record_attendance(self, member_id, event_id):
        """
        Records attendance for a member at a specific event.

        :param member_id: ID of the member.
        :param event_id: ID of the event.
        """
        try:
            cursor = self.connection.cursor()
            attendance_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('INSERT INTO attendance (member_id, event_id, attendance_date) VALUES (?, ?, ?)',
                           (member_id, event_id, attendance_date))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error recording attendance: {e}")

    def get_member_attendance(self, member_id):
        """
        Retrieves attendance records for a specific member.

        :param member_id: ID of the member.
        :return: List of attendance records.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT events.event_name, attendance.attendance_date
                FROM attendance
                JOIN events ON attendance.event_id = events.id
                WHERE attendance.member_id = ?
            ''', (member_id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving attendance: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    tracker = AttendanceTracker()
    tracker.add_member("John Doe", "john.doe@example.com")
    tracker.add_event("Annual Meeting", "2023-12-01")
    tracker.record_attendance(1, 1)
    attendance_records = tracker.get_member_attendance(1)
    print(attendance_records)
    tracker.close_connection()
```
