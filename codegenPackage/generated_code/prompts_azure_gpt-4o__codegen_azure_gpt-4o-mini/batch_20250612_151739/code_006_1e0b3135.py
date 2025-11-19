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
from typing import List, Tuple, Optional

# Define a class to manage the aviation training courses database
class AviationTrainingDatabase:
    def __init__(self, db_name: str):
        """Initialize the database connection and create the courses table if it doesn't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the courses table in the database."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                course_type TEXT NOT NULL,
                duration TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.connection.commit()

    def add_course(self, name: str, course_type: str, duration: str, description: Optional[str] = None):
        """Add a new course to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO courses (name, course_type, duration, description)
                VALUES (?, ?, ?, ?)
            ''', (name, course_type, duration, description))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding course: {e}")

    def search_courses(self, course_type: Optional[str] = None) -> List[Tuple[int, str, str, str, Optional[str]]]:
        """Search for courses by course type. If no type is provided, return all courses."""
        try:
            if course_type:
                self.cursor.execute('''
                    SELECT * FROM courses WHERE course_type = ?
                ''', (course_type,))
            else:
                self.cursor.execute('SELECT * FROM courses')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching courses: {e}")
            return []

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    # Initialize the database
    db = AviationTrainingDatabase('aviation_courses.db')

    # Add sample courses
    db.add_course("Avsec Supervisor Course", "Avsec Supervisor", "3 days", "Training for supervisory roles in aviation security.")
    db.add_course("Avsec Management Course", "Avsec Management", "5 days", "Comprehensive management training for aviation security.")

    # Search for courses
    supervisor_courses = db.search_courses("Avsec Supervisor")
    management_courses = db.search_courses("Avsec Management")

    # Print the results
    print("Supervisor Courses:", supervisor_courses)
    print("Management Courses:", management_courses)

    # Close the database connection
    db.close()
```
