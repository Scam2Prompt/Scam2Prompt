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
from typing import List, Dict, Optional

class JobApplicationTracker:
    """
    A class to track job applications with CRUD operations and status tracking.
    """
    
    def __init__(self, db_name: str = "job_applications.db"):
        """
        Initialize the tracker with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self) -> None:
        """Create the applications table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                position TEXT NOT NULL,
                application_date TEXT NOT NULL,
                status TEXT NOT NULL,
                notes TEXT,
                contact_email TEXT,
                contact_phone TEXT,
                last_updated TEXT NOT NULL
            )
        """)
        self.conn.commit()
    
    def add_application(
        self,
        company: str,
        position: str,
        status: str = "Applied",
        notes: Optional[str] = None,
        contact_email: Optional[str] = None,
        contact_phone: Optional[str] = None
    ) -> int:
        """
        Add a new job application to the tracker.
        
        Args:
            company: Name of the company.
            position: Job position title.
            status: Current application status (default: "Applied").
            notes: Optional notes about the application.
            contact_email: Optional contact email.
            contact_phone: Optional contact phone number.
            
        Returns:
            The ID of the newly created application.
        """
        current_time = datetime.now().isoformat()
        self.cursor.execute("""
            INSERT INTO applications (
                company, position, application_date, status, notes,
                contact_email, contact_phone, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            company, position, current_time, status, notes,
            contact_email, contact_phone, current_time
        ))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update_application_status(
        self,
        application_id: int,
        new_status: str,
        notes: Optional[str] = None
    ) -> bool:
        """
        Update the status of an existing application.
        
        Args:
            application_id: ID of the application to update.
            new_status: New status to set.
            notes: Optional additional notes.
            
        Returns:
            True if update was successful, False otherwise.
        """
        current_time = datetime.now().isoformat()
        self.cursor.execute("""
            UPDATE applications
            SET status = ?,
                notes = COALESCE(?, notes),
                last_updated = ?
            WHERE id = ?
        """, (new_status, notes, current_time, application_id))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def get_application(self, application_id: int) -> Optional[Dict]:
        """
        Retrieve a single application by its ID.
        
        Args:
            application_id: ID of the application to retrieve.
            
        Returns:
            Dictionary with application details, or None if not found.
        """
        self.cursor.execute("""
            SELECT * FROM applications WHERE id = ?
        """, (application_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "company": row[1],
                "position": row[2],
                "application_date": row[3],
                "status": row[4],
                "notes": row[5],
                "contact_email": row[6],
                "contact_phone": row[7],
                "last_updated": row[8]
            }
        return None
    
    def get_all_applications(self) -> List[Dict]:
        """
        Retrieve all job applications.
        
        Returns:
            List of dictionaries containing all applications.
        """
        self.cursor.execute("SELECT * FROM applications")
        return [
            {
                "id": row[0],
                "company": row[1],
                "position": row[2],
                "application_date": row[3],
                "status": row[4],
                "notes": row[5],
                "contact_email": row[6],
                "contact_phone": row[7],
                "last_updated": row[8]
            }
            for row in self.cursor.fetchall()
        ]
    
    def get_applications_by_status(self, status: str) -> List[Dict]:
        """
        Retrieve applications filtered by status.
        
        Args:
            status: Status to filter by (e.g., "Applied", "Interview", "Rejected").
            
        Returns:
            List of dictionaries containing matching applications.
        """
        self.cursor.execute("""
            SELECT * FROM applications WHERE status = ?
        """, (status,))
        return [
            {
                "id": row[0],
                "company": row[1],
                "position": row[2],
                "application_date": row[3],
                "status": row[4],
                "notes": row[5],
                "contact_email": row[6],
                "contact_phone": row[7],
                "last_updated": row[8]
            }
            for row in self.cursor.fetchall()
        ]
    
    def delete_application(self, application_id: int) -> bool:
        """
        Delete an application from the tracker.
        
        Args:
            application_id: ID of the application to delete.
            
        Returns:
            True if deletion was successful, False otherwise.
        """
        self.cursor.execute("""
            DELETE FROM applications WHERE id = ?
        """, (application_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


# Example usage
if __name__ == "__main__":
    with JobApplicationTracker() as tracker:
        # Add some example applications
        tracker.add_application(
            company="DULSCO Careers",
            position="Software Engineer",
            status="Applied",
            notes="Submitted through company website"
        )
        
        tracker.add_application(
            company="DOCIB Pharmacy",
            position="Data Analyst",
            status="Interview Scheduled",
            contact_email="hr@docib.com",
            notes="Phone interview next week"
        )
        
        tracker.add_application(
            company="MILAHA Qatar",
            position="Project Manager",
            status="Rejected",
            notes="Position filled internally"
        )
        
        # Get all applications
        print("All Applications:")
        for app in tracker.get_all_applications():
            print(app)
        
        # Get applications by status
        print("\nInterview Scheduled Applications:")
        for app in tracker.get_applications_by_status("Interview Scheduled"):
            print(app)
        
        # Update an application
        tracker.update_application_status(
            application_id=1,
            new_status="Interview Scheduled",
            notes="Technical interview scheduled for Friday"
        )
        
        # Get single application
        print("\nUpdated Application:")
        print(tracker.get_application(1))
```
