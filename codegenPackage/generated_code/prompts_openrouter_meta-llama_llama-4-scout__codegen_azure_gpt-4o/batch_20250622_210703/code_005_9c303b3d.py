"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Write a Python script to manage a simple preschool database, including information about teachers, students, and daily activities.
Generated: DETERMINISTIC_9c303b3d454188b1
Batch ID: 20250622_210703
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

# Database setup
DB_NAME = "preschool.db"

def create_tables():
    """Create tables for the preschool database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Create Teachers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            hire_date DATE NOT NULL
        )
        """)
        # Create Students table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            enrollment_date DATE NOT NULL
        )
        """)
        # Create Activities table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_name TEXT NOT NULL,
            activity_date DATE NOT NULL,
            teacher_id INTEGER NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES Teachers (id)
        )
        """)
        conn.commit()

def add_teacher(name, subject, hire_date):
    """Add a new teacher to the database."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO Teachers (name, subject, hire_date)
            VALUES (?, ?, ?)
            """, (name, subject, hire_date))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding teacher: {e}")

def add_student(name, age, enrollment_date):
    """Add a new student to the database."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO Students (name, age, enrollment_date)
            VALUES (?, ?, ?)
            """, (name, age, enrollment_date))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

def add_activity(activity_name, activity_date, teacher_id):
    """Add a new activity to the database."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO Activities (activity_name, activity_date, teacher_id)
            VALUES (?, ?, ?)
            """, (activity_name, activity_date, teacher_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding activity: {e}")

def view_table(table_name):
    """View all records from a specified table."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Error viewing table {table_name}: {e}")

def main():
    """Main function to interact with the preschool database."""
    create_tables()
    print("Preschool Database Management")
    while True:
        print("\nOptions:")
        print("1. Add Teacher")
        print("2. Add Student")
        print("3. Add Activity")
        print("4. View Teachers")
        print("5. View Students")
        print("6. View Activities")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter teacher's name: ")
            subject = input("Enter subject: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            add_teacher(name, subject, hire_date)
        elif choice == "2":
            name = input("Enter student's name: ")
            age = int(input("Enter age: "))
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            add_student(name, age, enrollment_date)
        elif choice == "3":
            activity_name = input("Enter activity name: ")
            activity_date = input("Enter activity date (YYYY-MM-DD): ")
            teacher_id = int(input("Enter teacher ID: "))
            add_activity(activity_name, activity_date, teacher_id)
        elif choice == "4":
            print("Teachers:")
            view_table("Teachers")
        elif choice == "5":
            print("Students:")
            view_table("Students")
        elif choice == "6":
            print("Activities:")
            view_table("Activities")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
