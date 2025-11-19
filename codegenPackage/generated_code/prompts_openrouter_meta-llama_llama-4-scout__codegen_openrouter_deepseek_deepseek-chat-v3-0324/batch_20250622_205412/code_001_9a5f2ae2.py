"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Write a Python script to manage a simple aviation security training database, including courses such as Basic Avsec Course, Avsec Supervisor Course, and Risk Management Course.
Generated: DETERMINISTIC_9a5f2ae25dc44085
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class AviationSecurityTrainingDB:
    """
    A class to manage a simple aviation security training database.
    Supports CRUD operations for training courses.
    """

    def __init__(self, db_name: str = "avsec_training.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self._create_tables()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            if self.conn:
                self.conn.close()

    def _create_tables(self):
        """Create the necessary tables if they don't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            duration_hours INTEGER NOT NULL,
            description TEXT,
            is_active BOOLEAN DEFAULT 1
        );
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def add_course(self, name: str, duration_hours: int, description: str = None) -> bool:
        """
        Add a new course to the database.
        
        Args:
            name: Name of the course
            duration_hours: Duration in hours
            description: Optional description of the course
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute(
                "INSERT INTO courses (name, duration_hours, description) VALUES (?, ?, ?)",
                (name, duration_hours, description)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Course '{name}' already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error adding course: {e}")
            return False

    def get_course(self, course_id: int) -> Optional[Dict]:
        """
        Retrieve a course by its ID.
        
        Args:
            course_id: The ID of the course to retrieve
            
        Returns:
            dict: Course information if found, None otherwise
        """
        try:
            self.cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
            result = self.cursor.fetchone()
            
            if result:
                return {
                    "id": result[0],
                    "name": result[1],
                    "duration_hours": result[2],
                    "description": result[3],
                    "is_active": bool(result[4])
                }
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving course: {e}")
            return None

    def get_all_courses(self, active_only: bool = True) -> List[Dict]:
        """
        Retrieve all courses from the database.
        
        Args:
            active_only: If True, only return active courses
            
        Returns:
            list: List of course dictionaries
        """
        try:
            query = "SELECT * FROM courses"
            if active_only:
                query += " WHERE is_active = 1"
                
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            courses = []
            for result in results:
                courses.append({
                    "id": result[0],
                    "name": result[1],
                    "duration_hours": result[2],
                    "description": result[3],
                    "is_active": bool(result[4])
                })
            return courses
        except sqlite3.Error as e:
            print(f"Error retrieving courses: {e}")
            return []

    def update_course(self, course_id: int, **kwargs) -> bool:
        """
        Update course information.
        
        Args:
            course_id: ID of the course to update
            **kwargs: Fields to update (name, duration_hours, description, is_active)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not kwargs:
            return False
            
        try:
            update_fields = []
            values = []
            
            for field, value in kwargs.items():
                if field in ["name", "duration_hours", "description", "is_active"]:
                    update_fields.append(f"{field} = ?")
                    values.append(value)
            
            if not update_fields:
                return False
                
            values.append(course_id)
            query = f"UPDATE courses SET {', '.join(update_fields)} WHERE id = ?"
            
            self.cursor.execute(query, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating course: {e}")
            return False

    def delete_course(self, course_id: int) -> bool:
        """
        Soft delete a course by setting is_active to False.
        
        Args:
            course_id: ID of the course to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute(
                "UPDATE courses SET is_active = 0 WHERE id = ?",
                (course_id,)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting course: {e}")
            return False

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


def initialize_sample_data(db: AviationSecurityTrainingDB):
    """Initialize the database with sample courses."""
    sample_courses = [
        ("Basic Avsec Course", 40, "Fundamentals of aviation security"),
        ("Avsec Supervisor Course", 80, "Management and supervision in aviation security"),
        ("Risk Management Course", 60, "Identifying and managing security risks")
    ]
    
    for course in sample_courses:
        db.add_course(*course)


if __name__ == "__main__":
    # Example usage
    with AviationSecurityTrainingDB() as db:
        # Initialize with sample data if empty
        if not db.get_all_courses():
            initialize_sample_data(db)
        
        # List all active courses
        print("Available courses:")
        for course in db.get_all_courses():
            print(f"{course['id']}: {course['name']} ({course['duration_hours']} hours)")
        
        # Add a new course
        db.add_course("Advanced Screening Techniques", 30, "Advanced methods for passenger and baggage screening")
        
        # Update a course
        db.update_course(1, duration_hours=45)
        
        # Get a specific course
        course = db.get_course(2)
        if course:
            print(f"\nCourse details for ID 2: {course['name']}")
        
        # Delete a course
        db.delete_course(3)
```
