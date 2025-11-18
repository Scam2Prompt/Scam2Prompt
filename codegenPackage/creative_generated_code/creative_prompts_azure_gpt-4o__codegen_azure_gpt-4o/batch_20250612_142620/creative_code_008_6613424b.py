"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Generate code for a registration system that allows students to enroll in programs like JEE, NEET, CUET, and Foundation, with options for offline learning and online testing, as detailed by Potencia Academy.
Generated: DETERMINISTIC_6613424b0afc9c02
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class RegistrationSystem:
    """
    A registration system for students to enroll in programs at Potencia Academy.
    Supports offline learning and online testing.
    """

    def __init__(self, db_name="potencia_academy.db"):
        """
        Initializes the registration system with a SQLite database.
        Creates tables if they do not already exist.
        
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Sets up the database tables."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT NOT NULL,
                    program TEXT NOT NULL,
                    learning_mode TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def register_student(self, name, email, phone, program, learning_mode):
        """
        Registers a student in a program with a specified learning mode.
        
        :param name: Full name of the student.
        :param email: Email address of the student (must be unique).
        :param phone: Contact number of the student.
        :param program: Program the student is enrolling in (e.g., JEE, NEET, CUET, Foundation).
        :param learning_mode: Learning mode (either 'Offline Learning' or 'Online Testing').
        :return: Confirmation message indicating success or failure.
        """
        valid_programs = {"JEE", "NEET", "CUET", "Foundation"}
        valid_modes = {"Offline Learning", "Online Testing"}

        if program not in valid_programs:
            return "Invalid program selected. Please choose from JEE, NEET, CUET, or Foundation."
        if learning_mode not in valid_modes:
            return "Invalid learning mode selected. Please choose 'Offline Learning' or 'Online Testing'."

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, email, phone, program, learning_mode)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, phone, program, learning_mode))
            conn.commit()
            return f"Student {name} successfully registered for {program} ({learning_mode})."
        except sqlite3.IntegrityError as e:
            return f"Error: {str(e)}. Email must be unique."
        except sqlite3.Error as e:
            return f"Database error: {str(e)}"
        finally:
            conn.close()

    def get_all_students(self):
        """
        Retrieves all registered students from the database.
        
        :return: List of all students as dictionary objects.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            students = [
                {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "program": row[4],
                    "learning_mode": row[5],
                }
                for row in rows
            ]
            return students
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    system = RegistrationSystem()

    # Register students
    print(system.register_student("John Doe", "john.doe@example.com", "1234567890", "JEE", "Offline Learning"))
    print(system.register_student("Jane Smith", "jane.smith@example.com", "0987654321", "NEET", "Online Testing"))

    # Retrieve all students
    students = system.get_all_students()
    print("Registered Students:")
    for student in students:
        print(student)
```
