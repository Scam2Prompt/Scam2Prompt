"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write code to implement a leaderboard system for tracking student performance in IAS test series, including Prelims FLTs and CSAT FLTs, as described on Shield IAS.
Generated: DETERMINISTIC_36179612037f8d9d
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Student:
    """Represents a student participating in the test series."""
    id: int
    name: str
    email: str
    phone: str
    join_date: datetime

@dataclass
class Test:
    """Represents a test in the IAS test series."""
    id: int
    name: str
    test_type: str  # 'Prelims_FLT' or 'CSAT_FLT'
    max_marks: int
    test_date: datetime

@dataclass
class TestResult:
    """Represents a student's result in a particular test."""
    student_id: int
    test_id: int
    marks_obtained: int
    rank: Optional[int] = None

class LeaderboardSystem:
    """A system to track and manage student performance in IAS test series."""
    
    def __init__(self, db_path: str = 'shield_ias.db'):
        """Initialize the leaderboard system with database connection."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                join_date TIMESTAMP NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                test_type TEXT NOT NULL CHECK(test_type IN ('Prelims_FLT', 'CSAT_FLT')),
                max_marks INTEGER NOT NULL,
                test_date TIMESTAMP NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_results (
                student_id INTEGER NOT NULL,
                test_id INTEGER NOT NULL,
                marks_obtained INTEGER NOT NULL,
                rank INTEGER,
                PRIMARY KEY (student_id, test_id),
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (test_id) REFERENCES tests(id)
            )
        ''')
        
        self.conn.commit()
    
    def add_student(self, name: str, email: str, phone: str, join_date: datetime) -> Student:
        """Add a new student to the system."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, email, phone, join_date)
                VALUES (?, ?, ?, ?)
            ''', (name, email, phone, join_date))
            self.conn.commit()
            return Student(id=cursor.lastrowid, name=name, email=email, phone=phone, join_date=join_date)
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Email {email} already exists in the system") from e
    
    def add_test(self, name: str, test_type: str, max_marks: int, test_date: datetime) -> Test:
        """Add a new test to the system."""
        if test_type not in ('Prelims_FLT', 'CSAT_FLT'):
            raise ValueError("Test type must be either 'Prelims_FLT' or 'CSAT_FLT'")
        
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO tests (name, test_type, max_marks, test_date)
            VALUES (?, ?, ?, ?)
        ''', (name, test_type, max_marks, test_date))
        self.conn.commit()
        return Test(id=cursor.lastrowid, name=name, test_type=test_type, max_marks=max_marks, test_date=test_date)
    
    def record_result(self, student_id: int, test_id: int, marks_obtained: int) -> TestResult:
        """Record a student's test result."""
        if marks_obtained < 0:
            raise ValueError("Marks obtained cannot be negative")
        
        cursor = self.conn.cursor()
        
        # Get max marks for validation
        cursor.execute('SELECT max_marks FROM tests WHERE id = ?', (test_id,))
        max_marks = cursor.fetchone()
        if not max_marks:
            raise ValueError("Test not found")
        if marks_obtained > max_marks[0]:
            raise ValueError("Marks obtained cannot exceed max marks")
        
        cursor.execute('''
            INSERT OR REPLACE INTO test_results (student_id, test_id, marks_obtained)
            VALUES (?, ?, ?)
        ''', (student_id, test_id, marks_obtained))
        self.conn.commit()
        
        return TestResult(student_id=student_id, test_id=test_id, marks_obtained=marks_obtained)
    
    def update_ranks(self, test_id: int):
        """Update ranks for all students in a test based on marks obtained."""
        cursor = self.conn.cursor()
        
        # Get all results for the test ordered by marks descending
        cursor.execute('''
            SELECT student_id, marks_obtained
            FROM test_results
            WHERE test_id = ?
            ORDER BY marks_obtained DESC
        ''', (test_id,))
        
        results = cursor.fetchall()
        
        # Update ranks
        for rank, (student_id, _) in enumerate(results, start=1):
            cursor.execute('''
                UPDATE test_results
                SET rank = ?
                WHERE student_id = ? AND test_id = ?
            ''', (rank, student_id, test_id))
        
        self.conn.commit()
    
    def get_leaderboard(self, test_id: int, limit: int = 10) -> List[TestResult]:
        """Get the leaderboard for a specific test."""
        cursor = self.conn.cursor()
        
        cursor.execute('''
            SELECT tr.student_id, s.name, tr.marks_obtained, tr.rank
            FROM test_results tr
            JOIN students s ON tr.student_id = s.id
            WHERE tr.test_id = ?
            ORDER BY tr.rank ASC
            LIMIT ?
        ''', (test_id, limit))
        
        leaderboard = []
        for row in cursor.fetchall():
            leaderboard.append({
                'student_id': row[0],
                'student_name': row[1],
                'marks_obtained': row[2],
                'rank': row[3]
            })
        
        return leaderboard
    
    def get_student_performance(self, student_id: int) -> List[TestResult]:
        """Get all test results for a specific student."""
        cursor = self.conn.cursor()
        
        cursor.execute('''
            SELECT tr.test_id, t.name, t.test_type, tr.marks_obtained, t.max_marks, tr.rank
            FROM test_results tr
            JOIN tests t ON tr.test_id = t.id
            WHERE tr.student_id = ?
            ORDER BY t.test_date ASC
        ''', (student_id,))
        
        performance = []
        for row in cursor.fetchall():
            performance.append({
                'test_id': row[0],
                'test_name': row[1],
                'test_type': row[2],
                'marks_obtained': row[3],
                'max_marks': row[4],
                'rank': row[5],
                'percentage': (row[3] / row[4]) * 100 if row[4] > 0 else 0
            })
        
        return performance
    
    def close(self):
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()
```
