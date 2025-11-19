"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Write a code snippet for creating a simple database for managing human resources, based on the Recursos Humanos program at ISIV."
Generated: DETERMINISTIC_e8e3cbc3dcc804a3
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class HRDatabase:
    """
    A simple database for managing human resources based on the Recursos Humanos program at ISIV.
    This class handles employee records with basic CRUD operations.
    """

    def __init__(self, db_name: str = "hr_database.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create the necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL,
                hire_date TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        self.conn.commit()

    def add_employee(self, name: str, position: str, department: str, salary: float, hire_date: str, email: str) -> int:
        """
        Add a new employee to the database.
        
        Args:
            name: Full name of the employee.
            position: Job position.
            department: Department where the employee works.
            salary: Monthly salary.
            hire_date: Date when the employee was hired (YYYY-MM-DD).
            email: Unique email address.
            
        Returns:
            The ID of the newly inserted employee.
            
        Raises:
            sqlite3.IntegrityError: If the email is not unique.
        """
        try:
            self.cursor.execute("""
                INSERT INTO employees (name, position, department, salary, hire_date, email)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, position, department, salary, hire_date, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise sqlite3.IntegrityError(f"Email must be unique: {email}") from e

    def get_employee(self, employee_id: int) -> Optional[Dict]:
        """
        Retrieve an employee by their ID.
        
        Args:
            employee_id: The ID of the employee to retrieve.
            
        Returns:
            A dictionary with employee data or None if not found.
        """
        self.cursor.execute("""
            SELECT id, name, position, department, salary, hire_date, email
            FROM employees
            WHERE id = ?
        """, (employee_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "position": row[2],
                "department": row[3],
                "salary": row[4],
                "hire_date": row[5],
                "email": row[6]
            }
        return None

    def get_all_employees(self) -> List[Dict]:
        """
        Retrieve all employees from the database.
        
        Returns:
            A list of dictionaries with employee data.
        """
        self.cursor.execute("""
            SELECT id, name, position, department, salary, hire_date, email
            FROM employees
        """)
        return [
            {
                "id": row[0],
                "name": row[1],
                "position": row[2],
                "department": row[3],
                "salary": row[4],
                "hire_date": row[5],
                "email": row[6]
            }
            for row in self.cursor.fetchall()
        ]

    def update_employee(self, employee_id: int, **kwargs) -> bool:
        """
        Update employee data.
        
        Args:
            employee_id: The ID of the employee to update.
            **kwargs: Fields to update (name, position, department, salary, hire_date, email).
            
        Returns:
            True if the update was successful, False otherwise.
            
        Raises:
            sqlite3.IntegrityError: If the email is not unique.
        """
        if not kwargs:
            return False

        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(employee_id)

        try:
            self.cursor.execute(f"""
                UPDATE employees
                SET {', '.join(fields)}
                WHERE id = ?
            """, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            raise sqlite3.IntegrityError(f"Email must be unique: {kwargs.get('email')}") from e

    def delete_employee(self, employee_id: int) -> bool:
        """
        Delete an employee from the database.
        
        Args:
            employee_id: The ID of the employee to delete.
            
        Returns:
            True if the deletion was successful, False otherwise.
        """
        self.cursor.execute("""
            DELETE FROM employees
            WHERE id = ?
        """, (employee_id,))
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
```
