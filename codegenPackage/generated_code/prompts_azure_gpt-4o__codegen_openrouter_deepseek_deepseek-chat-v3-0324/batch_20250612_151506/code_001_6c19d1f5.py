"""
Generated Code Metadata:
========================
Original URL: https://gnosisrew.com
Prompt: Generate a script to filter and display automotive products like batteries, audio systems, and interior modification accessories using a database schema inspired by the 汇博娱乐 product catalog.
Generated: DETERMINISTIC_6c19d1f5502e51f1
Batch ID: 20250612_151506
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

class AutomotiveProductFilter:
    """
    A class to filter and display automotive products from a database.
    Supports filtering by product type, price range, and brand.
    """
    
    def __init__(self, db_path: str = 'automotive_products.db'):
        """
        Initialize the database connection.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self.conn = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()
        
    def connect(self):
        """Establish database connection."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        except sqlite3.Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")
            
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
            
    def create_tables(self):
        """
        Create necessary tables if they don't exist.
        This is for demonstration purposes - in production, the schema would be managed separately.
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    brand TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_features (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    feature_name TEXT NOT NULL,
                    feature_value TEXT NOT NULL,
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Failed to create tables: {e}")
            
    def filter_products(
        self,
        category: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        brand: Optional[str] = None,
        in_stock: bool = True,
        limit: int = 100
    ) -> List[Dict]:
        """
        Filter products based on various criteria.
        
        Args:
            category: Product category (e.g., 'battery', 'audio', 'interior')
            min_price: Minimum price filter
            max_price: Maximum price filter
            brand: Brand name filter
            in_stock: Only show products with stock > 0
            limit: Maximum number of results to return
            
        Returns:
            List of product dictionaries matching the criteria
        """
        if not self.conn:
            raise ConnectionError("Database connection not established")
            
        try:
            cursor = self.conn.cursor()
            
            query = """
                SELECT 
                    p.id, p.name, p.category, p.brand, p.price, p.stock, p.description,
                    GROUP_CONCAT(pf.feature_name || ': ' || pf.feature_value, '; ') as features
                FROM products p
                LEFT JOIN product_features pf ON p.id = pf.product_id
                WHERE 1=1
            """
            
            params = []
            
            if category:
                query += " AND p.category = ?"
                params.append(category)
                
            if min_price is not None:
                query += " AND p.price >= ?"
                params.append(min_price)
                
            if max_price is not None:
                query += " AND p.price <= ?"
                params.append(max_price)
                
            if brand:
                query += " AND p.brand = ?"
                params.append(brand)
                
            if in_stock:
                query += " AND p.stock > 0"
                
            query += " GROUP BY p.id LIMIT ?"
            params.append(limit)
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            # Convert rows to dictionaries
            products = []
            for row in rows:
                product = dict(row)
                # Parse features string into a dictionary
                features = {}
                if product['features']:
                    for feature in product['features'].split('; '):
                        if ': ' in feature:
                            key, value = feature.split(': ', 1)
                            features[key.strip()] = value.strip()
                product['features'] = features
                products.append(product)
                
            return products
            
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to filter products: {e}")
            
    def display_products(self, products: List[Dict]):
        """
        Display products in a user-friendly format.
        
        Args:
            products: List of product dictionaries to display
        """
        if not products:
            print("No products found matching your criteria.")
            return
            
        print("\nAutomotive Products:")
        print("-" * 50)
        
        for product in products:
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Brand: {product['brand']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            
            if product['features']:
                print("Features:")
                for feature, value in product['features'].items():
                    print(f"  - {feature}: {value}")
                    
            print("-" * 50)
            
    def get_available_categories(self) -> List[str]:
        """
        Get all distinct product categories available in the database.
        
        Returns:
            List of category names
        """
        if not self.conn:
            raise ConnectionError("Database connection not established")
            
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM products ORDER BY category")
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get categories: {e}")
            
    def get_available_brands(self) -> List[str]:
        """
        Get all distinct product brands available in the database.
        
        Returns:
            List of brand names
        """
        if not self.conn:
            raise ConnectionError("Database connection not established")
            
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DISTINCT brand FROM products ORDER BY brand")
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get brands: {e}")


# Example usage
if __name__ == "__main__":
    try:
        with AutomotiveProductFilter() as product_filter:
            # Create tables (only needed for first run)
            product_filter.create_tables()
            
            # Example: Filter for audio systems in stock
            print("\nAvailable categories:", product_filter.get_available_categories())
            print("Available brands:", product_filter.get_available_brands())
            
            print("\nFiltering for audio systems in stock...")
            audio_products = product_filter.filter_products(
                category="audio",
                in_stock=True
            )
            product_filter.display_products(audio_products)
            
            # Example: Filter for interior accessories under $500
            print("\nFiltering for interior accessories under $500...")
            interior_products = product_filter.filter_products(
                category="interior",
                max_price=500
            )
            product_filter.display_products(interior_products)
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
