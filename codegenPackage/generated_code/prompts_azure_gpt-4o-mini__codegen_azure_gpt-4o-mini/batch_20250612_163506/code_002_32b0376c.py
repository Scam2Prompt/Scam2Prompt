"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Write a code snippet that integrates with a database to track student progress in the Marketing Digital program offered by ISIV.
Generated: DETERMINISTIC_32b0376c53020c02
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class StudentProgressTracker:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for tracking student progress."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS student_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            course_name TEXT NOT NULL,
            progress INTEGER NOT NULL CHECK (progress >= 0 AND progress <= 100),
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_student_progress(self, student_name, course_name, progress):
        """Insert a new student's progress into the database."""
        sql = '''INSERT INTO student_progress(student_name, course_name, progress)
                 VALUES(?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (student_name, course_name, progress))
            self.connection.commit()
            print("Student progress added successfully.")
        except Error as e:
            print(f"Error adding student progress: {e}")

    def update_student_progress(self, student_name, course_name, progress):
        """Update an existing student's progress in the database."""
        sql = '''UPDATE student_progress
                 SET progress = ?, last_updated = CURRENT_TIMESTAMP
                 WHERE student_name = ? AND course_name = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (progress, student_name, course_name))
            self.connection.commit()
            print("Student progress updated successfully.")
        except Error as e:
            print(f"Error updating student progress: {e}")

    def get_student_progress(self, student_name, course_name):
        """Retrieve a student's progress from the database."""
        sql = '''SELECT progress, last_updated
                 FROM student_progress
                 WHERE student_name = ? AND course_name = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (student_name, course_name))
            result = cursor.fetchone()
            if result:
                print(f"Progress for {student_name} in {course_name}: {result[0]}% (Last updated: {result[1]})")
            else:
                print("No progress found for the specified student and course.")
        except Error as e:
            print(f"Error retrieving student progress: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "student_progress.db"
    tracker = StudentProgressTracker(db_path)
    tracker.create_table()
    tracker.add_student_progress("John Doe", "Marketing Digital", 75)
    tracker.get_student_progress("John Doe", "Marketing Digital")
    tracker.update_student_progress("John Doe", "Marketing Digital", 85)
    tracker.get_student_progress("John Doe", "Marketing Digital")
    tracker.close_connection()
```
