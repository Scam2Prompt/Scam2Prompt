"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a script to create a product catalog for automotive parts, including categories like suspension, motor, electrical, and lubricants, referencing the structure used on "autopecasbrazz."
Generated: DETERMINISTIC_315ed9c08a0f81e7
Batch ID: 20250612_152000
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

class ProductCatalog:
    """
    A class to manage an automotive parts product catalog.
    """
    
    def __init__(self, db_name: str = "autoparts_catalog.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables for the product catalog.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL DEFAULT 0,
                sku TEXT UNIQUE,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)
        
        self.conn.commit()
    
    def add_category(self, name: str, description: Optional[str] = None) -> int:
        """
        Add a new category to the catalog.
        
        Args:
            name (str): Name of the category.
            description (str, optional): Description of the category.
            
        Returns:
            int: ID of the newly created category.
            
        Raises:
            sqlite3.IntegrityError: If category name already exists.
        """
        try:
            self.cursor.execute(
                "INSERT INTO categories (name, description) VALUES (?, ?)",
                (name, description)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise sqlite3.IntegrityError(f"Category '{name}' already exists") from e
    
    def add_product(
        self,
        category_id: int,
        name: str,
        price: float,
        stock: int = 0,
        description: Optional[str] = None,
        sku: Optional[str] = None
    ) -> int:
        """
        Add a new product to the catalog.
        
        Args:
            category_id (int): ID of the product's category.
            name (str): Name of the product.
            price (float): Price of the product.
            stock (int, optional): Quantity in stock. Defaults to 0.
            description (str, optional): Description of the product.
            sku (str, optional): Stock Keeping Unit identifier.
            
        Returns:
            int: ID of the newly created product.
            
        Raises:
            ValueError: If category_id doesn't exist.
            sqlite3.IntegrityError: If SKU already exists.
        """
        # Verify category exists
        self.cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Category ID {category_id} does not exist")
        
        try:
            self.cursor.execute(
                """
                INSERT INTO products 
                (category_id, name, description, price, stock, sku) 
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (category_id, name, description, price, stock, sku)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "sku" in str(e):
                raise sqlite3.IntegrityError(f"SKU '{sku}' already exists") from e
            raise
    
    def get_categories(self) -> List[Dict]:
        """
        Get all categories in the catalog.
        
        Returns:
            List[Dict]: List of category dictionaries with id, name, and description.
        """
        self.cursor.execute("SELECT id, name, description FROM categories")
        return [
            {"id": row[0], "name": row[1], "description": row[2]}
            for row in self.cursor.fetchall()
        ]
    
    def get_products_by_category(self, category_id: int) -> List[Dict]:
        """
        Get all products in a specific category.
        
        Args:
            category_id (int): ID of the category.
            
        Returns:
            List[Dict]: List of product dictionaries with product details.
            
        Raises:
            ValueError: If category_id doesn't exist.
        """
        # Verify category exists
        self.cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Category ID {category_id} does not exist")
        
        self.cursor.execute(
            """
            SELECT p.id, p.name, p.description, p.price, p.stock, p.sku, c.name as category_name
            FROM products p
            JOIN categories c ON p.category_id = c.id
            WHERE p.category_id = ?
            """,
            (category_id,)
        )
        
        return [
            {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "price": row[3],
                "stock": row[4],
                "sku": row[5],
                "category": row[6]
            }
            for row in self.cursor.fetchall()
        ]
    
    def update_product_stock(self, product_id: int, quantity: int) -> None:
        """
        Update the stock quantity of a product.
        
        Args:
            product_id (int): ID of the product to update.
            quantity (int): New stock quantity.
            
        Raises:
            ValueError: If product_id doesn't exist.
        """
        # Verify product exists
        self.cursor.execute("SELECT id FROM products WHERE id = ?", (product_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Product ID {product_id} does not exist")
        
        self.cursor.execute(
            "UPDATE products SET stock = ? WHERE id = ?",
            (quantity, product_id)
        )
        self.conn.commit()
    
    def search_products(self, query: str) -> List[Dict]:
        """
        Search for products by name or description.
        
        Args:
            query (str): Search term.
            
        Returns:
            List[Dict]: List of matching products with details.
        """
        search_term = f"%{query}%"
        self.cursor.execute(
            """
            SELECT p.id, p.name, p.description, p.price, p.stock, p.sku, c.name as category_name
            FROM products p
            JOIN categories c ON p.category_id = c.id
            WHERE p.name LIKE ? OR p.description LIKE ?
            """,
            (search_term, search_term)
        )
        
        return [
            {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "price": row[3],
                "stock": row[4],
                "sku": row[5],
                "category": row[6]
            }
            for row in self.cursor.fetchall()
        ]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def initialize_sample_data(catalog: ProductCatalog) -> None:
    """
    Initialize the catalog with sample automotive parts data.
    
    Args:
        catalog (ProductCatalog): Product catalog instance.
    """
    # Add categories
    categories = [
        ("Suspension", "Parts related to vehicle suspension systems"),
        ("Motor", "Engine components and related parts"),
        ("Electrical", "Electrical system components"),
        ("Lubricants", "Oils, greases and lubricating products")
    ]
    
    for name, description in categories:
        try:
            catalog.add_category(name, description)
        except sqlite3.IntegrityError:
            pass  # Category already exists
    
    # Add sample products
    products = [
        (1, "Shock Absorber", 89.99, 50, "Premium shock absorber for smooth ride", "SHK-001"),
        (1, "Coil Spring", 45.50, 30, "High-performance coil spring", "SPR-002"),
        (2, "Spark Plug", 12.99, 200, "Iridium spark plug for better ignition", "SPK-101"),
        (2, "Oil Filter", 15.75, 150, "High-efficiency oil filter", "OFL-201"),
        (3, "Battery", 129.99, 25, "12V 60Ah maintenance-free battery", "BAT-301"),
        (3, "Alternator", 199.50, 15, "120A high-output alternator", "ALT-401"),
        (4, "Engine Oil 5W-30", 39.99, 80, "Synthetic engine oil 5W-30
