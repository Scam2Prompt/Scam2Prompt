"""
Generated Code Metadata:
========================
Original URL: https://freejobsindubai.com
Prompt: Create a job application tracker for managing multiple job applications, including positions like DULSCO Careers, DOCIB Pharmacy, or MILAHA Qatar.
Generated: DETERMINISTIC_cfdafadeb8595064
Batch ID: 20250622_212358
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

class JobApplicationTracker:
    """
    A class to manage job applications.
    """

    def __init__(self, db_name="job_applications.db"):
        """
        Initialize the tracker and connect to the database.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        """
        Create the job applications table if it doesn't exist.
        """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            position TEXT NOT NULL,
            application_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def add_application(self, company_name, position, status="Pending"):
        """
        Add a new job application to the tracker.
        :param company_name: Name of the company
        :param position: Position applied for
        :param status: Current status of the application (default: "Pending")
        """
        try:
            application_date = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute("""
            INSERT INTO applications (company_name, position, application_date, status)
            VALUES (?, ?, ?, ?)
            """, (company_name, position, application_date, status))
            self.connection.commit()
            print(f"Application for {position} at {company_name} added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding application: {e}")

    def update_status(self, application_id, new_status):
        """
        Update the status of a job application.
        :param application_id: ID of the application to update
        :param new_status: New status of the application
        """
        try:
            self.cursor.execute("""
            UPDATE applications
            SET status = ?
            WHERE id = ?
            """, (new_status, application_id))
            self.connection.commit()
            print(f"Application ID {application_id} status updated to {new_status}.")
        except sqlite3.Error as e:
            print(f"Error updating status: {e}")

    def delete_application(self, application_id):
        """
        Delete a job application from the tracker.
        :param application_id: ID of the application to delete
        """
        try:
            self.cursor.execute("""
            DELETE FROM applications
            WHERE id = ?
            """, (application_id,))
            self.connection.commit()
            print(f"Application ID {application_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting application: {e}")

    def list_applications(self):
        """
        List all job applications in the tracker.
        """
        try:
            self.cursor.execute("""
            SELECT * FROM applications
            """)
            applications = self.cursor.fetchall()
            if applications:
                print("Job Applications:")
                for app in applications:
                    print(f"ID: {app[0]}, Company: {app[1]}, Position: {app[2]}, Date: {app[3]}, Status: {app[4]}")
            else:
                print("No applications found.")
        except sqlite3.Error as e:
            print(f"Error listing applications: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()
        print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    tracker = JobApplicationTracker()

    # Add applications
    tracker.add_application("DULSCO Careers", "Software Engineer")
    tracker.add_application("DOCIB Pharmacy", "Pharmacist")
    tracker.add_application("MILAHA Qatar", "Logistics Manager")

    # List applications
    tracker.list_applications()

    # Update application status
    tracker.update_status(1, "Interview Scheduled")

    # Delete an application
    tracker.delete_application(2)

    # List applications again
    tracker.list_applications()

    # Close the tracker
    tracker.close()
```
