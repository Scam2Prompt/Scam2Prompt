"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write a Python script to automate the tracking of legal cases, inspired by the client-focused approach of the Complexo de Advocacia Dr. Adriano Geoffrey.
Generated: DETERMINISTIC_44eff5679ae3feae
Batch ID: 20250612_162051
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

# Define a class to represent a legal case
class LegalCase:
    def __init__(self, case_id, client_name, case_type, status, created_at=None):
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.status = status
        self.created_at = created_at or datetime.now()

# Database handler class for managing legal cases
class LegalCaseDatabase:
    def __init__(self, db_name='legal_cases.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the legal_cases table if it doesn't exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS legal_cases (
                    case_id INTEGER PRIMARY KEY,
                    client_name TEXT NOT NULL,
                    case_type TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            ''')

    def add_case(self, legal_case):
        """Add a new legal case to the database."""
        with self.connection:
            self.connection.execute('''
                INSERT INTO legal_cases (client_name, case_type, status, created_at)
                VALUES (?, ?, ?, ?)
            ''', (legal_case.client_name, legal_case.case_type, legal_case.status, legal_case.created_at.isoformat()))

    def update_case_status(self, case_id, new_status):
        """Update the status of an existing legal case."""
        with self.connection:
            cursor = self.connection.execute('''
                UPDATE legal_cases
                SET status = ?
                WHERE case_id = ?
            ''', (new_status, case_id))
            if cursor.rowcount == 0:
                raise ValueError(f"No case found with ID: {case_id}")

    def get_all_cases(self):
        """Retrieve all legal cases from the database."""
        cursor = self.connection.execute('SELECT * FROM legal_cases')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Main function to demonstrate the functionality
def main():
    db = LegalCaseDatabase()

    # Example: Adding a new legal case
    try:
        new_case = LegalCase(case_id=None, client_name='John Doe', case_type='Civil', status='Open')
        db.add_case(new_case)
        print("Case added successfully.")
    except Exception as e:
        print(f"Error adding case: {e}")

    # Example: Updating a case status
    try:
        db.update_case_status(case_id=1, new_status='Closed')
        print("Case status updated successfully.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Error updating case status: {e}")

    # Example: Retrieving all cases
    try:
        cases = db.get_all_cases()
        print("Current legal cases:")
        for case in cases:
            print(case)
    except Exception as e:
        print(f"Error retrieving cases: {e}")

    # Close the database connection
    db.close()

if __name__ == '__main__':
    main()
```
