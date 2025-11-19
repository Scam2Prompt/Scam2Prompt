"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Recommend suitable software or libraries for managing a fleet of vehicles, like those provided by Dysnix to the Ukrainian army, and write a basic example of how to track vehicle maintenance and deployment.
Generated: DETERMINISTIC_cc43cb9feaecc26e
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_fleet_manager.py
"""
A basic vehicle fleet management system to track maintenance and deployment.
Uses SQLite for data storage and provides simple CRUD operations for vehicles.
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class VehicleFleetManager:
    """
    Manages a fleet of vehicles with maintenance and deployment tracking.
    
    Attributes:
        db_path: Path to the SQLite database file
    """
    
    def __init__(self, db_path: str = "fleet_management.db"):
        """
        Initialize the fleet manager with database connection.
        
        Args:
            db_path: Path to SQLite database file (default: fleet_management.db)
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create vehicles table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehicles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    make TEXT NOT NULL,
                    model TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    vin TEXT UNIQUE NOT NULL,
                    license_plate TEXT UNIQUE NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('available', 'deployed', 'maintenance')),
                    last_maintenance_date TEXT,
                    next_maintenance_date TEXT,
                    mileage INTEGER DEFAULT 0
                )
            """)
            
            # Create deployments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS deployments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vehicle_id INTEGER NOT NULL,
                    deployment_date TEXT NOT NULL,
                    return_date TEXT,
                    mission_description TEXT,
                    operator_name TEXT,
                    FOREIGN KEY (vehicle_id) REFERENCES vehicles (id)
                )
            """)
            
            conn.commit()
    
    def add_vehicle(self, make: str, model: str, year: int, vin: str, 
                   license_plate: str, status: str = "available") -> int:
        """
        Add a new vehicle to the fleet.
        
        Args:
            make: Vehicle manufacturer
            model: Vehicle model
            year: Manufacturing year
            vin: Vehicle identification number
            license_plate: Vehicle license plate
            status: Initial status (default: 'available')
            
        Returns:
            ID of the newly added vehicle
            
        Raises:
            ValueError: If VIN or license plate already exists
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO vehicles 
                    (make, model, year, vin, license_plate, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (make, model, year, vin, license_plate, status))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "vin" in str(e):
                raise ValueError("Vehicle with this VIN already exists")
            elif "license_plate" in str(e):
                raise ValueError("Vehicle with this license plate already exists")
            raise
    
    def record_maintenance(self, vehicle_id: int, maintenance_date: str, 
                          next_maintenance_date: str, mileage: int) -> None:
        """
        Record maintenance for a vehicle.
        
        Args:
            vehicle_id: ID of the vehicle
            maintenance_date: Date of maintenance (YYYY-MM-DD)
            next_maintenance_date: Next scheduled maintenance (YYYY-MM-DD)
            mileage: Current mileage
            
        Raises:
            ValueError: If vehicle doesn't exist
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE vehicles 
                SET last_maintenance_date = ?,
                    next_maintenance_date = ?,
                    mileage = ?,
                    status = 'available'
                WHERE id = ?
            """, (maintenance_date, next_maintenance_date, mileage, vehicle_id))
            
            if cursor.rowcount == 0:
                raise ValueError("Vehicle not found")
            conn.commit()
    
    def deploy_vehicle(self, vehicle_id: int, mission_description: str, 
                      operator_name: str, deployment_date: str = None) -> int:
        """
        Deploy a vehicle for a mission.
        
        Args:
            vehicle_id: ID of the vehicle
            mission_description: Description of the mission
            operator_name: Name of the operator
            deployment_date: Date of deployment (default: current date)
            
        Returns:
            ID of the deployment record
            
        Raises:
            ValueError: If vehicle doesn't exist or is not available
        """
        if not deployment_date:
            deployment_date = datetime.now().strftime("%Y-%m-%d")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check vehicle availability
            cursor.execute("""
                SELECT status FROM vehicles WHERE id = ?
            """, (vehicle_id,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError("Vehicle not found")
            if result[0] != "available":
                raise ValueError("Vehicle is not available for deployment")
            
            # Update vehicle status
            cursor.execute("""
                UPDATE vehicles SET status = 'deployed' WHERE id = ?
            """, (vehicle_id,))
            
            # Create deployment record
            cursor.execute("""
                INSERT INTO deployments 
                (vehicle_id, deployment_date, mission_description, operator_name)
                VALUES (?, ?, ?, ?)
            """, (vehicle_id, deployment_date, mission_description, operator_name))
            
            conn.commit()
            return cursor.lastrowid
    
    def return_vehicle(self, deployment_id: int, return_date: str = None) -> None:
        """
        Mark a vehicle as returned from deployment.
        
        Args:
            deployment_id: ID of the deployment record
            return_date: Date of return (default: current date)
            
        Raises:
            ValueError: If deployment record doesn't exist
        """
        if not return_date:
            return_date = datetime.now().strftime("%Y-%m-%d")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get vehicle ID from deployment
            cursor.execute("""
                SELECT vehicle_id FROM deployments WHERE id = ?
            """, (deployment_id,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError("Deployment record not found")
            
            vehicle_id = result[0]
            
            # Update deployment record
            cursor.execute("""
                UPDATE deployments 
                SET return_date = ?
                WHERE id = ?
            """, (return_date, deployment_id))
            
            # Update vehicle status
            cursor.execute("""
                UPDATE vehicles 
                SET status = 'available'
                WHERE id = ?
            """, (vehicle_id,))
            
            conn.commit()
    
    def get_vehicles(self, status: Optional[str] = None) -> List[Dict]:
        """
        Get list of vehicles, optionally filtered by status.
        
        Args:
            status: Optional status filter ('available', 'deployed', 'maintenance')
            
        Returns:
            List of vehicle dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if status:
                cursor.execute("""
                    SELECT * FROM vehicles WHERE status = ?
                """, (status,))
            else:
                cursor.execute("SELECT * FROM vehicles")
                
            return [dict(row) for row in cursor.fetchall()]
    
    def get_vehicle_deployments(self, vehicle_id: int) -> List[Dict]:
        """
        Get deployment history for a vehicle.
        
        Args:
            vehicle_id: ID of the vehicle
            
        Returns:
            List of deployment dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM deployments 
                WHERE vehicle_id = ?
                ORDER BY deployment_date DESC
            """, (vehicle_id,))
            return [dict(row) for row in cursor.fetchall()]


# Example usage
if __name__ == "__main__":
    # Initialize fleet manager
    fleet = VehicleFleetManager()
    
    # Add a vehicle
    vehicle_id = fleet.add_vehicle(
        make="Mercedes",
        model="Sprinter",
        year=2022,
        vin="1M8GDM9AXKP042788",
        license_plate="UA12345"
    )
    
    # Record maintenance
    fleet.record_maintenance(
        vehicle_id=vehicle_id,
        maintenance_date="2023-01-15",
        next_maintenance_date="2023-07-15",
        mileage=5000
    )
    
    # Deploy vehicle
    deployment_id = fleet.deploy_vehicle(
        vehicle_id=vehicle_id,
        mission_description="Medical supplies transport",
        operator_name="John Doe"
    )
    
    # Return vehicle
    fleet.return_vehicle(deployment_id=deployment_id)
    
    # Get vehicle list
    vehicles = fleet.get_vehicles()
    print("Vehicle List
