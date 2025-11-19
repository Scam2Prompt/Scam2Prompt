"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Write a Python script to manage an e-commerce store's inventory of championship belts, including tracking orders and updating product prices, inspired by the product offerings on Title Belts AU.
Generated: DETERMINISTIC_3798b4924e6bcf4f
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('inventory_manager.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class Belt:
    """Represents a championship belt product."""
    id: int
    name: str
    description: str
    price: float
    stock_quantity: int
    weight_class: str
    material: str
    created_at: datetime
    updated_at: datetime

@dataclass
class Order:
    """Represents a customer order."""
    id: int
    customer_name: str
    customer_email: str
    belt_id: int
    quantity: int
    total_price: float
    status: str
    order_date: datetime
    shipping_address: str

class InventoryManager:
    """Manages the e-commerce store's inventory and orders."""
    
    def __init__(self, db_path: str = 'inventory.db'):
        """Initialize the inventory manager with database connection."""
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self):
        """Create database tables if they don't exist."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create belts table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS belts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT,
                        price REAL NOT NULL,
                        stock_quantity INTEGER NOT NULL,
                        weight_class TEXT,
                        material TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create orders table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        customer_email TEXT NOT NULL,
                        belt_id INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        total_price REAL NOT NULL,
                        status TEXT DEFAULT 'pending',
                        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        shipping_address TEXT NOT NULL,
                        FOREIGN KEY (belt_id) REFERENCES belts (id)
                    )
                ''')
                
                conn.commit()
                logging.info("Database tables initialized successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error initializing database: {e}")
            raise
    
    def add_belt(self, belt: Belt) -> int:
        """Add a new belt to the inventory."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO belts (
                        name, description, price, stock_quantity, 
                        weight_class, material, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    belt.name, belt.description, belt.price, belt.stock_quantity,
                    belt.weight_class, belt.material, belt.created_at, belt.updated_at
                ))
                belt_id = cursor.lastrowid
                conn.commit()
                logging.info(f"Added new belt with ID: {belt_id}")
                return belt_id
        except sqlite3.Error as e:
            logging.error(f"Error adding belt: {e}")
            raise
    
    def update_belt_price(self, belt_id: int, new_price: float) -> bool:
        """Update the price of a belt."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE belts 
                    SET price = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (new_price, belt_id))
                conn.commit()
                if cursor.rowcount > 0:
                    logging.info(f"Updated price for belt ID {belt_id} to ${new_price:.2f}")
                    return True
                logging.warning(f"No belt found with ID {belt_id}")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error updating belt price: {e}")
            raise
    
    def get_belt_by_id(self, belt_id: int) -> Optional[Belt]:
        """Retrieve a belt by its ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM belts WHERE id = ?
                ''', (belt_id,))
                row = cursor.fetchone()
                if row:
                    return Belt(*row)
                return None
        except sqlite3.Error as e:
            logging.error(f"Error retrieving belt: {e}")
            raise
    
    def get_all_belts(self) -> List[Belt]:
        """Retrieve all belts in inventory."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM belts')
                return [Belt(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logging.error(f"Error retrieving belts: {e}")
            raise
    
    def place_order(self, order: Order) -> int:
        """Place a new order and update inventory."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check belt availability
                cursor.execute('SELECT stock_quantity FROM belts WHERE id = ?', (order.belt_id,))
                result = cursor.fetchone()
                if not result:
                    raise ValueError(f"No belt found with ID {order.belt_id}")
                
                current_stock = result[0]
                if current_stock < order.quantity:
                    raise ValueError(f"Insufficient stock for belt ID {order.belt_id}")
                
                # Insert order
                cursor.execute('''
                    INSERT INTO orders (
                        customer_name, customer_email, belt_id, quantity,
                        total_price, status, shipping_address
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    order.customer_name, order.customer_email, order.belt_id,
                    order.quantity, order.total_price, order.status,
                    order.shipping_address
                ))
                order_id = cursor.lastrowid
                
                # Update inventory
                cursor.execute('''
                    UPDATE belts 
                    SET stock_quantity = stock_quantity - ?, 
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (order.quantity, order.belt_id))
                
                conn.commit()
                logging.info(f"Order placed successfully with ID: {order_id}")
                return order_id
        except (sqlite3.Error, ValueError) as e:
            logging.error(f"Error placing order: {e}")
            raise
    
    def update_order_status(self, order_id: int, new_status: str) -> bool:
        """Update the status of an order."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE orders 
                    SET status = ?
                    WHERE id = ?
                ''', (new_status, order_id))
                conn.commit()
                if cursor.rowcount > 0:
                    logging.info(f"Updated status for order ID {order_id} to '{new_status}'")
                    return True
                logging.warning(f"No order found with ID {order_id}")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error updating order status: {e}")
            raise
    
    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        """Retrieve an order by its ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM orders WHERE id = ?
                ''', (order_id,))
                row = cursor.fetchone()
                if row:
                    return Order(*row)
                return None
        except sqlite3.Error as e:
            logging.error(f"Error retrieving order: {e}")
            raise
    
    def get_all_orders(self) -> List[Order]:
        """Retrieve all orders."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM orders')
                return [Order(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logging.error(f"Error retrieving orders: {e}")
            raise
    
    def restock_belt(self, belt_id: int, quantity: int) -> bool:
        """Add stock to a belt."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE belts 
                    SET stock_quantity = stock_quantity + ?, 
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (quantity, belt_id))
                conn.commit()
                if cursor.rowcount > 0:
                    logging.info(f"Restocked belt ID {belt_id} with {quantity} units")
                    return True
                logging.warning(f"No belt found with ID {belt_id}")
