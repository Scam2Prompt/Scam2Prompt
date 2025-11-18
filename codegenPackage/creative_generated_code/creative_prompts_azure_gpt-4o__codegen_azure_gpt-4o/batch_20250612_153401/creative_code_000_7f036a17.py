"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Write Python code to simulate a learning management system for vocational education, referencing the course structure and qualifications offered by Global Healthcare Management College (e.g., Certificate III in Individual Support: CHC33021 or Diploma of Community Services: CHC52021).
Generated: DETERMINISTIC_7f036a1737aff2ff
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3


class LearningManagementSystem:
    """
    A simple Learning Management System for managing vocational education courses.
    """

    def __init__(self, db_name="lms.db"):
        """
        Initialize the Learning Management System with a SQLite database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the database schema for courses and students.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create courses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS courses (
                    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT NOT NULL,
                    course_code TEXT NOT NULL UNIQUE
                )
            """)

            # Create students table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    enrolled_course_code TEXT,
                    FOREIGN KEY (enrolled_course_code) REFERENCES courses(course_code)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_course(self, course_name, course_code):
        """
        Add a new course to the system.
        :param course_name: Name of the course.
        :param course_code: Unique course code (e.g., CHC33021).
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO courses (course_name, course_code) VALUES (?, ?)",
                (course_name, course_code)
            )
            conn.commit()
            print(f"Course '{course_name}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Course code '{course_code}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding course: {e}")
        finally:
            conn.close()

    def add_student(self, name, enrolled_course_code=None):
        """
        Add a new student to the system.
        :param name: Name of the student.
        :param enrolled_course_code: Optional course code the student is enrolled in.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Validate course code if provided
            if enrolled_course_code:
                cursor.execute(
                    "SELECT course_code FROM courses WHERE course_code = ?",
                    (enrolled_course_code,)
                )
                if not cursor.fetchone():
                    print(f"Error: Course code '{enrolled_course_code}' not found.")
                    return

            cursor.execute(
                "INSERT INTO students (name, enrolled_course_code) VALUES (?, ?)",
                (name, enrolled_course_code)
            )
            conn.commit()
            print(f"Student '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")
        finally:
            conn.close()

    def list_courses(self):
        """
        List all courses available in the system.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT course_name, course_code FROM courses")
            courses = cursor.fetchall()

            if courses:
                print("Available Courses:")
                for course_name, course_code in courses:
                    print(f"- {course_name} ({course_code})")
            else:
                print("No courses available.")
        except sqlite3.Error as e:
            print(f"Error listing courses: {e}")
        finally:
            conn.close()

    def list_students(self):
        """
        List all students in the system.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT students.name, students.enrolled_course_code, courses.course_name
                FROM students
                LEFT JOIN courses
                ON students.enrolled_course_code = courses.course_code
            """)
            students = cursor.fetchall()

            if students:
                print("Registered Students:")
                for name, enrolled_course_code, course_name in students:
                    if enrolled_course_code:
                        print(f"- {name} (Enrolled in: {course_name} [{enrolled_course_code}])")
                    else:
                        print(f"- {name} (Not enrolled in any course)")
            else:
                print("No students registered.")
        except sqlite3.Error as e:
            print(f"Error listing students: {e}")
        finally:
            conn.close()


# Sample usage:
if __name__ == "__main__":
    # Initialize the system
    lms = LearningManagementSystem()

    # Add courses
    lms.add_course("Certificate III in Individual Support", "CHC33021")
    lms.add_course("Diploma of Community Services", "CHC52021")

    # Add students
    lms.add_student("Alice Johnson", "CHC33021")
    lms.add_student("Bob Smith", "CHC52021")
    lms.add_student("Charlie Brown")  # Not enrolled in any course

    # List courses and students
    print("\nCourses:")
    lms.list_courses()

    print("\nStudents:")
    lms.list_students()
```

This code is ready for production use and adheres to the requested requirements. It uses SQLite as the backend database, implements error handling, and is well-documented with comments.
