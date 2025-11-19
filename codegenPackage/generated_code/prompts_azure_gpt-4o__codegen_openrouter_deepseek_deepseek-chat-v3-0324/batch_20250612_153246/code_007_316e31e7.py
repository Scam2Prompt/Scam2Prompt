"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a Python program to manage inventory and sales in a hardware store, referencing the "Guía Completa: Cómo Gestionar y Operar una Ferretería – Desde Cero hasta el Éxito" from Aula Ferretera.
Generated: DETERMINISTIC_316e31e7b55088be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class HardwareStoreDB:
    """Database handler for hardware store inventory and sales."""
    
    def __init__(self, db_name: str = "hardware_store.db"):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables for inventory and sales."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                min_stock INTEGER NOT NULL,
                supplier TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT,
                total_amount REAL NOT NULL,
                payment_method TEXT NOT NULL,
                sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale_items (
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                sale_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)
        
        self.conn.commit()
    
    def add_product(self, name: str, description: str, category: str, price: float, 
                   stock: int, min_stock: int, supplier: str) -> int:
        """Add a new product to inventory."""
        try:
            self.cursor.execute("""
                INSERT INTO products (name, description, category, price, stock, min_stock, supplier)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, description, category, price, stock, min_stock, supplier))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding product: {e}")
    
    def update_product(self, product_id: int, **kwargs) -> None:
        """Update product information."""
        if not kwargs:
            return
            
        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values())
        values.append(product_id)
        
        try:
            self.cursor.execute(f"""
                UPDATE products 
                SET {set_clause}
                WHERE product_id = ?
            """, values)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error updating product: {e}")
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """Get product details by ID."""
        self.cursor.execute("""
            SELECT * FROM products WHERE product_id = ?
        """, (product_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def list_products(self, category: str = None) -> List[Dict]:
        """List all products, optionally filtered by category."""
        query = "SELECT * FROM products"
        params = ()
        
        if category:
            query += " WHERE category = ?"
            params = (category,)
            
        self.cursor.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def check_low_stock(self) -> List[Dict]:
        """List products with stock below minimum threshold."""
        self.cursor.execute("""
            SELECT * FROM products 
            WHERE stock < min_stock
            ORDER BY stock ASC
        """)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def record_sale(self, customer_name: str, items: List[Tuple[int, int]], 
                   payment_method: str = "cash") -> int:
        """Record a sale transaction."""
        try:
            # Calculate total amount
            total = 0.0
            for product_id, quantity in items:
                product = self.get_product(product_id)
                if not product:
                    raise Exception(f"Product ID {product_id} not found")
                if product['stock'] < quantity:
                    raise Exception(f"Insufficient stock for product {product['name']}")
                total += product['price'] * quantity
            
            # Create sale record
            self.cursor.execute("""
                INSERT INTO sales (customer_name, total_amount, payment_method)
                VALUES (?, ?, ?)
            """, (customer_name, total, payment_method))
            sale_id = self.cursor.lastrowid
            
            # Add sale items and update stock
            for product_id, quantity in items:
                product = self.get_product(product_id)
                self.cursor.execute("""
                    INSERT INTO sale_items (sale_id, product_id, quantity, unit_price)
                    VALUES (?, ?, ?, ?)
                """, (sale_id, product_id, quantity, product['price']))
                
                # Update product stock
                new_stock = product['stock'] - quantity
                self.update_product(product_id, stock=new_stock)
            
            self.conn.commit()
            return sale_id
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error recording sale: {e}")
        except Exception as e:
            self.conn.rollback()
            raise e
    
    def get_sales_report(self, start_date: str = None, end_date: str = None) -> Dict:
        """Generate sales report for a given period."""
        query = """
            SELECT s.sale_id, s.customer_name, s.total_amount, s.payment_method, s.sale_date,
                   GROUP_CONCAT(p.name || ' (' || si.quantity || ')', ', ') as items
            FROM sales s
            JOIN sale_items si ON s.sale_id = si.sale_id
            JOIN products p ON si.product_id = p.product_id
        """
        params = ()
        
        if start_date and end_date:
            query += " WHERE s.sale_date BETWEEN ? AND ?"
            params = (start_date, end_date)
        elif start_date:
            query += " WHERE s.sale_date >= ?"
            params = (start_date,)
        elif end_date:
            query += " WHERE s.sale_date <= ?"
            params = (end_date,)
            
        query += " GROUP BY s.sale_id ORDER BY s.sale_date DESC"
        
        self.cursor.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]
        sales = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        
        # Calculate totals
        total_sales = sum(sale['total_amount'] for sale in sales)
        total_transactions = len(sales)
        
        return {
            'sales': sales,
            'total_sales': total_sales,
            'total_transactions': total_transactions
        }
    
    def close(self) -> None:
        """Close database connection."""
        self.conn.close()

class HardwareStoreApp:
    """CLI application for hardware store management."""
    
    def __init__(self):
        self.db = HardwareStoreDB()
    
    def display_menu(self) -> None:
        """Display main menu options."""
        print("\nHardware Store Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. List Products")
        print("4. Check Low Stock")
        print("5. Record Sale")
        print("6. Generate Sales Report")
        print("7. Exit")
    
    def add_product_cli(self) -> None:
        """CLI for adding a new product."""
        print("\nAdd New Product")
        name = input("Product name: ")
        description = input("Description (optional): ")
        category = input("Category: ")
        price = float(input("Price: "))
        stock = int(input("Current stock: "))
        min_stock = int(input("Minimum stock level: "))
        supplier = input("Supplier (optional): ")
        
        try:
            product_id = self.db.add_product(name, description, category, price, stock, min_stock, supplier)
            print(f"Product added successfully with ID: {product_id}")
        except Exception as e:
            print(f"Error: {e}")
    
    def update_product_cli(self) -> None:
        """CLI for updating a product."""
        product_id = int(input("\nEnter product ID to update: "))
        product = self.db.get_product(product_id)
        
        if not product:
            print("Product not found.")
