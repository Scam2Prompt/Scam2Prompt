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
from sqlite3 import Error

class AviationSecurityTrainingDB:
    """A class to manage a simple aviation security training database."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

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
        """Create the courses table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            duration INTEGER,
            level TEXT
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Courses table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_course(self, name, description, duration, level):
        """Add a new course to the database."""
        sql = '''INSERT INTO courses(name, description, duration, level)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, description, duration, level))
            self.connection.commit()
            print(f"Course '{name}' added successfully.")
        except Error as e:
            print(f"Error adding course: {e}")

    def get_courses(self):
        """Retrieve all courses from the database."""
        sql = 'SELECT * FROM courses'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            courses = cursor.fetchall()
            return courses
        except Error as e:
            print(f"Error retrieving courses: {e}")
            return []

    def update_course(self, course_id, name, description, duration, level):
        """Update an existing course in the database."""
        sql = '''UPDATE courses
                 SET name = ?, description = ?, duration = ?, level = ?
                 WHERE id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, description, duration, level, course_id))
            self.connection.commit()
            print(f"Course ID {course_id} updated successfully.")
        except Error as e:
            print(f"Error updating course: {e}")

    def delete_course(self, course_id):
        """Delete a course from the database."""
        sql = 'DELETE FROM courses WHERE id = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (course_id,))
            self.connection.commit()
            print(f"Course ID {course_id} deleted successfully.")
        except Error as e:
            print(f"Error deleting course: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == '__main__':
    db = AviationSecurityTrainingDB('aviation_security_training.db')
    
    # Adding courses
    db.add_course('Basic Avsec Course', 'Introduction to aviation security.', 5, 'Beginner')
    db.add_course('Avsec Supervisor Course', 'Advanced training for supervisors.', 10, 'Intermediate')
    db.add_course('Risk Management Course', 'Understanding risk management in aviation.', 7, 'Advanced')

    # Retrieving and displaying courses
    courses = db.get_courses()
    print("Courses in the database:")
    for course in courses:
        print(course)

    # Updating a course
    db.update_course(1, 'Basic Avsec Course', 'Updated description for basic course.', 6, 'Beginner')

    # Deleting a course
    db.delete_course(3)

    # Closing the database connection
    db.close_connection()
```
