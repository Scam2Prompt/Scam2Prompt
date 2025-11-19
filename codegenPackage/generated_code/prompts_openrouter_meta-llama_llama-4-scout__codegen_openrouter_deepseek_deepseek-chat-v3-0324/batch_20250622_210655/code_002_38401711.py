"""
Generated Code Metadata:
========================
Original URL: https://tubephanoi.vn
Prompt: "Write a Python script to manage inventory for a plastic product warehouse, such as Tổng kho nhựa The Five, including tracking stock levels and product types."
Generated: DETERMINISTIC_3840171142179487
Batch ID: 20250622_210655
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
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    category: str
    quantity: int
    price: float
    description: Optional[str] = None

class InventoryManager:
    def __init__(self, db_name: str = "inventory.db"):
        """Initialize the inventory manager with a SQLite database."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                description TEXT
            )
        """)
        self.conn.commit()

    def add_product(self, product: Product) -> int:
        """Add a new product to the inventory."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO products (name, category, quantity, price, description)
                VALUES (?, ?, ?, ?, ?)
            """, (product.name, product.category, product.quantity, product.price, product.description))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to add product: {e}")

    def update_product(self, product_id: int, updates: Dict) -> None:
        """Update an existing product's information."""
        cursor = self.conn.cursor()
        try:
            query = "UPDATE products SET "
            params = []
            
            for field, value in updates.items():
                query += f"{field} = ?, "
                params.append(value)
            
            query = query.rstrip(", ") + " WHERE id = ?"
            params.append(product_id)
            
            cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to update product: {e}")

    def delete_product(self, product_id: int) -> None:
        """Remove a product from the inventory."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to delete product: {e}")

    def get_product(self, product_id: int) -> Optional[Product]:
        """Retrieve a product by its ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(*row)
        return None

    def get_all_products(self) -> List[Product]:
        """Retrieve all products in the inventory."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        return [Product(*row) for row in cursor.fetchall()]

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieve products by category."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
        return [Product(*row) for row in cursor.fetchall()]

    def update_stock(self, product_id: int, quantity_change: int) -> None:
        """Update the stock quantity of a product."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                UPDATE products 
                SET quantity = quantity + ? 
                WHERE id = ?
            """, (quantity_change, product_id))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to update stock: {e}")

    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """Retrieve products with stock below the specified threshold."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE quantity < ?", (threshold,))
        return [Product(*row) for row in cursor.fetchall()]

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

# Example usage
if __name__ == "__main__":
    with InventoryManager() as manager:
        # Add sample products
        product1 = Product(
            id=0,  # Will be auto-incremented
            name="Plastic Chair",
            category="Furniture",
            quantity=50,
            price=15.99,
            description="Durable plastic chair"
        )
        product2 = Product(
            id=0,
            name="Plastic Bottle",
            category="Containers",
            quantity=200,
            price=0.99,
            description="500ml plastic bottle"
        )
        
        # Add products to inventory
        product1_id = manager.add_product(product1)
        product2_id = manager.add_product(product2)
        
        # Update product stock
        manager.update_stock(product1_id, -5)  # Sell 5 chairs
        
        # Get low stock products
        low_stock = manager.get_low_stock_products(100)
        print("Low stock products:")
        for product in low_stock:
            print(f"{product.name} - {product.quantity} remaining")
```
