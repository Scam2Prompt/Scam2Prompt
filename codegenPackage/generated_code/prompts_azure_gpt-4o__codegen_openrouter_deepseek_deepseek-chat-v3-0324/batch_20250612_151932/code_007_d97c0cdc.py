"""
Generated Code Metadata:
========================
Original URL: https://registrations-arcium.hq.net
Prompt: Create code to search for products by name, such as "개성고려인삼탕" or "단너삼," and return their category and company information.
Generated: DETERMINISTIC_d97c0cdc9ec96483
Batch ID: 20250612_151932
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

class ProductSearch:
    """
    A class to search for products by name and retrieve their category and company information.
    """
    
    def __init__(self, db_path: str = 'products.db'):
        """
        Initialize the ProductSearch with a database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        
    def __enter__(self):
        """Establish database connection when entering context."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection when exiting context."""
        if self.conn:
            self.conn.close()
            
    def search_products(self, product_name: str) -> List[Dict[str, Optional[str]]]:
        """
        Search for products by name and return their category and company information.
        
        Args:
            product_name: The name or partial name of the product to search for.
            
        Returns:
            A list of dictionaries containing product information, or empty list if no matches.
            
        Raises:
            sqlite3.Error: If there's an error executing the database query.
        """
        if not self.conn:
            raise RuntimeError("Database connection not established. Use context manager.")
            
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT 
                    p.name as product_name,
                    c.name as category_name,
                    co.name as company_name
                FROM 
                    products p
                JOIN 
                    categories c ON p.category_id = c.id
                JOIN 
                    companies co ON p.company_id = co.id
                WHERE 
                    p.name LIKE ?
            """
            cursor.execute(query, (f'%{product_name}%',))
            results = cursor.fetchall()
            
            # Convert sqlite3.Row objects to dictionaries
            return [dict(row) for row in results]
            
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error occurred: {e}")
            
    @staticmethod
    def initialize_database(db_path: str = 'products.db'):
        """
        Initialize the database with sample tables and data.
        For demonstration purposes only.
        """
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            # Create tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS companies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category_id INTEGER,
                    company_id INTEGER,
                    FOREIGN KEY (category_id) REFERENCES categories(id),
                    FOREIGN KEY (company_id) REFERENCES companies(id)
                )
            """)
            
            # Insert sample data
            cursor.execute("INSERT OR IGNORE INTO companies (name) VALUES ('고려인삼공사')")
            cursor.execute("INSERT OR IGNORE INTO companies (name) VALUES ('단너삼식품')")
            
            cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('인삼제품')")
            cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('건강식품')")
            
            cursor.execute("""
                INSERT OR IGNORE INTO products (name, category_id, company_id)
                VALUES ('개성고려인삼탕', 1, 1)
            """)
            cursor.execute("""
                INSERT OR IGNORE INTO products (name, category_id, company_id)
                VALUES ('단너삼', 2, 2)
            """)
            
            conn.commit()


# Example usage
if __name__ == "__main__":
    # Initialize the database (for demonstration)
    ProductSearch.initialize_database()
    
    # Search for products
    with ProductSearch() as searcher:
        results = searcher.search_products("개성고려인삼탕")
        print("Search results for '개성고려인삼탕':", results)
        
        results = searcher.search_products("단너삼")
        print("Search results for '단너삼':", results)
```
