"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Write a Python script to manage a simple aviation security training database, including courses such as Basic Avsec Course, Avsec Supervisor Course, and Risk Management Course.
Generated: DETERMINISTIC_9a5f2ae25dc44085
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Constants for database and table names
DATABASE_NAME = "aviation_security_training.db"
TABLE_NAME = "courses"

# Function to initialize the database and create the table
def initialize_database():
    try:
        # Connect to the SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create the courses table if it doesn't exist
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Function to add a course to the database
def add_course(name, description):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute(f"""
        INSERT INTO {TABLE_NAME} (name, description)
        VALUES (?, ?)
        """, (name, description))

        conn.commit()
        print(f"Course '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding course: {e}")
    finally:
        conn.close()

# Function to list all courses in the database
def list_courses():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        courses = cursor.fetchall()

        if courses:
            print("Courses in the database:")
            for course in courses:
                print(f"ID: {course[0]}, Name: {course[1]}, Description: {course[2]}")
        else:
            print("No courses found in the database.")
    except sqlite3.Error as e:
        print(f"Error listing courses: {e}")
    finally:
        conn.close()

# Function to delete a course by ID
def delete_course(course_id):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (course_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Course with ID {course_id} deleted successfully.")
        else:
            print(f"No course found with ID {course_id}.")
    except sqlite3.Error as e:
        print(f"Error deleting course: {e}")
    finally:
        conn.close()

# Main function to demonstrate the functionality
def main():
    initialize_database()

    # Add sample courses
    add_course("Basic Avsec Course", "Introduction to aviation security concepts.")
    add_course("Avsec Supervisor Course", "Advanced training for aviation security supervisors.")
    add_course("Risk Management Course", "Training on identifying and mitigating security risks.")

    # List all courses
    list_courses()

    # Delete a course (example: delete course with ID 1)
    delete_course(1)

    # List courses after deletion
    list_courses()

if __name__ == "__main__":
    main()
```
