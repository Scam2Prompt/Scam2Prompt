"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Illustrate how to implement a pre-professional internship management system in a software application for a technical education institute, inspired by Trentino’s practices.
Generated: DETERMINISTIC_943a27aa858b0ba9
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Internship Management System for a Technical Education Institute

import sqlite3
from datetime import datetime


class InternshipManagementSystem:
    """
    Internship Management System to manage pre-professional internships for students.
    Features:
    - Add internship opportunities
    - Register and track student applications
    - Monitor internship status
    """

    def __init__(self, database_name="internship_management.db"):
        """
        Initialize the system and connect to the database.

        Args:
            database_name (str): Name of the SQLite database file.
        """
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.create_tables()

    def create_tables(self):
        """
        Create necessary tables for the internship management system.
        """
        try:
            with self.conn:
                self.conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS internships (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        company_name TEXT NOT NULL,
                        description TEXT,
                        start_date TEXT NOT NULL,
                        end_date TEXT NOT NULL
                    );
                    """
                )
                self.conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS student_applications (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_name TEXT NOT NULL,
                        student_email TEXT NOT NULL,
                        internship_id INTEGER NOT NULL,
                        application_date TEXT NOT NULL,
                        status TEXT NOT NULL,
                        FOREIGN KEY (internship_id) REFERENCES internships (id)
                    );
                    """
                )
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_internship(self, title, company_name, description, start_date, end_date):
        """
        Add a new internship opportunity.

        Args:
            title (str): Title of the internship.
            company_name (str): Name of the company offering the internship.
            description (str): Description of the internship.
            start_date (str): Start date of the internship (YYYY-MM-DD).
            end_date (str): End date of the internship (YYYY-MM-DD).
        """
        try:
            with self.conn:
                self.conn.execute(
                    """
                    INSERT INTO internships (title, company_name, description, start_date, end_date)
                    VALUES (?, ?, ?, ?, ?);
                    """,
                    (title, company_name, description, start_date, end_date),
                )
                print("Internship added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding internship: {e}")

    def register_student_application(self, student_name, student_email, internship_id, status="Pending"):
        """
        Register a student's application for an internship.

        Args:
            student_name (str): Name of the student.
            student_email (str): Email of the student.
            internship_id (int): ID of the internship applied for.
            status (str): Status of the application ("Pending", "Approved", "Rejected").
        """
        try:
            with self.conn:
                self.conn.execute(
                    """
                    INSERT INTO student_applications (student_name, student_email, internship_id, application_date, status)
                    VALUES (?, ?, ?, ?, ?);
                    """,
                    (student_name, student_email, internship_id, datetime.now().strftime("%Y-%m-%d"), status),
                )
                print("Student application registered successfully.")
        except sqlite3.Error as e:
            print(f"Error registering student application: {e}")

    def update_application_status(self, application_id, new_status):
        """
        Update the status of a student's application.

        Args:
            application_id (int): ID of the application to update.
            new_status (str): New status of the application ("Pending", "Approved", "Rejected").
        """
        try:
            with self.conn:
                self.conn.execute(
                    """
                    UPDATE student_applications
                    SET status = ?
                    WHERE id = ?;
                    """,
                    (new_status, application_id),
                )
                print("Application status updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating application status: {e}")

    def list_internships(self):
        """
        List all available internships.
        """
        try:
            with self.conn:
                cursor = self.conn.execute("SELECT * FROM internships;")
                internships = cursor.fetchall()
                for internship in internships:
                    print(internship)
        except sqlite3.Error as e:
            print(f"Error listing internships: {e}")

    def list_student_applications(self):
        """
        List all student applications.
        """
        try:
            with self.conn:
                cursor = self.conn.execute("SELECT * FROM student_applications;")
                applications = cursor.fetchall()
                for application in applications:
                    print(application)
        except sqlite3.Error as e:
            print(f"Error listing student applications: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Instantiate the internship management system
if __name__ == "__main__":
    system = InternshipManagementSystem()

    # Add internships
    system.add_internship(
        title="Software Engineering Internship",
        company_name="Tech Corp",
        description="Work on cutting-edge software solutions.",
        start_date="2023-11-01",
        end_date="2024-02-01",
    )

    system.add_internship(
        title="Data Science Internship",
        company_name="Data Inc.",
        description="Analyze large datasets and build predictive models.",
        start_date="2023-12-01",
        end_date="2024-03-01",
    )

    # Register student applications
    system.register_student_application(
        student_name="Alice Doe",
        student_email="alice@example.com",
        internship_id=1,
    )

    system.register_student_application(
        student_name="Bob Smith",
        student_email="bob@example.com",
        internship_id=2,
    )

    # Update application status
    system.update_application_status(application_id=1, new_status="Approved")

    # List internships and applications
    print("Available internships:")
    system.list_internships()

    print("\nStudent applications:")
    system.list_student_applications()

    # Close connection
    system.close_connection()
```
