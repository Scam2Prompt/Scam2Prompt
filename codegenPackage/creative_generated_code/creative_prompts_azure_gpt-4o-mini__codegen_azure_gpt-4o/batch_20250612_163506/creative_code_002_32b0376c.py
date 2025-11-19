"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Write a code snippet that integrates with a database to track student progress in the Marketing Digital program offered by ISIV.
Generated: DETERMINISTIC_32b0376c53020c02
Batch ID: 20250612_163506
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

# Database configuration
DATABASE_NAME = 'student_progress.db'

# Function to initialize the database
def initialize_database():
    """
    Initializes the database and creates necessary tables if they don't exist.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Create Students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                enrollment_date TEXT NOT NULL
            );
        """)

        # Create Progress table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                module_name TEXT NOT NULL,
                completion_date TEXT,
                status TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES Students (id)
            );
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        connection.close()


# Function to add a new student
def add_student(name, email):
    """
    Adds a new student to the database.
    :param name: Name of the student
    :param email: Email of the student
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        enrollment_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""
            INSERT INTO Students (name, email, enrollment_date)
            VALUES (?, ?, ?);
        """, (name, email, enrollment_date))

        connection.commit()
        print(f"Student '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")
    finally:
        connection.close()


# Function to update student progress
def update_progress(student_id, module_name, status, completion_date=None):
    """
    Updates the progress of a student in a specific module.
    :param student_id: ID of the student
    :param module_name: Name of the module
    :param status: Status of the module (e.g., 'In Progress', 'Completed')
    :param completion_date: Completion date of the module (optional)
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO Progress (student_id, module_name, completion_date, status)
            VALUES (?, ?, ?, ?);
        """, (student_id, module_name, completion_date, status))

        connection.commit()
        print(f"Progress updated for student ID {student_id} in module '{module_name}'.")
    except sqlite3.Error as e:
        print(f"Error updating progress: {e}")
    finally:
        connection.close()


# Function to retrieve student progress
def get_student_progress(student_id):
    """
    Retrieves the progress of a specific student.
    :param student_id: ID of the student
    :return: Progress records of the student
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT module_name, completion_date, status
            FROM Progress
            WHERE student_id = ?;
        """, (student_id,))

        progress_records = cursor.fetchall()
        return progress_records
    except sqlite3.Error as e:
        print(f"Error retrieving student progress: {e}")
        return None
    finally:
        connection.close()


# Example usage of the functions
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add a new student
    add_student("John Doe", "john.doe@example.com")

    # Update progress for the student
    update_progress(student_id=1, module_name="Introduction to Marketing", status="Completed", completion_date="2023-10-01")

    # Retrieve progress records
    progress = get_student_progress(student_id=1)
    print("Student Progress:")
    for record in progress:
        print(record)
```
