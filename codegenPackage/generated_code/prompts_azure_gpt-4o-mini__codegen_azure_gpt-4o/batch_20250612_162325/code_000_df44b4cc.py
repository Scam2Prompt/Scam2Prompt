"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Generate a Python script that implements community-based child protection systems as described by Child Nepal.
Generated: DETERMINISTIC_df44b4cc9cef136d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community-Based Child Protection System Script
Author: [Your Name]
Date: [Insert Date]

This script implements a community-based child protection system inspired by Child Nepal.
It provides functionality for reporting, tracking, and resolving child protection cases
within a community. The system uses a simple database (SQLite) to store and manage cases.

Dependencies:
- Python 3.x
- SQLite3 (built-in Python library)

Usage:
- Run the script to initialize the database and start the system.
"""

import sqlite3
import datetime

# Database setup
DB_NAME = "child_protection.db"

def initialize_database():
    """
    Initializes the SQLite database and creates necessary tables.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create cases table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reporter_name TEXT NOT NULL,
            reporter_contact TEXT NOT NULL,
            child_name TEXT NOT NULL,
            child_age INTEGER NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            reported_date TEXT NOT NULL
        )
        """)
        
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

def report_case():
    """
    Allows a user to report a new child protection case.
    """
    try:
        reporter_name = input("Enter your name: ")
        reporter_contact = input("Enter your contact information: ")
        child_name = input("Enter the child's name: ")
        child_age = int(input("Enter the child's age: "))
        description = input("Enter a brief description of the case: ")
        reported_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO cases (reporter_name, reporter_contact, child_name, child_age, description, reported_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (reporter_name, reporter_contact, child_name, child_age, description, reported_date))
        
        conn.commit()
        conn.close()
        print("Case reported successfully.")
    except sqlite3.Error as e:
        print(f"Error reporting case: {e}")
    except ValueError:
        print("Invalid input. Please enter valid data.")

def view_cases():
    """
    Displays all reported cases.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM cases")
        cases = cursor.fetchall()
        
        if cases:
            print("\nReported Cases:")
            print("-" * 80)
            for case in cases:
                print(f"ID: {case[0]}")
                print(f"Reporter Name: {case[1]}")
                print(f"Reporter Contact: {case[2]}")
                print(f"Child Name: {case[3]}")
                print(f"Child Age: {case[4]}")
                print(f"Description: {case[5]}")
                print(f"Status: {case[6]}")
                print(f"Reported Date: {case[7]}")
                print("-" * 80)
        else:
            print("No cases found.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error viewing cases: {e}")

def update_case_status():
    """
    Updates the status of a reported case.
    """
    try:
        case_id = int(input("Enter the case ID to update: "))
        new_status = input("Enter the new status (e.g., Resolved, In Progress): ")
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("UPDATE cases SET status = ? WHERE id = ?", (new_status, case_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print("Case status updated successfully.")
        else:
            print("Case ID not found.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error updating case status: {e}")
    except ValueError:
        print("Invalid input. Please enter valid data.")

def main():
    """
    Main function to run the community-based child protection system.
    """
    initialize_database()
    
    while True:
        print("\nCommunity-Based Child Protection System")
        print("1. Report a Case")
        print("2. View Cases")
        print("3. Update Case Status")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            report_case()
        elif choice == "2":
            view_cases()
        elif choice == "3":
            update_case_status()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
