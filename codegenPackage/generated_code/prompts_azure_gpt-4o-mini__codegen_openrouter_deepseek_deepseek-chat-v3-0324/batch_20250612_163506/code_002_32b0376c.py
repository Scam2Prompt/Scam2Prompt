"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Write a code snippet that integrates with a database to track student progress in the Marketing Digital program offered by ISIV.
Generated: DETERMINISTIC_32b0376c53020c02
Batch ID: 20250612_163506
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
from dataclasses import dataclass

@dataclass
class Student:
    """Represents a student in the Marketing Digital program."""
    student_id: int
    name: str
    email: str
    progress: float  # Percentage of program completed (0-100)
    last_updated: str  # ISO format date string

class StudentProgressTracker:
    """Handles database operations for tracking student progress."""
    
    def __init__(self, db_path: str = "isiv_marketing_digital.db"):
        """Initialize the database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._create_table()
    
    def _create_table(self) -> None:
        """Create the students table if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    progress REAL NOT NULL CHECK(progress >= 0 AND progress <= 100),
                    last_updated TEXT NOT NULL
                )
            """)
            conn.commit()
    
    def add_student(self, student: Student) -> bool:
        """Add a new student to the database.
        
        Args:
            student: Student object to add.
            
        Returns:
            bool: True if successful, False if student already exists.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO students (student_id, name, email, progress, last_updated)
                    VALUES (?, ?, ?, ?, ?)
                """, (student.student_id, student.name, student.email, 
                      student.progress, student.last_updated))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def update_progress(self, student_id: int, new_progress: float, last_updated: str) -> bool:
        """Update a student's progress.
        
        Args:
            student_id: ID of the student to update.
            new_progress: New progress percentage (0-100).
            last_updated: ISO format date string.
            
        Returns:
            bool: True if successful, False if student doesn't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE students
                SET progress = ?, last_updated = ?
                WHERE student_id = ?
            """, (new_progress, last_updated, student_id))
            conn.commit()
            return cursor.rowcount > 0
    
    def get_student(self, student_id: int) -> Optional[Student]:
        """Retrieve a student by ID.
        
        Args:
            student_id: ID of the student to retrieve.
            
        Returns:
            Optional[Student]: Student object if found, None otherwise.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT student_id, name, email, progress, last_updated
                FROM students
                WHERE student_id = ?
            """, (student_id,))
            row = cursor.fetchone()
            return Student(*row) if row else None
    
    def get_all_students(self) -> List[Student]:
        """Retrieve all students.
        
        Returns:
            List[Student]: List of all students in the database.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT student_id, name, email, progress, last_updated
                FROM students
            """)
            return [Student(*row) for row in cursor.fetchall()]
    
    def get_students_by_progress_range(self, min_progress: float, max_progress: float) -> List[Student]:
        """Retrieve students within a progress range.
        
        Args:
            min_progress: Minimum progress percentage (0-100).
            max_progress: Maximum progress percentage (0-100).
            
        Returns:
            List[Student]: Students within the specified progress range.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT student_id, name, email, progress, last_updated
                FROM students
                WHERE progress BETWEEN ? AND ?
                ORDER BY progress DESC
            """, (min_progress, max_progress))
            return [Student(*row) for row in cursor.fetchall()]
    
    def delete_student(self, student_id: int) -> bool:
        """Delete a student from the database.
        
        Args:
            student_id: ID of the student to delete.
            
        Returns:
            bool: True if successful, False if student doesn't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM students
                WHERE student_id = ?
            """, (student_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_progress_stats(self) -> Dict[str, float]:
        """Calculate statistics about student progress.
        
        Returns:
            Dict[str, float]: Dictionary containing average, min, and max progress.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT AVG(progress), MIN(progress), MAX(progress)
                FROM students
            """)
            avg, min_p, max_p = cursor.fetchone()
            return {
                "average_progress": avg,
                "min_progress": min_p,
                "max_progress": max_p
            }
```
