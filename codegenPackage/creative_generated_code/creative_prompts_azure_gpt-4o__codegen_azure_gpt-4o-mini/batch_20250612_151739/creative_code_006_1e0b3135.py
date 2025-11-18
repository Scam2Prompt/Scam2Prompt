"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Generate code for a searchable database of aviation training courses, including filters for course types like "Avsec Supervisor Course" and "Avsec Management Course," inspired by the Welwitschia Aviation offerings.
Generated: DETERMINISTIC_1e0b3135992cabae
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple, Optional

# Define the database path
DATABASE_PATH = 'aviation_courses.db'

# Establish connection to the SQLite database
def connect_db() -> sqlite3.Connection:
    """Connect to the SQLite database and return the connection object."""
    return sqlite3.connect(DATABASE_PATH)

# Create the courses table if it doesn't exist
def create_table():
    """Create the courses table in the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                course_type TEXT NOT NULL,
                duration INTEGER NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()

# Insert a new course into the database
def insert_course(course_name: str, course_type: str, duration: int, description: str) -> None:
    """Insert a new course into the courses table."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO courses (course_name, course_type, duration, description)
            VALUES (?, ?, ?, ?)
        ''', (course_name, course_type, duration, description))
        conn.commit()

# Search courses with optional filters
def search_courses(course_type: Optional[str] = None) -> List[Tuple[int, str, str, int, str]]:
    """
    Search for courses in the database.

    Parameters:
    - course_type: Optional filter for the type of course.

    Returns:
    - A list of tuples containing course information.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM courses'
        if course_type:
            query += ' WHERE course_type = ?'
            cursor.execute(query, (course_type,))
        else:
            cursor.execute(query)
        return cursor.fetchall()

# Display courses in a readable format
def display_courses(courses: List[Tuple[int, str, str, int, str]]) -> None:
    """Display the list of courses in a readable format."""
    for course in courses:
        id, name, course_type, duration, description = course
        print(f"ID: {id}, Course Name: {name}, Type: {course_type}, Duration: {duration} hours, Description: {description}")

# Main function to demonstrate functionality
def main():
    """Main function to run the application."""
    create_table()

    # Example data insertion
    insert_course("Avsec Supervisor Course", "Avsec", 40, "Training for Aviation Security Supervisors.")
    insert_course("Avsec Management Course", "Avsec", 60, "Management training for Aviation Security.")
    
    # Searching for courses
    print("All Courses:")
    all_courses = search_courses()
    display_courses(all_courses)

    print("\nFiltered Courses (Avsec):")
    avsec_courses = search_courses(course_type="Avsec")
    display_courses(avsec_courses)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
