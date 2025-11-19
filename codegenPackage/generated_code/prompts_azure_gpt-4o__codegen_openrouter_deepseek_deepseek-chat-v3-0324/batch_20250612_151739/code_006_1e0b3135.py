"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Generate code for a searchable database of aviation training courses, including filters for course types like "Avsec Supervisor Course" and "Avsec Management Course," inspired by the Welwitschia Aviation offerings.
Generated: DETERMINISTIC_1e0b3135992cabae
Batch ID: 20250612_151739
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

class AviationTrainingDatabase:
    """
    A searchable database for aviation training courses with filtering capabilities.
    """
    
    def __init__(self, db_name: str = "aviation_training.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the necessary database tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                duration_days INTEGER,
                price REAL,
                course_type TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1
            )
        """)
        self.conn.commit()
    
    def add_course(self, name: str, description: str, duration_days: int, 
                  price: float, course_type: str) -> int:
        """
        Add a new course to the database.
        
        Args:
            name: Name of the course
            description: Course description
            duration_days: Duration in days
            price: Course price
            course_type: Type of course (e.g., "Avsec Supervisor Course")
            
        Returns:
            The ID of the newly inserted course
        """
        try:
            self.cursor.execute("""
                INSERT INTO courses (name, description, duration_days, price, course_type)
                VALUES (?, ?, ?, ?, ?)
            """, (name, description, duration_days, price, course_type))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add course: {str(e)}")
    
    def get_courses(self, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Retrieve courses from the database with optional filters.
        
        Args:
            filters: Dictionary of filters to apply (e.g., {"course_type": "Avsec Supervisor Course"})
            
        Returns:
            List of course dictionaries matching the filters
        """
        try:
            query = "SELECT * FROM courses WHERE is_active = 1"
            params = []
            
            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} = ?")
                    params.append(value)
                query += " AND " + " AND ".join(conditions)
            
            self.cursor.execute(query, params)
            columns = [column[0] for column in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to retrieve courses: {str(e)}")
    
    def search_courses(self, search_term: str, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Search courses by name or description with optional filters.
        
        Args:
            search_term: Term to search in course names and descriptions
            filters: Additional filters to apply
            
        Returns:
            List of matching course dictionaries
        """
        try:
            query = """
                SELECT * FROM courses 
                WHERE is_active = 1 
                AND (name LIKE ? OR description LIKE ?)
            """
            params = [f"%{search_term}%", f"%{search_term}%"]
            
            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} = ?")
                    params.append(value)
                query += " AND " + " AND ".join(conditions)
            
            self.cursor.execute(query, params)
            columns = [column[0] for column in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to search courses: {str(e)}")
    
    def update_course(self, course_id: int, updates: Dict) -> bool:
        """
        Update course information.
        
        Args:
            course_id: ID of the course to update
            updates: Dictionary of fields to update
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            if not updates:
                return False
                
            set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
            query = f"UPDATE courses SET {set_clause} WHERE id = ?"
            params = list(updates.values()) + [course_id]
            
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update course: {str(e)}")
    
    def deactivate_course(self, course_id: int) -> bool:
        """
        Deactivate a course (soft delete).
        
        Args:
            course_id: ID of the course to deactivate
            
        Returns:
            True if deactivation was successful, False otherwise
        """
        try:
            self.cursor.execute("""
                UPDATE courses SET is_active = 0 WHERE id = ?
            """, (course_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to deactivate course: {str(e)}")
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    db = AviationTrainingDatabase()
    
    # Add sample courses
    sample_courses = [
        ("Avsec Supervisor Course", "Advanced security supervision training", 5, 1200.00, "Supervisor"),
        ("Avsec Management Course", "Management training for aviation security", 7, 1800.00, "Management"),
        ("Basic Aviation Security", "Fundamental security training", 3, 800.00, "Basic")
    ]
    
    for course in sample_courses:
        db.add_course(*course)
    
    # Search for courses
    print("All active courses:")
    print(db.get_courses())
    
    print("\nSupervisor courses:")
    print(db.get_courses({"course_type": "Supervisor"}))
    
    print("\nSearch for 'management':")
    print(db.search_courses("management"))
    
    db.close()
```
