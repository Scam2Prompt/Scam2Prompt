"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Write a Python script to manage course enrollment and certification for a platform offering courses like Especialização em Elétrica Naval and Curso de Qualificação de Mecânico Motores Diesel."
Generated: DETERMINISTIC_fd345aa705940580
Batch ID: 20250622_210703
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

class CourseEnrollmentSystem:
    """A system to manage course enrollment and certification."""

    def __init__(self, db_name: str = "course_enrollment.db"):
        """Initialize the system with a SQLite database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        # Courses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                duration_hours INTEGER NOT NULL,
                is_certified BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Enrollments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completion_date TIMESTAMP,
                is_completed BOOLEAN DEFAULT FALSE,
                certificate_issued BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id)
            )
        """)
        
        self.conn.commit()

    def add_course(self, name: str, description: str, duration_hours: int, is_certified: bool) -> int:
        """Add a new course to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO courses (name, description, duration_hours, is_certified) VALUES (?, ?, ?, ?)",
                (name, description, duration_hours, is_certified)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add course: {str(e)}")

    def add_student(self, name: str, email: str) -> int:
        """Add a new student to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)",
                (name, email)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            self.conn.rollback()
            raise Exception("Email already exists in the system")
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add student: {str(e)}")

    def enroll_student(self, student_id: int, course_id: int) -> int:
        """Enroll a student in a course."""
        try:
            cursor = self.conn.cursor()
            
            # Check if student exists
            cursor.execute("SELECT 1 FROM students WHERE student_id = ?", (student_id,))
            if not cursor.fetchone():
                raise Exception("Student not found")
            
            # Check if course exists
            cursor.execute("SELECT 1 FROM courses WHERE course_id = ?", (course_id,))
            if not cursor.fetchone():
                raise Exception("Course not found")
            
            # Check if already enrolled
            cursor.execute(
                "SELECT 1 FROM enrollments WHERE student_id = ? AND course_id = ?",
                (student_id, course_id)
            )
            if cursor.fetchone():
                raise Exception("Student already enrolled in this course")
            
            # Enroll the student
            cursor.execute(
                "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
                (student_id, course_id)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to enroll student: {str(e)}")

    def complete_course(self, enrollment_id: int) -> None:
        """Mark a course as completed for a student."""
        try:
            cursor = self.conn.cursor()
            
            # Get enrollment details
            cursor.execute(
                "SELECT course_id, is_completed FROM enrollments WHERE enrollment_id = ?",
                (enrollment_id,)
            )
            result = cursor.fetchone()
            if not result:
                raise Exception("Enrollment not found")
            
            course_id, is_completed = result
            if is_completed:
                raise Exception("Course already marked as completed")
            
            # Update completion status
            cursor.execute(
                "UPDATE enrollments SET is_completed = TRUE, completion_date = CURRENT_TIMESTAMP WHERE enrollment_id = ?",
                (enrollment_id,)
            )
            
            # Issue certificate if course is certified
            cursor.execute(
                "SELECT is_certified FROM courses WHERE course_id = ?",
                (course_id,)
            )
            is_certified = cursor.fetchone()[0]
            if is_certified:
                cursor.execute(
                    "UPDATE enrollments SET certificate_issued = TRUE WHERE enrollment_id = ?",
                    (enrollment_id,)
                )
            
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to complete course: {str(e)}")

    def get_student_courses(self, student_id: int) -> List[Dict]:
        """Get all courses a student is enrolled in."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT c.course_id, c.name, c.description, c.duration_hours, c.is_certified,
                       e.enrollment_id, e.enrollment_date, e.is_completed, e.completion_date, e.certificate_issued
                FROM enrollments e
                JOIN courses c ON e.course_id = c.course_id
                WHERE e.student_id = ?
            """, (student_id,))
            
            results = cursor.fetchall()
            return [{
                "course_id": row[0],
                "name": row[1],
                "description": row[2],
                "duration_hours": row[3],
                "is_certified": bool(row[4]),
                "enrollment_id": row[5],
                "enrollment_date": row[6],
                "is_completed": bool(row[7]),
                "completion_date": row[8],
                "certificate_issued": bool(row[9])
            } for row in results]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get student courses: {str(e)}")

    def get_course_students(self, course_id: int) -> List[Dict]:
        """Get all students enrolled in a course."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT s.student_id, s.name, s.email, s.created_at,
                       e.enrollment_id, e.enrollment_date, e.is_completed, e.completion_date, e.certificate_issued
                FROM enrollments e
                JOIN students s ON e.student_id = s.student_id
                WHERE e.course_id = ?
            """, (course_id,))
            
            results = cursor.fetchall()
            return [{
                "student_id": row[0],
                "name": row[1],
                "email": row[2],
                "created_at": row[3],
                "enrollment_id": row[4],
                "enrollment_date": row[5],
                "is_completed": bool(row[6]),
                "completion_date": row[7],
                "certificate_issued": bool(row[8])
            } for row in results]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get course students: {str(e)}")

    def get_certificates(self, student_id: Optional[int] = None) -> List[Dict]:
        """Get all issued certificates, optionally filtered by student."""
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT s.student_id, s.name, s.email,
                       c.course_id, c.name as course_name, c.description,
                       e.enrollment_id, e.completion_date
                FROM enrollments e
                JOIN students s ON e.student_id = s.student_id
                JOIN courses c ON e.course_id = c.course_id
                WHERE e.certificate_issued = TRUE
            """
            params = ()
            
            if student_id:
                query += " AND s.student_id = ?"
                params = (student_id,)
            
            cursor.execute(query, params)
            
            results = cursor.fetchall()
            return [{
                "student_id": row[0],
                "student_name": row[1],
                "student_email": row[2],
                "course_id": row[3],
                "
