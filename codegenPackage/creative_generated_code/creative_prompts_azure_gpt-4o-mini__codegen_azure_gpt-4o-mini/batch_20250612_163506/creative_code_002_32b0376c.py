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
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the students table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            progress INTEGER NOT NULL CHECK (progress >= 0 AND progress <= 100)
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Created table: students")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_student(self, name):
        """Add a new student to the database."""
        sql = "INSERT INTO students (name, progress) VALUES (?, ?)"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, 0))
            self.connection.commit()
            print(f"Added student: {name}")
        except Error as e:
            print(f"Error adding student: {e}")

    def update_progress(self, student_id, progress):
        """Update the progress of a student."""
        if not (0 <= progress <= 100):
            print("Progress must be between 0 and 100.")
            return
        sql = "UPDATE students SET progress = ? WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (progress, student_id))
            self.connection.commit()
            print(f"Updated progress for student ID {student_id} to {progress}%")
        except Error as e:
            print(f"Error updating progress: {e}")

    def get_student_progress(self, student_id):
        """Retrieve the progress of a student."""
        sql = "SELECT name, progress FROM students WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (student_id,))
            student = cursor.fetchone()
            if student:
                print(f"Student: {student[0]}, Progress: {student[1]}%")
                return student
            else:
                print(f"No student found with ID {student_id}")
        except Error as e:
            print(f"Error retrieving student progress: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Example usage
    tracker = StudentProgressTracker("isiv_marketing.db")
    tracker.create_table()
    tracker.add_student("John Doe")
    tracker.update_progress(1, 75)
    tracker.get_student_progress(1)
    tracker.close_connection()
```
