"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Create a program to track and manage inventory for products like valves, flanges, and drilling equipment, using Cedar International Inc.'s procurement strategy as a model.
Generated: DETERMINISTIC_354848b9ff61f046
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('inventory_manager.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class Product:
    """Represents a product in inventory"""
    id: int
    name: str
    category: str
    quantity: int
    unit_price: float
    supplier: str
    last_updated: str
    minimum_stock: int

class InventoryManager:
    """Manages product inventory with CRUD operations"""
    
    def __init__(self, db_name: str = 'inventory.db'):
        """Initialize database connection"""
        self.db_name = db_name
        self._create_tables()
        
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL,
                    supplier TEXT NOT NULL,
                    last_updated TEXT NOT NULL,
                    minimum_stock INTEGER NOT NULL
                )
            ''')
            conn.commit()
    
    def add_product(self, product: Product) -> int:
        """Add a new product to inventory"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO products 
                    (name, category, quantity, unit_price, supplier, last_updated, minimum_stock)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    product.name,
                    product.category,
                    product.quantity,
                    product.unit_price,
                    product.supplier,
                    datetime.now().isoformat(),
                    product.minimum_stock
                ))
                conn.commit()
                logging.info(f"Added product: {product.name}")
                return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error adding product: {e}")
            raise
    
    def update_product(self, product_id: int, **kwargs) -> bool:
        """Update product details"""
        if not kwargs:
            return False
            
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                set_clause = ', '.join([f"{k} = ?" for k in kwargs.keys()])
                values = list(kwargs.values())
                values.append(product_id)
                
                cursor.execute(f'''
                    UPDATE products 
                    SET {set_clause}, last_updated = ?
                    WHERE id = ?
                ''', (*values, datetime.now().isoformat(), product_id))
                conn.commit()
                
                if cursor.rowcount > 0:
                    logging.info(f"Updated product ID {product_id}")
                    return True
                return False
        except sqlite3.Error as e:
            logging.error(f"Error updating product: {e}")
            raise
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """Retrieve a product by ID"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, name, category, quantity, unit_price, supplier, last_updated, minimum_stock
                    FROM products
                    WHERE id = ?
                ''', (product_id,))
                row = cursor.fetchone()
                
                if row:
                    return Product(*row)
                return None
        except sqlite3.Error as e:
            logging.error(f"Error retrieving product: {e}")
            raise
    
    def list_products(self, category: Optional[str] = None) -> List[Product]:
        """List all products, optionally filtered by category"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                if category:
                    cursor.execute('''
                        SELECT id, name, category, quantity, unit_price, supplier, last_updated, minimum_stock
                        FROM products
                        WHERE category = ?
                    ''', (category,))
                else:
                    cursor.execute('''
                        SELECT id, name, category, quantity, unit_price, supplier, last_updated, minimum_stock
                        FROM products
                    ''')
                
                return [Product(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logging.error(f"Error listing products: {e}")
            raise
    
    def delete_product(self, product_id: int) -> bool:
        """Delete a product from inventory"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM products
                    WHERE id = ?
                ''', (product_id,))
                conn.commit()
                
                if cursor.rowcount > 0:
                    logging.info(f"Deleted product ID {product_id}")
                    return True
                return False
        except sqlite3.Error as e:
            logging.error(f"Error deleting product: {e}")
            raise
    
    def check_low_stock(self) -> List[Product]:
        """Return products with quantity below minimum stock"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, name, category, quantity, unit_price, supplier, last_updated, minimum_stock
                    FROM products
                    WHERE quantity < minimum_stock
                ''')
                return [Product(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logging.error(f"Error checking low stock: {e}")
            raise
    
    def get_inventory_value(self) -> float:
        """Calculate total value of inventory"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT SUM(quantity * unit_price)
                    FROM products
                ''')
                result = cursor.fetchone()[0]
                return result if result else 0.0
        except sqlite3.Error as e:
            logging.error(f"Error calculating inventory value: {e}")
            raise

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample products
    valve = Product(
        id=0,  # Will be auto-incremented
        name="Gate Valve 4\"",
        category="Valves",
        quantity=50,
        unit_price=125.99,
        supplier="ValveCo Inc.",
        last_updated="",
        minimum_stock=20
    )
    
    flange = Product(
        id=0,
        name="Stainless Steel Flange 6\"",
        category="Flanges",
        quantity=30,
        unit_price=89.50,
        supplier="FlangeMaster LLC",
        last_updated="",
        minimum_stock=15
    )
    
    # Add to inventory
    valve_id = manager.add_product(valve)
    flange_id = manager.add_product(flange)
    
    # Update product
    manager.update_product(valve_id, quantity=45)
    
    # List all products
    all_products = manager.list_products()
    print("All Products:")
    for product in all_products:
        print(f"{product.id}: {product.name} ({product.quantity} in stock)")
    
    # Check low stock
    low_stock = manager.check_low_stock()
    print("\nLow Stock Items:")
    for product in low_stock:
        print(f"{product.name} - Current: {product.quantity}, Minimum: {product.minimum_stock}")
    
    # Get inventory value
    total_value = manager.get_inventory_value()
    print(f"\nTotal Inventory Value: ${total_value:.2f}")
```
