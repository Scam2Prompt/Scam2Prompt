"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Write code to create an e-commerce product catalog for items like "Car Mounts," "Mount Plates," and "3M Sticky Adhesive," using a database schema that supports categories and subcategories as described on the Volport website.
Generated: DETERMINISTIC_62df4486a97a53b6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error
from typing import List, Dict, Optional

class ProductCatalog:
    """
    A class to manage an e-commerce product catalog with categories and subcategories.
    Uses SQLite as the database backend.
    """

    def __init__(self, db_file: str = "product_catalog.db"):
        """
        Initialize the ProductCatalog with a SQLite database file.
        
        Args:
            db_file (str): Path to the SQLite database file. Defaults to "product_catalog.db".
        """
        self.db_file = db_file
        self.conn = None
        self._initialize_database()

    def _initialize_database(self) -> None:
        """
        Create the database tables if they don't exist.
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            cursor = self.conn.cursor()

            # Create categories table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT
                )
            """)

            # Create subcategories table with foreign key to categories
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS subcategories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories (id),
                    UNIQUE (name, category_id)
                )
            """)

            # Create products table with foreign keys to categories and subcategories
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock_quantity INTEGER NOT NULL DEFAULT 0,
                    category_id INTEGER NOT NULL,
                    subcategory_id INTEGER,
                    FOREIGN KEY (category_id) REFERENCES categories (id),
                    FOREIGN KEY (subcategory_id) REFERENCES subcategories (id),
                    UNIQUE (name, category_id, subcategory_id)
                )
            """)

            self.conn.commit()
        except Error as e:
            print(f"Error initializing database: {e}")
            if self.conn:
                self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def add_category(self, name: str, description: str = None) -> int:
        """
        Add a new category to the catalog.
        
        Args:
            name (str): Name of the category
            description (str, optional): Description of the category
            
        Returns:
            int: ID of the newly created category
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO categories (name, description) VALUES (?, ?)",
                (name, description)
            )
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding category: {e}")
            self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def add_subcategory(self, name: str, category_id: int, description: str = None) -> int:
        """
        Add a new subcategory to a category.
        
        Args:
            name (str): Name of the subcategory
            category_id (int): ID of the parent category
            description (str, optional): Description of the subcategory
            
        Returns:
            int: ID of the newly created subcategory
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO subcategories (name, description, category_id) VALUES (?, ?, ?)",
                (name, description, category_id)
            )
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding subcategory: {e}")
            self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def add_product(
        self,
        name: str,
        price: float,
        category_id: int,
        subcategory_id: int = None,
        description: str = None,
        stock_quantity: int = 0
    ) -> int:
        """
        Add a new product to the catalog.
        
        Args:
            name (str): Name of the product
            price (float): Price of the product
            category_id (int): ID of the product's category
            subcategory_id (int, optional): ID of the product's subcategory
            description (str, optional): Description of the product
            stock_quantity (int, optional): Quantity in stock. Defaults to 0.
            
        Returns:
            int: ID of the newly created product
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO products 
                (name, description, price, stock_quantity, category_id, subcategory_id) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (name, description, price, stock_quantity, category_id, subcategory_id)
            )
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding product: {e}")
            self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def get_categories(self) -> List[Dict]:
        """
        Get all categories in the catalog.
        
        Returns:
            List[Dict]: List of category dictionaries with id, name, and description
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, name, description FROM categories")
            return [{"id": row[0], "name": row[1], "description": row[2]} for row in cursor.fetchall()]
        except Error as e:
            print(f"Error getting categories: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def get_subcategories(self, category_id: int) -> List[Dict]:
        """
        Get all subcategories for a specific category.
        
        Args:
            category_id (int): ID of the parent category
            
        Returns:
            List[Dict]: List of subcategory dictionaries with id, name, and description
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT id, name, description FROM subcategories WHERE category_id = ?",
                (category_id,)
            )
            return [{"id": row[0], "name": row[1], "description": row[2]} for row in cursor.fetchall()]
        except Error as e:
            print(f"Error getting subcategories: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def get_products(
        self,
        category_id: Optional[int] = None,
        subcategory_id: Optional[int] = None
    ) -> List[Dict]:
        """
        Get products filtered by category and/or subcategory.
        
        Args:
            category_id (int, optional): Filter by category ID
            subcategory_id (int, optional): Filter by subcategory ID
            
        Returns:
            List[Dict]: List of product dictionaries with all product details
        """
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT p.id, p.name, p.description, p.price, p.stock_quantity, 
                       c.name as category_name, s.name as subcategory_name
                FROM products p
                JOIN categories c ON p.category_id = c.id
                LEFT JOIN subcategories s ON p.subcategory_id = s.id
            """
            params = []
            
            if category_id and subcategory_id:
                query += " WHERE p.category_id = ? AND p.subcategory_id = ?"
                params.extend([category_id, subcategory_id])
            elif category_id:
                query += " WHERE p.category_id = ?"
                params.append(category_id)
            elif subcategory_id:
                query += " WHERE p.subcategory_id = ?"
                params.append(subcategory_id)
                
            cursor.execute(query, params)
            
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "price": row[3],
                    "stock_quantity": row[4],
                    "category": row[5],
                    "subcategory": row[6]
                }
                for row in cursor.fetchall()
            ]
        except Error as e:
            print(f"Error getting products: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


# Example usage
if __name__ == "__main__":
    with ProductCatalog() as catalog:
        # Add categories
        mounts_id = catalog.add_category("Car Mounts", "Various types of car mounts for devices")
        accessories_id = catalog.add_category("Accessories", "Mounting accessories")
        
        # Add subcategories
        phone_mounts_id = catalog.add_subcategory("Phone Mounts",
