"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write a script to schedule and manage fundraising activities, including assigning volunteers and tracking progress, inspired by CRM.f's activity planning tools.
Generated: DETERMINISTIC_5728e84d86fb2fd2
Batch ID: 20250612_151354
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
from typing import List, Optional

# Database setup and connection
class Database:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        # Create tables for activities and volunteers if they don't exist
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL DEFAULT 'Scheduled'
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS volunteers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS activity_volunteers (
                    activity_id INTEGER,
                    volunteer_id INTEGER,
                    FOREIGN KEY (activity_id) REFERENCES activities (id),
                    FOREIGN KEY (volunteer_id) REFERENCES volunteers (id),
                    PRIMARY KEY (activity_id, volunteer_id)
                )
            ''')

    def close(self):
        self.connection.close()


# Activity management class
class ActivityManager:
    def __init__(self, db: Database):
        self.db = db

    def add_activity(self, name: str, date: str, description: Optional[str] = None):
        """Add a new fundraising activity"""
        try:
            with self.db.connection:
                self.db.connection.execute('''
                    INSERT INTO activities (name, date, description)
                    VALUES (?, ?, ?)
                ''', (name, date, description))
        except sqlite3.Error as e:
            print(f"Error adding activity: {e}")

    def get_activities(self) -> List[dict]:
        """Retrieve all fundraising activities"""
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT * FROM activities')
        activities = cursor.fetchall()
        return [dict(id=row[0], name=row[1], date=row[2], description=row[3], status=row[4]) for row in activities]

    def update_activity_status(self, activity_id: int, status: str):
        """Update the status of a fundraising activity"""
        try:
            with self.db.connection:
                self.db.connection.execute('''
                    UPDATE activities SET status = ? WHERE id = ?
                ''', (status, activity_id))
        except sqlite3.Error as e:
            print(f"Error updating activity status: {e}")

    def assign_volunteer(self, activity_id: int, volunteer_id: int):
        """Assign a volunteer to a fundraising activity"""
        try:
            with self.db.connection:
                self.db.connection.execute('''
                    INSERT INTO activity_volunteers (activity_id, volunteer_id)
                    VALUES (?, ?)
                ''', (activity_id, volunteer_id))
        except sqlite3.IntegrityError:
            print("This volunteer is already assigned to this activity.")
        except sqlite3.Error as e:
            print(f"Error assigning volunteer: {e}")


# Volunteer management class
class VolunteerManager:
    def __init__(self, db: Database):
        self.db = db

    def add_volunteer(self, name: str, email: str):
        """Add a new volunteer"""
        try:
            with self.db.connection:
                self.db.connection.execute('''
                    INSERT INTO volunteers (name, email)
                    VALUES (?, ?)
                ''', (name, email))
        except sqlite3.IntegrityError:
            print("This email is already associated with a volunteer.")
        except sqlite3.Error as e:
            print(f"Error adding volunteer: {e}")

    def get_volunteers(self) -> List[dict]:
        """Retrieve all volunteers"""
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT * FROM volunteers')
        volunteers = cursor.fetchall()
        return [dict(id=row[0], name=row[1], email=row[2]) for row in volunteers]


# Main function to run the application
def main():
    db = Database('fundraising.db')
    activity_manager = ActivityManager(db)
    volunteer_manager = VolunteerManager(db)

    # Example usage:
    volunteer_manager.add_volunteer("Alice Johnson", "alice@example.com")
    volunteer_manager.add_volunteer("Bob Smith", "bob@example.com")

    activity_manager.add_activity("Charity Run", "2024-05-15", "Annual charity run for local community.")
    activity_manager.add_activity("Bake Sale", "2024-06-20", "Bake sale to raise funds for the shelter.")

    # Assign volunteers to activities
    volunteers = volunteer_manager.get_volunteers()
    activities = activity_manager.get_activities()

    if volunteers and activities:
        activity_manager.assign_volunteer(activities[0]['id'], volunteers[0]['id'])
        activity_manager.assign_volunteer(activities[1]['id'], volunteers[1]['id'])

    # Update the status of an activity
    activity_manager.update_activity_status(activities[0]['id'], 'Completed')

    # Close database connection
    db.close()


if __name__ == '__main__':
    main()
```
