"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Create a basic structure for a school management system using a database, including tables for students, teachers, and courses, reflecting the bilingual education system of Del Sol Montessori."
Generated: DETERMINISTIC_0fb9484d0fad6b09
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict

class SchoolManagementSystem:
    """
    A basic school management system for Del Sol Montessori bilingual education.
    Manages students, teachers, and courses in a SQLite database.
    """
    
    def __init__(self, db_name: str = "del_sol_montessori.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the necessary tables in the database."""
        # Students table (bilingual fields)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name_en TEXT NOT NULL,
                last_name_en TEXT NOT NULL,
                first_name_es TEXT NOT NULL,
                last_name_es TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                grade_level INTEGER NOT NULL,
                enrollment_date TEXT NOT NULL,
                is_active INTEGER DEFAULT 1
            )
        """)
        
        # Teachers table (bilingual fields)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name_en TEXT NOT NULL,
                last_name_en TEXT NOT NULL,
                first_name_es TEXT NOT NULL,
                last_name_es TEXT NOT NULL,
                hire_date TEXT NOT NULL,
                specialization_en TEXT NOT NULL,
                specialization_es TEXT NOT NULL,
                is_active INTEGER DEFAULT 1
            )
        """)
        
        # Courses table (bilingual fields)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_en TEXT NOT NULL,
                name_es TEXT NOT NULL,
                description_en TEXT,
                description_es TEXT,
                grade_level INTEGER NOT NULL,
                is_bilingual INTEGER DEFAULT 1
            )
        """)
        
        # Student-Course enrollment table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_courses (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        """)
        
        # Teacher-Course assignment table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teacher_courses (
                assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                teacher_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                assignment_date TEXT NOT NULL,
                FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        """)
        
        self.conn.commit()
    
    def add_student(self, first_name_en: str, last_name_en: str, 
                   first_name_es: str, last_name_es: str,
                   birth_date: str, grade_level: int, 
                   enrollment_date: str) -> int:
        """Add a new student to the database."""
        try:
            self.cursor.execute("""
                INSERT INTO students 
                (first_name_en, last_name_en, first_name_es, last_name_es,
                 birth_date, grade_level, enrollment_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (first_name_en, last_name_en, first_name_es, last_name_es,
                  birth_date, grade_level, enrollment_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def add_teacher(self, first_name_en: str, last_name_en: str,
                   first_name_es: str, last_name_es: str,
                   hire_date: str, specialization_en: str,
                   specialization_es: str) -> int:
        """Add a new teacher to the database."""
        try:
            self.cursor.execute("""
                INSERT INTO teachers 
                (first_name_en, last_name_en, first_name_es, last_name_es,
                 hire_date, specialization_en, specialization_es)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (first_name_en, last_name_en, first_name_es, last_name_es,
                  hire_date, specialization_en, specialization_es))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def add_course(self, name_en: str, name_es: str,
                  description_en: Optional[str], description_es: Optional[str],
                  grade_level: int, is_bilingual: bool = True) -> int:
        """Add a new course to the database."""
        try:
            self.cursor.execute("""
                INSERT INTO courses 
                (name_en, name_es, description_en, description_es,
                 grade_level, is_bilingual)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name_en, name_es, description_en, description_es,
                  grade_level, int(is_bilingual)))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def enroll_student_in_course(self, student_id: int, course_id: int,
                               enrollment_date: str) -> int:
        """Enroll a student in a course."""
        try:
            self.cursor.execute("""
                INSERT INTO student_courses 
                (student_id, course_id, enrollment_date)
                VALUES (?, ?, ?)
            """, (student_id, course_id, enrollment_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def assign_teacher_to_course(self, teacher_id: int, course_id: int,
                               assignment_date: str) -> int:
        """Assign a teacher to a course."""
        try:
            self.cursor.execute("""
                INSERT INTO teacher_courses 
                (teacher_id, course_id, assignment_date)
                VALUES (?, ?, ?)
            """, (teacher_id, course_id, assignment_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def get_students(self, active_only: bool = True) -> List[Dict]:
        """Retrieve all students from the database."""
        query = "SELECT * FROM students"
        if active_only:
            query += " WHERE is_active = 1"
        
        self.cursor.execute(query)
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_teachers(self, active_only: bool = True) -> List[Dict]:
        """Retrieve all teachers from the database."""
        query = "SELECT * FROM teachers"
        if active_only:
            query += " WHERE is_active = 1"
        
        self.cursor.execute(query)
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_courses(self) -> List[Dict]:
        """Retrieve all courses from the database."""
        self.cursor.execute("SELECT * FROM courses")
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the connection."""
        self.close()
```
