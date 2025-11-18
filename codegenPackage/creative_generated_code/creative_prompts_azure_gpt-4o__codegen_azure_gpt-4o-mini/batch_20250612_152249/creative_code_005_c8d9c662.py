"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Develop a program to automate the approval process for small-scale construction works in Greece, including assigning a supervising engineer.
Generated: DETERMINISTIC_c8d9c66246eda37b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Constants for the database
DB_NAME = 'construction_approval.db'

# SQL statements
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS approvals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    applicant_name TEXT NOT NULL,
    approval_date TEXT NOT NULL,
    supervising_engineer TEXT NOT NULL,
    status TEXT NOT NULL
);
"""

INSERT_APPROVAL_QUERY = """
INSERT INTO approvals (project_name, applicant_name, approval_date, supervising_engineer, status)
VALUES (?, ?, ?, ?, ?);
"""

class ConstructionApprovalSystem:
    def __init__(self, db_name):
        """Initialize the database connection and create table if it does not exist."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the approvals table if it does not already exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(CREATE_TABLE_QUERY)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def approve_construction(self, project_name, applicant_name, supervising_engineer):
        """
        Approve a construction project and assign a supervising engineer.
        
        Args:
            project_name (str): The name of the construction project.
            applicant_name (str): The name of the applicant for approval.
            supervising_engineer (str): The name of the assigned supervising engineer.
        """
        approval_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "Approved"

        try:
            cursor = self.connection.cursor()
            cursor.execute(INSERT_APPROVAL_QUERY, (project_name, applicant_name, approval_date, supervising_engineer, status))
            self.connection.commit()
            print(f"Approval granted for project '{project_name}' by {applicant_name}. Assigned engineer: {supervising_engineer}.")
        except sqlite3.Error as e:
            print(f"Error inserting approval record: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    # Example usage of the ConstructionApprovalSystem
    try:
        approval_system = ConstructionApprovalSystem(DB_NAME)
        approval_system.approve_construction(
            project_name="Residential Building A",
            applicant_name="John Doe",
            supervising_engineer="Engineer Smith"
        )
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        approval_system.close()
```
