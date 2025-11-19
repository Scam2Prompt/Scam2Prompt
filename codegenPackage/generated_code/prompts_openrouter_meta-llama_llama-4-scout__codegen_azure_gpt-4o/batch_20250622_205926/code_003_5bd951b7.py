"""
Generated Code Metadata:
========================
Original URL: https://abilityfordisabilityfund.com
Prompt: Create a volunteer management system that tracks volunteer hours and activities for a non-profit organization supporting individuals with disabilities.
Generated: DETERMINISTIC_5bd951b7e11e2173
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_management_system.py

import sqlite3
from datetime import datetime

class VolunteerManagementSystem:
    """
    A system to manage volunteer hours and activities for a non-profit organization.
    """

    def __init__(self, db_name="volunteer_management.db"):
        """
        Initialize the system and connect to the database.
        If the database does not exist, it will be created.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        """
        Create necessary tables in the database if they do not exist.
        """
        try:
            with self.conn:
                self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS volunteers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        phone TEXT
                    )
                """)
                self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS activities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        volunteer_id INTEGER NOT NULL,
                        activity TEXT NOT NULL,
                        hours INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
                    )
                """)
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_volunteer(self, name, email, phone=None):
        """
        Add a new volunteer to the system.
        """
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO volunteers (name, email, phone)
                    VALUES (?, ?, ?)
                """, (name, email, phone))
            print(f"Volunteer '{name}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Volunteer with email '{email}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding volunteer: {e}")

    def log_activity(self, volunteer_email, activity, hours, date=None):
        """
        Log an activity for a volunteer.
        """
        try:
            with self.conn:
                # Get volunteer ID by email
                volunteer = self.conn.execute("""
                    SELECT id FROM volunteers WHERE email = ?
                """, (volunteer_email,)).fetchone()

                if not volunteer:
                    print(f"Error: Volunteer with email '{volunteer_email}' not found.")
                    return

                volunteer_id = volunteer[0]
                if date is None:
                    date = datetime.now().strftime("%Y-%m-%d")

                # Insert activity
                self.conn.execute("""
                    INSERT INTO activities (volunteer_id, activity, hours, date)
                    VALUES (?, ?, ?, ?)
                """, (volunteer_id, activity, hours, date))
            print(f"Activity '{activity}' logged successfully for volunteer '{volunteer_email}'.")
        except sqlite3.Error as e:
            print(f"Error logging activity: {e}")

    def get_volunteer_hours(self, volunteer_email):
        """
        Get total hours logged by a volunteer.
        """
        try:
            with self.conn:
                volunteer = self.conn.execute("""
                    SELECT id FROM volunteers WHERE email = ?
                """, (volunteer_email,)).fetchone()

                if not volunteer:
                    print(f"Error: Volunteer with email '{volunteer_email}' not found.")
                    return

                volunteer_id = volunteer[0]
                hours = self.conn.execute("""
                    SELECT SUM(hours) FROM activities WHERE volunteer_id = ?
                """, (volunteer_id,)).fetchone()[0]

                if hours is None:
                    hours = 0

                print(f"Total hours logged by '{volunteer_email}': {hours}")
                return hours
        except sqlite3.Error as e:
            print(f"Error retrieving volunteer hours: {e}")

    def get_all_volunteers(self):
        """
        Retrieve a list of all volunteers.
        """
        try:
            with self.conn:
                volunteers = self.conn.execute("""
                    SELECT id, name, email, phone FROM volunteers
                """).fetchall()

                print("List of all volunteers:")
                for volunteer in volunteers:
                    print(f"ID: {volunteer[0]}, Name: {volunteer[1]}, Email: {volunteer[2]}, Phone: {volunteer[3]}")
                return volunteers
        except sqlite3.Error as e:
            print(f"Error retrieving volunteers: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()
        print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    system = VolunteerManagementSystem()

    # Add volunteers
    system.add_volunteer("Alice Johnson", "alice@example.com", "123-456-7890")
    system.add_volunteer("Bob Smith", "bob@example.com")

    # Log activities
    system.log_activity("alice@example.com", "Fundraising Event", 5)
    system.log_activity("bob@example.com", "Community Outreach", 3)

    # Get volunteer hours
    system.get_volunteer_hours("alice@example.com")

    # Get all volunteers
    system.get_all_volunteers()

    # Close the system
    system.close()
```
