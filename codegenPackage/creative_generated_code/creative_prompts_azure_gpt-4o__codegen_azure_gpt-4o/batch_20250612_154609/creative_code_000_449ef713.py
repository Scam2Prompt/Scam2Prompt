"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Write Python code to integrate a membership management system for organizations like the Idaho Association of Commerce & Industry, including features for member login and event registration.
Generated: DETERMINISTIC_449ef7135ba70ddd
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from datetime import datetime

# Constants
DATABASE_FILE = 'membership_system.db'

# Utility functions
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_database():
    """Initializes the database with necessary tables."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Create members table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create events table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    ''')

    # Create event registrations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            event_id INTEGER NOT NULL,
            registration_date TEXT NOT NULL,
            FOREIGN KEY (member_id) REFERENCES members (id),
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')

    conn.commit()
    conn.close()

# Member management functions
def register_member(name, email, password):
    """Registers a new member."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(password)
        cursor.execute('''
            INSERT INTO members (name, email, password)
            VALUES (?, ?, ?)
        ''', (name, email, hashed_password))
        conn.commit()
        print(f"Member '{name}' registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

def member_login(email, password):
    """Logs in a member and verifies credentials."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM members WHERE email = ? AND password = ?
        ''', (email, hash_password(password)))
        member = cursor.fetchone()
        if member:
            print(f"Welcome, {member[1]}!")
            return member[0]  # Return member ID
        else:
            print("Invalid email or password.")
            return None
    finally:
        conn.close()

# Event management functions
def create_event(name, description, date):
    """Creates a new event."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO events (name, description, date)
            VALUES (?, ?, ?)
        ''', (name, description, date))
        conn.commit()
        print(f"Event '{name}' created successfully.")
    finally:
        conn.close()

def register_for_event(member_id, event_id):
    """Registers a member for an event."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        registration_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO registrations (member_id, event_id, registration_date)
            VALUES (?, ?, ?)
        ''', (member_id, event_id, registration_date))
        conn.commit()
        print(f"Member ID {member_id} registered for Event ID {event_id}.")
    except sqlite3.IntegrityError:
        print("Error: Invalid member ID or event ID.")
    finally:
        conn.close()

def view_events():
    """Displays all available events."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM events')
        events = cursor.fetchall()
        print("Available Events:")
        for event in events:
            print(f"ID: {event[0]}, Name: {event[1]}, Date: {event[3]}")
    finally:
        conn.close()

# Main execution (for testing purposes)
if __name__ == "__main__":
    # Initialize the database
    create_database()

    # Example usage
    register_member("John Doe", "john.doe@example.com", "securepassword")
    member_id = member_login("john.doe@example.com", "securepassword")
    if member_id:
        create_event("Annual Meeting", "Discuss yearly progress", "2023-12-01")
        view_events()
        register_for_event(member_id, 1)
```
