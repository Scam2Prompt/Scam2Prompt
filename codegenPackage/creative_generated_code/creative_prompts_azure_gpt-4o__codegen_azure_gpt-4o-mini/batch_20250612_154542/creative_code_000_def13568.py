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

# Define the database schema for managing student enrollments
class StudentEnrollmentDB:
    def __init__(self, db_name='enrollment.db'):
        """Initialize the database connection and create tables."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables for students, courses, and enrollments."""
        try:
            # Create students table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            ''')

            # Create courses table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT NOT NULL
                )
            ''')

            # Create enrollments table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS enrollments (
                    student_id INTEGER,
                    course_id INTEGER,
                    enrollment_date TEXT NOT NULL,
                    PRIMARY KEY (student_id, course_id),
                    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
                    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating tables: {e}")
            self.connection.rollback()

    def add_student(self, first_name, last_name, email):
        """Add a new student to the students table."""
        try:
            self.cursor.execute('''
                INSERT INTO students (first_name, last_name, email)
                VALUES (?, ?, ?)
            ''', (first_name, last_name, email))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: A student with email '{email}' already exists.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding a student: {e}")
            self.connection.rollback()

    def add_course(self, course_name):
        """Add a new course to the courses table."""
        try:
            self.cursor.execute('''
                INSERT INTO courses (course_name)
                VALUES (?)
            ''', (course_name,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while adding a course: {e}")
            self.connection.rollback()

    def enroll_student(self, student_id, course_id):
        """Enroll a student in a course."""
        try:
            enrollment_date = sqlite3.datetime.datetime.now().isoformat()
            self.cursor.execute('''
                INSERT INTO enrollments (student_id, course_id, enrollment_date)
                VALUES (?, ?, ?)
            ''', (student_id, course_id, enrollment_date))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: Student with ID {student_id} is already enrolled in course ID {course_id}.")
        except sqlite3.Error as e:
            print(f"An error occurred while enrolling a student: {e}")
            self.connection.rollback()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == '__main__':
    db = StudentEnrollmentDB()

    # Adding courses
    db.add_course("Cocina Nacional e Internacional")
    db.add_course("Pastelería y Panificación")
    db.add_course("Bar y Mixología")

    # Adding students
    db.add_student("John", "Doe", "john.doe@example.com")
    db.add_student("Jane", "Smith", "jane.smith@example.com")

    # Enrolling students
    db.enroll_student(1, 1)  # Enroll John in Cocina Nacional e Internacional
    db.enroll_student(2, 2)  # Enroll Jane in Pastelería y Panificación

    db.close()
```
