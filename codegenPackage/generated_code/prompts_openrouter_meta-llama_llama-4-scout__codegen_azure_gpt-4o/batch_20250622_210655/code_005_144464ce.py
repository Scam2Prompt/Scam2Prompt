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
"""
Event Attendance and Member Engagement Tracking System

This script provides a system for tracking event attendance and member engagement
for an organization. It uses SQLite for data storage and provides functionality
to add members, create events, record attendance, and generate engagement reports.

Requirements:
- Python 3.x
- SQLite3 (built-in Python library)
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "ibcaj_event_tracking.db"

def initialize_database():
    """
    Initialize the database with required tables.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create Members table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Members (
            MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT UNIQUE NOT NULL,
            JoinDate DATE NOT NULL
        )
        """)

        # Create Events table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Events (
            EventID INTEGER PRIMARY KEY AUTOINCREMENT,
            EventName TEXT NOT NULL,
            EventDate DATE NOT NULL
        )
        """)

        # Create Attendance table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Attendance (
            AttendanceID INTEGER PRIMARY KEY AUTOINCREMENT,
            MemberID INTEGER NOT NULL,
            EventID INTEGER NOT NULL,
            FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
            FOREIGN KEY (EventID) REFERENCES Events(EventID)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_member(name, email):
    """
    Add a new member to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        join_date = datetime.now().date()
        cursor.execute("INSERT INTO Members (Name, Email, JoinDate) VALUES (?, ?, ?)", (name, email, join_date))
        conn.commit()
        print(f"Member '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    except sqlite3.Error as e:
        print(f"Error adding member: {e}")
    finally:
        conn.close()

def create_event(event_name, event_date):
    """
    Create a new event in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Events (EventName, EventDate) VALUES (?, ?)", (event_name, event_date))
        conn.commit()
        print(f"Event '{event_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating event: {e}")
    finally:
        conn.close()

def record_attendance(member_id, event_id):
    """
    Record attendance for a member at an event.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Attendance (MemberID, EventID) VALUES (?, ?)", (member_id, event_id))
        conn.commit()
        print(f"Attendance recorded for MemberID {member_id} at EventID {event_id}.")
    except sqlite3.Error as e:
        print(f"Error recording attendance: {e}")
    finally:
        conn.close()

def generate_engagement_report():
    """
    Generate a report of member engagement based on attendance.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT Members.Name, Members.Email, COUNT(Attendance.AttendanceID) AS EventCount
        FROM Members
        LEFT JOIN Attendance ON Members.MemberID = Attendance.MemberID
        GROUP BY Members.MemberID
        ORDER BY EventCount DESC
        """)

        report = cursor.fetchall()
        print("Member Engagement Report:")
        print("Name\t\tEmail\t\tEvents Attended")
        print("-" * 50)
        for row in report:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
    except sqlite3.Error as e:
        print(f"Error generating report: {e}")
    finally:
        conn.close()

# Main script execution
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_member("Alice Johnson", "alice@example.com")
    add_member("Bob Smith", "bob@example.com")

    create_event("Annual Gala", "2023-12-15")
    create_event("Monthly Meetup", "2023-11-10")

    record_attendance(1, 1)
    record_attendance(2, 1)
    record_attendance(1, 2)

    generate_engagement_report()
```
