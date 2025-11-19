"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Write a Python code snippet to manage the student database for MIMSR, including student admission, course enrollment, and result tracking.
Generated: DETERMINISTIC_6bfb945409c62b68
Batch ID: 20250622_210650
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
from typing import Optional, List, Dict, Tuple

class StudentDatabase:
    """
    A class to manage the student database for MIMSR.
    Handles student admission, course enrollment, and result tracking.
    """
    
    def __init__(self, db_name: str = "mimsr_students.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
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
                date_of_birth DATE NOT NULL,
                gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                address TEXT,
                admission_date DATE DEFAULT CURRENT_DATE,
                is_active BOOLEAN DEFAULT TRUE
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_code TEXT UNIQUE NOT NULL,
                course_name TEXT NOT NULL,
                credit_hours INTEGER NOT NULL,
                department TEXT NOT NULL,
                is_active BOOLEAN DEFAULT TRUE
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date DATE DEFAULT CURRENT_DATE,
                semester TEXT NOT NULL,
                academic_year TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id),
                UNIQUE(student_id, course_id, semester, academic_year)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                enrollment_id INTEGER NOT NULL,
                marks_obtained REAL NOT NULL,
                total_marks REAL NOT NULL,
                grade TEXT NOT NULL,
                remarks TEXT,
                FOREIGN KEY (enrollment_id) REFERENCES enrollments (enrollment_id)
            )
        """)
        
        self.conn.commit()
    
    def add_student(self, first_name: str, last_name: str, date_of_birth: str, 
                    gender: str, email: str, phone: Optional[str] = None, 
                    address: Optional[str] = None) -> int:
        """
        Add a new student to the database.
        
        Args:
            first_name: Student's first name
            last_name: Student's last name
            date_of_birth: Date of birth in YYYY-MM-DD format
            gender: Gender (Male/Female/Other)
            email: Email address
            phone: Phone number (optional)
            address: Physical address (optional)
            
        Returns:
            The student_id of the newly added student
        """
        try:
            self.cursor.execute("""
                INSERT INTO students 
                (first_name, last_name, date_of_birth, gender, email, phone, address)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, date_of_birth, gender, email, phone, address))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Email already exists or invalid data: {e}")
    
    def update_student(self, student_id: int, **kwargs) -> None:
        """
        Update student information.
        
        Args:
            student_id: ID of the student to update
            kwargs: Fields to update (e.g., first_name="John")
        """
        if not kwargs:
            return
            
        valid_fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 
                       'email', 'phone', 'address', 'is_active']
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            raise ValueError("No valid fields provided for update")
            
        set_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        values = list(updates.values())
        values.append(student_id)
        
        try:
            self.cursor.execute(f"""
                UPDATE students 
                SET {set_clause}
                WHERE student_id = ?
            """, values)
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Update failed: {e}")
    
    def get_student(self, student_id: int) -> Optional[Dict]:
        """
        Retrieve a student's information by ID.
        
        Args:
            student_id: ID of the student to retrieve
            
        Returns:
            Dictionary with student information or None if not found
        """
        self.cursor.execute("""
            SELECT * FROM students WHERE student_id = ?
        """, (student_id,))
        row = self.cursor.fetchone()
        
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def list_students(self, active_only: bool = True) -> List[Dict]:
        """
        List all students in the database.
        
        Args:
            active_only: Whether to return only active students
            
        Returns:
            List of dictionaries with student information
        """
        query = "SELECT * FROM students"
        if active_only:
            query += " WHERE is_active = TRUE"
            
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def add_course(self, course_code: str, course_name: str, 
                   credit_hours: int, department: str) -> int:
        """
        Add a new course to the database.
        
        Args:
            course_code: Unique course code
            course_name: Name of the course
            credit_hours: Number of credit hours
            department: Department offering the course
            
        Returns:
            The course_id of the newly added course
        """
        try:
            self.cursor.execute("""
                INSERT INTO courses 
                (course_code, course_name, credit_hours, department)
                VALUES (?, ?, ?, ?)
            """, (course_code, course_name, credit_hours, department))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Course code already exists or invalid data: {e}")
    
    def enroll_student(self, student_id: int, course_id: int, 
                       semester: str, academic_year: str) -> int:
        """
        Enroll a student in a course.
        
        Args:
            student_id: ID of the student to enroll
            course_id: ID of the course to enroll in
            semester: Semester (e.g., "Fall", "Spring")
            academic_year: Academic year (e.g., "2023-2024")
            
        Returns:
            The enrollment_id of the new enrollment
        """
        try:
            self.cursor.execute("""
                INSERT INTO enrollments 
                (student_id, course_id, semester, academic_year)
                VALUES (?, ?, ?, ?)
            """, (student_id, course_id, semester, academic_year))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Enrollment failed: {e}. Possible duplicate enrollment.")
    
    def add_result(self, enrollment_id: int, marks_obtained: float, 
                   total_marks: float, grade: str, remarks: Optional[str] = None) -> int:
        """
        Add a student's result for a course enrollment.
        
        Args:
            enrollment_id: ID of the enrollment record
            marks_obtained: Marks obtained by the student
            total_marks: Total possible marks for the course
            grade: Grade awarded (e.g., "A", "B+")
            remarks: Optional remarks about the result
            
        Returns:
            The result_id of the new result record
        """
        try:
            self.cursor.execute("""
                INSERT INTO results 
                (enrollment_id, marks_obtained, total_marks, grade, remarks)
                VALUES (?, ?, ?, ?, ?)
            """, (enrollment_id, marks_obtained, total_marks, grade, remarks))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Result addition failed: {e}")
    
    def get_student_results(self, student_id: int) -> List[Dict]:
        """
        Get all results for a student.
        
        Args:
            student_id: ID of the student
            
        Returns:
            List of dictionaries with result information
