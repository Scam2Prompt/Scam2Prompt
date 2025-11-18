"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Write code to implement a volunteer management system for RM, including features for registration, task assignment, and tracking hours contributed.
Generated: DETERMINISTIC_e7aedb137e0b7e95
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Volunteer Management System for RM
Author: [Your Name]
Description: This Python program allows RM to manage volunteers, including features for registration, task assignment, 
and tracking contributed hours.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "volunteer_management.db"

def initialize_database():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create volunteers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS volunteers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT
    )
    """)
    
    # Create tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        volunteer_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        hours INTEGER NOT NULL,
        assigned_date TEXT NOT NULL,
        FOREIGN KEY (volunteer_id) REFERENCES volunteers (id)
    )
    """)
    
    conn.commit()
    conn.close()

# Volunteer registration
def register_volunteer(name, email, phone=None):
    """
    Registers a new volunteer.
    :param name: Volunteer name
    :param email: Volunteer email (must be unique)
    :param phone: Volunteer phone number (optional)
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO volunteers (name, email, phone) VALUES (?, ?, ?)
        """, (name, email, phone))
        conn.commit()
        print(f"Volunteer '{name}' registered successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. Email '{email}' is already registered.")
    finally:
        conn.close()

# Assign a task
def assign_task(volunteer_id, description, hours):
    """
    Assigns a task to a volunteer.
    :param volunteer_id: ID of the volunteer
    :param description: Description of the task
    :param hours: Estimated hours for the task
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        assigned_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
        INSERT INTO tasks (volunteer_id, description, hours, assigned_date) 
        VALUES (?, ?, ?, ?)
        """, (volunteer_id, description, hours, assigned_date))
        conn.commit()
        print(f"Task '{description}' assigned to Volunteer ID {volunteer_id} successfully!")
    except sqlite3.Error as e:
        print(f"Error assigning task: {e}")
    finally:
        conn.close()

# Track hours contributed
def track_hours(volunteer_id):
    """
    Tracks the total hours contributed by a volunteer.
    :param volunteer_id: ID of the volunteer
    :return: Total hours contributed by the volunteer
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT SUM(hours) FROM tasks WHERE volunteer_id = ?
        """, (volunteer_id,))
        total_hours = cursor.fetchone()[0]
        if total_hours:
            print(f"Volunteer ID {volunteer_id} has contributed a total of {total_hours} hours.")
        else:
            print(f"No hours logged for Volunteer ID {volunteer_id}.")
        return total_hours or 0
    except sqlite3.Error as e:
        print(f"Error tracking hours: {e}")
        return 0
    finally:
        conn.close()

# Main function for testing
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Example usage
    register_volunteer("Alice Johnson", "alice@example.com", "123-456-7890")
    register_volunteer("Bob Smith", "bob@example.com")
    
    assign_task(1, "Organize fundraising event", 5)
    assign_task(1, "Prepare presentations", 3)
    assign_task(2, "Manage social media", 4)
    
    track_hours(1)  # Should return 8
    track_hours(2)  # Should return 4
```
