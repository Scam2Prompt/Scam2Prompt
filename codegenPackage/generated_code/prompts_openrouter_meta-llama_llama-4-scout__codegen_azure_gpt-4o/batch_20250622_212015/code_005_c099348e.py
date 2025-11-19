"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Develop a system to track student attendance and performance in courses related to gastronomy and tourism, using a suitable programming language and database."
Generated: DETERMINISTIC_c099348e6536e30b
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "student_management.db"

# Initialize the database
def initialize_database():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create Students table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """)

        # Create Courses table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
        """)

        # Create Attendance table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES Students(student_id),
            FOREIGN KEY(course_id) REFERENCES Courses(course_id)
        )
        """)

        # Create Performance table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Performance (
            performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            grade TEXT NOT NULL,
            feedback TEXT,
            FOREIGN KEY(student_id) REFERENCES Students(student_id),
            FOREIGN KEY(course_id) REFERENCES Courses(course_id)
        )
        """)

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Add a new student
def add_student(name, email):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

# Add a new course
def add_course(name, category):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Courses (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error adding course: {e}")

# Record attendance
def record_attendance(student_id, course_id, status):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO Attendance (student_id, course_id, date, status) VALUES (?, ?, ?, ?)",
                       (student_id, course_id, date, status))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error recording attendance: {e}")

# Record performance
def record_performance(student_id, course_id, grade, feedback=None):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Performance (student_id, course_id, grade, feedback) VALUES (?, ?, ?, ?)",
                       (student_id, course_id, grade, feedback))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error recording performance: {e}")

# Fetch student details
def fetch_students():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()
        conn.close()
        return students
    except sqlite3.Error as e:
        print(f"Error fetching students: {e}")
        return []

# Fetch course details
def fetch_courses():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        courses = cursor.fetchall()
        conn.close()
        return courses
    except sqlite3.Error as e:
        print(f"Error fetching courses: {e}")
        return []

# Fetch attendance records
def fetch_attendance():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT a.attendance_id, s.name AS student_name, c.name AS course_name, a.date, a.status
        FROM Attendance a
        JOIN Students s ON a.student_id = s.student_id
        JOIN Courses c ON a.course_id = c.course_id
        """)
        attendance_records = cursor.fetchall()
        conn.close()
        return attendance_records
    except sqlite3.Error as e:
        print(f"Error fetching attendance records: {e}")
        return []

# Fetch performance records
def fetch_performance():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT p.performance_id, s.name AS student_name, c.name AS course_name, p.grade, p.feedback
        FROM Performance p
        JOIN Students s ON p.student_id = s.student_id
        JOIN Courses c ON p.course_id = c.course_id
        """)
        performance_records = cursor.fetchall()
        conn.close()
        return performance_records
    except sqlite3.Error as e:
        print(f"Error fetching performance records: {e}")
        return []

# Main function for testing
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample data
    add_student("Alice Johnson", "alice@example.com")
    add_student("Bob Smith", "bob@example.com")
    add_course("Introduction to Gastronomy", "Gastronomy")
    add_course("Tourism Management", "Tourism")

    # Record attendance
    record_attendance(1, 1, "Present")
    record_attendance(2, 2, "Absent")

    # Record performance
    record_performance(1, 1, "A", "Excellent work!")
    record_performance(2, 2, "B", "Needs improvement.")

    # Fetch and display data
    print("Students:", fetch_students())
    print("Courses:", fetch_courses())
    print("Attendance Records:", fetch_attendance())
    print("Performance Records:", fetch_performance())
```
