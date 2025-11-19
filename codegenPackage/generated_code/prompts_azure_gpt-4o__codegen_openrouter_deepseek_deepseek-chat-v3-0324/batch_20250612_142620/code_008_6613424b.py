"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate code for a registration system that allows students to enroll in programs like JEE, NEET, CUET, and Foundation, with options for offline learning and online testing, as detailed by Potencia Academy.
Generated: DETERMINISTIC_6613424b0afc9c02
Batch ID: 20250612_142620
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
from enum import Enum
import re
import hashlib

class ProgramType(Enum):
    JEE = "JEE"
    NEET = "NEET"
    CUET = "CUET"
    FOUNDATION = "Foundation"

class LearningMode(Enum):
    OFFLINE = "Offline"
    ONLINE = "Online"

class TestMode(Enum):
    OFFLINE = "Offline"
    ONLINE = "Online"

class RegistrationSystem:
    def __init__(self, db_name="potencia_academy.db"):
        """Initialize the registration system with database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                registration_date TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                program TEXT NOT NULL,
                learning_mode TEXT NOT NULL,
                test_mode TEXT NOT NULL,
                enrollment_date TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        """)
        self.conn.commit()

    def _validate_email(self, email):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def _validate_phone(self, phone):
        """Validate phone number format (10 digits)."""
        return len(phone) == 10 and phone.isdigit()

    def _hash_password(self, password):
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_student(self, name, email, phone, password):
        """
        Register a new student.
        
        Args:
            name: Student's full name
            email: Valid email address
            phone: 10-digit phone number
            password: Password to be hashed
        
        Returns:
            student_id if successful, None otherwise
        """
        if not all([name, email, phone, password]):
            raise ValueError("All fields are required")
        
        if not self._validate_email(email):
            raise ValueError("Invalid email format")
        
        if not self._validate_phone(phone):
            raise ValueError("Phone must be 10 digits")
        
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        password_hash = self._hash_password(password)
        registration_date = datetime.now().isoformat()
        
        try:
            self.cursor.execute(
                "INSERT INTO students (name, email, phone, password_hash, registration_date) VALUES (?, ?, ?, ?, ?)",
                (name, email, phone, password_hash, registration_date)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already registered")

    def enroll_program(self, student_id, program, learning_mode, test_mode):
        """
        Enroll a student in a program.
        
        Args:
            student_id: ID of registered student
            program: ProgramType enum value
            learning_mode: LearningMode enum value
            test_mode: TestMode enum value
        
        Returns:
            enrollment_id if successful
        """
        if not isinstance(program, ProgramType):
            raise ValueError("Invalid program type")
        
        if not isinstance(learning_mode, LearningMode):
            raise ValueError("Invalid learning mode")
        
        if not isinstance(test_mode, TestMode):
            raise ValueError("Invalid test mode")
        
        # Check if student exists
        self.cursor.execute("SELECT id FROM students WHERE id = ?", (student_id,))
        if not self.cursor.fetchone():
            raise ValueError("Student not found")
        
        enrollment_date = datetime.now().isoformat()
        
        self.cursor.execute(
            "INSERT INTO enrollments (student_id, program, learning_mode, test_mode, enrollment_date) VALUES (?, ?, ?, ?, ?)",
            (student_id, program.value, learning_mode.value, test_mode.value, enrollment_date)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_student_enrollments(self, student_id):
        """Get all enrollments for a student."""
        self.cursor.execute("""
            SELECT e.id, e.program, e.learning_mode, e.test_mode, e.enrollment_date
            FROM enrollments e
            WHERE e.student_id = ?
            ORDER BY e.enrollment_date DESC
        """, (student_id,))
        return self.cursor.fetchall()

    def authenticate_student(self, email, password):
        """
        Authenticate a student.
        
        Returns:
            student_id if authentication succeeds, None otherwise
        """
        password_hash = self._hash_password(password)
        self.cursor.execute(
            "SELECT id FROM students WHERE email = ? AND password_hash = ?",
            (email, password_hash)
        )
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        """Close database connection."""
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
