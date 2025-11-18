"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Write Python code to create a database schema for managing student enrollments in courses like "Cocina Nacional e Internacional," "Pastelería y Panificación," and "Bar y Mixología" offered by Egatur.
Generated: DETERMINISTIC_def13568ae0dba9a
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Function to create the database schema
def create_database_schema():
    try:
        # Connect to the SQLite database (or create it)
        connection = sqlite3.connect('egatur_enrollments.db')
        cursor = connection.cursor()

        # Create table for students
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT
        );
        ''')

        # Create table for courses
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL UNIQUE
        );
        ''')

        # Create table for enrollments (relationship between Students and Courses)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
            FOREIGN KEY (student_id) REFERENCES Students (student_id),
            FOREIGN KEY (course_id) REFERENCES Courses (course_id),
            UNIQUE (student_id, course_id)
        );
        ''')

        # Populate the Courses table with initial data
        courses = [
            ('Cocina Nacional e Internacional',),
            ('Pastelería y Panificación',),
            ('Bar y Mixología',)
        ]
        cursor.executemany('''
        INSERT OR IGNORE INTO Courses (course_name)
        VALUES (?);
        ''', courses)

        # Commit changes and close connection
        connection.commit()
        print("Database schema created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()

# Main entry point
if __name__ == "__main__":
    create_database_schema()
```
