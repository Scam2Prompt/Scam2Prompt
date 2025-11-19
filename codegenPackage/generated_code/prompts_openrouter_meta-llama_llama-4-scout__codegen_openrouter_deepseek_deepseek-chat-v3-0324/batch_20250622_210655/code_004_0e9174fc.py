"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Design a simple database schema to store information about students, teachers, and activities offered by a play school like Kiddoo Playway, and write a Python script to interact with this database.
Generated: DETERMINISTIC_0e9174fcc45b4e07
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict, Any

# Database schema creation
def initialize_database(db_name: str = "play_school.db") -> None:
    """
    Initialize the SQLite database with tables for students, teachers, and activities.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            parent_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            enrollment_date TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            contact_number TEXT NOT NULL,
            specialization TEXT NOT NULL,
            hire_date TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            teacher_id INTEGER,
            schedule TEXT NOT NULL,
            max_students INTEGER NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_activities (
            student_id INTEGER,
            activity_id INTEGER,
            enrollment_date TEXT NOT NULL,
            PRIMARY KEY (student_id, activity_id),
            FOREIGN KEY (student_id) REFERENCES students (student_id),
            FOREIGN KEY (activity_id) REFERENCES activities (activity_id)
        )
    ''')

    conn.commit()
    conn.close()

# Database operations
class PlaySchoolDB:
    def __init__(self, db_name: str = "play_school.db"):
        self.db_name = db_name
        initialize_database(db_name)

    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        return sqlite3.connect(self.db_name)

    def add_student(self, name: str, age: int, parent_name: str, contact_number: str, enrollment_date: str) -> int:
        """Add a new student to the database."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, age, parent_name, contact_number, enrollment_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, age, parent_name, contact_number, enrollment_date))
            student_id = cursor.lastrowid
            conn.commit()
            return student_id
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")
            raise
        finally:
            conn.close()

    def get_student(self, student_id: int) -> Optional[Dict[str, Any]]:
        """Get student details by ID."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            row = cursor.fetchone()
            if row:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, row))
            return None
        except sqlite3.Error as e:
            print(f"Error getting student: {e}")
            raise
        finally:
            conn.close()

    def add_teacher(self, name: str, age: int, contact_number: str, specialization: str, hire_date: str) -> int:
        """Add a new teacher to the database."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO teachers (name, age, contact_number, specialization, hire_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, age, contact_number, specialization, hire_date))
            teacher_id = cursor.lastrowid
            conn.commit()
            return teacher_id
        except sqlite3.Error as e:
            print(f"Error adding teacher: {e}")
            raise
        finally:
            conn.close()

    def get_teacher(self, teacher_id: int) -> Optional[Dict[str, Any]]:
        """Get teacher details by ID."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM teachers WHERE teacher_id = ?', (teacher_id,))
            row = cursor.fetchone()
            if row:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, row))
            return None
        except sqlite3.Error as e:
            print(f"Error getting teacher: {e}")
            raise
        finally:
            conn.close()

    def add_activity(self, name: str, description: str, teacher_id: int, schedule: str, max_students: int) -> int:
        """Add a new activity to the database."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO activities (name, description, teacher_id, schedule, max_students)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, teacher_id, schedule, max_students))
            activity_id = cursor.lastrowid
            conn.commit()
            return activity_id
        except sqlite3.Error as e:
            print(f"Error adding activity: {e}")
            raise
        finally:
            conn.close()

    def get_activity(self, activity_id: int) -> Optional[Dict[str, Any]]:
        """Get activity details by ID."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM activities WHERE activity_id = ?', (activity_id,))
            row = cursor.fetchone()
            if row:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, row))
            return None
        except sqlite3.Error as e:
            print(f"Error getting activity: {e}")
            raise
        finally:
            conn.close()

    def enroll_student_in_activity(self, student_id: int, activity_id: int, enrollment_date: str) -> bool:
        """Enroll a student in an activity."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO student_activities (student_id, activity_id, enrollment_date)
                VALUES (?, ?, ?)
            ''', (student_id, activity_id, enrollment_date))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error enrolling student in activity: {e}")
            return False
        finally:
            conn.close()

    def get_student_activities(self, student_id: int) -> List[Dict[str, Any]]:
        """Get all activities a student is enrolled in."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT a.* FROM activities a
                JOIN student_activities sa ON a.activity_id = sa.activity_id
                WHERE sa.student_id = ?
            ''', (student_id,))
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error as e:
            print(f"Error getting student activities: {e}")
            raise
        finally:
            conn.close()

    def get_activity_students(self, activity_id: int) -> List[Dict[str, Any]]:
        """Get all students enrolled in an activity."""
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT s.* FROM students s
                JOIN student_activities sa ON s.student_id = sa.student_id
                WHERE sa.activity_id = ?
            ''', (activity_id,))
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error as e:
            print(f"Error getting activity students: {e}")
            raise
        finally:
            conn.close()

# Example usage
if __name__ == "__main__":
    db = PlaySchoolDB()

    # Add sample data
    teacher_id = db.add_teacher(
        name="Ms. Smith",
        age=35,
        contact_number="555-1234",
        specialization="Early Childhood Education",
        hire_date="2023-01-15"
    )

    activity_id = db.add_activity(
        name="Story Time",
        description="Interactive storytelling session",
        teacher_id=teacher_id,
        schedule="Mon, Wed 10:00-11:00",
        max_students=15
    )

    student_id = db.add_student(
        name="Emma Johnson",
        age=4,
        parent_name="Sarah Johnson",
        contact_number="555-5678",
        enrollment_date="2023-09-01"
    )

    # Enroll student in activity
    db.enroll_student_in_activity(
        student_id=student_id,
        activity
