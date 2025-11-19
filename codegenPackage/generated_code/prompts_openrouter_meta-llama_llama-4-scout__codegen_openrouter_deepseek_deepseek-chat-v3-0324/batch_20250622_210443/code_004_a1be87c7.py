"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Design a system to track and analyze student progress for a language learning program like DME, including metrics for engagement and skill development."
Generated: DETERMINISTIC_a1be87c70b5daa38
Batch ID: 20250622_210443
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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class StudentProgressTracker:
    """System to track and analyze student progress in a language learning program."""
    
    def __init__(self, db_path: str = 'student_progress.db'):
        """Initialize the tracker with database connection.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Students table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        registration_date TEXT NOT NULL,
                        level TEXT DEFAULT 'beginner'
                    )
                ''')
                
                # Engagement metrics table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS engagement_metrics (
                        metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        login_count INTEGER DEFAULT 0,
                        time_spent_minutes INTEGER DEFAULT 0,
                        lessons_completed INTEGER DEFAULT 0,
                        FOREIGN KEY (student_id) REFERENCES students (student_id)
                    )
                ''')
                
                # Skill development table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS skill_metrics (
                        skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        vocabulary_score INTEGER DEFAULT 0,
                        grammar_score INTEGER DEFAULT 0,
                        listening_score INTEGER DEFAULT 0,
                        speaking_score INTEGER DEFAULT 0,
                        FOREIGN KEY (student_id) REFERENCES students (student_id)
                    )
                ''')
                
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def add_student(self, name: str, email: str, level: str = 'beginner') -> int:
        """Register a new student.
        
        Args:
            name: Student's name
            email: Student's email (must be unique)
            level: Starting proficiency level
            
        Returns:
            The newly created student ID
            
        Raises:
            ValueError: If email already exists
            sqlite3.Error: For database errors
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                registration_date = datetime.now().isoformat()
                cursor.execute('''
                    INSERT INTO students (name, email, registration_date, level)
                    VALUES (?, ?, ?, ?)
                ''', (name, email, registration_date, level))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Email {email} already exists in the system")
        except sqlite3.Error as e:
            logger.error(f"Error adding student: {e}")
            raise
    
    def record_engagement(self, student_id: int, login_count: int = 0, 
                         time_spent_minutes: int = 0, lessons_completed: int = 0) -> None:
        """Record daily engagement metrics for a student.
        
        Args:
            student_id: ID of the student
            login_count: Number of logins for the day
            time_spent_minutes: Total minutes spent learning
            lessons_completed: Number of lessons completed
            
        Raises:
            ValueError: If student_id doesn't exist
            sqlite3.Error: For database errors
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check student exists
                cursor.execute('SELECT 1 FROM students WHERE student_id = ?', (student_id,))
                if not cursor.fetchone():
                    raise ValueError(f"Student ID {student_id} not found")
                
                date = datetime.now().date().isoformat()
                cursor.execute('''
                    INSERT INTO engagement_metrics 
                    (student_id, date, login_count, time_spent_minutes, lessons_completed)
                    VALUES (?, ?, ?, ?, ?)
                ''', (student_id, date, login_count, time_spent_minutes, lessons_completed))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error recording engagement: {e}")
            raise
    
    def record_skill_development(self, student_id: int, vocabulary_score: int = 0,
                                grammar_score: int = 0, listening_score: int = 0,
                                speaking_score: int = 0) -> None:
        """Record skill development metrics for a student.
        
        Args:
            student_id: ID of the student
            vocabulary_score: Score for vocabulary (0-100)
            grammar_score: Score for grammar (0-100)
            listening_score: Score for listening (0-100)
            speaking_score: Score for speaking (0-100)
            
        Raises:
            ValueError: If student_id doesn't exist or scores are invalid
            sqlite3.Error: For database errors
        """
        if not (0 <= vocabulary_score <= 100 and
                0 <= grammar_score <= 100 and
                0 <= listening_score <= 100 and
                0 <= speaking_score <= 100):
            raise ValueError("All scores must be between 0 and 100")
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check student exists
                cursor.execute('SELECT 1 FROM students WHERE student_id = ?', (student_id,))
                if not cursor.fetchone():
                    raise ValueError(f"Student ID {student_id} not found")
                
                date = datetime.now().date().isoformat()
                cursor.execute('''
                    INSERT INTO skill_metrics 
                    (student_id, date, vocabulary_score, grammar_score, 
                     listening_score, speaking_score)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (student_id, date, vocabulary_score, grammar_score, 
                      listening_score, speaking_score))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error recording skill development: {e}")
            raise
    
    def get_student_progress(self, student_id: int) -> Dict:
        """Get comprehensive progress report for a student.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Dictionary containing student info, engagement metrics, and skill development
            
        Raises:
            ValueError: If student_id doesn't exist
            sqlite3.Error: For database errors
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                # Get student info
                cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
                student = cursor.fetchone()
                if not student:
                    raise ValueError(f"Student ID {student_id} not found")
                
                # Get engagement metrics (last 30 days)
                cursor.execute('''
                    SELECT * FROM engagement_metrics 
                    WHERE student_id = ? 
                    AND date >= date('now', '-30 days')
                    ORDER BY date DESC
                ''', (student_id,))
                engagement = cursor.fetchall()
                
                # Get skill metrics (last 30 days)
                cursor.execute('''
                    SELECT * FROM skill_metrics 
                    WHERE student_id = ? 
                    AND date >= date('now', '-30 days')
                    ORDER BY date DESC
                ''', (student_id,))
                skills = cursor.fetchall()
                
                return {
                    'student_info': dict(student),
                    'engagement_metrics': [dict(row) for row in engagement],
                    'skill_metrics': [dict(row) for row in skills]
                }
        except sqlite3.Error as e:
            logger.error(f"Error getting student progress: {e}")
            raise
    
    def calculate_engagement_score(self, student_id: int) -> float:
        """Calculate an overall engagement score (0-100) for a student.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Engagement score (0-100)
            
        Raises:
            ValueError: If student_id doesn't exist
            sqlite3.Error: For database errors
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check student exists
                cursor.execute('SELECT 1 FROM students WHERE student_id = ?', (student_id,))
                if not cursor.fetchone():
                    raise ValueError(f"Student ID {student_id} not found")
                
                # Get metrics for last 30 days
                cursor.execute('''
                    SELECT 
                        SUM(login_count) as total_logins,
                        SUM(time_spent_minutes) as total_time,
                        SUM(lessons_completed) as total_lessons
                    FROM engagement_metrics
                    WHERE student_id = ?
                    AND date >= date
