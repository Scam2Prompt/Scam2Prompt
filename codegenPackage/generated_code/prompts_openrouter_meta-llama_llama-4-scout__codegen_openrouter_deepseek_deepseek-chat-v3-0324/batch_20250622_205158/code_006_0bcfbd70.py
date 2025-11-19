"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Develop a supply chain management system for PDC Brush, taking into account their commitment to sustainable practices and responsible sourcing.
Generated: DETERMINISTIC_0bcfbd702fee93a4
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_management.py

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class SupplyChainManager:
    """
    A supply chain management system for PDC Brush with sustainable practices tracking.
    """
    
    def __init__(self, db_name: str = "pdc_brush_supply_chain.db"):
        """
        Initialize the supply chain manager with a database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary database tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        # Suppliers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_email TEXT NOT NULL,
            phone TEXT,
            address TEXT,
            sustainability_rating INTEGER CHECK(sustainability_rating BETWEEN 1 AND 5),
            certification TEXT,
            last_audit_date TEXT,
            is_active BOOLEAN DEFAULT 1
        )
        """)
        
        # Materials table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            material_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            unit TEXT NOT NULL,
            carbon_footprint REAL,
            is_recyclable BOOLEAN,
            is_biodegradable BOOLEAN,
            renewable_percentage REAL
        )
        """)
        
        # Supplier Materials relationship
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS supplier_materials (
            supplier_id INTEGER,
            material_id INTEGER,
            price_per_unit REAL NOT NULL,
            lead_time_days INTEGER NOT NULL,
            minimum_order_quantity INTEGER NOT NULL,
            PRIMARY KEY (supplier_id, material_id),
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
            FOREIGN KEY (material_id) REFERENCES materials(material_id)
        )
        """)
        
        # Orders table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            expected_delivery_date TEXT,
            actual_delivery_date TEXT,
            status TEXT CHECK(status IN ('pending', 'shipped', 'delivered', 'cancelled')),
            total_cost REAL NOT NULL,
            sustainability_score REAL,
            notes TEXT,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        )
        """)
        
        # Order Items table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            material_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (material_id) REFERENCES materials(material_id)
        )
        """)
        
        # Inventory table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            last_updated TEXT NOT NULL,
            location TEXT,
            batch_number TEXT,
            FOREIGN KEY (material_id) REFERENCES materials(material_id)
        )
        """)
        
        self.conn.commit()
    
    def add_supplier(
        self,
        name: str,
        contact_email: str,
        phone: str,
        address: str,
        sustainability_rating: int,
        certification: str,
        last_audit_date: str
    ) -> int:
        """
        Add a new supplier to the database.
        
        Args:
            name: Supplier name
            contact_email: Contact email
            phone: Contact phone
            address: Physical address
            sustainability_rating: Rating from 1-5
            certification: Sustainability certifications
            last_audit_date: Date of last sustainability audit (YYYY-MM-DD)
            
        Returns:
            The ID of the newly added supplier
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO suppliers (
                name, contact_email, phone, address, 
                sustainability_rating, certification, last_audit_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, contact_email, phone, address, 
                 sustainability_rating, certification, last_audit_date))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add supplier: {str(e)}")
    
    def add_material(
        self,
        name: str,
        description: str,
        unit: str,
        carbon_footprint: float,
        is_recyclable: bool,
        is_biodegradable: bool,
        renewable_percentage: float
    ) -> int:
        """
        Add a new material to the database.
        
        Args:
            name: Material name
            description: Description of the material
            unit: Measurement unit (kg, liter, etc.)
            carbon_footprint: Carbon footprint per unit
            is_recyclable: Whether the material is recyclable
            is_biodegradable: Whether the material is biodegradable
            renewable_percentage: Percentage of renewable content
            
        Returns:
            The ID of the newly added material
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO materials (
                name, description, unit, carbon_footprint,
                is_recyclable, is_biodegradable, renewable_percentage
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, description, unit, carbon_footprint,
                 is_recyclable, is_biodegradable, renewable_percentage))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add material: {str(e)}")
    
    def add_supplier_material(
        self,
        supplier_id: int,
        material_id: int,
        price_per_unit: float,
        lead_time_days: int,
        minimum_order_quantity: int
    ) -> None:
        """
        Link a supplier to a material they provide.
        
        Args:
            supplier_id: ID of the supplier
            material_id: ID of the material
            price_per_unit: Price per unit of material
            lead_time_days: Days needed for delivery
            minimum_order_quantity: Minimum order quantity
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO supplier_materials (
                supplier_id, material_id, price_per_unit, 
                lead_time_days, minimum_order_quantity
            ) VALUES (?, ?, ?, ?, ?)
            """, (supplier_id, material_id, price_per_unit, 
                 lead_time_days, minimum_order_quantity))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add supplier material: {str(e)}")
    
    def create_order(
        self,
        supplier_id: int,
        order_date: str,
        expected_delivery_date: str,
        items: List[Dict[str, float]],
        notes: str = ""
    ) -> int:
        """
        Create a new purchase order.
        
        Args:
            supplier_id: ID of the supplier
            order_date: Date of order (YYYY-MM-DD)
            expected_delivery_date: Expected delivery date (YYYY-MM-DD)
            items: List of dictionaries with material_id and quantity
            notes: Optional order notes
            
        Returns:
            The ID of the newly created order
        """
        try:
            cursor = self.conn.cursor()
            
            # Calculate total cost and sustainability score
            total_cost = 0.0
            sustainability_score = 0.0
            total_items = 0
            
            for item in items:
                cursor.execute("""
                SELECT sm.price_per_unit, m.carbon_footprint, m.renewable_percentage
                FROM supplier_materials sm
                JOIN materials m ON sm.material_id = m.material_id
                WHERE sm.supplier_id = ? AND sm.material_id = ?
                """, (supplier_id, item['material_id']))
                
                result = cursor.fetchone()
                if not result:
                    raise Exception(f"Supplier doesn't provide material ID {item['material_id']}")
                
                price_per_unit, carbon_footprint, renewable_percentage = result
                total_cost += price_per_unit * item['quantity']
                sustainability_score += (renewable_percentage - carbon_footprint) * item['quantity']
                total_items += item['quantity']
            
            if total_items > 0:
                sustainability_score /= total_items
            
            # Create the order
            cursor.execute("""
            INSERT INTO orders (
                supplier_id, order_date, expected_delivery_date,
                status, total_cost, sustainability_score, notes
            ) VALUES (?, ?, ?, 'pending', ?, ?, ?)
