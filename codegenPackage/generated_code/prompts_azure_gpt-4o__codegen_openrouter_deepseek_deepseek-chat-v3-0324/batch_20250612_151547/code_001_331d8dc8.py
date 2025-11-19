"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Generate a script for managing warehouse inventory tailored to Fealty Worldwide's warehousing services, including storage, distribution, and pre-positioning of products.
Generated: DETERMINISTIC_331d8dc8b3161d9e
Batch ID: 20250612_151547
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

class WarehouseInventory:
    """
    A class to manage warehouse inventory for Fealty Worldwide's warehousing services.
    Handles storage, distribution, and pre-positioning of products.
    """
    
    def __init__(self, db_path: str = "warehouse.db"):
        """
        Initialize the inventory system with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize the database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Products table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sku TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    unit_price REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Inventory table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    warehouse_location TEXT NOT NULL,
                    quantity INTEGER NOT NULL DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products (product_id)
                )
            """)
            
            # Movements table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movements (
                    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    from_location TEXT,
                    to_location TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    movement_type TEXT NOT NULL,  -- 'inbound', 'outbound', 'transfer'
                    movement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT,
                    FOREIGN KEY (product_id) REFERENCES products (product_id)
                )
            """)
            
            # Pre-positioning table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS prepositioning (
                    preposition_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    target_location TEXT NOT NULL,
                    target_quantity INTEGER NOT NULL,
                    deadline DATE NOT NULL,
                    status TEXT DEFAULT 'pending',  -- 'pending', 'in-progress', 'completed'
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products (product_id)
                )
            """)
            
            conn.commit()
    
    def add_product(self, sku: str, name: str, unit_price: float, 
                   description: str = None, category: str = None) -> int:
        """
        Add a new product to the inventory system.
        
        Args:
            sku: Stock Keeping Unit (unique identifier)
            name: Product name
            unit_price: Price per unit
            description: Product description (optional)
            category: Product category (optional)
            
        Returns:
            The product_id of the newly created product
            
        Raises:
            ValueError: If SKU already exists
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO products (sku, name, description, category, unit_price)
                    VALUES (?, ?, ?, ?, ?)
                """, (sku, name, description, category, unit_price))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Product with SKU '{sku}' already exists")
    
    def update_product(self, product_id: int, **kwargs) -> None:
        """
        Update product information.
        
        Args:
            product_id: ID of the product to update
            **kwargs: Fields to update (sku, name, description, category, unit_price)
            
        Raises:
            ValueError: If product_id doesn't exist or invalid fields provided
        """
        if not kwargs:
            raise ValueError("No fields to update provided")
            
        valid_fields = {'sku', 'name', 'description', 'category', 'unit_price'}
        invalid_fields = set(kwargs.keys()) - valid_fields
        if invalid_fields:
            raise ValueError(f"Invalid fields to update: {invalid_fields}")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if product exists
            cursor.execute("SELECT 1 FROM products WHERE product_id = ?", (product_id,))
            if not cursor.fetchone():
                raise ValueError(f"Product with ID {product_id} doesn't exist")
            
            # Build update query
            set_clause = ", ".join(f"{field} = ?" for field in kwargs.keys())
            query = f"UPDATE products SET {set_clause} WHERE product_id = ?"
            
            cursor.execute(query, (*kwargs.values(), product_id))
            conn.commit()
    
    def get_product(self, product_id: int) -> Dict:
        """
        Get product details by ID.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            Dictionary with product details
            
        Raises:
            ValueError: If product_id doesn't exist
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT product_id, sku, name, description, category, unit_price, created_at
                FROM products
                WHERE product_id = ?
            """, (product_id,))
            
            row = cursor.fetchone()
            if not row:
                raise ValueError(f"Product with ID {product_id} doesn't exist")
                
            return {
                'product_id': row[0],
                'sku': row[1],
                'name': row[2],
                'description': row[3],
                'category': row[4],
                'unit_price': row[5],
                'created_at': row[6]
            }
    
    def add_inventory(self, product_id: int, warehouse_location: str, quantity: int) -> None:
        """
        Add inventory for a product at a specific warehouse location.
        
        Args:
            product_id: ID of the product
            warehouse_location: Location identifier
            quantity: Quantity to add
            
        Raises:
            ValueError: If product_id doesn't exist or quantity is invalid
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if product exists
            cursor.execute("SELECT 1 FROM products WHERE product_id = ?", (product_id,))
            if not cursor.fetchone():
                raise ValueError(f"Product with ID {product_id} doesn't exist")
            
            # Check if inventory record exists
            cursor.execute("""
                SELECT inventory_id, quantity FROM inventory
                WHERE product_id = ? AND warehouse_location = ?
            """, (product_id, warehouse_location))
            
            result = cursor.fetchone()
            
            if result:
                # Update existing inventory
                new_quantity = result[1] + quantity
                cursor.execute("""
                    UPDATE inventory
                    SET quantity = ?, last_updated = CURRENT_TIMESTAMP
                    WHERE inventory_id = ?
                """, (new_quantity, result[0]))
            else:
                # Create new inventory record
                cursor.execute("""
                    INSERT INTO inventory (product_id, warehouse_location, quantity)
                    VALUES (?, ?, ?)
                """, (product_id, warehouse_location, quantity))
            
            # Record movement
            cursor.execute("""
                INSERT INTO movements (product_id, to_location, quantity, movement_type)
                VALUES (?, ?, ?, 'inbound')
            """, (product_id, warehouse_location, quantity))
            
            conn.commit()
    
    def remove_inventory(self, product_id: int, warehouse_location: str, quantity: int) -> None:
        """
        Remove inventory for a product from a specific warehouse location.
        
        Args:
            product_id: ID of the product
            warehouse_location: Location identifier
            quantity: Quantity to remove
            
        Raises:
            ValueError: If product_id doesn't exist, quantity is invalid, or insufficient stock
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if product exists
            cursor.execute("SELECT 1 FROM products WHERE product_id = ?", (product_id,))
            if not cursor.fetchone():
                raise ValueError(f"Product with ID {product_id} doesn't exist")
            
            # Check current inventory
            cursor.execute("""
                SELECT inventory_id, quantity FROM inventory
                WHERE product_id = ? AND warehouse_location = ?
            """, (product_id, warehouse_location))
            
            result = cursor.fetchone()
            
            if not result:
                raise ValueError(f"No inventory found for product {product_id} at location {warehouse_location}")
            
            current_quantity = result[1]
            if current_quantity < quantity:
                raise ValueError(f"Insufficient stock. Available: {current_quantity}, Requested: {quantity}")
            
            # Update inventory
            new_quantity = current_quantity - quantity
            if new_quantity == 0:
