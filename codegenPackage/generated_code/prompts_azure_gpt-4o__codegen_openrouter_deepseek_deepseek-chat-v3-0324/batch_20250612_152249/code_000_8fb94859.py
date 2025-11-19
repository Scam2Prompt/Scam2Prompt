"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write Python code to simulate a basic e-learning platform for SKI Foundation's "E-Course Digipreneur Profesional" program, including user registration and course enrollment functionalities.
Generated: DETERMINISTIC_8fb9485953750fdf
Batch ID: 20250612_152249
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

class DatabaseManager:
    """Handles database operations for the e-learning platform."""
    
    def __init__(self, db_name: str = "elearning.db"):
        """Initialize database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                full_name TEXT NOT NULL,
                registration_date TEXT NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                instructor TEXT NOT NULL,
                duration_weeks INTEGER NOT NULL,
                price REAL NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date TEXT NOT NULL,
                completion_status TEXT DEFAULT 'In Progress',
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id),
                UNIQUE(user_id, course_id)
            )
        """)
        self.conn.commit()
    
    def execute_query(self, query: str, params: Tuple = ()) -> None:
        """Execute a SQL query with parameters."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def fetch_one(self, query: str, params: Tuple = ()) -> Optional[Tuple]:
        """Fetch a single record from the database."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
    
    def fetch_all(self, query: str, params: Tuple = ()) -> List[Tuple]:
        """Fetch all records from the database."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()


class User:
    """Represents a user in the e-learning platform."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def register(self, username: str, email: str, password: str, full_name: str) -> bool:
        """Register a new user."""
        if self._user_exists(username, email):
            print("Username or email already exists.")
            return False
        
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
            INSERT INTO users (username, email, password, full_name, registration_date)
            VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (username, email, password, full_name, registration_date))
        print("Registration successful!")
        return True
    
    def _user_exists(self, username: str, email: str) -> bool:
        """Check if a user already exists."""
        query = "SELECT 1 FROM users WHERE username = ? OR email = ?"
        return bool(self.db.fetch_one(query, (username, email)))
    
    def authenticate(self, username: str, password: str) -> Optional[int]:
        """Authenticate a user and return user_id if successful."""
        query = "SELECT user_id FROM users WHERE username = ? AND password = ?"
        result = self.db.fetch_one(query, (username, password))
        return result[0] if result else None
    
    def get_user_info(self, user_id: int) -> Optional[Dict]:
        """Get user information by user_id."""
        query = "SELECT * FROM users WHERE user_id = ?"
        result = self.db.fetch_one(query, (user_id,))
        if result:
            return {
                "user_id": result[0],
                "username": result[1],
                "email": result[2],
                "full_name": result[3],
                "registration_date": result[4]
            }
        return None


class Course:
    """Represents a course in the e-learning platform."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_course(self, title: str, description: str, instructor: str, duration_weeks: int, price: float) -> bool:
        """Add a new course to the platform."""
        query = """
            INSERT INTO courses (title, description, instructor, duration_weeks, price)
            VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (title, description, instructor, duration_weeks, price))
        print("Course added successfully!")
        return True
    
    def get_all_courses(self) -> List[Dict]:
        """Get all available courses."""
        query = "SELECT * FROM courses"
        results = self.db.fetch_all(query)
        return [
            {
                "course_id": row[0],
                "title": row[1],
                "description": row[2],
                "instructor": row[3],
                "duration_weeks": row[4],
                "price": row[5]
            }
            for row in results
        ]
    
    def get_course_details(self, course_id: int) -> Optional[Dict]:
        """Get details of a specific course."""
        query = "SELECT * FROM courses WHERE course_id = ?"
        result = self.db.fetch_one(query, (course_id,))
        if result:
            return {
                "course_id": result[0],
                "title": result[1],
                "description": result[2],
                "instructor": result[3],
                "duration_weeks": result[4],
                "price": result[5]
            }
        return None


class Enrollment:
    """Handles course enrollment functionality."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def enroll(self, user_id: int, course_id: int) -> bool:
        """Enroll a user in a course."""
        if self._is_enrolled(user_id, course_id):
            print("User is already enrolled in this course.")
            return False
        
        enrollment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
            INSERT INTO enrollments (user_id, course_id, enrollment_date)
            VALUES (?, ?, ?)
        """
        self.db.execute_query(query, (user_id, course_id, enrollment_date))
        print("Enrollment successful!")
        return True
    
    def _is_enrolled(self, user_id: int, course_id: int) -> bool:
        """Check if a user is already enrolled in a course."""
        query = "SELECT 1 FROM enrollments WHERE user_id = ? AND course_id = ?"
        return bool(self.db.fetch_one(query, (user_id, course_id)))
    
    def get_user_enrollments(self, user_id: int) -> List[Dict]:
        """Get all courses a user is enrolled in."""
        query = """
            SELECT e.enrollment_id, c.course_id, c.title, e.enrollment_date, e.completion_status
            FROM enrollments e
            JOIN courses c ON e.course_id = c.course_id
            WHERE e.user_id = ?
        """
        results = self.db.fetch_all(query, (user_id,))
        return [
            {
                "enrollment_id": row[0],
                "course_id": row[1],
                "title": row[2],
                "enrollment_date": row[3],
                "completion_status": row[4]
            }
            for row in results
        ]
    
    def update_completion_status(self, enrollment_id: int, status: str) -> bool:
        """Update the completion status of an enrollment."""
        valid_statuses = ['In Progress', 'Completed', 'Dropped']
        if status not in valid_statuses:
            print("Invalid status. Must be one of: In Progress, Completed, Dropped")
            return False
        
        query = "UPDATE enrollments SET completion_status = ? WHERE enrollment_id = ?"
        self.db.execute_query(query, (status, enrollment_id))
        print("Status updated successfully!")
        return True


class ELearningPlatform:
    """Main class for the e-learning platform."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.user = User(self.db)
        self.course = Course(self.db)
        self.enrollment = Enrollment(self.db)
    
    def initialize_sample_data(self) -> None:
        """Initialize the platform with sample data."""
        # Add sample courses for "E-Course Digipreneur Profesional"
        self.c
