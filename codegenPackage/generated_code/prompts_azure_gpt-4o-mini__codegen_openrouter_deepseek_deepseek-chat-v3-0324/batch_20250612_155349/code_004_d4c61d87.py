"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: Provide a code example for tracking service requests and maintenance history for York chillers in a database.
Generated: DETERMINISTIC_d4c61d870925d682
Batch ID: 20250612_155349
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
from typing import List, Dict, Optional

class ChillerDatabase:
    """Database handler for York chiller service requests and maintenance history."""
    
    def __init__(self, db_path: str = "york_chillers.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chillers (
            chiller_id TEXT PRIMARY KEY,
            model TEXT NOT NULL,
            serial_number TEXT UNIQUE NOT NULL,
            installation_date TEXT NOT NULL,
            location TEXT NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS service_requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            chiller_id TEXT NOT NULL,
            request_date TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Open', 'In Progress', 'Completed', 'Cancelled')),
            priority TEXT NOT NULL CHECK(priority IN ('Low', 'Medium', 'High', 'Critical')),
            FOREIGN KEY (chiller_id) REFERENCES chillers(chiller_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenance_history (
            maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            chiller_id TEXT NOT NULL,
            maintenance_date TEXT NOT NULL,
            maintenance_type TEXT NOT NULL,
            description TEXT NOT NULL,
            technician TEXT NOT NULL,
            parts_replaced TEXT,
            FOREIGN KEY (chiller_id) REFERENCES chillers(chiller_id)
        )
        """)
        
        self.conn.commit()
    
    def add_chiller(self, chiller_id: str, model: str, serial_number: str, 
                    installation_date: str, location: str) -> None:
        """Add a new chiller to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO chillers 
            (chiller_id, model, serial_number, installation_date, location)
            VALUES (?, ?, ?, ?, ?)
            """, (chiller_id, model, serial_number, installation_date, location))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Chiller with ID {chiller_id} or serial number {serial_number} already exists") from e
    
    def create_service_request(self, chiller_id: str, description: str, 
                              priority: str = 'Medium') -> int:
        """Create a new service request for a chiller."""
        if priority not in ('Low', 'Medium', 'High', 'Critical'):
            raise ValueError("Invalid priority level")
        
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO service_requests 
        (chiller_id, request_date, description, status, priority)
        VALUES (?, ?, ?, ?, ?)
        """, (chiller_id, datetime.now().isoformat(), description, 'Open', priority))
        self.conn.commit()
        return cursor.lastrowid
    
    def update_service_request_status(self, request_id: int, status: str) -> None:
        """Update the status of a service request."""
        if status not in ('Open', 'In Progress', 'Completed', 'Cancelled'):
            raise ValueError("Invalid status")
        
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE service_requests 
        SET status = ? 
        WHERE request_id = ?
        """, (status, request_id))
        self.conn.commit()
    
    def add_maintenance_record(self, chiller_id: str, maintenance_type: str, 
                              description: str, technician: str, 
                              parts_replaced: Optional[str] = None) -> int:
        """Add a maintenance record for a chiller."""
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO maintenance_history 
        (chiller_id, maintenance_date, maintenance_type, description, technician, parts_replaced)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (chiller_id, datetime.now().isoformat(), maintenance_type, 
              description, technician, parts_replaced))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_chiller_service_history(self, chiller_id: str) -> List[Dict]:
        """Get all service requests and maintenance records for a chiller."""
        cursor = self.conn.cursor()
        
        # Get service requests
        cursor.execute("""
        SELECT request_id, request_date, description, status, priority
        FROM service_requests
        WHERE chiller_id = ?
        ORDER BY request_date DESC
        """, (chiller_id,))
        service_requests = [dict(zip(['request_id', 'request_date', 'description', 'status', 'priority'], row)) 
                           for row in cursor.fetchall()]
        
        # Get maintenance history
        cursor.execute("""
        SELECT maintenance_id, maintenance_date, maintenance_type, description, technician, parts_replaced
        FROM maintenance_history
        WHERE chiller_id = ?
        ORDER BY maintenance_date DESC
        """, (chiller_id,))
        maintenance_history = [dict(zip(['maintenance_id', 'maintenance_date', 'maintenance_type', 
                                        'description', 'technician', 'parts_replaced'], row)) 
                              for row in cursor.fetchall()]
        
        return {
            'service_requests': service_requests,
            'maintenance_history': maintenance_history
        }
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# Example usage
if __name__ == "__main__":
    with ChillerDatabase() as db:
        # Add a chiller
        db.add_chiller(
            chiller_id="YC-001",
            model="YVAA",
            serial_number="SN12345",
            installation_date="2022-01-15",
            location="Building A, Floor 3"
        )
        
        # Create a service request
        request_id = db.create_service_request(
            chiller_id="YC-001",
            description="Low refrigerant levels",
            priority="High"
        )
        
        # Add maintenance record
        maintenance_id = db.add_maintenance_record(
            chiller_id="YC-001",
            maintenance_type="Preventive",
            description="Routine inspection and cleaning",
            technician="John Smith",
            parts_replaced="Air filters"
        )
        
        # Update service request status
        db.update_service_request_status(request_id, "Completed")
        
        # Get service history
        history = db.get_chiller_service_history("YC-001")
        print(history)
```
