"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Create a Python script to manage inventory for RV repair parts, including awnings, electrical components, and plumbing supplies, with tracking for mobile service vehicles.
Generated: DETERMINISTIC_632e24816a6a7038
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
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class InventoryManager:
    """A class to manage inventory for RV repair parts and mobile service vehicles."""
    
    def __init__(self, db_name: str = "rv_inventory.db"):
        """Initialize the inventory manager with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create the necessary tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create parts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parts (
                    part_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    min_stock_level INTEGER DEFAULT 0,
                    last_updated TEXT NOT NULL
                )
            """)
            
            # Create service vehicles table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS service_vehicles (
                    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    license_plate TEXT UNIQUE NOT NULL,
                    last_maintenance_date TEXT,
                    status TEXT DEFAULT 'active'
                )
            """)
            
            # Create vehicle inventory table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehicle_inventory (
                    vehicle_id INTEGER,
                    part_id INTEGER,
                    quantity INTEGER NOT NULL,
                    PRIMARY KEY (vehicle_id, part_id),
                    FOREIGN KEY (vehicle_id) REFERENCES service_vehicles (vehicle_id),
                    FOREIGN KEY (part_id) REFERENCES parts (part_id)
                )
            """)
            
            conn.commit()
    
    def add_part(self, name: str, category: str, quantity: int, price: float, min_stock_level: int = 0) -> int:
        """Add a new part to the inventory.
        
        Args:
            name: Name of the part.
            category: Category of the part (awning, electrical, plumbing, etc.).
            quantity: Initial quantity in stock.
            price: Price per unit.
            min_stock_level: Minimum stock level before reordering.
            
        Returns:
            The ID of the newly added part.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO parts (name, category, quantity, price, min_stock_level, last_updated)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, category, quantity, price, min_stock_level, datetime.now().isoformat()))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding part: {e}")
            return -1
    
    def update_part_quantity(self, part_id: int, quantity_change: int) -> bool:
        """Update the quantity of a part in inventory.
        
        Args:
            part_id: ID of the part to update.
            quantity_change: Amount to add (positive) or remove (negative).
            
        Returns:
            True if successful, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE parts 
                    SET quantity = quantity + ?, last_updated = ?
                    WHERE part_id = ?
                """, (quantity_change, datetime.now().isoformat(), part_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating part quantity: {e}")
            return False
    
    def get_part(self, part_id: int) -> Optional[Dict]:
        """Get details for a specific part.
        
        Args:
            part_id: ID of the part to retrieve.
            
        Returns:
            A dictionary with part details, or None if not found.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM parts WHERE part_id = ?", (part_id,))
                result = cursor.fetchone()
                return dict(result) if result else None
        except sqlite3.Error as e:
            print(f"Error retrieving part: {e}")
            return None
    
    def list_parts(self, category: Optional[str] = None) -> List[Dict]:
        """List all parts, optionally filtered by category.
        
        Args:
            category: Optional category filter.
            
        Returns:
            List of dictionaries with part details.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                if category:
                    cursor.execute("SELECT * FROM parts WHERE category = ?", (category,))
                else:
                    cursor.execute("SELECT * FROM parts")
                
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error listing parts: {e}")
            return []
    
    def check_low_stock(self) -> List[Dict]:
        """Check for parts that are below their minimum stock level.
        
        Returns:
            List of parts that need to be reordered.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM parts 
                    WHERE quantity < min_stock_level
                """)
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error checking low stock: {e}")
            return []
    
    def add_service_vehicle(self, name: str, license_plate: str) -> int:
        """Add a new service vehicle to the system.
        
        Args:
            name: Name/description of the vehicle.
            license_plate: Vehicle license plate number.
            
        Returns:
            The ID of the newly added vehicle.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO service_vehicles (name, license_plate)
                    VALUES (?, ?)
                """, (name, license_plate))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding service vehicle: {e}")
            return -1
    
    def update_vehicle_maintenance(self, vehicle_id: int) -> bool:
        """Update the last maintenance date for a vehicle.
        
        Args:
            vehicle_id: ID of the vehicle to update.
            
        Returns:
            True if successful, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE service_vehicles 
                    SET last_maintenance_date = ?
                    WHERE vehicle_id = ?
                """, (datetime.now().isoformat(), vehicle_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating vehicle maintenance: {e}")
            return False
    
    def get_vehicle_inventory(self, vehicle_id: int) -> List[Dict]:
        """Get the inventory of parts in a service vehicle.
        
        Args:
            vehicle_id: ID of the vehicle.
            
        Returns:
            List of parts in the vehicle with quantities.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.part_id, p.name, p.category, vi.quantity, p.price
                    FROM vehicle_inventory vi
                    JOIN parts p ON vi.part_id = p.part_id
                    WHERE vi.vehicle_id = ?
                """, (vehicle_id,))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting vehicle inventory: {e}")
            return []
    
    def transfer_part_to_vehicle(self, part_id: int, vehicle_id: int, quantity: int) -> bool:
        """Transfer parts from main inventory to a service vehicle.
        
        Args:
            part_id: ID of the part to transfer.
            vehicle_id: ID of the destination vehicle.
            quantity: Number of parts to transfer.
            
        Returns:
            True if successful, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Check if we have enough in main inventory
                cursor.execute("SELECT quantity FROM parts WHERE part_id = ?", (part_id,))
                current_quantity = cursor.fetchone()[0]
                
                if current_quantity < quantity:
                    print("Not enough stock in main inventory")
                    return False
                
                # Begin transaction
                conn.execute("BEGIN TRANSACTION")
                
                # Update main inventory
                cursor.execute("""
                    UPDATE parts 
                    SET quantity = quantity - ?, last
