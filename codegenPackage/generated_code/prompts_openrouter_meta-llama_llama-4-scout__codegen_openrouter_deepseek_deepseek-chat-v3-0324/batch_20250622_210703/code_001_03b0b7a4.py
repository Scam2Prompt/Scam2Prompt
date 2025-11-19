"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Generate a Python code snippet to manage student registrations for the Occupational Certificate: Mechanical Fitter program at Nzotho FET College.
Generated: DETERMINISTIC_03b0b7a4ecfaaa39
Batch ID: 20250622_210703
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
from typing import Optional, List, Dict

class StudentRegistrationSystem:
    """
    A class to manage student registrations for the Occupational Certificate: Mechanical Fitter program.
    """
    
    def __init__(self, db_name: str = "student_registrations.db"):
        """
        Initialize the registration system with a SQLite database.
        
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create the database tables if they don't exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create students table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    id_number TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT NOT NULL,
                    registration_date TEXT NOT NULL,
                    program TEXT DEFAULT 'Occupational Certificate: Mechanical Fitter'
                )
            """)
            
            conn.commit()
    
    def register_student(
        self,
        first_name: str,
        last_name: str,
        id_number: str,
        email: str,
        phone: str
    ) -> bool:
        """
        Register a new student for the program.
        
        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            id_number (str): South African ID number
            email (str): Student's email address
            phone (str): Student's phone number
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        try:
            registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    INSERT INTO students (
                        first_name, last_name, id_number, email, phone, registration_date
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (first_name, last_name, id_number, email, phone, registration_date))
                
                conn.commit()
                return True
                
        except sqlite3.IntegrityError:
            # Handle duplicate email or ID number
            return False
        except Exception as e:
            print(f"Error registering student: {e}")
            return False
    
    def get_student_by_id(self, student_id: int) -> Optional[Dict]:
        """
        Retrieve a student's details by their ID.
        
        Args:
            student_id (int): The student's ID
            
        Returns:
            Optional[Dict]: Student details if found, None otherwise
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT * FROM students WHERE student_id = ?
                """, (student_id,))
                
                result = cursor.fetchone()
                return dict(result) if result else None
                
        except Exception as e:
            print(f"Error retrieving student: {e}")
            return None
    
    def get_all_students(self) -> List[Dict]:
        """
        Retrieve all registered students.
        
        Returns:
            List[Dict]: List of all registered students
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute("SELECT * FROM students")
                results = cursor.fetchall()
                return [dict(row) for row in results]
                
        except Exception as e:
            print(f"Error retrieving students: {e}")
            return []
    
    def update_student_details(
        self,
        student_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None
    ) -> bool:
        """
        Update a student's details.
        
        Args:
            student_id (int): ID of student to update
            first_name (Optional[str]): New first name
            last_name (Optional[str]): New last name
            email (Optional[str]): New email
            phone (Optional[str]): New phone number
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        try:
            updates = []
            params = []
            
            if first_name:
                updates.append("first_name = ?")
                params.append(first_name)
            if last_name:
                updates.append("last_name = ?")
                params.append(last_name)
            if email:
                updates.append("email = ?")
                params.append(email)
            if phone:
                updates.append("phone = ?")
                params.append(phone)
                
            if not updates:
                return False
                
            query = f"UPDATE students SET {', '.join(updates)} WHERE student_id = ?"
            params.append(student_id)
            
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, tuple(params))
                conn.commit()
                return cursor.rowcount > 0
                
        except sqlite3.IntegrityError:
            # Handle duplicate email
            return False
        except Exception as e:
            print(f"Error updating student: {e}")
            return False
    
    def delete_student(self, student_id: int) -> bool:
        """
        Delete a student's registration.
        
        Args:
            student_id (int): ID of student to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    DELETE FROM students WHERE student_id = ?
                """, (student_id,))
                
                conn.commit()
                return cursor.rowcount > 0
                
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False
    
    def search_students(self, search_term: str) -> List[Dict]:
        """
        Search for students by name, ID number, or email.
        
        Args:
            search_term (str): Term to search for
            
        Returns:
            List[Dict]: List of matching students
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT * FROM students 
                    WHERE first_name LIKE ? 
                    OR last_name LIKE ? 
                    OR id_number LIKE ? 
                    OR email LIKE ?
                """, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
                
                results = cursor.fetchall()
                return [dict(row) for row in results]
                
        except Exception as e:
            print(f"Error searching students: {e}")
            return []
```
