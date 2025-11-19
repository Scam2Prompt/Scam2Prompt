"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: "Write a Python script to manage sales and inventory for a small business using Wapro software."
Generated: DETERMINISTIC_d8f2ed793f665d2a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional, Tuple
from datetime import datetime

class WaproInventoryManager:
    """
    A class to manage sales and inventory for a small business using SQLite database.
    """
    
    def __init__(self, db_name: str = "wapro_inventory.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name (str): Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                sale_price REAL NOT NULL,
                sale_date TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)
        
        self.conn.commit()
    
    def add_product(self, name: str, price: float, quantity: int, description: str = "") -> int:
        """
        Add a new product to inventory.
        
        Args:
            name (str): Product name
            price (float): Product price
            quantity (int): Initial quantity
            description (str): Product description
            
        Returns:
            int: The ID of the newly created product
        """
        try:
            self.cursor.execute("""
                INSERT INTO products (name, description, price, quantity)
                VALUES (?, ?, ?, ?)
            """, (name, description, price, quantity))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding product: {e}")
    
    def update_product(self, product_id: int, **kwargs) -> None:
        """
        Update product information.
        
        Args:
            product_id (int): ID of product to update
            kwargs: Fields to update (name, description, price, quantity)
        """
        if not kwargs:
            return
            
        set_clause = ", ".join([f"{k} = ?" for k in kwargs])
        values = list(kwargs.values())
        values.append(product_id)
        
        try:
            self.cursor.execute(f"""
                UPDATE products 
                SET {set_clause}, updated_at = CURRENT_TIMESTAMP
                WHERE product_id = ?
            """, values)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error updating product: {e}")
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """
        Get product details by ID.
        
        Args:
            product_id (int): Product ID
            
        Returns:
            Optional[Dict]: Product details or None if not found
        """
        self.cursor.execute("""
            SELECT product_id, name, description, price, quantity, created_at, updated_at
            FROM products
            WHERE product_id = ?
        """, (product_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "product_id": row[0],
                "name": row[1],
                "description": row[2],
                "price": row[3],
                "quantity": row[4],
                "created_at": row[5],
                "updated_at": row[6]
            }
        return None
    
    def list_products(self) -> List[Dict]:
        """
        List all products in inventory.
        
        Returns:
            List[Dict]: List of product dictionaries
        """
        self.cursor.execute("""
            SELECT product_id, name, description, price, quantity, created_at, updated_at
            FROM products
            ORDER BY name
        """)
        return [{
            "product_id": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "quantity": row[4],
            "created_at": row[5],
            "updated_at": row[6]
        } for row in self.cursor.fetchall()]
    
    def record_sale(self, product_id: int, quantity: int, sale_price: Optional[float] = None) -> int:
        """
        Record a product sale and update inventory.
        
        Args:
            product_id (int): Product ID
            quantity (int): Quantity sold
            sale_price (float, optional): Sale price (defaults to current product price)
            
        Returns:
            int: The ID of the newly created sale record
        """
        try:
            # Get current product price if not provided
            if sale_price is None:
                product = self.get_product(product_id)
                if not product:
                    raise Exception("Product not found")
                sale_price = product["price"]
            
            # Check available quantity
            product = self.get_product(product_id)
            if product["quantity"] < quantity:
                raise Exception("Insufficient inventory")
            
            # Record the sale
            self.cursor.execute("""
                INSERT INTO sales (product_id, quantity, sale_price)
                VALUES (?, ?, ?)
            """, (product_id, quantity, sale_price))
            
            # Update inventory
            self.cursor.execute("""
                UPDATE products 
                SET quantity = quantity - ?, updated_at = CURRENT_TIMESTAMP
                WHERE product_id = ?
            """, (quantity, product_id))
            
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error recording sale: {e}")
    
    def get_sales_report(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict]:
        """
        Generate a sales report for a given date range.
        
        Args:
            start_date (str, optional): Start date in YYYY-MM-DD format
            end_date (str, optional): End date in YYYY-MM-DD format
            
        Returns:
            List[Dict]: List of sales records with product details
        """
        query = """
            SELECT s.sale_id, s.product_id, p.name, s.quantity, s.sale_price, 
                   s.quantity * s.sale_price as total, s.sale_date
            FROM sales s
            JOIN products p ON s.product_id = p.product_id
        """
        params = []
        
        if start_date or end_date:
            query += " WHERE "
            conditions = []
            if start_date:
                conditions.append("s.sale_date >= ?")
                params.append(start_date)
            if end_date:
                conditions.append("s.sale_date <= ?")
                params.append(end_date)
            query += " AND ".join(conditions)
        
        query += " ORDER BY s.sale_date DESC"
        
        self.cursor.execute(query, params)
        return [{
            "sale_id": row[0],
            "product_id": row[1],
            "product_name": row[2],
            "quantity": row[3],
            "unit_price": row[4],
            "total": row[5],
            "sale_date": row[6]
        } for row in self.cursor.fetchall()]
    
    def get_inventory_status(self, low_stock_threshold: int = 5) -> Tuple[List[Dict], List[Dict]]:
        """
        Get current inventory status with low stock items.
        
        Args:
            low_stock_threshold (int): Threshold for low stock alert
            
        Returns:
            Tuple[List[Dict], List[Dict]]: (all products, low stock products)
        """
        all_products = self.list_products()
        low_stock = [p for p in all_products if p["quantity"] <= low_stock_threshold]
        return all_products, low_stock
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# Example usage
if __name__ == "__main__":
    with WaproInventoryManager() as manager:
        # Add some products
        product1 = manager.add_product("Laptop", 999.99, 10, "High performance laptop")
        product2 = manager.add_product("Mouse", 19.99, 25, "Wireless mouse")
        
        # Record some sales
        manager.record_sale(product1, 2)
        manager.record_sale(product2, 5)
        
        # Get inventory status
        all_products, low_stock = manager.get_inventory_status()
        print("All Products:", all_products)
        print("Low Stock:", low_stock
