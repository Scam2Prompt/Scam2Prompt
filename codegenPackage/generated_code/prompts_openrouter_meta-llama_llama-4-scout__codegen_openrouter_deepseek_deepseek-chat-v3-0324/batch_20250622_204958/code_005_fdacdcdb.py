"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: "Develop a system for tracking student attendance and performance in a modular certification program like the one offered at Trentino Institute."
Generated: DETERMINISTIC_fdacdcdb0bc468cc
Batch ID: 20250622_204958
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

class DatabaseManager:
    """Handles database operations for the student tracking system."""
    
    def __init__(self, db_name: str = "student_tracking.db"):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_tables()
    
    def _initialize_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                enrollment_date TEXT NOT NULL,
                program_id INTEGER NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS programs (
                program_id INTEGER PRIMARY KEY AUTOINCREMENT,
                program_name TEXT NOT NULL,
                description TEXT,
                duration_weeks INTEGER NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS modules (
                module_id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_name TEXT NOT NULL,
                program_id INTEGER NOT NULL,
                FOREIGN KEY (program_id) REFERENCES programs (program_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                module_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('present', 'absent', 'excused')),
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (module_id) REFERENCES modules (module_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS performance (
                performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                module_id INTEGER NOT NULL,
                score REAL NOT NULL,
                assessment_date TEXT NOT NULL,
                comments TEXT,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (module_id) REFERENCES modules (module_id)
            )
        """)
        
        self.conn.commit()
    
    def add_student(self, first_name: str, last_name: str, email: str, program_id: int) -> int:
        """Add a new student to the database."""
        try:
            enrollment_date = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date, program_id)
                VALUES (?, ?, ?, ?, ?)
            """, (first_name, last_name, email, enrollment_date, program_id))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Email already exists: {email}") from e
    
    def add_program(self, program_name: str, description: str, duration_weeks: int) -> int:
        """Add a new program to the database."""
        self.cursor.execute("""
            INSERT INTO programs (program_name, description, duration_weeks)
            VALUES (?, ?, ?)
        """, (program_name, description, duration_weeks))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_module(self, module_name: str, program_id: int) -> int:
        """Add a new module to a program."""
        self.cursor.execute("""
            INSERT INTO modules (module_name, program_id)
            VALUES (?, ?)
        """, (module_name, program_id))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def record_attendance(self, student_id: int, module_id: int, date: str, status: str) -> int:
        """Record student attendance for a module."""
        if status not in ('present', 'absent', 'excused'):
            raise ValueError("Invalid attendance status")
        
        self.cursor.execute("""
            INSERT INTO attendance (student_id, module_id, date, status)
            VALUES (?, ?, ?, ?)
        """, (student_id, module_id, date, status))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def record_performance(self, student_id: int, module_id: int, score: float, comments: str = None) -> int:
        """Record student performance for a module."""
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        
        assessment_date = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("""
            INSERT INTO performance (student_id, module_id, score, assessment_date, comments)
            VALUES (?, ?, ?, ?, ?)
        """, (student_id, module_id, score, assessment_date, comments))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_student_attendance(self, student_id: int) -> List[Dict]:
        """Get attendance records for a student."""
        self.cursor.execute("""
            SELECT a.date, m.module_name, a.status
            FROM attendance a
            JOIN modules m ON a.module_id = m.module_id
            WHERE a.student_id = ?
            ORDER BY a.date DESC
        """, (student_id,))
        return [{"date": row[0], "module": row[1], "status": row[2]} for row in self.cursor.fetchall()]
    
    def get_student_performance(self, student_id: int) -> List[Dict]:
        """Get performance records for a student."""
        self.cursor.execute("""
            SELECT m.module_name, p.score, p.assessment_date, p.comments
            FROM performance p
            JOIN modules m ON p.module_id = m.module_id
            WHERE p.student_id = ?
            ORDER BY p.assessment_date DESC
        """, (student_id,))
        return [{"module": row[0], "score": row[1], "date": row[2], "comments": row[3]} for row in self.cursor.fetchall()]
    
    def get_student_overview(self, student_id: int) -> Dict:
        """Get an overview of a student's attendance and performance."""
        attendance = self.get_student_attendance(student_id)
        performance = self.get_student_performance(student_id)
        
        self.cursor.execute("""
            SELECT s.first_name, s.last_name, p.program_name
            FROM students s
            JOIN programs p ON s.program_id = p.program_id
            WHERE s.student_id = ?
        """, (student_id,))
        student_info = self.cursor.fetchone()
        
        return {
            "student_id": student_id,
            "first_name": student_info[0],
            "last_name": student_info[1],
            "program": student_info[2],
            "attendance": attendance,
            "performance": performance
        }
    
    def get_module_attendance(self, module_id: int) -> List[Dict]:
        """Get attendance records for a module."""
        self.cursor.execute("""
            SELECT s.first_name, s.last_name, a.date, a.status
            FROM attendance a
            JOIN students s ON a.student_id = s.student_id
            WHERE a.module_id = ?
            ORDER BY a.date DESC
        """, (module_id,))
        return [{"name": f"{row[0]} {row[1]}", "date": row[2], "status": row[3]} for row in self.cursor.fetchall()]
    
    def get_module_performance(self, module_id: int) -> List[Dict]:
        """Get performance records for a module."""
        self.cursor.execute("""
            SELECT s.first_name, s.last_name, p.score, p.assessment_date, p.comments
            FROM performance p
            JOIN students s ON p.student_id = s.student_id
            WHERE p.module_id = ?
            ORDER BY p.score DESC
        """, (module_id,))
        return [{"name": f"{row[0]} {row[1]}", "score": row[2], "date": row[3], "comments": row[4]} for row in self.cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

class StudentTracker:
    """Main class for the student tracking system."""
    
    def __init__(self):
        self.db = DatabaseManager()
    
    def enroll_student(self, first_name: str, last_name: str, email: str, program_id: int) -> int:
        """Enroll a new student in a program."""
        return self.db.add_student(first_name, last_name, email, program_id)
    
    def create_program(self, program_name: str, description: str, duration_weeks: int) -> int:
        """Create a new certification program."""
        return self.db.add_program(program_name, description, duration_weeks)
    
    def add_program_module(self, module_name: str, program_id: int) -> int
