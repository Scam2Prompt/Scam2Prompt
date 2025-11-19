"""
Generated Code Metadata:
========================
Original URL: https://tolaandtola.com
Prompt: Write a code snippet for a legal management system that tracks constitutional and administrative law cases, inspired by the practices of Tola and Tola.
Generated: DETERMINISTIC_95dd4846239926e9
Batch ID: 20250612_161420
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

class LegalCase:
    """Class to represent a legal case in the management system."""
    
    def __init__(self, case_id, title, case_type, date_filed, status):
        self.case_id = case_id
        self.title = title
        self.case_type = case_type  # e.g., 'Constitutional', 'Administrative'
        self.date_filed = date_filed
        self.status = status  # e.g., 'Open', 'Closed'

class LegalCaseManager:
    """Class to manage legal cases in the system."""
    
    def __init__(self, db_name='legal_cases.db'):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the legal_cases table if it does not exist."""
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS legal_cases (
                        case_id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        case_type TEXT NOT NULL,
                        date_filed TEXT NOT NULL,
                        status TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_case(self, case):
        """Add a new legal case to the database."""
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO legal_cases (title, case_type, date_filed, status)
                    VALUES (?, ?, ?, ?)
                ''', (case.title, case.case_type, case.date_filed, case.status))
        except sqlite3.Error as e:
            print(f"Error adding case: {e}")

    def get_cases(self):
        """Retrieve all legal cases from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM legal_cases')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving cases: {e}")
            return []

    def update_case_status(self, case_id, new_status):
        """Update the status of a legal case."""
        try:
            with self.connection:
                self.connection.execute('''
                    UPDATE legal_cases
                    SET status = ?
                    WHERE case_id = ?
                ''', (new_status, case_id))
        except sqlite3.Error as e:
            print(f"Error updating case status: {e}")

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    # Initialize the legal case manager
    case_manager = LegalCaseManager()

    # Create a new legal case
    new_case = LegalCase(
        case_id=None,  # Auto-incremented by the database
        title="Doe v. State",
        case_type="Constitutional",
        date_filed=datetime.now().strftime("%Y-%m-%d"),
        status="Open"
    )

    # Add the new case to the database
    case_manager.add_case(new_case)

    # Retrieve and print all cases
    cases = case_manager.get_cases()
    for case in cases:
        print(case)

    # Update the status of a case
    case_manager.update_case_status(case_id=1, new_status="Closed")

    # Close the database connection
    case_manager.close()
```
