"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Design a school management system using a library or framework, incorporating features like air-conditioned computer labs and American-style management systems, as seen in Happy Boarding School.
Generated: DETERMINISTIC_486e3330d92c6de6
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py
from datetime import datetime
from typing import List, Optional, Dict
import sqlite3
from sqlite3 import Error
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='school_management.log'
)

class DatabaseManager:
    """Handles database operations for the school management system."""
    
    def __init__(self, db_file: str = "school_management.db"):
        self.db_file = db_file
        self.conn = None
        
    def __enter__(self):
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
    def connect(self) -> None:
        """Establish database connection."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            logging.info("Database connection established")
        except Error as e:
            logging.error(f"Database connection error: {e}")
            raise
            
    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed")
            
    def execute_query(self, query: str, params: tuple = ()) -> None:
        """Execute a SQL query."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
        except Error as e:
            logging.error(f"Query execution error: {e}")
            raise
            
    def fetch_data(self, query: str, params: tuple = ()) -> List[tuple]:
        """Fetch data from database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            logging.error(f"Data fetch error: {e}")
            raise

class Student:
    """Represents a student in the school."""
    
    def __init__(self, student_id: int, name: str, grade: str, dob: str):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.dob = dob
        
    def __str__(self) -> str:
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, DOB: {self.dob}"

class Teacher:
    """Represents a teacher in the school."""
    
    def __init__(self, teacher_id: int, name: str, subject: str, hire_date: str):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.hire_date = hire_date
        
    def __str__(self) -> str:
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}, Hire Date: {self.hire_date}"

class ComputerLab:
    """Represents an air-conditioned computer lab."""
    
    def __init__(self, lab_id: int, name: str, capacity: int, has_ac: bool = True):
        self.lab_id = lab_id
        self.name = name
        self.capacity = capacity
        self.has_ac = has_ac
        
    def __str__(self) -> str:
        ac_status = "with AC" if self.has_ac else "without AC"
        return f"Lab ID: {self.lab_id}, Name: {self.name}, Capacity: {self.capacity}, {ac_status}"

class SchoolManagementSystem:
    """Main school management system class."""
    
    def __init__(self):
        self.db_manager = DatabaseManager()
        self._initialize_database()
        
    def _initialize_database(self) -> None:
        """Initialize database tables if they don't exist."""
        with self.db_manager:
            # Create students table
            self.db_manager.execute_query("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    dob TEXT NOT NULL
                )
            """)
            
            # Create teachers table
            self.db_manager.execute_query("""
                CREATE TABLE IF NOT EXISTS teachers (
                    teacher_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    hire_date TEXT NOT NULL
                )
            """)
            
            # Create computer_labs table
            self.db_manager.execute_query("""
                CREATE TABLE IF NOT EXISTS computer_labs (
                    lab_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    capacity INTEGER NOT NULL,
                    has_ac INTEGER DEFAULT 1
                )
            """)
            
            # Create classes table
            self.db_manager.execute_query("""
                CREATE TABLE IF NOT EXISTS classes (
                    class_id INTEGER PRIMARY KEY,
                    teacher_id INTEGER,
                    subject TEXT NOT NULL,
                    schedule TEXT NOT NULL,
                    lab_id INTEGER,
                    FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id),
                    FOREIGN KEY(lab_id) REFERENCES computer_labs(lab_id)
                )
            """)
            
            # Create enrollments table
            self.db_manager.execute_query("""
                CREATE TABLE IF NOT EXISTS enrollments (
                    enrollment_id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    class_id INTEGER,
                    enrollment_date TEXT NOT NULL,
                    FOREIGN KEY(student_id) REFERENCES students(student_id),
                    FOREIGN KEY(class_id) REFERENCES classes(class_id)
                )
            """)
            
    def add_student(self, student: Student) -> None:
        """Add a new student to the system."""
        with self.db_manager:
            self.db_manager.execute_query(
                "INSERT INTO students VALUES (?, ?, ?, ?)",
                (student.student_id, student.name, student.grade, student.dob)
            )
            logging.info(f"Added student: {student.name}")
            
    def add_teacher(self, teacher: Teacher) -> None:
        """Add a new teacher to the system."""
        with self.db_manager:
            self.db_manager.execute_query(
                "INSERT INTO teachers VALUES (?, ?, ?, ?)",
                (teacher.teacher_id, teacher.name, teacher.subject, teacher.hire_date)
            )
            logging.info(f"Added teacher: {teacher.name}")
            
    def add_computer_lab(self, lab: ComputerLab) -> None:
        """Add a new computer lab to the system."""
        with self.db_manager:
            self.db_manager.execute_query(
                "INSERT INTO computer_labs VALUES (?, ?, ?, ?)",
                (lab.lab_id, lab.name, lab.capacity, 1 if lab.has_ac else 0)
            )
            logging.info(f"Added computer lab: {lab.name}")
            
    def get_all_students(self) -> List[Student]:
        """Retrieve all students from the system."""
        with self.db_manager:
            students_data = self.db_manager.fetch_data("SELECT * FROM students")
            return [
                Student(student_id, name, grade, dob)
                for student_id, name, grade, dob in students_data
            ]
            
    def get_all_teachers(self) -> List[Teacher]:
        """Retrieve all teachers from the system."""
        with self.db_manager:
            teachers_data = self.db_manager.fetch_data("SELECT * FROM teachers")
            return [
                Teacher(teacher_id, name, subject, hire_date)
                for teacher_id, name, subject, hire_date in teachers_data
            ]
            
    def get_all_computer_labs(self) -> List[ComputerLab]:
        """Retrieve all computer labs from the system."""
        with self.db_manager:
            labs_data = self.db_manager.fetch_data("SELECT * FROM computer_labs")
            return [
                ComputerLab(lab_id, name, capacity, bool(has_ac))
                for lab_id, name, capacity, has_ac in labs_data
            ]
            
    def schedule_class(self, teacher_id: int, subject: str, schedule: str, lab_id: Optional[int] = None) -> None:
        """Schedule a new class."""
        with self.db_manager:
            self.db_manager.execute_query(
                "INSERT INTO classes (teacher_id, subject, schedule, lab_id) VALUES (?, ?, ?, ?)",
                (teacher_id, subject, schedule, lab_id)
            )
            logging.info(f"Scheduled class for subject: {subject}")
            
    def enroll_student(self, student_id: int, class_id: int) -> None:
        """Enroll a student in a class."""
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        with self.db_manager:
            self.db_manager.execute_query(
                "INSERT INTO enrollments (student_id, class_id, enrollment_date) VALUES (?, ?, ?)",
                (student_id, class_id, enrollment_date)
            )
            logging.info(f"Enrolled student ID {student_id} in class ID {class_id}")
            
    def get_student_classes(self, student_id: int) -> List[Dict]:
        """Get all classes a student is enrolled in."""
        with self.db_manager:
            query = """
                SELECT c.class_id, t.name as teacher_name, c.subject, c.schedule, l.name as lab_name
                FROM enrollments e
                JOIN classes c ON e.class_id = c.class_id
                JOIN teachers t ON c.teacher_id = t.teacher_id
                LEFT JOIN computer_labs l ON c.lab_id = l.lab_id
