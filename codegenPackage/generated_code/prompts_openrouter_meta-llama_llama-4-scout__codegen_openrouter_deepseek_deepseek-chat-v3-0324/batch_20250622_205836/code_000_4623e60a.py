"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a Python code snippet to manage a logistics company's warehouse, including storage and inventory tracking, inspired by Bin Qutab Logistics L.L.C's warehousing services.
Generated: DETERMINISTIC_4623e60ab56a74cc
Batch ID: 20250622_205836
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

class WarehouseManager:
    """
    A class to manage warehouse operations including inventory tracking and storage management.
    """
    
    def __init__(self, db_name: str = "warehouse.db"):
        """
        Initialize the warehouse manager with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT,
                unit_price REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                location TEXT NOT NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movements (
                movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                source_location TEXT,
                destination_location TEXT NOT NULL,
                movement_type TEXT NOT NULL CHECK(movement_type IN ('inbound', 'outbound', 'transfer')),
                movement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)
        
        self.conn.commit()
    
    def add_product(self, name: str, unit_price: float, description: str = "", category: str = "") -> int:
        """
        Add a new product to the warehouse.
        
        Args:
            name: Product name
            unit_price: Price per unit
            description: Product description
            category: Product category
            
        Returns:
            The ID of the newly created product
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO products (name, description, category, unit_price)
            VALUES (?, ?, ?, ?)
        """, (name, description, category, unit_price))
        self.conn.commit()
        return cursor.lastrowid
    
    def update_inventory(self, product_id: int, quantity: int, location: str) -> None:
        """
        Update inventory for a product at a specific location.
        
        Args:
            product_id: ID of the product
            quantity: Quantity to add/remove
            location: Warehouse location
        """
        cursor = self.conn.cursor()
        
        # Check if inventory record exists
        cursor.execute("""
            SELECT quantity FROM inventory 
            WHERE product_id = ? AND location = ?
        """, (product_id, location))
        
        result = cursor.fetchone()
        
        if result:
            # Update existing record
            new_quantity = result[0] + quantity
            cursor.execute("""
                UPDATE inventory 
                SET quantity = ?, last_updated = CURRENT_TIMESTAMP
                WHERE product_id = ? AND location = ?
            """, (new_quantity, product_id, location))
        else:
            # Create new record
            cursor.execute("""
                INSERT INTO inventory (product_id, quantity, location)
                VALUES (?, ?, ?)
            """, (product_id, quantity, location))
        
        self.conn.commit()
    
    def record_movement(self, product_id: int, quantity: int, movement_type: str, 
                       destination_location: str, source_location: str = None, notes: str = "") -> None:
        """
        Record a product movement in the warehouse.
        
        Args:
            product_id: ID of the product being moved
            quantity: Quantity being moved
            movement_type: Type of movement ('inbound', 'outbound', 'transfer')
            destination_location: Destination location
            source_location: Source location (for transfers)
            notes: Additional notes about the movement
        """
        if movement_type not in ['inbound', 'outbound', 'transfer']:
            raise ValueError("Invalid movement type. Must be 'inbound', 'outbound', or 'transfer'")
            
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO movements (
                product_id, quantity, source_location, 
                destination_location, movement_type, notes
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (product_id, quantity, source_location, destination_location, movement_type, notes))
        self.conn.commit()
    
    def get_inventory(self, location: str = None) -> List[Dict]:
        """
        Get current inventory levels.
        
        Args:
            location: Optional filter for specific location
            
        Returns:
            List of inventory items with product details
        """
        cursor = self.conn.cursor()
        
        query = """
            SELECT p.product_id, p.name, p.description, p.category, p.unit_price,
                   i.quantity, i.location, i.last_updated
            FROM products p
            JOIN inventory i ON p.product_id = i.product_id
        """
        
        params = ()
        
        if location:
            query += " WHERE i.location = ?"
            params = (location,)
            
        cursor.execute(query, params)
        
        inventory = []
        for row in cursor.fetchall():
            inventory.append({
                'product_id': row[0],
                'name': row[1],
                'description': row[2],
                'category': row[3],
                'unit_price': row[4],
                'quantity': row[5],
                'location': row[6],
                'last_updated': row[7]
            })
            
        return inventory
    
    def get_product_movements(self, product_id: int, start_date: str = None, end_date: str = None) -> List[Dict]:
        """
        Get movement history for a specific product.
        
        Args:
            product_id: ID of the product
            start_date: Optional start date filter (YYYY-MM-DD)
            end_date: Optional end date filter (YYYY-MM-DD)
            
        Returns:
            List of movement records for the product
        """
        cursor = self.conn.cursor()
        
        query = """
            SELECT m.movement_id, p.name, m.quantity, m.source_location, 
                   m.destination_location, m.movement_type, m.movement_date, m.notes
            FROM movements m
            JOIN products p ON m.product_id = p.product_id
            WHERE m.product_id = ?
        """
        
        params = [product_id]
        
        if start_date:
            query += " AND m.movement_date >= ?"
            params.append(start_date)
            
        if end_date:
            query += " AND m.movement_date <= ?"
            params.append(end_date)
            
        query += " ORDER BY m.movement_date DESC"
        
        cursor.execute(query, tuple(params))
        
        movements = []
        for row in cursor.fetchall():
            movements.append({
                'movement_id': row[0],
                'product_name': row[1],
                'quantity': row[2],
                'source_location': row[3],
                'destination_location': row[4],
                'movement_type': row[5],
                'movement_date': row[6],
                'notes': row[7]
            })
            
        return movements
    
    def get_low_stock_items(self, threshold: int = 5) -> List[Dict]:
        """
        Get items with inventory levels below the specified threshold.
        
        Args:
            threshold: Minimum quantity threshold
            
        Returns:
            List of low stock items
        """
        cursor = self.conn.cursor()
        
        cursor.execute("""
            SELECT p.product_id, p.name, i.quantity, i.location
            FROM products p
            JOIN inventory i ON p.product_id = i.product_id
            WHERE i.quantity < ?
            ORDER BY i.quantity ASC
        """, (threshold,))
        
        low_stock = []
        for row in cursor.fetchall():
            low_stock.append({
                'product_id': row[0],
                'name': row[1],
                'quantity': row[2],
                'location': row[3]
            })
            
        return low_stock
    
    def transfer_inventory(self, product_id: int, quantity: int, 
                          source_location: str, destination_location: str) -> None:
        """
        Transfer inventory between locations.
        
        Args:
            product_id: ID of the product to transfer
            quantity: Quantity to transfer
            source_location: Current location of the inventory
            destination_location: New location for the inventory
        """
        cursor = self.conn.cursor()
        
        # Check if source has enough inventory
        cursor.execute("""
            SELECT quantity FROM inventory 
            WHERE product_id = ? AND location = ?
        """, (product_id, source_location))
        
        result = cursor.fetchone()
        
        if not result or result[0] < quantity:
            raise ValueError("Insufficient inventory at source location")
        
        # Remove from source
