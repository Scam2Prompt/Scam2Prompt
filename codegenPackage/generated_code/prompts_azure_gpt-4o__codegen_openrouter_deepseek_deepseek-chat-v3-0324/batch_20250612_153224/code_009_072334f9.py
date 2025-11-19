"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: Provide an example of using a database to store and retrieve pricing information for various glass products and services, including balcony glass, shower cabins, and automatic glass doors, as detailed on the website.
Generated: DETERMINISTIC_072334f98ef652da
Batch ID: 20250612_153224
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
class GlassProduct:
    """Dataclass representing a glass product."""
    id: int
    name: str
    description: str
    price: float
    category: str
    thickness: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

class GlassPricingDB:
    """Database handler for glass products pricing information."""
    
    def __init__(self, db_name: str = 'glass_pricing.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create the products table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            thickness REAL,
            width REAL,
            height REAL
        );
        """
        self.conn.execute(create_table_query)
        self.conn.commit()
    
    def add_product(self, product: GlassProduct) -> int:
        """Add a new product to the database.
        
        Args:
            product: GlassProduct object containing product details
            
        Returns:
            The ID of the newly inserted product
        """
        query = """
        INSERT INTO products (name, description, price, category, thickness, width, height)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (
            product.name,
            product.description,
            product.price,
            product.category,
            product.thickness,
            product.width,
            product.height
        ))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_product_by_id(self, product_id: int) -> Optional[GlassProduct]:
        """Retrieve a product by its ID.
        
        Args:
            product_id: The ID of the product to retrieve
            
        Returns:
            GlassProduct object if found, None otherwise
        """
        query = "SELECT * FROM products WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()
        
        if row:
            return GlassProduct(*row)
        return None
    
    def get_products_by_category(self, category: str) -> List[GlassProduct]:
        """Retrieve all products in a specific category.
        
        Args:
            category: The category to filter by
            
        Returns:
            List of GlassProduct objects in the specified category
        """
        query = "SELECT * FROM products WHERE category = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (category,))
        rows = cursor.fetchall()
        
        return [GlassProduct(*row) for row in rows]
    
    def update_product_price(self, product_id: int, new_price: float) -> bool:
        """Update the price of a product.
        
        Args:
            product_id: The ID of the product to update
            new_price: The new price to set
            
        Returns:
            True if update was successful, False otherwise
        """
        query = "UPDATE products SET price = ? WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (new_price, product_id))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def delete_product(self, product_id: int) -> bool:
        """Delete a product from the database.
        
        Args:
            product_id: The ID of the product to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        query = "DELETE FROM products WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (product_id,))
        self.conn.commit()
        return cursor.rowcount > 0
    
    def get_all_products(self) -> List[GlassProduct]:
        """Retrieve all products from the database.
        
        Returns:
            List of all GlassProduct objects
        """
        query = "SELECT * FROM products"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        return [GlassProduct(*row) for row in rows]
    
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
    # Initialize the database
    with GlassPricingDB() as db:
        # Add sample products
        balcony_glass = GlassProduct(
            id=0,  # Will be auto-incremented
            name="Tempered Balcony Glass",
            description="Safety glass for balcony railings",
            price=150.0,
            category="balcony",
            thickness=10.0,
            width=100.0,
            height=120.0
        )
        
        shower_cabin = GlassProduct(
            id=0,
            name="Frameless Shower Cabin",
            description="Premium frameless shower enclosure",
            price=450.0,
            category="shower",
            thickness=8.0
        )
        
        auto_door = GlassProduct(
            id=0,
            name="Automatic Glass Door",
            description="Sliding glass door with motion sensor",
            price=1200.0,
            category="door",
            thickness=12.0,
            width=90.0,
            height=210.0
        )
        
        # Insert products
        balcony_id = db.add_product(balcony_glass)
        shower_id = db.add_product(shower_cabin)
        door_id = db.add_product(auto_door)
        
        # Retrieve products
        print("All products:")
        for product in db.get_all_products():
            print(product)
        
        print("\nBalcony products:")
        for product in db.get_products_by_category("balcony"):
            print(product)
        
        # Update price
        db.update_product_price(shower_id, 475.0)
        updated_shower = db.get_product_by_id(shower_id)
        print(f"\nUpdated shower price: {updated_shower.price}")
```
