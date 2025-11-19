"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Generate a script to manage a database of Whirlpool appliance repair requests, including fields for appliance type (e.g., lavadoras, neveras, estufas), customer location (e.g., Bogotá, Soacha), and technician assignment.
Generated: DETERMINISTIC_effcf33b81c638d5
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict, Tuple
from enum import Enum

class ApplianceType(Enum):
    """Enumeration for appliance types."""
    LAVADORA = "lavadora"
    NEVERA = "nevera"
    ESTUFA = "estufa"
    OTRO = "otro"

class RepairRequestManager:
    """Manages Whirlpool appliance repair requests in a SQLite database."""
    
    def __init__(self, db_path: str = "whirlpool_repairs.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_path = db_path
        self.conn = None
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create the database and tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create repair_requests table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS repair_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT NOT NULL,
                    appliance_type TEXT NOT NULL,
                    location TEXT NOT NULL,
                    issue_description TEXT NOT NULL,
                    technician_id INTEGER,
                    status TEXT DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (technician_id) REFERENCES technicians(id)
                )
            ''')
            
            # Create technicians table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS technicians (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT,
                    location TEXT NOT NULL
                )
            ''')
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def add_repair_request(
        self,
        customer_name: str,
        appliance_type: ApplianceType,
        location: str,
        issue_description: str,
        technician_id: Optional[int] = None
    ) -> int:
        """Add a new repair request to the database.
        
        Args:
            customer_name: Name of the customer.
            appliance_type: Type of appliance (from ApplianceType enum).
            location: Customer's location (e.g., "Bogotá", "Soacha").
            issue_description: Description of the issue.
            technician_id: Optional ID of assigned technician.
            
        Returns:
            The ID of the newly created repair request.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO repair_requests (
                    customer_name,
                    appliance_type,
                    location,
                    issue_description,
                    technician_id
                ) VALUES (?, ?, ?, ?, ?)
            ''', (
                customer_name,
                appliance_type.value,
                location,
                issue_description,
                technician_id
            ))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding repair request: {e}")
            raise

    def assign_technician(self, request_id: int, technician_id: int) -> bool:
        """Assign a technician to a repair request.
        
        Args:
            request_id: ID of the repair request.
            technician_id: ID of the technician to assign.
            
        Returns:
            True if assignment was successful, False otherwise.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE repair_requests
                SET technician_id = ?, status = 'assigned'
                WHERE id = ?
            ''', (technician_id, request_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error assigning technician: {e}")
            raise

    def get_repair_requests(
        self,
        status: Optional[str] = None,
        location: Optional[str] = None,
        appliance_type: Optional[ApplianceType] = None
    ) -> List[Dict]:
        """Retrieve repair requests with optional filters.
        
        Args:
            status: Filter by status (e.g., 'pending', 'assigned', 'completed').
            location: Filter by customer location.
            appliance_type: Filter by appliance type.
            
        Returns:
            List of dictionaries representing repair requests.
        """
        try:
            cursor = self.conn.cursor()
            query = '''
                SELECT 
                    r.id, r.customer_name, r.appliance_type, r.location, 
                    r.issue_description, r.technician_id, r.status, r.created_at,
                    t.name as technician_name
                FROM repair_requests r
                LEFT JOIN technicians t ON r.technician_id = t.id
            '''
            conditions = []
            params = []
            
            if status:
                conditions.append("r.status = ?")
                params.append(status)
            if location:
                conditions.append("r.location = ?")
                params.append(location)
            if appliance_type:
                conditions.append("r.appliance_type = ?")
                params.append(appliance_type.value)
                
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
                
            cursor.execute(query, params)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error fetching repair requests: {e}")
            raise

    def add_technician(
        self,
        name: str,
        location: str,
        specialization: Optional[str] = None
    ) -> int:
        """Add a new technician to the database.
        
        Args:
            name: Technician's name.
            location: Technician's location (e.g., "Bogotá", "Soacha").
            specialization: Optional specialization (e.g., "lavadoras").
            
        Returns:
            The ID of the newly created technician.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO technicians (name, specialization, location)
                VALUES (?, ?, ?)
            ''', (name, specialization, location))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding technician: {e}")
            raise

    def get_available_technicians(
        self,
        location: Optional[str] = None,
        specialization: Optional[str] = None
    ) -> List[Dict]:
        """Retrieve technicians with optional filters.
        
        Args:
            location: Filter by technician location.
            specialization: Filter by technician specialization.
            
        Returns:
            List of dictionaries representing technicians.
        """
        try:
            cursor = self.conn.cursor()
            query = "SELECT id, name, specialization, location FROM technicians"
            conditions = []
            params = []
            
            if location:
                conditions.append("location = ?")
                params.append(location)
            if specialization:
                conditions.append("specialization = ?")
                params.append(specialization)
                
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
                
            cursor.execute(query, params)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error fetching technicians: {e}")
            raise

    def update_request_status(self, request_id: int, status: str) -> bool:
        """Update the status of a repair request.
        
        Args:
            request_id: ID of the repair request.
            status: New status (e.g., 'pending', 'assigned', 'completed').
            
        Returns:
            True if update was successful, False otherwise.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE repair_requests
                SET status = ?
                WHERE id = ?
            ''', (status, request_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating request status: {e}")
            raise

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
```
