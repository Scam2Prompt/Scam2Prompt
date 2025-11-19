"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Write a code snippet to create a simple database for tracking education projects, inspired by HARDA's education initiatives in the Horn of Africa.
Generated: DETERMINISTIC_c7b18293ca09bf4b
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# education_project_tracker.py

import sqlite3
from datetime import datetime

class EducationProjectTracker:
    def __init__(self, db_name):
        """
        Initialize the EducationProjectTracker with a database name.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             description TEXT,
             start_date DATE,
             end_date DATE,
             status TEXT CHECK(status IN ('active', 'inactive', 'completed')))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT UNIQUE,
             project_id INTEGER,
             FOREIGN KEY (project_id) REFERENCES projects (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT UNIQUE,
             project_id INTEGER,
             FOREIGN KEY (project_id) REFERENCES projects (id))
        ''')

        self.conn.commit()

    def add_project(self, name, description, start_date, end_date, status='active'):
        """
        Add a new education project.

        Args:
            name (str): The name of the project.
            description (str): A brief description of the project.
            start_date (str): The start date of the project in YYYY-MM-DD format.
            end_date (str): The end date of the project in YYYY-MM-DD format.
            status (str, optional): The status of the project. Defaults to 'active'.

        Returns:
            int: The ID of the newly added project.
        """
        try:
            self.cursor.execute('''
                INSERT INTO projects (name, description, start_date, end_date, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, start_date, end_date, status))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")
            return None

    def add_student(self, name, email, project_id):
        """
        Add a new student to a project.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.
            project_id (int): The ID of the project the student belongs to.

        Returns:
            int: The ID of the newly added student.
        """
        try:
            self.cursor.execute('''
                INSERT INTO students (name, email, project_id)
                VALUES (?, ?, ?)
            ''', (name, email, project_id))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")
            return None

    def add_teacher(self, name, email, project_id):
        """
        Add a new teacher to a project.

        Args:
            name (str): The name of the teacher.
            email (str): The email address of the teacher.
            project_id (int): The ID of the project the teacher belongs to.

        Returns:
            int: The ID of the newly added teacher.
        """
        try:
            self.cursor.execute('''
                INSERT INTO teachers (name, email, project_id)
                VALUES (?, ?, ?)
            ''', (name, email, project_id))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding teacher: {e}")
            return None

    def get_project(self, project_id):
        """
        Retrieve a project by its ID.

        Args:
            project_id (int): The ID of the project to retrieve.

        Returns:
            dict: A dictionary containing the project's details.
        """
        try:
            self.cursor.execute('''
                SELECT * FROM projects
                WHERE id = ?
            ''', (project_id,))
            project = self.cursor.fetchone()
            if project:
                return {
                    'id': project[0],
                    'name': project[1],
                    'description': project[2],
                    'start_date': project[3],
                    'end_date': project[4],
                    'status': project[5]
                }
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error retrieving project: {e}")
            return None

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    tracker = EducationProjectTracker('education_projects.db')

    # Add a new project
    project_id = tracker.add_project(
        'Horn of Africa Education Initiative',
        'A project to improve education in the Horn of Africa',
        '2022-01-01',
        '2023-12-31'
    )
    print(f"Project ID: {project_id}")

    # Add students and teachers to the project
    student_id = tracker.add_student('John Doe', 'john.doe@example.com', project_id)
    teacher_id = tracker.add_teacher('Jane Smith', 'jane.smith@example.com', project_id)
    print(f"Student ID: {student_id}, Teacher ID: {teacher_id}")

    # Retrieve the project
    project = tracker.get_project(project_id)
    print(project)

    # Close the database connection
    tracker.close_connection()


if __name__ == '__main__':
    main()
```
