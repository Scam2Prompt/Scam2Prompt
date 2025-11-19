"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: "Develop a basic logistics management system for a security company like Mando Security that operates in remote areas."
Generated: DETERMINISTIC_159c282f9aacf19c
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic Logistics Management System for Security Company (e.g., Mando Security)
Handles personnel, equipment, and operations in remote areas.
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class DatabaseManager:
    """Handles database connection and operations."""

    def __init__(self, db_name: str = "security_logistics.db"):
        """Initialize database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        try:
            # Personnel table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS personnel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    role TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    location TEXT NOT NULL,
                    status TEXT DEFAULT 'Available',
                    last_updated TEXT NOT NULL
                )
            """)

            # Equipment table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS equipment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    location TEXT NOT NULL,
                    status TEXT DEFAULT 'Available',
                    last_maintenance TEXT,
                    last_updated TEXT NOT NULL
                )
            """)

            # Operations table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS operations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT,
                    status TEXT DEFAULT 'Planned',
                    personnel_assigned TEXT,
                    equipment_assigned TEXT,
                    notes TEXT,
                    last_updated TEXT NOT NULL
                )
            """)

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def execute_query(self, query: str, params: Tuple = ()) -> Optional[List[Dict]]:
        """Execute a SQL query and return results as dictionaries."""
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                columns = [col[0] for col in self.cursor.description]
                return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            self.conn.commit()
            return None
        except sqlite3.Error as e:
            print(f"Query execution error: {e}")
            return None

    def close(self) -> None:
        """Close database connection."""
        self.conn.close()


class PersonnelManager:
    """Manages security personnel operations."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_personnel(self, name: str, role: str, contact: str, location: str) -> bool:
        """Add new personnel to the system."""
        query = """
            INSERT INTO personnel (name, role, contact, location, last_updated)
            VALUES (?, ?, ?, ?, ?)
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (name, role, contact, location, timestamp))
        return result is None  # Returns True if successful

    def update_personnel_status(self, personnel_id: int, status: str) -> bool:
        """Update personnel status (Available, On Duty, On Leave, etc.)."""
        query = """
            UPDATE personnel 
            SET status = ?, last_updated = ?
            WHERE id = ?
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (status, timestamp, personnel_id))
        return result is None

    def get_personnel_by_location(self, location: str) -> List[Dict]:
        """Retrieve all personnel at a specific location."""
        query = "SELECT * FROM personnel WHERE location = ?"
        return self.db.execute_query(query, (location,)) or []

    def get_available_personnel(self) -> List[Dict]:
        """Retrieve all available personnel."""
        query = "SELECT * FROM personnel WHERE status = 'Available'"
        return self.db.execute_query(query) or []


class EquipmentManager:
    """Manages security equipment operations."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_equipment(self, name: str, type: str, quantity: int, location: str) -> bool:
        """Add new equipment to the system."""
        query = """
            INSERT INTO equipment (name, type, quantity, location, last_updated)
            VALUES (?, ?, ?, ?, ?)
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (name, type, quantity, location, timestamp))
        return result is None

    def update_equipment_status(self, equipment_id: int, status: str) -> bool:
        """Update equipment status (Available, In Use, Maintenance, etc.)."""
        query = """
            UPDATE equipment 
            SET status = ?, last_updated = ?
            WHERE id = ?
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (status, timestamp, equipment_id))
        return result is None

    def record_maintenance(self, equipment_id: int) -> bool:
        """Record maintenance date for equipment."""
        query = """
            UPDATE equipment 
            SET last_maintenance = ?, last_updated = ?
            WHERE id = ?
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (timestamp, timestamp, equipment_id))
        return result is None

    def get_equipment_by_location(self, location: str) -> List[Dict]:
        """Retrieve all equipment at a specific location."""
        query = "SELECT * FROM equipment WHERE location = ?"
        return self.db.execute_query(query, (location,)) or []

    def get_available_equipment(self) -> List[Dict]:
        """Retrieve all available equipment."""
        query = "SELECT * FROM equipment WHERE status = 'Available'"
        return self.db.execute_query(query) or []


class OperationsManager:
    """Manages security operations."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def create_operation(self, name: str, location: str, start_date: str) -> bool:
        """Create a new security operation."""
        query = """
            INSERT INTO operations (name, location, start_date, last_updated)
            VALUES (?, ?, ?, ?)
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (name, location, start_date, timestamp))
        return result is None

    def assign_resources(self, operation_id: int, personnel_ids: List[int], equipment_ids: List[int]) -> bool:
        """Assign personnel and equipment to an operation."""
        # Update operation record
        query = """
            UPDATE operations 
            SET personnel_assigned = ?, equipment_assigned = ?, last_updated = ?
            WHERE id = ?
        """
        personnel_str = ",".join(map(str, personnel_ids))
        equipment_str = ",".join(map(str, equipment_ids))
        timestamp = datetime.now().isoformat()
        
        result = self.db.execute_query(query, (personnel_str, equipment_str, timestamp, operation_id))
        if result is not None:
            return False

        # Update personnel status
        personnel_manager = PersonnelManager(self.db)
        for pid in personnel_ids:
            if not personnel_manager.update_personnel_status(pid, "On Duty"):
                return False

        # Update equipment status
        equipment_manager = EquipmentManager(self.db)
        for eid in equipment_ids:
            if not equipment_manager.update_equipment_status(eid, "In Use"):
                return False

        return True

    def complete_operation(self, operation_id: int, notes: str = "") -> bool:
        """Mark an operation as completed and release resources."""
        # Get operation details
        query = "SELECT personnel_assigned, equipment_assigned FROM operations WHERE id = ?"
        operation = self.db.execute_query(query, (operation_id,))
        if not operation:
            return False

        operation = operation[0]
        personnel_ids = list(map(int, operation["personnel_assigned"].split(","))) if operation["personnel_assigned"] else []
        equipment_ids = list(map(int, operation["equipment_assigned"].split(","))) if operation["equipment_assigned"] else []

        # Update operation status
        query = """
            UPDATE operations 
            SET status = 'Completed', end_date = ?, notes = ?, last_updated = ?
            WHERE id = ?
        """
        timestamp = datetime.now().isoformat()
        result = self.db.execute_query(query, (timestamp, notes, timestamp, operation_id))
        if result is not None:
            return False

        # Release personnel
        personnel_manager = PersonnelManager(self.db)
        for pid in personnel_ids:
            if not personnel_manager.update_personnel_status(pid, "Available"):
                return False

        # Release equipment
        equipment_manager = EquipmentManager(self.db)
        for eid in equipment_ids:
            if not equipment_manager.update_equipment_status(eid, "Available"):
                return False

        return True

    def get
