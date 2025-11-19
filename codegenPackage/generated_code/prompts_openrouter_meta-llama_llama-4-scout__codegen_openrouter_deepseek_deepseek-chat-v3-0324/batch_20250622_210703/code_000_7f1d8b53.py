"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Write a Python script to manage inventory for a food distribution company like Global Group, including tracking products, shipments, and warehouse locations."
Generated: DETERMINISTIC_7f1d8b53323c4879
Batch ID: 20250622_210703
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
    """A class to manage inventory for a food distribution company."""
    
    def __init__(self, db_name: str = "inventory.db"):
        """Initialize the inventory manager with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create products table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    unit_price REAL NOT NULL,
                    quantity INTEGER NOT NULL DEFAULT 0,
                    min_stock_level INTEGER DEFAULT 10,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create warehouses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS warehouses (
                    warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    capacity INTEGER NOT NULL,
                    current_occupancy INTEGER DEFAULT 0
                )
            """)
            
            # Create shipments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS shipments (
                    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    warehouse_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    shipment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expected_arrival TIMESTAMP,
                    status TEXT DEFAULT 'pending',
                    FOREIGN KEY (product_id) REFERENCES products (product_id),
                    FOREIGN KEY (warehouse_id) REFERENCES warehouses (warehouse_id)
                )
            """)
            
            # Create inventory_locations table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory_locations (
                    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    warehouse_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products (product_id),
                    FOREIGN KEY (warehouse_id) REFERENCES warehouses (warehouse_id),
                    UNIQUE(product_id, warehouse_id)
                )
            """)
            
            conn.commit()

    def add_product(self, name: str, description: str, category: str, unit_price: float, 
                   quantity: int = 0, min_stock_level: int = 10) -> int:
        """Add a new product to the inventory.
        
        Args:
            name: Name of the product.
            description: Description of the product.
            category: Product category.
            unit_price: Price per unit.
            quantity: Initial quantity in stock.
            min_stock_level: Minimum stock level before reorder.
            
        Returns:
            The ID of the newly added product.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO products (name, description, category, unit_price, quantity, min_stock_level)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, description, category, unit_price, quantity, min_stock_level))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise Exception(f"Failed to add product: {str(e)}")

    def add_warehouse(self, name: str, location: str, capacity: int) -> int:
        """Add a new warehouse.
        
        Args:
            name: Name of the warehouse.
            location: Physical location.
            capacity: Total capacity in units.
            
        Returns:
            The ID of the newly added warehouse.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO warehouses (name, location, capacity)
                    VALUES (?, ?, ?)
                """, (name, location, capacity))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise Exception(f"Failed to add warehouse: {str(e)}")

    def create_shipment(self, product_id: int, warehouse_id: int, quantity: int, 
                       expected_arrival: Optional[str] = None) -> int:
        """Create a new shipment.
        
        Args:
            product_id: ID of the product being shipped.
            warehouse_id: ID of the destination warehouse.
            quantity: Quantity being shipped.
            expected_arrival: Expected arrival date (YYYY-MM-DD).
            
        Returns:
            The ID of the newly created shipment.
        """
        try:
            # Check if product exists and has sufficient stock
            product = self.get_product(product_id)
            if product is None:
                raise Exception("Product not found")
                
            if product['quantity'] < quantity:
                raise Exception("Insufficient stock for shipment")
                
            # Check if warehouse exists
            warehouse = self.get_warehouse(warehouse_id)
            if warehouse is None:
                raise Exception("Warehouse not found")
                
            # Check warehouse capacity
            if warehouse['current_occupancy'] + quantity > warehouse['capacity']:
                raise Exception("Warehouse capacity exceeded")
                
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Update product quantity
                cursor.execute("""
                    UPDATE products 
                    SET quantity = quantity - ?
                    WHERE product_id = ?
                """, (quantity, product_id))
                
                # Create shipment
                cursor.execute("""
                    INSERT INTO shipments (product_id, warehouse_id, quantity, expected_arrival)
                    VALUES (?, ?, ?, ?)
                """, (product_id, warehouse_id, quantity, expected_arrival))
                
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise Exception(f"Failed to create shipment: {str(e)}")

    def receive_shipment(self, shipment_id: int) -> None:
        """Mark a shipment as received and update inventory.
        
        Args:
            shipment_id: ID of the shipment to receive.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Get shipment details
                cursor.execute("""
                    SELECT product_id, warehouse_id, quantity 
                    FROM shipments 
                    WHERE shipment_id = ? AND status = 'pending'
                """, (shipment_id,))
                shipment = cursor.fetchone()
                
                if not shipment:
                    raise Exception("Shipment not found or already received")
                    
                product_id, warehouse_id, quantity = shipment
                
                # Update shipment status
                cursor.execute("""
                    UPDATE shipments 
                    SET status = 'received', shipment_date = CURRENT_TIMESTAMP
                    WHERE shipment_id = ?
                """, (shipment_id,))
                
                # Update warehouse occupancy
                cursor.execute("""
                    UPDATE warehouses 
                    SET current_occupancy = current_occupancy + ?
                    WHERE warehouse_id = ?
                """, (quantity, warehouse_id))
                
                # Update inventory location
                cursor.execute("""
                    INSERT OR REPLACE INTO inventory_locations (product_id, warehouse_id, quantity)
                    VALUES (?, ?, COALESCE(
                        (SELECT quantity FROM inventory_locations 
                         WHERE product_id = ? AND warehouse_id = ?), 0) + ?)
                """, (product_id, warehouse_id, product_id, warehouse_id, quantity))
                
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Failed to receive shipment: {str(e)}")

    def get_product(self, product_id: int) -> Optional[Dict]:
        """Get product details by ID.
        
        Args:
            product_id: ID of the product to retrieve.
            
        Returns:
            A dictionary with product details, or None if not found.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
                product = cursor.fetchone()
                return dict(product) if product else None
        except sqlite3.Error as e:
            raise Exception(f"Failed to get product: {str(e)}")

    def get_warehouse(self, warehouse_id: int) -> Optional[Dict]:
        """Get warehouse details by ID.
        
        Args:
            warehouse_id: ID of the warehouse to retrieve.
            
        Returns:
            A dictionary with warehouse details, or None if not found.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM warehouses WHERE warehouse_id = ?", (warehouse_id,))
                warehouse = cursor.fetchone()
                return dict(warehouse) if warehouse else None
        except sqlite3.Error as e:
            raise Exception(f"Failed to get warehouse: {str(e)}")

    def get_shipment(self, shipment_id: int) -> Optional[Dict]:
        """Get shipment details by ID.
        
        Args:
