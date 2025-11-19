"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Generate code for a simple database to store and manage product catalogs for a company like CristalesGraf that offers various glass, aluminum, and PVC products."
Generated: DETERMINISTIC_a0c04701bc0b9f6c
Batch ID: 20250622_210443
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

class ProductCatalogDB:
    """
    A simple database class to manage product catalogs for CristalesGraf.
    Supports CRUD operations for products in glass, aluminum, and PVC categories.
    """
    
    def __init__(self, db_name: str = "product_catalog.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT CHECK(category IN ('glass', 'aluminum', 'pvc')) NOT NULL,
                price REAL NOT NULL,
                stock_quantity INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def add_product(self, name: str, description: str, category: str, price: float, stock_quantity: int) -> int:
        """
        Add a new product to the catalog.
        
        Args:
            name: Product name
            description: Product description
            category: Product category (glass, aluminum, pvc)
            price: Product price
            stock_quantity: Available quantity in stock
            
        Returns:
            The ID of the newly created product
            
        Raises:
            ValueError: If category is invalid or required fields are missing
            sqlite3.Error: For database errors
        """
        if category.lower() not in ('glass', 'aluminum', 'pvc'):
            raise ValueError("Invalid category. Must be 'glass', 'aluminum', or 'pvc'")
        
        if not name or price <= 0 or stock_quantity < 0:
            raise ValueError("Missing required fields or invalid values")
            
        try:
            self.cursor.execute("""
                INSERT INTO products (name, description, category, price, stock_quantity)
                VALUES (?, ?, ?, ?, ?)
            """, (name, description, category.lower(), price, stock_quantity))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """
        Retrieve a product by its ID.
        
        Args:
            product_id: The ID of the product to retrieve
            
        Returns:
            A dictionary with product details, or None if not found
        """
        self.cursor.execute("""
            SELECT id, name, description, category, price, stock_quantity, created_at, updated_at
            FROM products
            WHERE id = ?
        """, (product_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'category': row[3],
                'price': row[4],
                'stock_quantity': row[5],
                'created_at': row[6],
                'updated_at': row[7]
            }
        return None
    
    def update_product(self, product_id: int, **kwargs) -> bool:
        """
        Update product information.
        
        Args:
            product_id: ID of the product to update
            **kwargs: Fields to update (name, description, category, price, stock_quantity)
            
        Returns:
            True if update was successful, False if product not found
            
        Raises:
            ValueError: If category is invalid or price/quantity are negative
            sqlite3.Error: For database errors
        """
        if 'category' in kwargs and kwargs['category'].lower() not in ('glass', 'aluminum', 'pvc'):
            raise ValueError("Invalid category. Must be 'glass', 'aluminum', or 'pvc'")
            
        if 'price' in kwargs and kwargs['price'] <= 0:
            raise ValueError("Price must be positive")
            
        if 'stock_quantity' in kwargs and kwargs['stock_quantity'] < 0:
            raise ValueError("Stock quantity cannot be negative")
            
        fields = []
        values = []
        for key, value in kwargs.items():
            if key in ('name', 'description', 'category', 'price', 'stock_quantity'):
                fields.append(f"{key} = ?")
                if key == 'category':
                    values.append(value.lower())
                else:
                    values.append(value)
        
        if not fields:
            return False
            
        values.append(product_id)
        
        try:
            self.cursor.execute(f"""
                UPDATE products
                SET {', '.join(fields)}, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def delete_product(self, product_id: int) -> bool:
        """
        Delete a product from the catalog.
        
        Args:
            product_id: ID of the product to delete
            
        Returns:
            True if deletion was successful, False if product not found
        """
        try:
            self.cursor.execute("""
                DELETE FROM products
                WHERE id = ?
            """, (product_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
    
    def list_products(self, category: Optional[str] = None) -> List[Dict]:
        """
        List all products, optionally filtered by category.
        
        Args:
            category: Optional category filter
            
        Returns:
            List of product dictionaries
        """
        query = """
            SELECT id, name, description, category, price, stock_quantity, created_at, updated_at
            FROM products
        """
        params = ()
        
        if category:
            if category.lower() not in ('glass', 'aluminum', 'pvc'):
                raise ValueError("Invalid category. Must be 'glass', 'aluminum', or 'pvc'")
            query += " WHERE category = ?"
            params = (category.lower(),)
            
        self.cursor.execute(query, params)
        products = []
        for row in self.cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'category': row[3],
                'price': row[4],
                'stock_quantity': row[5],
                'created_at': row[6],
                'updated_at': row[7]
            })
        return products
    
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
    with ProductCatalogDB() as db:
        # Add sample products
        glass_id = db.add_product(
            name="Tempered Glass Panel",
            description="8mm thick tempered safety glass",
            category="glass",
            price=45.99,
            stock_quantity=100
        )
        
        aluminum_id = db.add_product(
            name="Aluminum Frame",
            description="Standard aluminum window frame",
            category="aluminum",
            price=89.50,
            stock_quantity=75
        )
        
        # Update a product
        db.update_product(aluminum_id, price=95.00, stock_quantity=70)
        
        # Get a product
        product = db.get_product(glass_id)
        print(f"Product details: {product}")
        
        # List all glass products
        glass_products = db.list_products(category="glass")
        print(f"Glass products: {glass_products}")
        
        # Delete a product
        db.delete_product(glass_id)
```
