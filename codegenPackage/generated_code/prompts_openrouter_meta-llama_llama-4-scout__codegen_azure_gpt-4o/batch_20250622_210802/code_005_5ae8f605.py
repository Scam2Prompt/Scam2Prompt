"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Design a system to track student progress and certification for various courses offered by Global Healthcare Management College, including the Advanced Diploma of Civil Construction Design (RII60520).
Generated: DETERMINISTIC_5ae8f605d220a69c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sqlite3
from datetime import datetime

# Database setup
DATABASE_NAME = "student_progress.db"

# Initialize the database connection
def initialize_database():
    """
    Creates the necessary tables for tracking student progress and certifications.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date TEXT NOT NULL
        )
    """)

    # Create Courses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_code TEXT NOT NULL UNIQUE
        )
    """)

    # Create Progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Progress (
            progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            progress_percentage INTEGER NOT NULL CHECK(progress_percentage BETWEEN 0 AND 100),
            certification_status TEXT NOT NULL CHECK(certification_status IN ('Not Certified', 'Certified')),
            FOREIGN KEY(student_id) REFERENCES Students(student_id),
            FOREIGN KEY(course_id) REFERENCES Courses(course_id)
        )
    """)

    connection.commit()
    connection.close()

# Add a new student
def add_student(name, email):
    """
    Adds a new student to the database.
    :param name: Name of the student
    :param email: Email of the student
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
            INSERT INTO Students (name, email, enrollment_date)
            VALUES (?, ?, ?)
        """, (name, email, enrollment_date))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Add a new course
def add_course(course_name, course_code):
    """
    Adds a new course to the database.
    :param course_name: Name of the course
    :param course_code: Unique code for the course
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Courses (course_name, course_code)
            VALUES (?, ?)
        """, (course_name, course_code))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Update student progress
def update_progress(student_id, course_id, progress_percentage, certification_status):
    """
    Updates the progress of a student in a specific course.
    :param student_id: ID of the student
    :param course_id: ID of the course
    :param progress_percentage: Progress percentage (0-100)
    :param certification_status: Certification status ('Not Certified' or 'Certified')
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Progress (student_id, course_id, progress_percentage, certification_status)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(student_id, course_id) DO UPDATE SET
            progress_percentage = excluded.progress_percentage,
            certification_status = excluded.certification_status
        """, (student_id, course_id, progress_percentage, certification_status))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Fetch student progress
def fetch_student_progress(student_id):
    """
    Fetches the progress of a student across all courses.
    :param student_id: ID of the student
    :return: List of progress records
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT Courses.course_name, Progress.progress_percentage, Progress.certification_status
            FROM Progress
            JOIN Courses ON Progress.course_id = Courses.course_id
            WHERE Progress.student_id = ?
        """, (student_id,))
        progress_records = cursor.fetchall()
        return progress_records
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        connection.close()

# Main function for testing
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample data
    add_student("John Doe", "john.doe@example.com")
    add_course("Advanced Diploma of Civil Construction Design", "RII60520")

    # Update progress
    update_progress(1, 1, 75, "Not Certified")

    # Fetch and display progress
    progress = fetch_student_progress(1)
    for record in progress:
        print(f"Course: {record[0]}, Progress: {record[1]}%, Certification Status: {record[2]}")
```
