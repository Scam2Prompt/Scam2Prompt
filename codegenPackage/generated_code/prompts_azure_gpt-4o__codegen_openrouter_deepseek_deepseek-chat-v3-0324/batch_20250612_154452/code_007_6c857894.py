"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Provide a step-by-step guide for implementing a point-of-sale system with electronic invoicing and inventory control, referencing TICOM Software's specialized RMS features.
Generated: DETERMINISTIC_6c857894f158a017
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Point of Sale (POS) System with Electronic Invoicing and Inventory Control
Inspired by TICOM Software's RMS features
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

# Database setup and connection
class DatabaseManager:
    def __init__(self, db_name: str = "pos_system.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary tables for the POS system"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                barcode TEXT UNIQUE,
                category TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                address TEXT,
                tax_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS invoices (
                invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                invoice_number TEXT UNIQUE NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                subtotal REAL NOT NULL,
                tax REAL NOT NULL,
                total REAL NOT NULL,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS invoice_items (
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                total_price REAL NOT NULL,
                FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory_log (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity_change INTEGER NOT NULL,
                previous_stock INTEGER NOT NULL,
                new_stock INTEGER NOT NULL,
                reason TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)

        self.conn.commit()

    def execute_query(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a SQL query with parameters"""
        try:
            return self.cursor.execute(query, params)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def commit(self):
        """Commit changes to the database"""
        self.conn.commit()

    def close(self):
        """Close the database connection"""
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Product Management
class ProductManager:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_product(self, name: str, price: float, stock: int, description: str = "", 
                   barcode: str = "", category: str = "") -> int:
        """Add a new product to the inventory"""
        query = """
            INSERT INTO products (name, description, price, stock, barcode, category)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (name, description, price, stock, barcode, category))
        self.db.commit()
        return self.db.cursor.lastrowid

    def update_product(self, product_id: int, **kwargs):
        """Update product information"""
        if not kwargs:
            return

        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE products SET {set_clause} WHERE product_id = ?"
        params = tuple(kwargs.values()) + (product_id,)
        
        self.db.execute_query(query, params)
        self.db.commit()

    def get_product(self, product_id: int) -> Optional[Dict]:
        """Get product details by ID"""
        query = "SELECT * FROM products WHERE product_id = ?"
        result = self.db.execute_query(query, (product_id,)).fetchone()
        
        if result:
            columns = [desc[0] for desc in self.db.cursor.description]
            return dict(zip(columns, result))
        return None

    def list_products(self) -> List[Dict]:
        """List all products in inventory"""
        query = "SELECT * FROM products"
        results = self.db.execute_query(query).fetchall()
        
        columns = [desc[0] for desc in self.db.cursor.description]
        return [dict(zip(columns, row)) for row in results]

    def update_stock(self, product_id: int, quantity_change: int, reason: str = ""):
        """Update product stock and log the change"""
        with self.db.conn:
            # Get current stock
            current_stock = self.db.execute_query(
                "SELECT stock FROM products WHERE product_id = ?", 
                (product_id,)
            ).fetchone()[0]
            
            new_stock = current_stock + quantity_change
            if new_stock < 0:
                raise ValueError("Insufficient stock")
            
            # Update product stock
            self.db.execute_query(
                "UPDATE products SET stock = ? WHERE product_id = ?",
                (new_stock, product_id)
            )
            
            # Log inventory change
            self.db.execute_query(
                """INSERT INTO inventory_log 
                (product_id, quantity_change, previous_stock, new_stock, reason)
                VALUES (?, ?, ?, ?, ?)""",
                (product_id, quantity_change, current_stock, new_stock, reason)
            )
            self.db.commit()


# Customer Management
class CustomerManager:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_customer(self, name: str, email: str = "", phone: str = "", 
                    address: str = "", tax_id: str = "") -> int:
        """Add a new customer to the database"""
        query = """
            INSERT INTO customers (name, email, phone, address, tax_id)
            VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (name, email, phone, address, tax_id))
        self.db.commit()
        return self.db.cursor.lastrowid

    def update_customer(self, customer_id: int, **kwargs):
        """Update customer information"""
        if not kwargs:
            return

        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE customers SET {set_clause} WHERE customer_id = ?"
        params = tuple(kwargs.values()) + (customer_id,)
        
        self.db.execute_query(query, params)
        self.db.commit()

    def get_customer(self, customer_id: int) -> Optional[Dict]:
        """Get customer details by ID"""
        query = "SELECT * FROM customers WHERE customer_id = ?"
        result = self.db.execute_query(query, (customer_id,)).fetchone()
        
        if result:
            columns = [desc[0] for desc in self.db.cursor.description]
            return dict(zip(columns, result))
        return None

    def list_customers(self) -> List[Dict]:
        """List all customers"""
        query = "SELECT * FROM customers"
        results = self.db.execute_query(query).fetchall()
        
        columns = [desc[0] for desc in self.db.cursor.description]
        return [dict(zip(columns, row)) for row in results]


# Invoice and POS System
class POSSystem:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.product_manager = ProductManager(db_manager)
        self.customer_manager = CustomerManager(db_manager)

    def generate_invoice_number(self) -> str:
        """Generate a unique invoice number based on timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"INV-{timestamp}"

    def create_invoice(self, customer_id: int, items: List[Dict], tax_rate: float = 0.16) -> int:
        """
        Create a new invoice with items
        items format: [{"product_id": x, "quantity": y}, ...]
        """
        with self.db.conn:
            # Calculate totals
            subtotal = 0
            invoice_items = []
            
            for item in items:
                product = self.product_manager.get_product(item["product_id"])
                if not product:
                    raise ValueError(f"Product ID {item['product_id']} not found")
                
                if product["stock"] < item["quantity"]:
                    raise ValueError(f"Insufficient stock for product {product['name']}")
                
                item
