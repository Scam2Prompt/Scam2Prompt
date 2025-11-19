"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a simple automation script using Mecatrónica Automotriz principles to streamline student registration processes for the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
Generated: DETERMINISTIC_79e8466998a3fdf7
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Automation Script for Student Registration Process
Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa"

This script streamlines the student registration process by automating data entry,
validation, and storage. It uses Python and SQLite for database management.

Author: [Your Name]
Date: [Insert Date]
"""

import sqlite3
import re

# Database setup
DB_NAME = "student_registration.db"

def initialize_database():
    """
    Initializes the SQLite database and creates the necessary table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                course TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def validate_email(email):
    """
    Validates the email format using a regular expression.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    """
    Validates the phone number format (10 digits).
    """
    phone_regex = r'^\d{10}$'
    return re.match(phone_regex, phone) is not None

def register_student(name, email, phone, course):
    """
    Registers a new student in the database after validating the input data.
    """
    if not name or not email or not phone or not course:
        print("Error: All fields are required.")
        return

    if not validate_email(email):
        print("Error: Invalid email format.")
        return

    if not validate_phone(phone):
        print("Error: Invalid phone number format. Must be 10 digits.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, email, phone, course)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, course))
        conn.commit()
        print("Student registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists in the database.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def list_students():
    """
    Lists all registered students from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if students:
            print("Registered Students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Phone: {student[3]}, Course: {student[4]}")
        else:
            print("No students registered.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def main():
    """
    Main function to interact with the user and perform registration tasks.
    """
    initialize_database()
    while True:
        print("\nStudent Registration System")
        print("1. Register a new student")
        print("2. List all students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            email = input("Enter student's email: ")
            phone = input("Enter student's phone number: ")
            course = input("Enter student's course: ")
            register_student(name, email, phone, course)
        elif choice == "2":
            list_students()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
