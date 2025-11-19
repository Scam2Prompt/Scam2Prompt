"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Write Python code to create a database schema for managing student enrollments in courses like "Cocina Nacional e Internacional," "Pastelería y Panificación," and "Bar y Mixología" offered by Egatur.
Generated: DETERMINISTIC_def13568ae0dba9a
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from sqlite3 import Error

class EgaturDatabase:
    def __init__(self, db_file):
        """
        Initialize a connection to the SQLite database.

        Args:
            db_file (str): Path to the SQLite database file.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite Database at {db_file}")
        except Error as e:
            print(e)

    def create_tables(self):
        """
        Create the database schema for managing student enrollments.
        """
        # Create table for courses
        create_courses_table = """
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                description TEXT
            );
        """
        try:
            self.conn.execute(create_courses_table)
        except Error as e:
            print(e)

        # Create table for students
        create_students_table = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """
        try:
            self.conn.execute(create_students_table)
        except Error as e:
            print(e)

        # Create table for enrollments
        create_enrollments_table = """
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date DATE NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id)
            );
        """
        try:
            self.conn.execute(create_enrollments_table)
        except Error as e:
            print(e)

        # Insert courses offered by Egatur
        insert_courses = """
            INSERT OR IGNORE INTO courses (course_name, description)
            VALUES
                ('Cocina Nacional e Internacional', 'Course on national and international cuisine'),
                ('Pastelería y Panificación', 'Course on pastry and bread making'),
                ('Bar y Mixología', 'Course on bartending and mixology');
        """
        try:
            self.conn.execute(insert_courses)
            self.conn.commit()
        except Error as e:
            print(e)

    def close_connection(self):
        """
        Close the connection to the SQLite database.
        """
        if self.conn:
            self.conn.close()
            print("SQLite Connection is closed")

def main():
    database = EgaturDatabase('egatur.db')
    database.create_tables()
    database.close_connection()

if __name__ == '__main__':
    main()
```
