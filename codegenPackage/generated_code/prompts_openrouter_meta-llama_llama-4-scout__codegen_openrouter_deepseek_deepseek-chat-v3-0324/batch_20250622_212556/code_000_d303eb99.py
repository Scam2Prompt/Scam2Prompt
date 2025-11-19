"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: "Write a Python code snippet to create a simple database for managing inventory of spiritual products like 3D energy globes and aura scanners."
Generated: DETERMINISTIC_d303eb99469cbba5
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class InventoryManager:
    """
    A simple inventory management system for spiritual products.
    Handles CRUD operations for products in an SQLite database.
    """
    
    def __init__(self, db_name: str = "spiritual_inventory.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the products table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def add_product(self, name: str, price: float, quantity: int, 
                   description: Optional[str] = None, 
                   category: Optional[str] = None) -> int:
        """
        Add a new product to the inventory.
        Returns the ID of the newly created product.
        """
        try:
            self.cursor.execute("""
                INSERT INTO products (name, description, category, price, quantity)
                VALUES (?, ?, ?, ?, ?)
            """, (name, description, category, price, quantity))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding product: {e}")
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """
        Retrieve a product by its ID.
        Returns None if product not found.
        """
        self.cursor.execute("""
            SELECT id, name, description, category, price, quantity, created_at
            FROM products WHERE id = ?
        """, (product_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "category": row[3],
                "price": row[4],
                "quantity": row[5],
                "created_at": row[6]
            }
        return None
    
    def update_product(self, product_id: int, **kwargs) -> bool:
        """
        Update product details. Accepts any of these fields:
        name, description, category, price, quantity.
        Returns True if update was successful, False otherwise.
        """
        valid_fields = {"name", "description", "category", "price", "quantity"}
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            return False
        
        set_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        values = list(updates.values())
        values.append(product_id)
        
        try:
            self.cursor.execute(f"""
                UPDATE products SET {set_clause} WHERE id = ?
            """, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error updating product: {e}")
    
    def delete_product(self, product_id: int) -> bool:
        """
        Delete a product from the inventory.
        Returns True if deletion was successful, False otherwise.
        """
        try:
            self.cursor.execute("""
                DELETE FROM products WHERE id = ?
            """, (product_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error deleting product: {e}")
    
    def list_products(self, category: Optional[str] = None) -> List[Dict]:
        """
        List all products, optionally filtered by category.
        """
        query = """
            SELECT id, name, description, category, price, quantity, created_at
            FROM products
        """
        params = ()
        
        if category:
            query += " WHERE category = ?"
            params = (category,)
        
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        
        return [{
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "category": row[3],
            "price": row[4],
            "quantity": row[5],
            "created_at": row[6]
        } for row in rows]
    
    def update_quantity(self, product_id: int, change: int) -> bool:
        """
        Update product quantity by adding/subtracting the change value.
        Returns True if update was successful, False otherwise.
        """
        try:
            self.cursor.execute("""
                UPDATE products 
                SET quantity = quantity + ? 
                WHERE id = ?
            """, (change, product_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error updating quantity: {e}")
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()

# Example usage
if __name__ == "__main__":
    with InventoryManager() as manager:
        # Add sample products
        globe_id = manager.add_product(
            name="3D Energy Globe",
            description="Harmonizes energy in your space",
            category="Energy Tools",
            price=49.99,
            quantity=10
        )
        
        scanner_id = manager.add_product(
            name="Aura Scanner Pro",
            description="Detects and visualizes aura energy",
            category="Diagnostic Tools",
            price=199.99,
            quantity=5
        )
        
        # List all products
        print("All Products:")
        for product in manager.list_products():
            print(product)
        
        # Update quantity
        manager.update_quantity(globe_id, -2)  # Sell 2 globes
        
        # Get updated product
        globe = manager.get_product(globe_id)
        print(f"\nUpdated Globe Quantity: {globe['quantity']}")
```
