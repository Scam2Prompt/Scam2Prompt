"""
Generated Code Metadata:
========================
Original URL: https://fujimitsudynamic.com
Prompt: Develop a maintenance tracking system for ball screws and spindles, ensuring accuracy within 2 microns, as per Fujimitsu Dynamic's standards.
Generated: DETERMINISTIC_0058f401889a04c5
Batch ID: 20250612_154239
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
from typing import Optional, Tuple, List, Dict

# Database schema and setup
DB_NAME = "maintenance_tracking.db"

def initialize_database() -> None:
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create ball screws table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ball_screws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serial_number TEXT UNIQUE NOT NULL,
            manufacturer TEXT NOT NULL,
            installation_date TEXT NOT NULL,
            last_maintenance_date TEXT,
            accuracy REAL CHECK(accuracy <= 2.0),
            status TEXT CHECK(status IN ('operational', 'maintenance', 'retired')),
            notes TEXT
        )
    """)
    
    # Create spindles table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spindles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serial_number TEXT UNIQUE NOT NULL,
            manufacturer TEXT NOT NULL,
            installation_date TEXT NOT NULL,
            last_maintenance_date TEXT,
            accuracy REAL CHECK(accuracy <= 2.0),
            status TEXT CHECK(status IN ('operational', 'maintenance', 'retired')),
            notes TEXT
        )
    """)
    
    # Create maintenance history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenance_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            component_type TEXT CHECK(component_type IN ('ball_screw', 'spindle')),
            component_id INTEGER NOT NULL,
            maintenance_date TEXT NOT NULL,
            performed_by TEXT NOT NULL,
            accuracy_before REAL,
            accuracy_after REAL CHECK(accuracy_after <= 2.0),
            notes TEXT,
            FOREIGN KEY (component_id) REFERENCES ball_screws(id) OR spindles(id)
        )
    """)
    
    conn.commit()
    conn.close()

class MaintenanceTracker:
    """Main class for tracking ball screw and spindle maintenance."""
    
    def __init__(self):
        initialize_database()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        return sqlite3.connect(DB_NAME)
    
    def add_component(self, component_type: str, serial_number: str, manufacturer: str, 
                     installation_date: str, accuracy: float, notes: Optional[str] = None) -> bool:
        """
        Add a new component to the tracking system.
        
        Args:
            component_type: Either 'ball_screw' or 'spindle'
            serial_number: Unique serial number
            manufacturer: Manufacturer name
            installation_date: Date of installation (YYYY-MM-DD)
            accuracy: Initial accuracy in microns (must be <= 2.0)
            notes: Optional notes about the component
            
        Returns:
            bool: True if successful, False otherwise
        """
        if accuracy > 2.0:
            raise ValueError("Accuracy must be 2.0 microns or better")
            
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            table = "ball_screws" if component_type == "ball_screw" else "spindles"
            
            cursor.execute(
                f"""
                INSERT INTO {table} (
                    serial_number, manufacturer, installation_date, 
                    accuracy, status, notes
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (serial_number, manufacturer, installation_date, 
                 accuracy, "operational", notes)
            )
            
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()
    
    def record_maintenance(self, component_type: str, component_id: int, 
                         performed_by: str, accuracy_after: float, 
                         notes: Optional[str] = None) -> bool:
        """
        Record a maintenance event for a component.
        
        Args:
            component_type: Either 'ball_screw' or 'spindle'
            component_id: ID of the component
            performed_by: Name of technician performing maintenance
            accuracy_after: Measured accuracy after maintenance (must be <= 2.0)
            notes: Optional notes about the maintenance
            
        Returns:
            bool: True if successful, False otherwise
        """
        if accuracy_after > 2.0:
            raise ValueError("Accuracy must be 2.0 microns or better")
            
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Get current accuracy before maintenance
            table = "ball_screws" if component_type == "ball_screw" else "spindles"
            cursor.execute(f"SELECT accuracy FROM {table} WHERE id = ?", (component_id,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError("Component not found")
                
            accuracy_before = result[0]
            
            # Record maintenance in history
            cursor.execute(
                """
                INSERT INTO maintenance_history (
                    component_type, component_id, maintenance_date,
                    performed_by, accuracy_before, accuracy_after, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (component_type, component_id, datetime.now().isoformat(),
                 performed_by, accuracy_before, accuracy_after, notes)
            )
            
            # Update component record
            cursor.execute(
                f"""
                UPDATE {table} 
                SET last_maintenance_date = ?, accuracy = ?, status = 'operational'
                WHERE id = ?
                """,
                (datetime.now().isoformat(), accuracy_after, component_id)
            )
            
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()
    
    def get_component_status(self, component_type: str, component_id: int) -> Optional[Dict]:
        """
        Get current status of a component.
        
        Args:
            component_type: Either 'ball_screw' or 'spindle'
            component_id: ID of the component
            
        Returns:
            dict: Component information if found, None otherwise
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            table = "ball_screws" if component_type == "ball_screw" else "spindles"
            
            cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (component_id,))
            result = cursor.fetchone()
            
            if not result:
                return None
                
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, result))
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()
    
    def get_maintenance_history(self, component_type: str, component_id: int) -> List[Dict]:
        """
        Get maintenance history for a component.
        
        Args:
            component_type: Either 'ball_screw' or 'spindle'
            component_id: ID of the component
            
        Returns:
            list: List of maintenance records
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute(
                """
                SELECT * FROM maintenance_history 
                WHERE component_type = ? AND component_id = ?
                ORDER BY maintenance_date DESC
                """,
                (component_type, component_id)
            )
            
            results = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            
            return [dict(zip(columns, row)) for row in results]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            conn.close()
    
    def set_component_status(self, component_type: str, component_id: int, 
                           status: str, notes: Optional[str] = None) -> bool:
        """
        Set the status of a component.
        
        Args:
            component_type: Either 'ball_screw' or 'spindle'
            component_id: ID of the component
            status: New status ('operational', 'maintenance', or 'retired')
            notes: Optional notes about the status change
            
        Returns:
            bool: True if successful, False otherwise
        """
        valid_statuses = ['operational', 'maintenance', 'retired']
        if status not in valid_statuses:
            raise ValueError(f"Status must be one of {valid_statuses}")
            
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            table = "ball_screws" if component_type == "ball_screw" else "spindles"
            
            cursor.execute(
                f"""
                UPDATE {table} 
                SET status = ?, notes = ?
                WHERE id = ?
                """,
                (status, notes, component_id)
            )
            
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()
    
    def get_components_needing_maintenance(self, component_type: str, 
                                         days_threshold: int = 180) -> List[Dict]:
        """
        Get components that need maintenance based on days since last maintenance.
