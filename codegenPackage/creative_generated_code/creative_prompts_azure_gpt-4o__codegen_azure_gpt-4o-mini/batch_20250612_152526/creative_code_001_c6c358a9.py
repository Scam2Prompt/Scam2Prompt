"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Recommend a library or API for managing educational institution data, including features for tracking student performance, managing administrative tasks, and generating reports like those mentioned in the Politécnico Municipal's system.
Generated: DETERMINISTIC_c6c358a914f4ed56
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from typing import List, Dict, Any

class EducationalInstitutionDB:
    """
    A class to manage educational institution data including students, 
    performance tracking, administrative tasks, and report generation.
    """

    def __init__(self, db_name: str):
        """
        Initializes the database connection.
        
        :param db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates necessary tables if they do not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                class TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS performance (
                performance_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject TEXT,
                grade TEXT,
                FOREIGN KEY(student_id) REFERENCES students(student_id)
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS administrative_tasks (
                task_id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                due_date TEXT
            )
        ''')
        
        self.conn.commit()

    def add_student(self, name: str, age: int, class_name: str):
        """Adds a new student to the database.
        
        :param name: Name of the student.
        :param age: Age of the student.
        :param class_name: Class of the student.
        """
        try:
            self.cursor.execute('''
                INSERT INTO students (name, age, class) VALUES (?, ?, ?)
            ''', (name, age, class_name))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")

    def record_performance(self, student_id: int, subject: str, grade: str):
        """Records a student's performance in a subject.
        
        :param student_id: ID of the student.
        :param subject: Subject name.
        :param grade: Grade received.
        """
        try:
            self.cursor.execute('''
                INSERT INTO performance (student_id, subject, grade) VALUES (?, ?, ?)
            ''', (student_id, subject, grade))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error recording performance: {e}")

    def add_task(self, description: str, due_date: str):
        """Adds an administrative task to the database.
        
        :param description: Description of the task.
        :param due_date: Due date for the task.
        """
        try:
            self.cursor.execute('''
                INSERT INTO administrative_tasks (description, due_date) VALUES (?, ?)
            ''', (description, due_date))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding task: {e}")

    def generate_report(self, student_id: int) -> Dict[str, Any]:
        """Generates a report for a specific student.
        
        :param student_id: ID of the student.
        :return: A dictionary containing student details and performance.
        """
        try:
            self.cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            student = self.cursor.fetchone()

            self.cursor.execute('SELECT * FROM performance WHERE student_id = ?', (student_id,))
            performance = self.cursor.fetchall()

            report = {
                "student": student,
                "performance": performance
            }
            return report
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")
            return {}

    def close(self):
        """Closes the database connection."""
        self.conn.close()


# Example usage of the EducationalInstitutionDB class
if __name__ == "__main__":
    db = EducationalInstitutionDB('institution_data.db')
    db.add_student("John Doe", 20, "Computer Science")
    db.record_performance(1, "Mathematics", "A")
    db.add_task("Submit project report", "2023-12-01")
    
    report = db.generate_report(1)
    print(report)  # Display the generated report

    db.close()
```
