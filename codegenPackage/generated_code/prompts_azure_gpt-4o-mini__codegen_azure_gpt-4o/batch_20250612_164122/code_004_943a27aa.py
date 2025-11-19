"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Illustrate how to implement a pre-professional internship management system in a software application for a technical education institute, inspired by Trentino’s practices.
Generated: DETERMINISTIC_943a27aa858b0ba9
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pre-Professional Internship Management System
This script implements a basic internship management system for a technical education institute.
It allows administrators to manage students, internships, and companies, inspired by Trentino's practices.
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "internship_management.db"

def initialize_database():
    """
    Initializes the database with required tables.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create Students table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            course TEXT NOT NULL
        )
        """)

        # Create Companies table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_person TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            industry TEXT NOT NULL
        )
        """)

        # Create Internships table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Internships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            company_id INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Pending', 'Ongoing', 'Completed')),
            FOREIGN KEY(student_id) REFERENCES Students(id),
            FOREIGN KEY(company_id) REFERENCES Companies(id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_student(name, email, phone, course):
    """
    Adds a new student to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Students (name, email, phone, course)
        VALUES (?, ?, ?, ?)
        """, (name, email, phone, course))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")
    finally:
        conn.close()

def add_company(name, contact_person, email, phone, industry):
    """
    Adds a new company to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Companies (name, contact_person, email, phone, industry)
        VALUES (?, ?, ?, ?, ?)
        """, (name, contact_person, email, phone, industry))
        conn.commit()
        print("Company added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding company: {e}")
    finally:
        conn.close()

def assign_internship(student_id, company_id, start_date, end_date):
    """
    Assigns an internship to a student.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Internships (student_id, company_id, start_date, end_date, status)
        VALUES (?, ?, ?, ?, 'Pending')
        """, (student_id, company_id, start_date, end_date))
        conn.commit()
        print("Internship assigned successfully.")
    except sqlite3.Error as e:
        print(f"Error assigning internship: {e}")
    finally:
        conn.close()

def update_internship_status(internship_id, status):
    """
    Updates the status of an internship.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Internships
        SET status = ?
        WHERE id = ?
        """, (status, internship_id))
        conn.commit()
        print("Internship status updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating internship status: {e}")
    finally:
        conn.close()

def list_students():
    """
    Lists all students in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()
        for student in students:
            print(student)
    except sqlite3.Error as e:
        print(f"Error listing students: {e}")
    finally:
        conn.close()

def list_companies():
    """
    Lists all companies in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Companies")
        companies = cursor.fetchall()
        for company in companies:
            print(company)
    except sqlite3.Error as e:
        print(f"Error listing companies: {e}")
    finally:
        conn.close()

def list_internships():
    """
    Lists all internships in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Internships")
        internships = cursor.fetchall()
        for internship in internships:
            print(internship)
    except sqlite3.Error as e:
        print(f"Error listing internships: {e}")
    finally:
        conn.close()

# Main execution
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_student("Alice Johnson", "alice@example.com", "1234567890", "Computer Science")
    add_company("TechCorp", "John Doe", "contact@techcorp.com", "0987654321", "Software Development")
    assign_internship(1, 1, "2023-01-01", "2023-06-01")
    update_internship_status(1, "Ongoing")

    print("\nStudents:")
    list_students()

    print("\nCompanies:")
    list_companies()

    print("\nInternships:")
    list_internships()
```
