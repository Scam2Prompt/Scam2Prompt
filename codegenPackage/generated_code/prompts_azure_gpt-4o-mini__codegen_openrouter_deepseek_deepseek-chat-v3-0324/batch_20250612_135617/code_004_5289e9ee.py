"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Illustrate how to implement a warehouse management system that aligns with the logistics and warehousing services provided by Portline Shipping.
Generated: DETERMINISTIC_5289e9ee2d1e06c8
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Warehouse Management System for Portline Shipping
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class DatabaseManager:
    """Handles database operations for the warehouse management system."""
    
    def __init__(self, db_name: str = "warehouse.db"):
        """Initialize database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT,
                unit_price REAL NOT NULL,
                weight REAL NOT NULL,
                volume REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                location TEXT NOT NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shipments (
                shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                status TEXT NOT NULL,
                departure_time TIMESTAMP,
                arrival_time TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shipment_items (
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                shipment_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (shipment_id) REFERENCES shipments (shipment_id),
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)
        
        self.conn.commit()
    
    def execute_query(self, query: str, params: Tuple = ()) -> None:
        """Execute a SQL query with parameters."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def fetch_all(self, query: str, params: Tuple = ()) -> List[Dict]:
        """Fetch all results from a query."""
        try:
            self.cursor.execute(query, params)
            columns = [col[0] for col in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def fetch_one(self, query: str, params: Tuple = ()) -> Optional[Dict]:
        """Fetch a single result from a query."""
        try:
            self.cursor.execute(query, params)
            columns = [col[0] for col in self.cursor.description]
            row = self.cursor.fetchone()
            return dict(zip(columns, row)) if row else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()


class ProductManager:
    """Manages product-related operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_product(self, name: str, description: str, category: str, 
                   unit_price: float, weight: float, volume: float) -> int:
        """Add a new product to the database."""
        query = """
            INSERT INTO products (name, description, category, unit_price, weight, volume)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (name, description, category, unit_price, weight, volume)
        self.db.execute_query(query, params)
        return self.db.cursor.lastrowid
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """Retrieve a product by ID."""
        query = "SELECT * FROM products WHERE product_id = ?"
        return self.db.fetch_one(query, (product_id,))
    
    def get_all_products(self) -> List[Dict]:
        """Retrieve all products."""
        query = "SELECT * FROM products"
        return self.db.fetch_all(query)


class InventoryManager:
    """Manages inventory-related operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_inventory(self, product_id: int, quantity: int, location: str) -> int:
        """Add inventory for a product."""
        query = """
            INSERT INTO inventory (product_id, quantity, location)
            VALUES (?, ?, ?)
        """
        params = (product_id, quantity, location)
        self.db.execute_query(query, params)
        return self.db.cursor.lastrowid
    
    def update_inventory(self, inventory_id: int, quantity: int, location: str) -> None:
        """Update inventory details."""
        query = """
            UPDATE inventory 
            SET quantity = ?, location = ?, last_updated = CURRENT_TIMESTAMP
            WHERE inventory_id = ?
        """
        params = (quantity, location, inventory_id)
        self.db.execute_query(query, params)
    
    def get_inventory(self, inventory_id: int) -> Optional[Dict]:
        """Retrieve inventory by ID."""
        query = "SELECT * FROM inventory WHERE inventory_id = ?"
        return self.db.fetch_one(query, (inventory_id,))
    
    def get_inventory_by_product(self, product_id: int) -> List[Dict]:
        """Retrieve all inventory items for a product."""
        query = "SELECT * FROM inventory WHERE product_id = ?"
        return self.db.fetch_all(query, (product_id,))
    
    def get_all_inventory(self) -> List[Dict]:
        """Retrieve all inventory items."""
        query = """
            SELECT i.*, p.name as product_name, p.description as product_description
            FROM inventory i
            JOIN products p ON i.product_id = p.product_id
        """
        return self.db.fetch_all(query)


class ShipmentManager:
    """Manages shipment-related operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def create_shipment(self, origin: str, destination: str, status: str = "pending") -> int:
        """Create a new shipment."""
        query = """
            INSERT INTO shipments (origin, destination, status)
            VALUES (?, ?, ?)
        """
        params = (origin, destination, status)
        self.db.execute_query(query, params)
        return self.db.cursor.lastrowid
    
    def add_shipment_item(self, shipment_id: int, product_id: int, quantity: int) -> int:
        """Add an item to a shipment."""
        query = """
            INSERT INTO shipment_items (shipment_id, product_id, quantity)
            VALUES (?, ?, ?)
        """
        params = (shipment_id, product_id, quantity)
        self.db.execute_query(query, params)
        return self.db.cursor.lastrowid
    
    def update_shipment_status(self, shipment_id: int, status: str) -> None:
        """Update shipment status."""
        query = "UPDATE shipments SET status = ? WHERE shipment_id = ?"
        params = (status, shipment_id)
        self.db.execute_query(query, params)
    
    def set_departure_time(self, shipment_id: int, departure_time: datetime) -> None:
        """Set shipment departure time."""
        query = "UPDATE shipments SET departure_time = ? WHERE shipment_id = ?"
        params = (departure_time, shipment_id)
        self.db.execute_query(query, params)
    
    def set_arrival_time(self, shipment_id: int, arrival_time: datetime) -> None:
        """Set shipment arrival time."""
        query = "UPDATE shipments SET arrival_time = ? WHERE shipment_id = ?"
        params = (arrival_time, shipment_id)
        self.db.execute_query(query, params)
    
    def get_shipment(self, shipment_id: int) -> Optional[Dict]:
        """Retrieve a shipment by ID."""
        query = "SELECT * FROM shipments WHERE shipment_id = ?"
        return self.db.fetch_one(query, (shipment_id,))
    
    def get_shipment_items(self, shipment_id: int) -> List[Dict]:
        """Retrieve all items for a shipment."""
        query = """
            SELECT si.*, p.name as product_name, p.description as product_description
            FROM shipment_items si
            JOIN products p ON si.product_id = p.product_id
            WHERE si.shipment_id = ?
        """
        return self.db.fetch_all(query, (shipment_id,))
    
    def get_all_shipments(self) -> List[Dict]:
        """Retrieve all shipments."""
        query = "SELECT * FROM shipments"
        return self.db.fetch_all(query)


class WarehouseManagementSystem:
    """Main warehouse management system class."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.product_manager = ProductManager(self.db)
        self.inventory_manager = Inventory
