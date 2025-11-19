"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Develop a basic CRM system for a wood products supplier like Maderas Elaboradas, incorporating features for tracking customer inquiries, orders, and product deliveries.
Generated: DETERMINISTIC_e5033854ce332841
Batch ID: 20250622_212822
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
from typing import Optional, List, Dict, Tuple

class CRMDB:
    """Database handler for the CRM system."""
    
    def __init__(self, db_name: str = "wood_products_crm.db"):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                address TEXT,
                company TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                notes TEXT,
                status TEXT DEFAULT 'open',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                total_amount REAL NOT NULL,
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deliveries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                delivery_date TIMESTAMP,
                status TEXT DEFAULT 'scheduled',
                tracking_number TEXT,
                notes TEXT,
                FOREIGN KEY (order_id) REFERENCES orders (id)
            )
        """)
        
        self.conn.commit()
    
    def add_customer(self, name: str, email: str, phone: str = None, address: str = None, company: str = None) -> int:
        """Add a new customer to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO customers (name, email, phone, address, company) VALUES (?, ?, ?, ?, ?)",
                (name, email, phone, address, company)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists in the system")
    
    def add_product(self, name: str, price: float, description: str = None, stock: int = 0) -> int:
        """Add a new product to the database."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)",
            (name, description, price, stock)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def create_inquiry(self, customer_id: int, product_id: int, notes: str = None) -> int:
        """Create a new customer inquiry."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO inquiries (customer_id, product_id, notes) VALUES (?, ?, ?)",
            (customer_id, product_id, notes)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def create_order(self, customer_id: int, items: List[Dict[str, int]], notes: str = None) -> int:
        """Create a new order with items."""
        try:
            cursor = self.conn.cursor()
            
            # Calculate total amount
            total = 0.0
            for item in items:
                cursor.execute("SELECT price FROM products WHERE id = ?", (item['product_id'],))
                product = cursor.fetchone()
                if not product:
                    raise ValueError(f"Product with ID {item['product_id']} not found")
                total += product[0] * item['quantity']
            
            # Create order
            cursor.execute(
                "INSERT INTO orders (customer_id, total_amount, notes) VALUES (?, ?, ?)",
                (customer_id, total, notes)
            )
            order_id = cursor.lastrowid
            
            # Add order items
            for item in items:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
                    (order_id, item['product_id'], item['quantity'], item.get('unit_price', 0))
                )
            
            self.conn.commit()
            return order_id
        except Exception as e:
            self.conn.rollback()
            raise e
    
    def schedule_delivery(self, order_id: int, delivery_date: datetime, tracking_number: str = None, notes: str = None) -> int:
        """Schedule a delivery for an order."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO deliveries (order_id, delivery_date, tracking_number, notes) VALUES (?, ?, ?, ?)",
            (order_id, delivery_date, tracking_number, notes)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_customer_orders(self, customer_id: int) -> List[Tuple]:
        """Get all orders for a customer."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM orders WHERE customer_id = ?",
            (customer_id,)
        )
        return cursor.fetchall()
    
    def get_order_details(self, order_id: int) -> Dict:
        """Get order details including items."""
        cursor = self.conn.cursor()
        
        # Get order info
        cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        order = cursor.fetchone()
        if not order:
            return None
        
        # Get order items
        cursor.execute(
            "SELECT p.name, oi.quantity, oi.unit_price FROM order_items oi JOIN products p ON oi.product_id = p.id WHERE oi.order_id = ?",
            (order_id,)
        )
        items = cursor.fetchall()
        
        return {
            'order': order,
            'items': items
        }
    
    def update_order_status(self, order_id: int, status: str) -> None:
        """Update the status of an order."""
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE orders SET status = ? WHERE id = ?",
            (status, order_id)
        )
        self.conn.commit()
    
    def update_delivery_status(self, delivery_id: int, status: str) -> None:
        """Update the status of a delivery."""
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE deliveries SET status = ? WHERE id = ?",
            (status, delivery_id)
        )
        self.conn.commit()
    
    def get_pending_orders(self) -> List[Tuple]:
        """Get all pending orders."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE status = 'pending'")
        return cursor.fetchall()
    
    def get_scheduled_deliveries(self) -> List[Tuple]:
        """Get all scheduled deliveries."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM deliveries WHERE status = 'scheduled'")
        return cursor.fetchall()
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

class WoodProductsCRM:
    """Main CRM system class."""
    
    def __init__(self):
        self.db = CRMDB()
    
    def add_customer(self, name: str, email: str, phone: str = None, address: str = None, company: str = None) -> int:
        """Add a new customer."""
        return self.db.add_customer(name, email, phone, address, company)
    
    def add_product(self, name: str, price: float, description: str = None, stock: int = 0) -> int:
        """Add a new product."""
        return self.db.add_product(name, price, description, stock)
    
    def create_inquiry(self, customer_id: int, product_id: int, notes: str = None) -> int:
        """Create a new inquiry."""
        return self.db.create_inquiry(customer_id, product_id, notes)
    
    def create_order(self, customer_id: int, items: List[Dict[str, int]], notes: str = None) -> int:
        """Create a new order
