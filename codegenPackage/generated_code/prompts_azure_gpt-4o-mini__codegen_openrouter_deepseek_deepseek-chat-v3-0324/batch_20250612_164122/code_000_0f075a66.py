"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Generate a Python script that connects to a database for managing student records in a technical education institution like I.E.S.T.P. Trentino Juan Pablo II.
Generated: DETERMINISTIC_0f075a660d12cf3e
Batch ID: 20250612_164122
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

class StudentDatabase:
    """
    A class to manage student records in a SQLite database.
    """

    def __init__(self, db_name: str = "student_records.db") -> None:
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                dni TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                career TEXT NOT NULL,
                semester INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_student(self, first_name: str, last_name: str, dni: str, email: str, 
                    career: str, semester: int, phone: Optional[str] = None) -> bool:
        """
        Add a new student record to the database.
        
        Args:
            first_name: Student's first name.
            last_name: Student's last name.
            dni: Student's national ID (must be unique).
            email: Student's email (must be unique).
            career: Student's career program.
            semester: Current semester (1-10).
            phone: Optional phone number.
            
        Returns:
            bool: True if successful, False if failed.
        """
        try:
            self.cursor.execute("""
                INSERT INTO students 
                (first_name, last_name, dni, email, phone, career, semester)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (first_name, last_name, dni, email, phone, career, semester))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: DNI or Email already exists.")
            return False
        except Exception as e:
            print(f"Error adding student: {e}")
            return False

    def get_student(self, student_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a student record by ID.
        
        Args:
            student_id: The ID of the student to retrieve.
            
        Returns:
            dict: Student record if found, None otherwise.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM students WHERE id = ?
            """, (student_id,))
            row = self.cursor.fetchone()
            if row:
                columns = [desc[0] for desc in self.cursor.description]
                return dict(zip(columns, row))
            return None
        except Exception as e:
            print(f"Error retrieving student: {e}")
            return None

    def update_student(self, student_id: int, **kwargs) -> bool:
        """
        Update a student record.
        
        Args:
            student_id: ID of the student to update.
            kwargs: Fields to update (e.g., first_name="New Name").
            
        Returns:
            bool: True if successful, False otherwise.
        """
        if not kwargs:
            return False

        set_clause = ", ".join([f"{key} = ?" for key in kwargs])
        values = list(kwargs.values())
        values.append(student_id)

        try:
            self.cursor.execute(f"""
                UPDATE students SET {set_clause} WHERE id = ?
            """, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating student: {e}")
            return False

    def delete_student(self, student_id: int) -> bool:
        """
        Delete a student record.
        
        Args:
            student_id: ID of the student to delete.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            self.cursor.execute("""
                DELETE FROM students WHERE id = ?
            """, (student_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False

    def list_students(self, career: Optional[str] = None, 
                      semester: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        List all students, optionally filtered by career or semester.
        
        Args:
            career: Filter by career program.
            semester: Filter by semester.
            
        Returns:
            list: List of student records.
        """
        query = "SELECT * FROM students"
        params = []
        
        if career or semester:
            conditions = []
            if career:
                conditions.append("career = ?")
                params.append(career)
            if semester:
                conditions.append("semester = ?")
                params.append(semester)
            query += " WHERE " + " AND ".join(conditions)
        
        try:
            self.cursor.execute(query, params)
            rows = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            print(f"Error listing students: {e}")
            return []

    def __del__(self) -> None:
        """Clean up the database connection."""
        if hasattr(self, 'conn'):
            self.conn.close()

# Example usage
if __name__ == "__main__":
    db = StudentDatabase()
    
    # Add a student
    db.add_student(
        first_name="Juan",
        last_name="Perez",
        dni="12345678",
        email="juan@example.com",
        career="Software Engineering",
        semester=3,
        phone="987654321"
    )
    
    # List all students
    students = db.list_students()
    print("All students:", students)
    
    # List students in a specific career
    cs_students = db.list_students(career="Software Engineering")
    print("CS students:", cs_students)
```
