"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.haim-lawyer.co.il
Prompt: Generate a code snippet for a legal document management system that can handle civil, commercial, real estate, and labor law cases, similar to the services offered by Haim Shukrani's law firm.
Generated: DETERMINISTIC_bbfd30bc37cb6660
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
from datetime import datetime

class LegalDocumentManagementSystem:
    """
    A system for managing legal documents related to civil, commercial,
    real estate, and labor law cases.
    """

    def __init__(self, db_name="legal_documents.db"):
        """
        Initialize the LegalDocumentManagementSystem instance with a database connection.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self._setup_database()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def _setup_database(self):
        """
        Create the necessary tables if they don't exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_number TEXT NOT NULL,
                    case_type TEXT NOT NULL CHECK (case_type IN ('Civil', 'Commercial', 'Real Estate', 'Labor')),
                    client_name TEXT NOT NULL,
                    description TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
            raise
    
    def add_case(self, case_number, case_type, client_name, description):
        """
        Add a new case to the system.

        Args:
            case_number (str): Unique identifier for the case.
            case_type (str): Type of case (Civil, Commercial, Real Estate, or Labor).
            client_name (str): Name of the client.
            description (str): Description of the case.

        Returns:
            bool: True if the case was added successfully, False otherwise.
        """
        try:
            if case_type not in ['Civil', 'Commercial', 'Real Estate', 'Labor']:
                raise ValueError("Invalid case type. Must be one of: Civil, Commercial, Real Estate, Labor.")

            self.cursor.execute("""
                INSERT INTO cases (case_number, case_type, client_name, description, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (case_number, case_type, client_name, description, datetime.now()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error while adding case: {e}")
            return False
        except ValueError as ve:
            print(f"Value error: {ve}")
            return False

    def get_cases(self, case_type=None):
        """
        Retrieve cases from the system, optionally filtered by case type.

        Args:
            case_type (str, optional): Filter by case type. Defaults to None.

        Returns:
            list: A list of cases matching the criteria.
        """
        try:
            if case_type and case_type not in ['Civil', 'Commercial', 'Real Estate', 'Labor']:
                raise ValueError("Invalid case type. Must be one of: Civil, Commercial, Real Estate, Labor.")

            query = "SELECT * FROM cases"
            params = ()
            if case_type:
                query += " WHERE case_type = ?"
                params = (case_type,)
            
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error while retrieving cases: {e}")
            return []
        except ValueError as ve:
            print(f"Value error: {ve}")
            return []

    def delete_case(self, case_id):
        """
        Delete a case by its ID.

        Args:
            case_id (int): ID of the case to delete.

        Returns:
            bool: True if the case was deleted successfully, False otherwise.
        """
        try:
            self.cursor.execute("DELETE FROM cases WHERE id = ?", (case_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error while deleting case: {e}")
            return False

    def close(self):
        """
        Close the database connection.
        """
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Error while closing the database: {e}")

# Example usage:
if __name__ == "__main__":
    system = LegalDocumentManagementSystem()
    system.add_case("12345", "Civil", "John Doe", "Case description for John Doe.")
    cases = system.get_cases("Civil")
    print("Retrieved Civil cases:", cases)
    system.delete_case(1)  # Assuming the first case ID is 1
    system.close()
```
