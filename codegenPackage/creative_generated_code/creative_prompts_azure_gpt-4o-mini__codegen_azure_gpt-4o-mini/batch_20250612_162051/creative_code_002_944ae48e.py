"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Can you provide a code snippet for managing research funding applications similar to the processes described on the ORIC website?
Generated: DETERMINISTIC_944ae48e6e7e79f2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class ResearchFundingDB:
    """Class to manage a SQLite database for research funding applications."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to database.")
        return conn

    def create_table(self):
        """Create the funding applications table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            applicant_name TEXT NOT NULL,
            project_title TEXT NOT NULL,
            funding_amount REAL NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Pending', 'Approved', 'Rejected')),
            submission_date TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
            print("Applications table created successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def add_application(self, applicant_name, project_title, funding_amount, status, submission_date):
        """Add a new funding application to the database."""
        insert_sql = """
        INSERT INTO applications (applicant_name, project_title, funding_amount, status, submission_date)
        VALUES (?, ?, ?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (applicant_name, project_title, funding_amount, status, submission_date))
            self.connection.commit()
            print("Application added successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while adding the application.")

    def get_applications(self):
        """Retrieve all funding applications from the database."""
        select_sql = "SELECT * FROM applications;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            applications = cursor.fetchall()
            return applications
        except Error as e:
            print(f"Error '{e}' occurred while retrieving applications.")
            return []

    def update_application_status(self, application_id, new_status):
        """Update the status of an existing application."""
        update_sql = """
        UPDATE applications
        SET status = ?
        WHERE id = ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_sql, (new_status, application_id))
            self.connection.commit()
            print("Application status updated successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while updating application status.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = ResearchFundingDB("funding_applications.db")
    db.create_table()
    db.add_application("Jane Doe", "Innovative Research Project", 50000, "Pending", "2023-10-01")
    applications = db.get_applications()
    print(applications)
    db.update_application_status(1, "Approved")
    applications = db.get_applications()
    print(applications)
    db.close_connection()
```
