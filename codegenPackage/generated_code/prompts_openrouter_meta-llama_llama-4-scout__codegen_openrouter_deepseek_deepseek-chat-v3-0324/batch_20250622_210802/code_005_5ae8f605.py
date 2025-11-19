"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Design a system to track student progress and certification for various courses offered by Global Healthcare Management College, including the Advanced Diploma of Civil Construction Design (RII60520).
Generated: DETERMINISTIC_5ae8f605d220a69c
Batch ID: 20250622_210802
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
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# Database configuration
DATABASE_NAME = "ghmc_student_progress.db"

class StudentProgressTracker:
    """
    A system to track student progress and certification for courses at Global Healthcare Management College.
    """
    
    def __init__(self):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(DATABASE_NAME)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables in the database."""
        cursor = self.conn.cursor()
        
        # Courses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id TEXT PRIMARY KEY,
                course_name TEXT NOT NULL,
                description TEXT,
                duration_months INTEGER,
                is_active BOOLEAN DEFAULT 1
            )
        """)
        
        # Students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                enrollment_date DATE NOT NULL
            )
        """)
        
        # Modules table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS modules (
                module_id TEXT PRIMARY KEY,
                course_id TEXT NOT NULL,
                module_name TEXT NOT NULL,
                description TEXT,
                credits INTEGER NOT NULL,
                FOREIGN KEY (course_id) REFERENCES courses (course_id)
            )
        """)
        
        # Student progress table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_progress (
                progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                module_id TEXT NOT NULL,
                completion_status TEXT NOT NULL CHECK(completion_status IN ('Not Started', 'In Progress', 'Completed')),
                completion_date DATE,
                grade TEXT CHECK(grade IN ('A', 'B', 'C', 'D', 'F', '')),
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (module_id) REFERENCES modules (module_id),
                UNIQUE(student_id, module_id)
            )
        """)
        
        # Certifications table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certifications (
                certification_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                course_id TEXT NOT NULL,
                issue_date DATE NOT NULL,
                expiry_date DATE,
                is_revoked BOOLEAN DEFAULT 0,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id)
            )
        """)
        
        self.conn.commit()
    
    def add_course(self, course_id: str, course_name: str, description: str, duration_months: int) -> bool:
        """Add a new course to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO courses (course_id, course_name, description, duration_months) VALUES (?, ?, ?, ?)",
                (course_id, course_name, description, duration_months)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def add_student(self, student_id: str, first_name: str, last_name: str, email: str, phone: str = None) -> bool:
        """Add a new student to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO students (student_id, first_name, last_name, email, phone, enrollment_date) VALUES (?, ?, ?, ?, ?, ?)",
                (student_id, first_name, last_name, email, phone, datetime.now().date())
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def add_module(self, module_id: str, course_id: str, module_name: str, description: str, credits: int) -> bool:
        """Add a new module to a course."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO modules (module_id, course_id, module_name, description, credits) VALUES (?, ?, ?, ?, ?)",
                (module_id, course_id, module_name, description, credits)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def update_student_progress(self, student_id: str, module_id: str, status: str, completion_date: str = None, grade: str = None) -> bool:
        """Update a student's progress for a specific module."""
        try:
            cursor = self.conn.cursor()
            
            # Check if record exists
            cursor.execute(
                "SELECT 1 FROM student_progress WHERE student_id = ? AND module_id = ?",
                (student_id, module_id)
            )
            exists = cursor.fetchone()
            
            if exists:
                cursor.execute(
                    """UPDATE student_progress 
                    SET completion_status = ?, 
                        completion_date = ?, 
                        grade = ? 
                    WHERE student_id = ? AND module_id = ?""",
                    (status, completion_date, grade, student_id, module_id)
                )
            else:
                cursor.execute(
                    """INSERT INTO student_progress 
                    (student_id, module_id, completion_status, completion_date, grade) 
                    VALUES (?, ?, ?, ?, ?)""",
                    (student_id, module_id, status, completion_date, grade)
                )
            
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False
    
    def issue_certification(self, student_id: str, course_id: str, expiry_date: str = None) -> bool:
        """Issue a certification to a student for completing a course."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO certifications (student_id, course_id, issue_date, expiry_date) VALUES (?, ?, ?, ?)",
                (student_id, course_id, datetime.now().date(), expiry_date)
            )
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False
    
    def get_student_progress(self, student_id: str) -> List[Dict]:
        """Get all progress records for a student."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT m.module_name, sp.completion_status, sp.completion_date, sp.grade, c.course_name
            FROM student_progress sp
            JOIN modules m ON sp.module_id = m.module_id
            JOIN courses c ON m.course_id = c.course_id
            WHERE sp.student_id = ?
        """, (student_id,))
        
        results = cursor.fetchall()
        return [
            {
                "module_name": row[0],
                "completion_status": row[1],
                "completion_date": row[2],
                "grade": row[3],
                "course_name": row[4]
            }
            for row in results
        ]
    
    def get_course_modules(self, course_id: str) -> List[Dict]:
        """Get all modules for a specific course."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT module_id, module_name, description, credits FROM modules WHERE course_id = ?",
            (course_id,)
        )
        
        results = cursor.fetchall()
        return [
            {
                "module_id": row[0],
                "module_name": row[1],
                "description": row[2],
                "credits": row[3]
            }
            for row in results
        ]
    
    def get_student_certifications(self, student_id: str) -> List[Dict]:
        """Get all certifications for a student."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT c.course_name, cert.issue_date, cert.expiry_date, cert.is_revoked
            FROM certifications cert
            JOIN courses c ON cert.course_id = c.course_id
            WHERE cert.student_id = ?
        """, (student_id,))
        
        results = cursor.fetchall()
        return [
            {
                "course_name": row[0],
                "issue_date": row[1],
                "expiry_date": row[2],
                "is_revoked": bool(row[3])
            }
            for row in results
        ]
    
    def check_course_completion(self, student_id: str, course_id: str) -> Tuple[bool, Optional[Dict]]:
        """
        Check if a student has completed all modules for a course.
        Returns a tuple with completion status and certification details if completed.
        """
        cursor = self.conn.cursor()
        
        # Get total modules in course
        cursor.execute(
            "SELECT COUNT(*) FROM modules WHERE course_id = ?",
            (course_id,)
        )
        total_modules = cursor.fetchone()[0]
        
        # Get completed modules by student
        cursor.execute("""
            SELECT COUNT(*) 
            FROM student_progress sp
            JOIN modules m ON sp.module_id = m.module_id
            WHERE sp.student_id = ? AND m.c
