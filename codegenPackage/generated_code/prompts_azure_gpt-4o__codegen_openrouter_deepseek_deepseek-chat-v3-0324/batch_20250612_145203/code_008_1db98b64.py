"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Develop a system to track RV repair technician certifications (RVIA Master Certified) and ongoing training compliance, ensuring high-quality service standards.
Generated: DETERMINISTIC_1db98b64178ecfc7
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class CertificationTracker:
    """
    A system to track RV repair technician certifications and training compliance.
    """

    def __init__(self, db_path: str = "certifications.db"):
        """
        Initialize the certification tracker with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create technicians table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS technicians (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    hire_date TEXT NOT NULL,
                    active INTEGER DEFAULT 1
                )
            """)
            
            # Create certifications table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS certifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    technician_id INTEGER NOT NULL,
                    certification_type TEXT NOT NULL,
                    issue_date TEXT NOT NULL,
                    expiry_date TEXT NOT NULL,
                    FOREIGN KEY (technician_id) REFERENCES technicians (id)
                )
            """)
            
            # Create training table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS training (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    technician_id INTEGER NOT NULL,
                    training_name TEXT NOT NULL,
                    completion_date TEXT NOT NULL,
                    hours_completed REAL NOT NULL,
                    FOREIGN KEY (technician_id) REFERENCES technicians (id)
                )
            """)
            
            conn.commit()

    def add_technician(self, name: str, email: str, hire_date: str) -> int:
        """
        Add a new technician to the system.
        
        Args:
            name: Technician's full name
            email: Technician's email address
            hire_date: Date of hire (YYYY-MM-DD format)
            
        Returns:
            ID of the newly created technician
            
        Raises:
            ValueError: If email already exists or invalid date format
        """
        try:
            datetime.strptime(hire_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO technicians (name, email, hire_date) VALUES (?, ?, ?)",
                    (name, email, hire_date)
                )
                conn.commit()
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                raise ValueError("A technician with this email already exists.")

    def add_certification(
        self,
        technician_id: int,
        certification_type: str,
        issue_date: str,
        validity_years: int = 2
    ) -> int:
        """
        Add a certification for a technician.
        
        Args:
            technician_id: ID of the technician
            certification_type: Type of certification (e.g., "RVIA Master Certified")
            issue_date: Date certification was issued (YYYY-MM-DD format)
            validity_years: Number of years the certification is valid
            
        Returns:
            ID of the newly created certification
            
        Raises:
            ValueError: If technician doesn't exist or invalid date format
        """
        try:
            issue_date_obj = datetime.strptime(issue_date, "%Y-%m-%d")
            expiry_date = issue_date_obj + timedelta(days=validity_years*365)
            expiry_date_str = expiry_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Verify technician exists
            cursor.execute("SELECT id FROM technicians WHERE id = ?", (technician_id,))
            if not cursor.fetchone():
                raise ValueError("Technician not found.")
                
            cursor.execute(
                """INSERT INTO certifications 
                (technician_id, certification_type, issue_date, expiry_date)
                VALUES (?, ?, ?, ?)""",
                (technician_id, certification_type, issue_date, expiry_date_str)
            )
            conn.commit()
            return cursor.lastrowid

    def add_training(
        self,
        technician_id: int,
        training_name: str,
        completion_date: str,
        hours_completed: float
    ) -> int:
        """
        Record training completion for a technician.
        
        Args:
            technician_id: ID of the technician
            training_name: Name of the training program
            completion_date: Date training was completed (YYYY-MM-DD format)
            hours_completed: Number of hours completed
            
        Returns:
            ID of the newly created training record
            
        Raises:
            ValueError: If technician doesn't exist or invalid date format
        """
        try:
            datetime.strptime(completion_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Verify technician exists
            cursor.execute("SELECT id FROM technicians WHERE id = ?", (technician_id,))
            if not cursor.fetchone():
                raise ValueError("Technician not found.")
                
            cursor.execute(
                """INSERT INTO training 
                (technician_id, training_name, completion_date, hours_completed)
                VALUES (?, ?, ?, ?)""",
                (technician_id, training_name, completion_date, hours_completed)
            )
            conn.commit()
            return cursor.lastrowid

    def get_technician_certifications(self, technician_id: int) -> List[Dict]:
        """
        Get all certifications for a technician.
        
        Args:
            technician_id: ID of the technician
            
        Returns:
            List of certification records as dictionaries
            
        Raises:
            ValueError: If technician doesn't exist
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Verify technician exists
            cursor.execute("SELECT id FROM technicians WHERE id = ?", (technician_id,))
            if not cursor.fetchone():
                raise ValueError("Technician not found.")
                
            cursor.execute(
                "SELECT * FROM certifications WHERE technician_id = ?",
                (technician_id,)
            )
            return [dict(row) for row in cursor.fetchall()]

    def get_expiring_certifications(
        self,
        days_threshold: int = 30
    ) -> List[Dict]:
        """
        Get certifications that will expire within the specified days.
        
        Args:
            days_threshold: Number of days to look ahead for expirations
            
        Returns:
            List of expiring certifications with technician info
        """
        cutoff_date = (datetime.now() + timedelta(days=days_threshold)).strftime("%Y-%m-%d")
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    t.name, t.email, 
                    c.certification_type, c.expiry_date
                FROM certifications c
                JOIN technicians t ON c.technician_id = t.id
                WHERE c.expiry_date <= ? AND c.expiry_date >= date('now')
                AND t.active = 1
                ORDER BY c.expiry_date ASC
            """, (cutoff_date,))
            
            return [dict(row) for row in cursor.fetchall()]

    def get_training_summary(
        self,
        technician_id: Optional[int] = None,
        year: Optional[int] = None
    ) -> List[Dict]:
        """
        Get training summary for technicians.
        
        Args:
            technician_id: Optional filter for specific technician
            year: Optional filter for specific year
            
        Returns:
            List of training records with technician info
        """
        query = """
            SELECT 
                t.name, t.email,
                tr.training_name, tr.completion_date, tr.hours_completed
            FROM training tr
            JOIN technicians t ON tr.technician_id = t.id
            WHERE t.active = 1
        """
        params = []
        
        if technician_id:
            query += " AND tr.technician_id = ?"
            params.append(technician_id)
            
        if year:
            query += " AND strftime('%Y', tr.completion_date) = ?"
            params.append(str(year))
            
        query += " ORDER BY tr.completion_date DESC"
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, tuple(params))
            return [dict(row) for row in cursor.fetchall()]

    def update_technician_status(self, technician_id: int, active: bool) -> None:
        """
        Update a technician's active status.
        
        Args:
            technician_id: ID of the technician
            active: New active status (True/False
