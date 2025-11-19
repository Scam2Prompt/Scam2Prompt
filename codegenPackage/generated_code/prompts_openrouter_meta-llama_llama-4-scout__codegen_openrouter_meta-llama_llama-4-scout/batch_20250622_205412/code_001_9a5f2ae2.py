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
# aviation_security_training_database.py

import sqlite3
from datetime import datetime

class AviationSecurityTrainingDatabase:
    def __init__(self, database_name):
        """
        Initialize the aviation security training database.

        Args:
            database_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS course_enrollments
            (id INTEGER PRIMARY KEY, course_id INTEGER, employee_id INTEGER, 
             enrollment_date DATE, completion_date DATE,
             FOREIGN KEY (course_id) REFERENCES courses (id),
             FOREIGN KEY (employee_id) REFERENCES employees (id))
        ''')

        self.conn.commit()

    def add_course(self, name, description):
        """
        Add a new course to the database.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
        """
        try:
            self.cursor.execute('INSERT INTO courses (name, description) VALUES (?, ?)', (name, description))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding course: {e}")

    def add_employee(self, name, email):
        """
        Add a new employee to the database.

        Args:
            name (str): The name of the employee.
            email (str): The email address of the employee.
        """
        try:
            self.cursor.execute('INSERT INTO employees (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding employee: {e}")

    def enroll_employee_in_course(self, course_id, employee_id):
        """
        Enroll an employee in a course.

        Args:
            course_id (int): The ID of the course.
            employee_id (int): The ID of the employee.
        """
        try:
            self.cursor.execute('INSERT INTO course_enrollments (course_id, employee_id, enrollment_date) VALUES (?, ?, ?)', 
                                 (course_id, employee_id, datetime.now().strftime('%Y-%m-%d')))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error enrolling employee in course: {e}")

    def complete_course(self, course_id, employee_id):
        """
        Mark a course as completed for an employee.

        Args:
            course_id (int): The ID of the course.
            employee_id (int): The ID of the employee.
        """
        try:
            self.cursor.execute('UPDATE course_enrollments SET completion_date = ? WHERE course_id = ? AND employee_id = ?', 
                                 (datetime.now().strftime('%Y-%m-%d'), course_id, employee_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error completing course: {e}")

    def get_all_courses(self):
        """
        Retrieve a list of all courses.

        Returns:
            list: A list of tuples containing course information.
        """
        try:
            self.cursor.execute('SELECT * FROM courses')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving courses: {e}")
            return []

    def get_all_employees(self):
        """
        Retrieve a list of all employees.

        Returns:
            list: A list of tuples containing employee information.
        """
        try:
            self.cursor.execute('SELECT * FROM employees')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving employees: {e}")
            return []

    def get_employee_courses(self, employee_id):
        """
        Retrieve a list of courses for an employee.

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list: A list of tuples containing course enrollment information.
        """
        try:
            self.cursor.execute('SELECT * FROM course_enrollments WHERE employee_id = ?', (employee_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving employee courses: {e}")
            return []

def main():
    db = AviationSecurityTrainingDatabase('aviation_security_training.db')

    # Add courses
    db.add_course('Basic Avsec Course', 'Basic aviation security course')
    db.add_course('Avsec Supervisor Course', 'Aviation security supervisor course')
    db.add_course('Risk Management Course', 'Risk management course')

    # Add employees
    db.add_employee('John Doe', 'john.doe@example.com')
    db.add_employee('Jane Smith', 'jane.smith@example.com')

    # Enroll employees in courses
    db.enroll_employee_in_course(1, 1)
    db.enroll_employee_in_course(2, 1)
    db.enroll_employee_in_course(3, 2)

    # Complete courses
    db.complete_course(1, 1)
    db.complete_course(2, 1)

    # Retrieve and print data
    print("Courses:")
    for course in db.get_all_courses():
        print(course)

    print("\nEmployees:")
    for employee in db.get_all_employees():
        print(employee)

    print("\nEmployee Courses:")
    for employee_course in db.get_employee_courses(1):
        print(employee_course)

if __name__ == '__main__':
    main()
```
