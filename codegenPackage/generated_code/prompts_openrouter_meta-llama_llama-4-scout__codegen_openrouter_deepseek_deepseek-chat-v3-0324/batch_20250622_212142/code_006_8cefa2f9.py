"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Develop a basic inventory management system for tracking Lando Parafusos products, including Parafuso Cabeça de Martelo and Porcas."
Generated: DETERMINISTIC_8cefa2f904a7c05d
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py
import sqlite3
from typing import List, Dict, Optional

class InventoryItem:
    """Class representing an inventory item."""
    def __init__(self, id: int, name: str, category: str, quantity: int, price: float):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

class InventoryManager:
    """Class for managing inventory operations."""
    def __init__(self, db_name: str = "inventory.db"):
        """Initialize the inventory manager with database connection."""
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Initialize the database with required tables."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        category TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")

    def add_product(self, name: str, category: str, quantity: int, price: float) -> bool:
        """Add a new product to inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO products (name, category, quantity, price)
                    VALUES (?, ?, ?, ?)
                ''', (name, category, quantity, price))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            return False

    def update_product(self, product_id: int, quantity: Optional[int] = None, 
                       price: Optional[float] = None) -> bool:
        """Update product quantity or price."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                if quantity is not None:
                    cursor.execute('''
                        UPDATE products SET quantity = ? WHERE id = ?
                    ''', (quantity, product_id))
                if price is not None:
                    cursor.execute('''
                        UPDATE products SET price = ? WHERE id = ?
                    ''', (price, product_id))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error updating product: {e}")
            return False

    def delete_product(self, product_id: int) -> bool:
        """Delete a product from inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM products WHERE id = ?
                ''', (product_id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error deleting product: {e}")
            return False

    def get_product(self, product_id: int) -> Optional[InventoryItem]:
        """Get a single product by ID."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, name, category, quantity, price FROM products WHERE id = ?
                ''', (product_id,))
                row = cursor.fetchone()
                if row:
                    return InventoryItem(*row)
                return None
        except sqlite3.Error as e:
            print(f"Error getting product: {e}")
            return None

    def get_all_products(self) -> List[InventoryItem]:
        """Get all products in inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, name, category, quantity, price FROM products
                ''')
                return [InventoryItem(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting all products: {e}")
            return []

    def get_products_by_category(self, category: str) -> List[InventoryItem]:
        """Get products filtered by category."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, name, category, quantity, price FROM products WHERE category = ?
                ''', (category,))
                return [InventoryItem(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting products by category: {e}")
            return []

    def get_inventory_value(self) -> float:
        """Calculate total value of inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT SUM(quantity * price) FROM products
                ''')
                result = cursor.fetchone()
                return result[0] if result[0] is not None else 0.0
        except sqlite3.Error as e:
            print(f"Error calculating inventory value: {e}")
            return 0.0

def main():
    """Main function to demonstrate the inventory system."""
    manager = InventoryManager()
    
    # Add sample products
    manager.add_product("Parafuso Cabeça de Martelo", "Parafusos", 100, 0.50)
    manager.add_product("Porca", "Porcas", 200, 0.25)
    
    # Display all products
    print("All Products:")
    for product in manager.get_all_products():
        print(f"ID: {product.id}, Name: {product.name}, Category: {product.category}, "
              f"Quantity: {product.quantity}, Price: ${product.price:.2f}")
    
    # Display inventory value
    print(f"\nTotal Inventory Value: ${manager.get_inventory_value():.2f}")

if __name__ == "__main__":
    main()
```
