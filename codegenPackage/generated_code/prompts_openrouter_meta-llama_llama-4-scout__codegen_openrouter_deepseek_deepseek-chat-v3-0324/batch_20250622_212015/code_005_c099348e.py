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
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class StudentAttendanceSystem:
    """
    A system to track student attendance and performance in gastronomy and tourism courses.
    Uses SQLite as the database backend.
    """
    
    def __init__(self, db_name: str = "student_attendance.db"):
        """
        Initialize the system with a database connection.
        Creates tables if they don't exist.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                enrollment_date TEXT NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                course_code TEXT UNIQUE NOT NULL,
                description TEXT,
                credits INTEGER NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id),
                UNIQUE(student_id, course_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                enrollment_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('present', 'absent', 'late', 'excused')),
                FOREIGN KEY (enrollment_id) REFERENCES enrollments (enrollment_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                enrollment_id INTEGER NOT NULL,
                assignment_name TEXT NOT NULL,
                grade REAL NOT NULL,
                max_grade REAL NOT NULL,
                date_recorded TEXT NOT NULL,
                FOREIGN KEY (enrollment_id) REFERENCES enrollments (enrollment_id)
            )
        """)
        
        self.conn.commit()
    
    def add_student(self, first_name: str, last_name: str, email: str) -> int:
        """
        Add a new student to the system.
        Returns the student_id of the newly added student.
        """
        try:
            enrollment_date = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (?, ?, ?, ?)",
                (first_name, last_name, email, enrollment_date)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists in the system")
    
    def add_course(self, course_name: str, course_code: str, description: str, credits: int) -> int:
        """
        Add a new course to the system.
        Returns the course_id of the newly added course.
        """
        try:
            self.cursor.execute(
                "INSERT INTO courses (course_name, course_code, description, credits) VALUES (?, ?, ?, ?)",
                (course_name, course_code, description, credits)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Course code already exists in the system")
    
    def enroll_student(self, student_id: int, course_id: int) -> int:
        """
        Enroll a student in a course.
        Returns the enrollment_id of the new enrollment.
        """
        try:
            enrollment_date = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute(
                "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
                (student_id, course_id, enrollment_date)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Student is already enrolled in this course")
    
    def record_attendance(self, enrollment_id: int, date: str, status: str) -> int:
        """
        Record attendance for a student in a course.
        Returns the attendance_id of the new record.
        """
        try:
            self.cursor.execute(
                "INSERT INTO attendance (enrollment_id, date, status) VALUES (?, ?, ?)",
                (enrollment_id, date, status)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Attendance already recorded for this student on this date")
    
    def record_grade(self, enrollment_id: int, assignment_name: str, grade: float, max_grade: float) -> int:
        """
        Record a grade for a student in a course.
        Returns the grade_id of the new record.
        """
        try:
            date_recorded = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute(
                "INSERT INTO grades (enrollment_id, assignment_name, grade, max_grade, date_recorded) VALUES (?, ?, ?, ?, ?)",
                (enrollment_id, assignment_name, grade, max_grade, date_recorded)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            raise ValueError(f"Error recording grade: {str(e)}")
    
    def get_student_attendance(self, student_id: int, course_id: int) -> List[Dict]:
        """
        Get attendance records for a student in a specific course.
        Returns a list of attendance records as dictionaries.
        """
        self.cursor.execute("""
            SELECT a.date, a.status 
            FROM attendance a
            JOIN enrollments e ON a.enrollment_id = e.enrollment_id
            WHERE e.student_id = ? AND e.course_id = ?
            ORDER BY a.date
        """, (student_id, course_id))
        
        return [{"date": row[0], "status": row[1]} for row in self.cursor.fetchall()]
    
    def get_student_grades(self, student_id: int, course_id: int) -> List[Dict]:
        """
        Get grade records for a student in a specific course.
        Returns a list of grade records as dictionaries.
        """
        self.cursor.execute("""
            SELECT g.assignment_name, g.grade, g.max_grade, g.date_recorded
            FROM grades g
            JOIN enrollments e ON g.enrollment_id = e.enrollment_id
            WHERE e.student_id = ? AND e.course_id = ?
            ORDER BY g.date_recorded
        """, (student_id, course_id))
        
        return [{
            "assignment_name": row[0],
            "grade": row[1],
            "max_grade": row[2],
            "date_recorded": row[3]
        } for row in self.cursor.fetchall()]
    
    def get_course_average(self, course_id: int) -> Optional[float]:
        """
        Calculate the average grade for all students in a course.
        Returns None if no grades exist for the course.
        """
        self.cursor.execute("""
            SELECT AVG(g.grade / g.max_grade * 100)
            FROM grades g
            JOIN enrollments e ON g.enrollment_id = e.enrollment_id
            WHERE e.course_id = ?
        """, (course_id,))
        
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else None
    
    def get_student_average(self, student_id: int, course_id: int) -> Optional[float]:
        """
        Calculate the average grade for a student in a course.
        Returns None if no grades exist for the student in this course.
        """
        self.cursor.execute("""
            SELECT AVG(g.grade / g.max_grade * 100)
            FROM grades g
            JOIN enrollments e ON g.enrollment_id = e.enrollment_id
            WHERE e.student_id = ? AND e.course_id = ?
        """, (student_id, course_id))
        
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else None
    
    def get_attendance_rate(self, student_id: int, course_id: int) -> Tuple[int, int, float]:
        """
        Calculate attendance rate for a student in a course.
        Returns tuple of (present_count, total_days, attendance_rate).
        """
        self.cursor.execute("""
            SELECT COUNT(*),
                   SUM(CASE WHEN status = 'present' THEN 1 ELSE 0 END)
            FROM attendance a
            JOIN enrollments e ON a.enrollment_id = e.enrollment_id
            WHERE e.student_id = ? AND e
