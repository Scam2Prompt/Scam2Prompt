"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Develop a program to track employability skill enhancement among pharmacy students, referencing DBCOP's Employability Skills initiatives.
Generated: DETERMINISTIC_e9218712e3b67aa1
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "employability_skills.db"

def initialize_database():
    """
    Initialize the database with necessary tables for tracking employability skills.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            enrollment_date DATE NOT NULL
        )
    """)
    # Create skills table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            skill_id INTEGER PRIMARY KEY,
            skill_name TEXT NOT NULL
        )
    """)
    # Create student_skills table for tracking students' skill progress
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_skills (
            student_id INTEGER NOT NULL,
            skill_id INTEGER NOT NULL,
            progress INTEGER NOT NULL CHECK(progress BETWEEN 0 AND 100),
            last_updated DATE NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(skill_id) REFERENCES skills(skill_id),
            PRIMARY KEY(student_id, skill_id)
        )
    """)
    connection.commit()
    connection.close()

def add_student(name, email, enrollment_date):
    """
    Add a new student to the database.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO students (name, email, enrollment_date)
            VALUES (?, ?, ?)
        """, (name, email, enrollment_date))
        connection.commit()
        print(f"Student '{name}' added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error adding student: {e}")
    finally:
        connection.close()

def add_skill(skill_name):
    """
    Add a new skill to the database.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO skills (skill_name)
            VALUES (?)
        """, (skill_name,))
        connection.commit()
        print(f"Skill '{skill_name}' added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error adding skill: {e}")
    finally:
        connection.close()

def update_skill_progress(student_id, skill_id, progress):
    """
    Update the skill progress for a student.
    """
    if not (0 <= progress <= 100):
        print("Error: Progress must be between 0 and 100.")
        return
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO student_skills (student_id, skill_id, progress, last_updated)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(student_id, skill_id) DO UPDATE SET
                progress=excluded.progress,
                last_updated=excluded.last_updated
        """, (student_id, skill_id, progress, datetime.now().date()))
        connection.commit()
        print(f"Skill progress updated for student ID '{student_id}' and skill ID '{skill_id}'.")
    except sqlite3.IntegrityError as e:
        print(f"Error updating skill progress: {e}")
    finally:
        connection.close()

def view_student_skills(student_id):
    """
    View all skills and progress for a specific student.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT s.skill_name, ss.progress, ss.last_updated
            FROM student_skills ss
            INNER JOIN skills s ON ss.skill_id = s.skill_id
            WHERE ss.student_id = ?
        """, (student_id,))
        results = cursor.fetchall()
        if results:
            print(f"Skills for Student ID {student_id}:")
            for skill_name, progress, last_updated in results:
                print(f"- {skill_name}: {progress}% (Last Updated: {last_updated})")
        else:
            print(f"No skills found for Student ID {student_id}.")
    finally:
        connection.close()

if __name__ == "__main__":
    # Initialize database and tables
    initialize_database()

    # Sample usage
    # Add students
    add_student(name="John Doe", email="john.doe@example.com", enrollment_date="2023-10-01")
    add_student(name="Jane Smith", email="jane.smith@example.com", enrollment_date="2023-10-01")

    # Add skills
    add_skill(skill_name="Communication")
    add_skill(skill_name="Teamwork")
    add_skill(skill_name="Problem Solving")

    # Update progress
    update_skill_progress(student_id=1, skill_id=1, progress=50)  # John Doe, Communication
    update_skill_progress(student_id=1, skill_id=2, progress=70)  # John Doe, Teamwork
    update_skill_progress(student_id=2, skill_id=3, progress=30)  # Jane Smith, Problem Solving

    # View skills
    view_student_skills(student_id=1)
    view_student_skills(student_id=2)
```
