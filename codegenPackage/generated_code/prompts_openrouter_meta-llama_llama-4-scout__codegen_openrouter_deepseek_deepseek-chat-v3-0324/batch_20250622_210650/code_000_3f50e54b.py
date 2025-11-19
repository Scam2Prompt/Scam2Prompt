"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Generate a Python code snippet for managing polygraph test results, including patient information, test dates, and results, using a SQLite database."
Generated: DETERMINISTIC_3f50e54ba6f36d16
Batch ID: 20250622_210650
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
from typing import Optional, List, Dict, Tuple

class PolygraphTestManager:
    """
    A class to manage polygraph test results using SQLite database.
    Handles patient information, test dates, and results.
    """

    def __init__(self, db_name: str = "polygraph_tests.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                gender TEXT,
                contact_number TEXT,
                email TEXT,
                address TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tests (
                test_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                test_date TEXT NOT NULL,
                examiner_name TEXT NOT NULL,
                test_type TEXT NOT NULL,
                result TEXT NOT NULL,
                notes TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (patient_id) REFERENCES patients (patient_id)
            )
        """)
        self.conn.commit()

    def add_patient(
        self,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        gender: Optional[str] = None,
        contact_number: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None
    ) -> int:
        """
        Add a new patient to the database.
        
        Args:
            first_name: Patient's first name
            last_name: Patient's last name
            date_of_birth: Patient's date of birth (YYYY-MM-DD)
            gender: Patient's gender
            contact_number: Patient's contact number
            email: Patient's email address
            address: Patient's physical address
            
        Returns:
            The ID of the newly created patient
            
        Raises:
            ValueError: If required fields are missing or date format is invalid
        """
        if not first_name or not last_name or not date_of_birth:
            raise ValueError("First name, last name, and date of birth are required")
        
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date of birth must be in YYYY-MM-DD format")

        self.cursor.execute("""
            INSERT INTO patients (
                first_name, last_name, date_of_birth, gender,
                contact_number, email, address
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, date_of_birth, gender,
              contact_number, email, address))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_test(
        self,
        patient_id: int,
        test_date: str,
        examiner_name: str,
        test_type: str,
        result: str,
        notes: Optional[str] = None
    ) -> int:
        """
        Add a new test result for a patient.
        
        Args:
            patient_id: ID of the patient
            test_date: Date of the test (YYYY-MM-DD)
            examiner_name: Name of the examiner
            test_type: Type of polygraph test
            result: Test result (e.g., "Deceptive", "Non-Deceptive", "Inconclusive")
            notes: Additional notes about the test
            
        Returns:
            The ID of the newly created test
            
        Raises:
            ValueError: If required fields are missing, date format is invalid,
                       or patient doesn't exist
        """
        if not patient_id or not test_date or not examiner_name or not test_type or not result:
            raise ValueError("All fields except notes are required")

        try:
            datetime.strptime(test_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Test date must be in YYYY-MM-DD format")

        # Verify patient exists
        self.cursor.execute("SELECT 1 FROM patients WHERE patient_id = ?", (patient_id,))
        if not self.cursor.fetchone():
            raise ValueError("Patient does not exist")

        self.cursor.execute("""
            INSERT INTO tests (
                patient_id, test_date, examiner_name, test_type, result, notes
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (patient_id, test_date, examiner_name, test_type, result, notes))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_patient(self, patient_id: int) -> Optional[Dict]:
        """
        Retrieve patient information by ID.
        
        Args:
            patient_id: ID of the patient to retrieve
            
        Returns:
            Dictionary with patient information or None if not found
        """
        self.cursor.execute("""
            SELECT * FROM patients WHERE patient_id = ?
        """, (patient_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None

    def get_patient_tests(self, patient_id: int) -> List[Dict]:
        """
        Retrieve all tests for a specific patient.
        
        Args:
            patient_id: ID of the patient
            
        Returns:
            List of dictionaries with test information
        """
        self.cursor.execute("""
            SELECT * FROM tests WHERE patient_id = ? ORDER BY test_date DESC
        """, (patient_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def search_patients(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        date_of_birth: Optional[str] = None
    ) -> List[Dict]:
        """
        Search for patients by name and/or date of birth.
        
        Args:
            first_name: First name to search (partial match)
            last_name: Last name to search (partial match)
            date_of_birth: Exact date of birth to search
            
        Returns:
            List of dictionaries with matching patient information
        """
        query = "SELECT * FROM patients WHERE 1=1"
        params = []

        if first_name:
            query += " AND first_name LIKE ?"
            params.append(f"%{first_name}%")
        if last_name:
            query += " AND last_name LIKE ?"
            params.append(f"%{last_name}%")
        if date_of_birth:
            query += " AND date_of_birth = ?"
            params.append(date_of_birth)

        self.cursor.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def update_patient(
        self,
        patient_id: int,
        **kwargs
    ) -> bool:
        """
        Update patient information.
        
        Args:
            patient_id: ID of the patient to update
            kwargs: Fields to update (e.g., first_name="John")
            
        Returns:
            True if update was successful, False if patient not found
            
        Raises:
            ValueError: If trying to update invalid fields
        """
        valid_fields = {
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'contact_number', 'email', 'address'
        }

        invalid_fields = set(kwargs.keys()) - valid_fields
        if invalid_fields:
            raise ValueError(f"Invalid fields to update: {invalid_fields}")

        if not kwargs:
            return False

        set_clause = ", ".join([f"{k} = ?" for k in kwargs.keys()])
        query = f"UPDATE patients SET {set_clause} WHERE patient_id = ?"
        params = list(kwargs.values()) + [patient_id]

        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_patient(self, patient_id: int) -> bool:
        """
        Delete a patient and all their tests.
        
        Args:
            patient_id: ID of the patient to delete
            
        Returns:
            True if deletion was successful, False if patient not found
        """
        self.cursor.execute("DELETE FROM tests WHERE patient_id = ?", (patient_id,))
        self.cursor.execute("DELETE FROM patients WHERE patient_id = ?", (patient_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get_all_tests(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        result: Optional[str] = None
    ) -> List[Dict]:
        """
        Retrieve all tests with optional
