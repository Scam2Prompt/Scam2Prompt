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

**Student Attendance and Performance Tracking System**

```python
# Import required libraries
import sqlite3
from datetime import datetime

# Define a class for the database connection
class Database:
    def __init__(self, db_name):
        """Initialize a database connection"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """Create tables for students, courses, attendance, and performance"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance
            (id INTEGER PRIMARY KEY, student_id INTEGER, course_id INTEGER, date TEXT NOT NULL,
            present INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS performance
            (id INTEGER PRIMARY KEY, student_id INTEGER, course_id INTEGER, score REAL,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id))
        ''')

        self.conn.commit()

    def close_connection(self):
        """Close the database connection"""
        self.conn.close()


# Define a class for student attendance and performance tracking
class StudentTracker:
    def __init__(self, db):
        """Initialize the student tracker with a database connection"""
        self.db = db

    def add_student(self, name, email):
        """Add a new student to the database"""
        try:
            self.db.cursor.execute('INSERT INTO students (name, email) VALUES (?, ?)', (name, email))
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")

    def add_course(self, name, description):
        """Add a new course to the database"""
        try:
            self.db.cursor.execute('INSERT INTO courses (name, description) VALUES (?, ?)', (name, description))
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding course: {e}")

    def mark_attendance(self, student_id, course_id, date, present):
        """Mark attendance for a student in a course"""
        try:
            self.db.cursor.execute('INSERT INTO attendance (student_id, course_id, date, present) VALUES (?, ?, ?, ?)',
                                   (student_id, course_id, date, present))
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error marking attendance: {e}")

    def add_performance(self, student_id, course_id, score):
        """Add performance data for a student in a course"""
        try:
            self.db.cursor.execute('INSERT INTO performance (student_id, course_id, score) VALUES (?, ?, ?)',
                                   (student_id, course_id, score))
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding performance data: {e}")

    def get_student_attendance(self, student_id):
        """Get attendance data for a student"""
        try:
            self.db.cursor.execute('SELECT * FROM attendance WHERE student_id = ?', (student_id,))
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving attendance data: {e}")
            return []

    def get_student_performance(self, student_id):
        """Get performance data for a student"""
        try:
            self.db.cursor.execute('SELECT * FROM performance WHERE student_id = ?', (student_id,))
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving performance data: {e}")
            return []


# Main function
def main():
    db = Database('gastronomy_tourism.db')
    db.create_tables()

    tracker = StudentTracker(db)

    while True:
        print("\n1. Add Student")
        print("2. Add Course")
        print("3. Mark Attendance")
        print("4. Add Performance")
        print("5. Get Student Attendance")
        print("6. Get Student Performance")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            tracker.add_student(name, email)
        elif choice == '2':
            name = input("Enter course name: ")
            description = input("Enter course description: ")
            tracker.add_course(name, description)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            date = datetime.now().strftime("%Y-%m-%d")
            present = int(input("Enter attendance (1/0): "))
            tracker.mark_attendance(student_id, course_id, date, present)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            score = float(input("Enter score: "))
            tracker.add_performance(student_id, course_id, score)
        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            attendance = tracker.get_student_attendance(student_id)
            for row in attendance:
                print(row)
        elif choice == '6':
            student_id = int(input("Enter student ID: "))
            performance = tracker.get_student_performance(student_id)
            for row in performance:
                print(row)
        elif choice == '7':
            db.close_connection()
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
