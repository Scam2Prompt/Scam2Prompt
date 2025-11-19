"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Write a program to track and log preventive maintenance activities for data center equipment, including UPS systems, surge suppressors, and process chillers, following the practices of Technical Power Service, Inc.
Generated: DETERMINISTIC_1662e8096b9f2aeb
Batch ID: 20250612_153225
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
from typing import Dict, List, Optional, Tuple

class MaintenanceTracker:
    """
    A class to track and log preventive maintenance activities for data center equipment.
    """

    def __init__(self, db_path: str = "maintenance.db"):
        """
        Initialize the MaintenanceTracker with a SQLite database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """
        Initialize the database with required tables if they don't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create equipment table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS equipment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    model TEXT,
                    serial_number TEXT UNIQUE,
                    location TEXT,
                    installation_date TEXT,
                    last_maintenance_date TEXT
                )
            """)
            
            # Create maintenance_log table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS maintenance_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    equipment_id INTEGER NOT NULL,
                    maintenance_date TEXT NOT NULL,
                    technician TEXT NOT NULL,
                    description TEXT NOT NULL,
                    next_maintenance_date TEXT,
                    FOREIGN KEY (equipment_id) REFERENCES equipment (id)
                )
            """)
            
            conn.commit()

    def add_equipment(
        self,
        name: str,
        equipment_type: str,
        model: Optional[str] = None,
        serial_number: Optional[str] = None,
        location: Optional[str] = None,
        installation_date: Optional[str] = None
    ) -> int:
        """
        Add a new piece of equipment to the tracking system.
        
        Args:
            name: Name of the equipment.
            equipment_type: Type of equipment (e.g., "UPS", "Surge Suppressor", "Process Chiller").
            model: Model number of the equipment.
            serial_number: Serial number of the equipment.
            location: Location of the equipment.
            installation_date: Date of installation (YYYY-MM-DD format).
            
        Returns:
            The ID of the newly added equipment.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO equipment (
                        name, type, model, serial_number, location, installation_date
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (name, equipment_type, model, serial_number, location, installation_date))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Serial number must be unique: {e}") from e

    def log_maintenance(
        self,
        equipment_id: int,
        technician: str,
        description: str,
        maintenance_date: Optional[str] = None,
        next_maintenance_date: Optional[str] = None
    ) -> int:
        """
        Log a maintenance activity for a piece of equipment.
        
        Args:
            equipment_id: ID of the equipment being maintained.
            technician: Name of the technician performing maintenance.
            description: Description of maintenance performed.
            maintenance_date: Date of maintenance (YYYY-MM-DD format). Defaults to current date.
            next_maintenance_date: Recommended date for next maintenance (YYYY-MM-DD format).
            
        Returns:
            The ID of the maintenance log entry.
        """
        if maintenance_date is None:
            maintenance_date = datetime.now().strftime("%Y-%m-%d")
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Log the maintenance activity
                cursor.execute("""
                    INSERT INTO maintenance_log (
                        equipment_id, maintenance_date, technician, description, next_maintenance_date
                    ) VALUES (?, ?, ?, ?, ?)
                """, (equipment_id, maintenance_date, technician, description, next_maintenance_date))
                
                # Update last maintenance date in equipment table
                cursor.execute("""
                    UPDATE equipment
                    SET last_maintenance_date = ?
                    WHERE id = ?
                """, (maintenance_date, equipment_id))
                
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise ValueError(f"Error logging maintenance: {e}") from e

    def get_equipment(self, equipment_id: int) -> Dict:
        """
        Retrieve equipment details by ID.
        
        Args:
            equipment_id: ID of the equipment to retrieve.
            
        Returns:
            Dictionary containing equipment details.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM equipment WHERE id = ?", (equipment_id,))
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"No equipment found with ID {equipment_id}")
            return dict(result)

    def get_maintenance_history(self, equipment_id: int) -> List[Dict]:
        """
        Retrieve maintenance history for a piece of equipment.
        
        Args:
            equipment_id: ID of the equipment.
            
        Returns:
            List of dictionaries containing maintenance records.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM maintenance_log
                WHERE equipment_id = ?
                ORDER BY maintenance_date DESC
            """, (equipment_id,))
            return [dict(row) for row in cursor.fetchall()]

    def get_due_for_maintenance(self, days_threshold: int = 30) -> List[Dict]:
        """
        Get equipment that is due or overdue for maintenance.
        
        Args:
            days_threshold: Number of days to consider as threshold for due maintenance.
            
        Returns:
            List of equipment dictionaries with maintenance status.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Get equipment with no maintenance history
            cursor.execute("""
                SELECT e.*, NULL as last_maintenance_date
                FROM equipment e
                LEFT JOIN maintenance_log ml ON e.id = ml.equipment_id
                WHERE ml.id IS NULL
            """)
            no_history = [dict(row) for row in cursor.fetchall()]
            
            # Get equipment with overdue maintenance
            cursor.execute("""
                SELECT e.*, ml.maintenance_date as last_maintenance_date
                FROM equipment e
                JOIN (
                    SELECT equipment_id, MAX(maintenance_date) as maintenance_date
                    FROM maintenance_log
                    GROUP BY equipment_id
                ) ml ON e.id = ml.equipment_id
                WHERE date(ml.maintenance_date, '+' || ? || ' days') < date('now')
                OR (e.last_maintenance_date IS NULL AND e.installation_date IS NOT NULL 
                    AND date(e.installation_date, '+' || ? || ' days') < date('now'))
            """, (days_threshold, days_threshold))
            
            overdue = [dict(row) for row in cursor.fetchall()]
            
            return no_history + overdue

    def generate_report(self, start_date: str, end_date: str) -> List[Dict]:
        """
        Generate a report of maintenance activities within a date range.
        
        Args:
            start_date: Start date for report (YYYY-MM-DD format).
            end_date: End date for report (YYYY-MM-DD format).
            
        Returns:
            List of maintenance activities with equipment details.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    e.name as equipment_name,
                    e.type as equipment_type,
                    e.location,
                    ml.maintenance_date,
                    ml.technician,
                    ml.description,
                    ml.next_maintenance_date
                FROM maintenance_log ml
                JOIN equipment e ON ml.equipment_id = e.id
                WHERE date(ml.maintenance_date) BETWEEN date(?) AND date(?)
                ORDER BY ml.maintenance_date DESC
            """, (start_date, end_date))
            return [dict(row) for row in cursor.fetchall()]

# Example usage
if __name__ == "__main__":
    tracker = MaintenanceTracker()
    
    # Add some equipment
    ups_id = tracker.add_equipment(
        name="Main UPS",
        equipment_type="UPS",
        model="APC Symmetra PX 100kW",
        serial_number="UPS12345",
        location="Data Center A",
        installation_date="2022-01-15"
    )
    
    chiller_id = tracker.add_equipment(
        name="Primary Chiller",
        equipment_type="Process Chiller",
        model="Liebert PCW 30T",
        serial_number="CHL67890",
        location="Data Center B",
        installation_date="2022-02-20"
    )
    
    # Log some maintenance
    tracker.log_maintenance(
        equipment_id=ups_id,
        technician="John Smith",
        description
