"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write a Python code snippet to manage inventory of drilling equipment and electrical division products for an oil and gas company using Cedar International Inc.'s supply chain solutions.
Generated: DETERMINISTIC_8a569754cffdea64
Batch ID: 20250622_205536
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

class InventoryManager:
    """
    A class to manage inventory for drilling equipment and electrical division products.
    Integrates with Cedar International Inc.'s supply chain solutions.
    """
    
    def __init__(self, db_name: str = "inventory.db"):
        """
        Initialize the inventory manager with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT CHECK(category IN ('drilling', 'electrical')) NOT NULL,
            description TEXT,
            unit_price REAL NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 0,
            min_stock_level INTEGER NOT NULL DEFAULT 5,
            supplier TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            transaction_type TEXT CHECK(transaction_type IN ('purchase', 'sale', 'adjustment')) NOT NULL,
            notes TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products (product_id)
        )
        """)
        
        self.conn.commit()
    
    def add_product(self, name: str, category: str, unit_price: float, 
                   quantity: int = 0, description: str = "", 
                   min_stock_level: int = 5, supplier: str = "") -> int:
        """
        Add a new product to inventory.
        
        Args:
            name: Product name
            category: 'drilling' or 'electrical'
            unit_price: Price per unit
            quantity: Initial quantity
            description: Product description
            min_stock_level: Minimum stock level before reorder
            supplier: Supplier information
            
        Returns:
            The ID of the newly added product
        """
        if category not in ('drilling', 'electrical'):
            raise ValueError("Category must be either 'drilling' or 'electrical'")
        
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO products (name, category, description, unit_price, quantity, min_stock_level, supplier)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, category, description, unit_price, quantity, min_stock_level, supplier))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def update_product(self, product_id: int, **kwargs) -> None:
        """
        Update product information.
        
        Args:
            product_id: ID of product to update
            kwargs: Fields to update (name, category, description, unit_price, quantity, min_stock_level, supplier)
        """
        valid_fields = {'name', 'category', 'description', 'unit_price', 'quantity', 'min_stock_level', 'supplier'}
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            return
        
        if 'category' in updates and updates['category'] not in ('drilling', 'electrical'):
            raise ValueError("Category must be either 'drilling' or 'electrical'")
        
        set_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        values = list(updates.values())
        values.append(product_id)
        
        cursor = self.conn.cursor()
        cursor.execute(f"""
        UPDATE products 
        SET {set_clause}, last_updated = CURRENT_TIMESTAMP
        WHERE product_id = ?
        """, values)
        
        self.conn.commit()
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """
        Get product details by ID.
        
        Args:
            product_id: ID of product to retrieve
            
        Returns:
            Dictionary of product details or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT product_id, name, category, description, unit_price, quantity, min_stock_level, supplier, last_updated
        FROM products
        WHERE product_id = ?
        """, (product_id,))
        
        row = cursor.fetchone()
        if not row:
            return None
            
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, row))
    
    def list_products(self, category: Optional[str] = None, 
                     low_stock: bool = False) -> List[Dict]:
        """
        List all products with optional filters.
        
        Args:
            category: Filter by category ('drilling' or 'electrical')
            low_stock: Only show products below minimum stock level
            
        Returns:
            List of product dictionaries
        """
        cursor = self.conn.cursor()
        query = """
        SELECT product_id, name, category, description, unit_price, quantity, min_stock_level, supplier, last_updated
        FROM products
        WHERE 1=1
        """
        params = []
        
        if category:
            if category not in ('drilling', 'electrical'):
                raise ValueError("Category must be either 'drilling' or 'electrical'")
            query += " AND category = ?"
            params.append(category)
            
        if low_stock:
            query += " AND quantity < min_stock_level"
            
        cursor.execute(query, params)
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def record_transaction(self, product_id: int, quantity: int, 
                         transaction_type: str, notes: str = "") -> int:
        """
        Record an inventory transaction (purchase, sale, or adjustment).
        
        Args:
            product_id: ID of product involved
            quantity: Quantity changed (positive for purchase, negative for sale)
            transaction_type: 'purchase', 'sale', or 'adjustment'
            notes: Additional notes about the transaction
            
        Returns:
            The ID of the newly created transaction
        """
        if transaction_type not in ('purchase', 'sale', 'adjustment'):
            raise ValueError("Transaction type must be 'purchase', 'sale', or 'adjustment'")
        
        cursor = self.conn.cursor()
        
        # Update product quantity
        if transaction_type == 'purchase':
            cursor.execute("""
            UPDATE products 
            SET quantity = quantity + ?, last_updated = CURRENT_TIMESTAMP
            WHERE product_id = ?
            """, (quantity, product_id))
        elif transaction_type == 'sale':
            # Check if enough stock is available
            current_qty = self.get_product(product_id)['quantity']
            if current_qty < quantity:
                raise ValueError("Insufficient stock for this sale")
            cursor.execute("""
            UPDATE products 
            SET quantity = quantity - ?, last_updated = CURRENT_TIMESTAMP
            WHERE product_id = ?
            """, (quantity, product_id))
        else:  # adjustment
            cursor.execute("""
            UPDATE products 
            SET quantity = ?, last_updated = CURRENT_TIMESTAMP
            WHERE product_id = ?
            """, (quantity, product_id))
        
        # Record the transaction
        cursor.execute("""
        INSERT INTO transactions (product_id, quantity, transaction_type, notes)
        VALUES (?, ?, ?, ?)
        """, (product_id, abs(quantity), transaction_type, notes))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def get_transaction_history(self, product_id: Optional[int] = None, 
                              start_date: Optional[str] = None,
                              end_date: Optional[str] = None) -> List[Dict]:
        """
        Get transaction history with optional filters.
        
        Args:
            product_id: Filter by product ID
            start_date: Filter transactions after this date (YYYY-MM-DD)
            end_date: Filter transactions before this date (YYYY-MM-DD)
            
        Returns:
            List of transaction dictionaries
        """
        cursor = self.conn.cursor()
        query = """
        SELECT t.transaction_id, t.product_id, p.name as product_name, 
               t.quantity, t.transaction_type, t.notes, t.timestamp
        FROM transactions t
        JOIN products p ON t.product_id = p.product_id
        WHERE 1=1
        """
        params = []
        
        if product_id:
            query += " AND t.product_id = ?"
            params.append(product_id)
            
        if start_date:
            query += " AND t.timestamp >= ?"
            params.append(start_date)
            
        if end_date:
            query += " AND t.timestamp <= ?"
            params.append(end_date)
            
        query += " ORDER BY t.timestamp DESC"
        
        cursor.execute(query, params)
        
        columns = [desc[0] for desc in cursor.description]
