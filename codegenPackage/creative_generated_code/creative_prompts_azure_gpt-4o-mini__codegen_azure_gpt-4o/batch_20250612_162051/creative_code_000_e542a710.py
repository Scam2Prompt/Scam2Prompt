"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercedariasgye.edu.ec
Prompt: Generate a Python script to automate the process of managing student admissions for an educational institution, similar to the admissions process described on the MercedariasGye website.
Generated: DETERMINISTIC_e542a71099e40aea
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Student Admissions Management System

This script provides functionality to manage student admissions for an educational institution.
It includes features to add new applicants, view applicant details, update applicant status, 
and generate reports. The data is stored in a local SQLite database.
"""

import sqlite3
import os


class AdmissionsManager:
    def __init__(self, db_name="admissions.db"):
        """
        Initializes the Admissions Manager and sets up the database connection.

        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = None
        self._setup_database()

    def _setup_database(self):
        """
        Creates the database file and necessary tables if they don't exist.
        """
        if not os.path.exists(self.db_name):
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS applicants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL,
                    parent_contact TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending' CHECK(status IN ('Pending', 'Accepted', 'Rejected'))
                )
            """)
            self.connection.commit()
        else:
            self.connection = sqlite3.connect(self.db_name)

    def add_applicant(self, name, age, grade, parent_contact):
        """
        Adds a new applicant to the database.

        :param name: Name of the applicant
        :param age: Age of the applicant
        :param grade: Grade applying for
        :param parent_contact: Parent's contact information
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO applicants (name, age, grade, parent_contact) 
                VALUES (?, ?, ?, ?)
            """, (name, age, grade, parent_contact))
            self.connection.commit()
            print("Applicant added successfully!")
        except sqlite3.Error as e:
            print(f"Error adding applicant: {e}")

    def view_applicant_details(self, applicant_id):
        """
        Retrieves and displays details of a specific applicant.

        :param applicant_id: ID of the applicant
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM applicants WHERE id = ?", (applicant_id,))
            applicant = cursor.fetchone()
            if applicant:
                print(f"ID: {applicant[0]}, Name: {applicant[1]}, Age: {applicant[2]}, "
                      f"Grade: {applicant[3]}, Parent Contact: {applicant[4]}, Status: {applicant[5]}")
            else:
                print("Applicant not found.")
        except sqlite3.Error as e:
            print(f"Error retrieving applicant details: {e}")

    def update_applicant_status(self, applicant_id, new_status):
        """
        Updates the admission status of an applicant.

        :param applicant_id: ID of the applicant
        :param new_status: New status ('Pending', 'Accepted', 'Rejected')
        """
        if new_status not in ('Pending', 'Accepted', 'Rejected'):
            print("Invalid status. Must be 'Pending', 'Accepted', or 'Rejected'.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE applicants 
                SET status = ? 
                WHERE id = ?
            """, (new_status, applicant_id))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Applicant status updated successfully!")
            else:
                print("Applicant not found.")
        except sqlite3.Error as e:
            print(f"Error updating applicant status: {e}")

    def generate_report(self):
        """
        Generates and displays a report of all applicants.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM applicants")
            applicants = cursor.fetchall()
            print("Admissions Report:")
            print("ID | Name | Age | Grade | Parent Contact | Status")
            print("-" * 50)
            for applicant in applicants:
                print(f"{applicant[0]} | {applicant[1]} | {applicant[2]} | {applicant[3]} | "
                      f"{applicant[4]} | {applicant[5]}")
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    manager = AdmissionsManager()

    # Sample usage of the AdmissionsManager class
    # Uncomment and modify the following lines for testing purposes

    # Add new applicants
    # manager.add_applicant("John Doe", 14, "9th Grade", "1234567890")
    # manager.add_applicant("Jane Smith", 12, "7th Grade", "0987654321")

    # View applicant details
    # manager.view_applicant_details(1)

    # Update applicant status
    # manager.update_applicant_status(1, "Accepted")

    # Generate admissions report
    # manager.generate_report()

    # Close the database connection
    manager.close_connection()
```
