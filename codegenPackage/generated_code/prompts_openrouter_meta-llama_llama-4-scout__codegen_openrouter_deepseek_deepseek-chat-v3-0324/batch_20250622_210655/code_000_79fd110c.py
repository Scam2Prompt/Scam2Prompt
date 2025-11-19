"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: "Write a Python script to manage an online store's inventory for Airsoft products, including tracking stock levels for items like Velcros Casco Balístico and Sudadera «GLITCH»."
Generated: DETERMINISTIC_79fd110c3cafcf3f
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
from typing import Dict, List, Optional, Tuple

class InventoryManager:
    """A class to manage an online store's inventory for Airsoft products."""
    
    def __init__(self, db_name: str = "inventory.db"):
        """Initialize the inventory manager with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL DEFAULT 0,
                    category TEXT,
                    sku TEXT UNIQUE
                )
            """)
            conn.commit()
    
    def add_product(self, name: str, price: float, stock: int, 
                   description: str = "", category: str = "", sku: str = "") -> bool:
        """Add a new product to the inventory.
        
        Args:
            name: Product name.
            price: Product price.
            stock: Initial stock quantity.
            description: Product description (optional).
            category: Product category (optional).
            sku: Stock keeping unit (optional).
            
        Returns:
            True if product was added successfully, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO products (name, description, price, stock, category, sku)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, description, price, stock, category, sku))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def update_stock(self, product_id: int, quantity: int) -> bool:
        """Update the stock quantity for a product.
        
        Args:
            product_id: ID of the product to update.
            quantity: New stock quantity (can be positive or negative for adjustments).
            
        Returns:
            True if stock was updated successfully, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE products 
                    SET stock = stock + ?
                    WHERE id = ?
                """, (quantity, product_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """Get product details by ID.
        
        Args:
            product_id: ID of the product to retrieve.
            
        Returns:
            Dictionary with product details or None if not found.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM products WHERE id = ?
                """, (product_id,))
                product = cursor.fetchone()
                return dict(product) if product else None
        except sqlite3.Error:
            return None
    
    def get_all_products(self) -> List[Dict]:
        """Get all products in the inventory.
        
        Returns:
            List of dictionaries with product details.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products")
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error:
            return []
    
    def search_products(self, search_term: str) -> List[Dict]:
        """Search for products by name or description.
        
        Args:
            search_term: Term to search for in product names and descriptions.
            
        Returns:
            List of dictionaries with matching products.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM products 
                    WHERE name LIKE ? OR description LIKE ?
                """, (f"%{search_term}%", f"%{search_term}%"))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error:
            return []
    
    def delete_product(self, product_id: int) -> bool:
        """Delete a product from the inventory.
        
        Args:
            product_id: ID of the product to delete.
            
        Returns:
            True if product was deleted successfully, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM products WHERE id = ?
                """, (product_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error:
            return False
    
    def get_low_stock_products(self, threshold: int = 5) -> List[Dict]:
        """Get products with stock levels below a threshold.
        
        Args:
            threshold: Minimum stock level threshold.
            
        Returns:
            List of dictionaries with low stock products.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM products WHERE stock < ?
                """, (threshold,))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error:
            return []


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample products
    manager.add_product(
        name="Velcros Casco Balístico",
        description="High-quality ballistic helmet with velcro attachments",
        price=149.99,
        stock=10,
        category="Helmets",
        sku="HELM-VEL-001"
    )
    
    manager.add_product(
        name="Sudadera «GLITCH»",
        description="Tactical hoodie with digital glitch pattern",
        price=59.99,
        stock=25,
        category="Clothing",
        sku="CLOTH-GLT-001"
    )
    
    # Display all products
    print("Current Inventory:")
    for product in manager.get_all_products():
        print(f"{product['id']}: {product['name']} - ${product['price']} ({product['stock']} in stock)")
    
    # Update stock
    manager.update_stock(1, -2)  # Sell 2 helmets
    manager.update_stock(2, 5)   # Add 5 hoodies
    
    # Check low stock
    print("\nLow Stock Items:")
    for product in manager.get_low_stock_products(10):
        print(f"{product['name']} is low on stock ({product['stock']} remaining)")
```
