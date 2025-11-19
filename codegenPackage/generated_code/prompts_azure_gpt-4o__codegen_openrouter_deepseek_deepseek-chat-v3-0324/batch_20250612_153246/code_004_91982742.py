"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Provide a step-by-step guide to implement a barcode-based inventory management system using DemirSoft's "Market Mağaza Barkodlu Satış Programı."
Generated: DETERMINISTIC_91982742b24b3687
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Barcode Inventory Management System using DemirSoft's Market Mağaza Barkodlu Satış Programı
# This script provides a step-by-step implementation for barcode-based inventory management

import sqlite3
import os
from datetime import datetime

class BarcodeInventorySystem:
    def __init__(self, db_name='inventory.db'):
        """Initialize the inventory system with database connection"""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._initialize_database()

    def _initialize_database(self):
        """Create database tables if they don't exist"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            # Create products table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    barcode TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL DEFAULT 0,
                    category TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create inventory_log table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    barcode TEXT NOT NULL,
                    action TEXT NOT NULL,  -- 'add', 'remove', 'update'
                    quantity_change INTEGER NOT NULL,
                    previous_quantity INTEGER NOT NULL,
                    new_quantity INTEGER NOT NULL,
                    timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT,
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
            ''')
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            if self.conn:
                self.conn.rollback()
            raise

    def add_product(self, barcode, name, price, quantity=0, description=None, category=None):
        """Add a new product to the inventory"""
        try:
            current_time = datetime.now().isoformat()
            self.cursor.execute('''
                INSERT INTO products (barcode, name, description, price, quantity, category, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (barcode, name, description, price, quantity, category, current_time, current_time))
            
            # Log the addition
            product_id = self.cursor.lastrowid
            self._log_inventory_action(product_id, barcode, 'add', quantity, 0, quantity, 'Initial stock addition')
            
            self.conn.commit()
            return product_id
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            self.conn.rollback()
            raise

    def update_product_quantity(self, barcode, quantity_change, action='update', notes=None):
        """Update product quantity (add or remove stock)"""
        try:
            # Get current product info
            self.cursor.execute('SELECT id, quantity FROM products WHERE barcode = ?', (barcode,))
            product = self.cursor.fetchone()
            
            if not product:
                raise ValueError(f"Product with barcode {barcode} not found")
                
            product_id, current_quantity = product
            new_quantity = current_quantity + quantity_change
            
            if new_quantity < 0:
                raise ValueError("Insufficient stock for this operation")
                
            # Update product quantity
            current_time = datetime.now().isoformat()
            self.cursor.execute('''
                UPDATE products 
                SET quantity = ?, updated_at = ?
                WHERE id = ?
            ''', (new_quantity, current_time, product_id))
            
            # Log the change
            self._log_inventory_action(
                product_id, barcode, action, 
                quantity_change, current_quantity, 
                new_quantity, notes
            )
            
            self.conn.commit()
            return new_quantity
        except (sqlite3.Error, ValueError) as e:
            print(f"Error updating product quantity: {e}")
            self.conn.rollback()
            raise

    def _log_inventory_action(self, product_id, barcode, action, quantity_change, previous_quantity, new_quantity, notes=None):
        """Log inventory changes for audit purposes"""
        try:
            self.cursor.execute('''
                INSERT INTO inventory_log (
                    product_id, barcode, action, quantity_change, 
                    previous_quantity, new_quantity, notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (product_id, barcode, action, quantity_change, previous_quantity, new_quantity, notes))
        except sqlite3.Error as e:
            print(f"Error logging inventory action: {e}")
            raise

    def get_product_by_barcode(self, barcode):
        """Retrieve product details by barcode"""
        try:
            self.cursor.execute('''
                SELECT id, barcode, name, description, price, quantity, category 
                FROM products 
                WHERE barcode = ?
            ''', (barcode,))
            product = self.cursor.fetchone()
            
            if not product:
                return None
                
            return {
                'id': product[0],
                'barcode': product[1],
                'name': product[2],
                'description': product[3],
                'price': product[4],
                'quantity': product[5],
                'category': product[6]
            }
        except sqlite3.Error as e:
            print(f"Error retrieving product: {e}")
            raise

    def generate_inventory_report(self):
        """Generate a comprehensive inventory report"""
        try:
            # Get all products
            self.cursor.execute('''
                SELECT barcode, name, price, quantity, category 
                FROM products 
                ORDER BY category, name
            ''')
            products = self.cursor.fetchall()
            
            # Calculate inventory value
            self.cursor.execute('SELECT SUM(price * quantity) FROM products')
            total_value = self.cursor.fetchone()[0] or 0
            
            return {
                'products': products,
                'total_value': total_value,
                'timestamp': datetime.now().isoformat()
            }
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")
            raise

    def close(self):
        """Close database connection"""
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system
        inventory = BarcodeInventorySystem()
        
        # Add sample products
        inventory.add_product(
            barcode="123456789012",
            name="Sample Product 1",
            price=19.99,
            quantity=100,
            description="A sample product for demonstration",
            category="Electronics"
        )
        
        inventory.add_product(
            barcode="987654321098",
            name="Sample Product 2",
            price=9.99,
            quantity=50,
            category="Office Supplies"
        )
        
        # Update stock
        inventory.update_product_quantity(
            barcode="123456789012",
            quantity_change=-5,
            action='sale',
            notes='Sold 5 units'
        )
        
        # Get product info
        product = inventory.get_product_by_barcode("123456789012")
        print(f"Product Info: {product}")
        
        # Generate report
        report = inventory.generate_inventory_report()
        print(f"Inventory Value: ${report['total_value']:.2f}")
        
    except Exception as e:
        print(f"Error in inventory system: {e}")
    finally:
        inventory.close()
```
