"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Describe a system to track and manage inventory for a cosmetics store, including products like ENZO-ORGANIC shampoo and GOLDWELL hair paste.
Generated: DETERMINISTIC_861775e381ed6f07
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py
import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Product:
    """Dataclass representing a cosmetic product."""
    id: int
    name: str
    brand: str
    category: str
    quantity: int
    price: float
    threshold: int

class InventoryManager:
    """Class to manage cosmetic inventory operations."""
    
    def __init__(self, db_name: str = "cosmetics_inventory.db"):
        """Initialize the inventory manager with database connection."""
        self.db_name = db_name
        self._create_tables()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Establish and return a database connection."""
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        brand TEXT NOT NULL,
                        category TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL,
                        threshold INTEGER NOT NULL,
                        UNIQUE(name, brand)
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Table creation error: {e}")
            raise
    
    def add_product(self, product: Product) -> int:
        """Add a new product to inventory."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO products (name, brand, category, quantity, price, threshold)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (product.name, product.brand, product.category, 
                      product.quantity, product.price, product.threshold))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            logger.warning(f"Product {product.name} from {product.brand} already exists")
            raise ValueError("Product already exists in inventory")
        except sqlite3.Error as e:
            logger.error(f"Error adding product: {e}")
            raise
    
    def update_product(self, product_id: int, updates: Dict[str, object]) -> None:
        """Update product information."""
        if not updates:
            return
            
        set_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        values = list(updates.values())
        values.append(product_id)
        
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(f"""
                    UPDATE products 
                    SET {set_clause}
                    WHERE id = ?
                """, values)
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error updating product: {e}")
            raise
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """Retrieve a product by ID."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM products WHERE id = ?
                """, (product_id,))
                row = cursor.fetchone()
                return Product(**row) if row else None
        except sqlite3.Error as e:
            logger.error(f"Error fetching product: {e}")
            raise
    
    def get_all_products(self) -> List[Product]:
        """Retrieve all products in inventory."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products")
                return [Product(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error fetching products: {e}")
            raise
    
    def delete_product(self, product_id: int) -> None:
        """Remove a product from inventory."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM products WHERE id = ?
                """, (product_id,))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error deleting product: {e}")
            raise
    
    def check_low_stock(self) -> List[Product]:
        """Return products with quantity below threshold."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM products 
                    WHERE quantity < threshold
                """)
                return [Product(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error checking low stock: {e}")
            raise
    
    def restock_product(self, product_id: int, quantity: int) -> None:
        """Add quantity to existing product stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE products 
                    SET quantity = quantity + ?
                    WHERE id = ?
                """, (quantity, product_id))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error restocking product: {e}")
            raise
    
    def sell_product(self, product_id: int, quantity: int) -> float:
        """Process product sale and return total price."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # Check available quantity
                cursor.execute("""
                    SELECT quantity, price FROM products WHERE id = ?
                """, (product_id,))
                result = cursor.fetchone()
                
                if not result:
                    raise ValueError("Product not found")
                
                available, price = result['quantity'], result['price']
                
                if available < quantity:
                    raise ValueError("Insufficient stock")
                
                # Update quantity
                cursor.execute("""
                    UPDATE products 
                    SET quantity = quantity - ?
                    WHERE id = ?
                """, (quantity, product_id))
                conn.commit()
                
                return price * quantity
        except sqlite3.Error as e:
            logger.error(f"Error processing sale: {e}")
            raise

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample products
    try:
        shampoo = Product(
            id=0,  # Will be auto-incremented
            name="ENZO-ORGANIC Shampoo",
            brand="ENZO",
            category="Hair Care",
            quantity=50,
            price=12.99,
            threshold=10
        )
        
        hair_paste = Product(
            id=0,
            name="GOLDWELL Hair Paste",
            brand="GOLDWELL",
            category="Styling",
            quantity=30,
            price=18.50,
            threshold=5
        )
        
        shampoo_id = manager.add_product(shampoo)
        hair_paste_id = manager.add_product(hair_paste)
        
        # Update product
        manager.update_product(hair_paste_id, {"price": 19.99})
        
        # Process sale
        total = manager.sell_product(shampoo_id, 2)
        logger.info(f"Sale total: ${total:.2f}")
        
        # Check low stock
        low_stock = manager.check_low_stock()
        for product in low_stock:
            logger.warning(f"Low stock: {product.name} ({product.quantity} remaining)")
            
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
