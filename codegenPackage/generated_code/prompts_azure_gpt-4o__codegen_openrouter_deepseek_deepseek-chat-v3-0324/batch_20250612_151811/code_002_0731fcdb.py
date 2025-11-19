"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Generate code for a driver training management system that incorporates features like certification tracking, as highlighted by Kalgate Technology's driver training services.
Generated: DETERMINISTIC_0731fcdb98a83420
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import sqlite3
from typing import List, Dict, Optional, Tuple

class DriverTrainingManagementSystem:
    """
    A driver training management system that handles driver certifications,
    training records, and compliance tracking.
    """
    
    def __init__(self, db_path: str = "driver_training.db"):
        """
        Initialize the system with a SQLite database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary database tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        # Drivers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                license_number TEXT UNIQUE NOT NULL,
                date_of_birth DATE NOT NULL,
                contact_number TEXT NOT NULL,
                email TEXT,
                address TEXT,
                date_joined DATE NOT NULL
            )
        """)
        
        # Certification types table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certification_types (
                cert_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                validity_period_months INTEGER NOT NULL,
                required_for_operation BOOLEAN DEFAULT FALSE
            )
        """)
        
        # Driver certifications table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS driver_certifications (
                cert_id INTEGER PRIMARY KEY AUTOINCREMENT,
                driver_id INTEGER NOT NULL,
                cert_type_id INTEGER NOT NULL,
                issue_date DATE NOT NULL,
                expiry_date DATE NOT NULL,
                issuing_authority TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('Active', 'Expired', 'Revoked')),
                FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
                FOREIGN KEY (cert_type_id) REFERENCES certification_types(cert_type_id)
            )
        """)
        
        # Training sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS training_sessions (
                session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                trainer_id INTEGER,
                session_date DATE NOT NULL,
                duration_hours REAL NOT NULL,
                location TEXT NOT NULL,
                FOREIGN KEY (trainer_id) REFERENCES drivers(driver_id)
            )
        """)
        
        # Driver training records
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS driver_training_records (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                driver_id INTEGER NOT NULL,
                session_id INTEGER NOT NULL,
                attendance_status TEXT NOT NULL CHECK(attendance_status IN ('Present', 'Absent', 'Excused')),
                score REAL,
                notes TEXT,
                FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
                FOREIGN KEY (session_id) REFERENCES training_sessions(session_id)
            )
        """)
        
        self.conn.commit()
    
    def add_driver(
        self,
        first_name: str,
        last_name: str,
        license_number: str,
        date_of_birth: str,
        contact_number: str,
        email: Optional[str] = None,
        address: Optional[str] = None
    ) -> int:
        """
        Add a new driver to the system.
        
        Args:
            first_name: Driver's first name
            last_name: Driver's last name
            license_number: Driver's license number
            date_of_birth: Date of birth (YYYY-MM-DD)
            contact_number: Contact phone number
            email: Optional email address
            address: Optional physical address
            
        Returns:
            The ID of the newly added driver
            
        Raises:
            ValueError: If license number already exists
            sqlite3.Error: For database errors
        """
        try:
            cursor = self.conn.cursor()
            date_joined = datetime.date.today().isoformat()
            
            cursor.execute(
                """
                INSERT INTO drivers (
                    first_name, last_name, license_number, date_of_birth,
                    contact_number, email, address, date_joined
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    first_name, last_name, license_number, date_of_birth,
                    contact_number, email, address, date_joined
                )
            )
            
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise ValueError(f"Driver with license number {license_number} already exists")
            raise
    
    def add_certification_type(
        self,
        name: str,
        validity_period_months: int,
        description: Optional[str] = None,
        required_for_operation: bool = False
    ) -> int:
        """
        Add a new certification type to the system.
        
        Args:
            name: Name of the certification
            validity_period_months: How many months the certification is valid
            description: Optional description
            required_for_operation: Whether this certification is required for operation
            
        Returns:
            The ID of the newly added certification type
            
        Raises:
            ValueError: If certification name already exists
            sqlite3.Error: For database errors
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute(
                """
                INSERT INTO certification_types (
                    name, description, validity_period_months, required_for_operation
                ) VALUES (?, ?, ?, ?)
                """,
                (name, description, validity_period_months, required_for_operation)
            )
            
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise ValueError(f"Certification type '{name}' already exists")
            raise
    
    def add_driver_certification(
        self,
        driver_id: int,
        cert_type_id: int,
        issue_date: str,
        issuing_authority: str,
        status: str = "Active"
    ) -> int:
        """
        Add a certification for a driver.
        
        Args:
            driver_id: ID of the driver
            cert_type_id: ID of the certification type
            issue_date: Date certification was issued (YYYY-MM-DD)
            issuing_authority: Organization that issued the certification
            status: Current status ('Active', 'Expired', 'Revoked')
            
        Returns:
            The ID of the newly added certification
            
        Raises:
            ValueError: For invalid inputs or if driver/cert type doesn't exist
            sqlite3.Error: For database errors
        """
        try:
            # Validate driver exists
            if not self._driver_exists(driver_id):
                raise ValueError(f"Driver with ID {driver_id} does not exist")
            
            # Validate certification type exists
            if not self._certification_type_exists(cert_type_id):
                raise ValueError(f"Certification type with ID {cert_type_id} does not exist")
            
            # Calculate expiry date
            validity_months = self._get_certification_validity(cert_type_id)
            issue_date_obj = datetime.date.fromisoformat(issue_date)
            expiry_date = self._calculate_expiry_date(issue_date_obj, validity_months)
            
            cursor = self.conn.cursor()
            
            cursor.execute(
                """
                INSERT INTO driver_certifications (
                    driver_id, cert_type_id, issue_date, expiry_date,
                    issuing_authority, status
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    driver_id, cert_type_id, issue_date, expiry_date.isoformat(),
                    issuing_authority, status
                )
            )
            
            self.conn.commit()
            return cursor.lastrowid
        except ValueError as e:
            raise ValueError(f"Invalid certification data: {str(e)}")
    
    def _driver_exists(self, driver_id: int) -> bool:
        """Check if a driver exists in the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM drivers WHERE driver_id = ?", (driver_id,))
        return cursor.fetchone() is not None
    
    def _certification_type_exists(self, cert_type_id: int) -> bool:
        """Check if a certification type exists in the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM certification_types WHERE cert_type_id = ?", (cert_type_id,))
        return cursor.fetchone() is not None
    
    def _get_certification_validity(self, cert_type_id: int) -> int:
        """Get the validity period in months for a certification type."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT validity_period_months FROM certification_types WHERE cert_type_id = ?",
            (cert_type_id,)
        )
        result = cursor.fetchone()
        if not result:
            raise ValueError(f"Certification type with ID {cert_type_id} not found")
        return result[0]
    
    def _calculate_expiry_date(self, issue_date: datetime.date, validity_months: int) -> datetime.date:
        """Calculate expiry date based on issue date and validity period."""
        year = issue_date
