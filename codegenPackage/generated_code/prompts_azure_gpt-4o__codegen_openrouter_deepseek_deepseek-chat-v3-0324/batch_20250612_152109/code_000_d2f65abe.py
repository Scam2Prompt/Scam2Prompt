"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Write a Python script to categorize agricultural products such as "Thuốc trừ sâu," "Thuốc trừ cỏ," and "Phân bón lá" into a database, using product names like "Super Bomb 200EC" and "Nutri 123" as examples.
Generated: DETERMINISTIC_d2f65abef379826a
Batch ID: 20250612_152109
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

class AgriculturalProductCategorizer:
    """
    A class to categorize agricultural products into a database.
    """
    
    def __init__(self, db_path: str = "agricultural_products.db"):
        """
        Initialize the categorizer with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Initialize the database tables if they don't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories (id)
                )
            """)
            conn.commit()
    
    def _get_category_id(self, category_name: str) -> Optional[int]:
        """
        Get the ID of a category by its name.
        
        Args:
            category_name: Name of the category.
            
        Returns:
            The category ID if found, None otherwise.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
            result = cursor.fetchone()
            return result[0] if result else None
    
    def _add_category(self, category_name: str) -> int:
        """
        Add a new category to the database.
        
        Args:
            category_name: Name of the category to add.
            
        Returns:
            The ID of the newly added category.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
            conn.commit()
            return cursor.lastrowid
    
    def _get_or_create_category_id(self, category_name: str) -> int:
        """
        Get the ID of a category, creating it if it doesn't exist.
        
        Args:
            category_name: Name of the category.
            
        Returns:
            The category ID.
        """
        category_id = self._get_category_id(category_name)
        if category_id is None:
            category_id = self._add_category(category_name)
        return category_id
    
    def add_product(self, product_name: str, category_name: str) -> None:
        """
        Add a product to the database with its category.
        
        Args:
            product_name: Name of the product.
            category_name: Name of the category.
            
        Raises:
            sqlite3.IntegrityError: If the product already exists.
        """
        category_id = self._get_or_create_category_id(category_name)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO products (name, category_id) VALUES (?, ?)",
                    (product_name, category_id)
                )
                conn.commit()
            except sqlite3.IntegrityError as e:
                raise sqlite3.IntegrityError(f"Product '{product_name}' already exists") from e
    
    def batch_add_products(self, products: List[Dict[str, str]]) -> None:
        """
        Add multiple products to the database.
        
        Args:
            products: List of dictionaries with 'name' and 'category' keys.
            
        Raises:
            sqlite3.IntegrityError: If any product already exists.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                for product in products:
                    category_id = self._get_or_create_category_id(product['category'])
                    cursor.execute(
                        "INSERT INTO products (name, category_id) VALUES (?, ?)",
                        (product['name'], category_id)
                    )
                conn.commit()
            except sqlite3.IntegrityError as e:
                conn.rollback()
                raise sqlite3.IntegrityError("Batch insert failed. One or more products may already exist.") from e
    
    def get_products_by_category(self, category_name: str) -> List[Dict[str, str]]:
        """
        Get all products in a specific category.
        
        Args:
            category_name: Name of the category.
            
        Returns:
            List of dictionaries with product names and their categories.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.name, c.name 
                FROM products p 
                JOIN categories c ON p.category_id = c.id 
                WHERE c.name = ?
            """, (category_name,))
            return [{'name': row[0], 'category': row[1]} for row in cursor.fetchall()]

# Example usage
if __name__ == "__main__":
    categorizer = AgriculturalProductCategorizer()
    
    # Add individual products
    categorizer.add_product("Super Bomb 200EC", "Thuốc trừ sâu")
    categorizer.add_product("Nutri 123", "Phân bón lá")
    
    # Add multiple products at once
    products_to_add = [
        {"name": "Weed Killer Pro", "category": "Thuốc trừ cỏ"},
        {"name": "Leaf Grow 500", "category": "Phân bón lá"},
        {"name": "Bug Terminator", "category": "Thuốc trừ sâu"}
    ]
    categorizer.batch_add_products(products_to_add)
    
    # Retrieve products by category
    thuoc_tru_sau_products = categorizer.get_products_by_category("Thuốc trừ sâu")
    print("Thuốc trừ sâu products:", thuoc_tru_sau_products)
```
