"""
Generated Code Metadata:
========================
Original URL: https://jiosell.com
Prompt: "Design a database schema to store product information from various online shops, including Jiosell, and implement efficient querying mechanisms."
Generated: DETERMINISTIC_4be2e36bdac5e31a
Batch ID: 20250622_212618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database Schema and Query Implementation for Product Information System

import sqlite3
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ProductDatabase:
    """Class to handle product database operations."""
    
    def __init__(self, db_path: str = 'products.db'):
        """Initialize database connection and create tables if they don't exist."""
        self.db_path = db_path
        self.conn = None
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables with proper schema."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create shops table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS shops (
                    shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    base_url TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    parent_id INTEGER REFERENCES categories(category_id),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create products table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    shop_id INTEGER NOT NULL REFERENCES shops(shop_id),
                    external_id TEXT NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT,
                    current_price REAL NOT NULL,
                    original_price REAL,
                    currency TEXT NOT NULL DEFAULT 'USD',
                    category_id INTEGER REFERENCES categories(category_id),
                    url TEXT NOT NULL,
                    image_url TEXT,
                    rating REAL,
                    review_count INTEGER,
                    in_stock BOOLEAN DEFAULT TRUE,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(shop_id, external_id)
                )
            ''')
            
            # Create price_history table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS price_history (
                    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL REFERENCES products(product_id),
                    price REAL NOT NULL,
                    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create indexes for faster queries
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_products_shop ON products(shop_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_products_price ON products(current_price)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_price_history_product ON price_history(product_id)')
            
            self.conn.commit()
            logging.info("Database initialized successfully")
            
        except sqlite3.Error as e:
            logging.error(f"Error initializing database: {e}")
            if self.conn:
                self.conn.rollback()
            raise
    
    def add_shop(self, name: str, base_url: str) -> int:
        """Add a new shop to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO shops (name, base_url) VALUES (?, ?)',
                (name, base_url)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error adding shop: {e}")
            self.conn.rollback()
            raise
    
    def add_category(self, name: str, parent_id: Optional[int] = None) -> int:
        """Add a new category to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO categories (name, parent_id) VALUES (?, ?)',
                (name, parent_id)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error adding category: {e}")
            self.conn.rollback()
            raise
    
    def add_product(self, product_data: Dict) -> int:
        """Add a new product to the database."""
        required_fields = ['shop_id', 'external_id', 'title', 'current_price', 'url']
        if not all(field in product_data for field in required_fields):
            raise ValueError("Missing required product fields")
        
        try:
            cursor = self.conn.cursor()
            
            # Insert product
            cursor.execute('''
                INSERT INTO products (
                    shop_id, external_id, title, description, current_price,
                    original_price, currency, category_id, url, image_url,
                    rating, review_count, in_stock
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                product_data['shop_id'],
                product_data['external_id'],
                product_data['title'],
                product_data.get('description'),
                product_data['current_price'],
                product_data.get('original_price'),
                product_data.get('currency', 'USD'),
                product_data.get('category_id'),
                product_data['url'],
                product_data.get('image_url'),
                product_data.get('rating'),
                product_data.get('review_count'),
                product_data.get('in_stock', True)
            ))
            
            product_id = cursor.lastrowid
            
            # Record price history
            cursor.execute('''
                INSERT INTO price_history (product_id, price)
                VALUES (?, ?)
            ''', (product_id, product_data['current_price']))
            
            self.conn.commit()
            return product_id
            
        except sqlite3.Error as e:
            logging.error(f"Error adding product: {e}")
            self.conn.rollback()
            raise
    
    def update_product_price(self, product_id: int, new_price: float) -> None:
        """Update product price and record price history."""
        try:
            cursor = self.conn.cursor()
            
            # Update current price
            cursor.execute('''
                UPDATE products
                SET current_price = ?, last_updated = CURRENT_TIMESTAMP
                WHERE product_id = ?
            ''', (new_price, product_id))
            
            # Record price history
            cursor.execute('''
                INSERT INTO price_history (product_id, price)
                VALUES (?, ?)
            ''', (product_id, new_price))
            
            self.conn.commit()
            
        except sqlite3.Error as e:
            logging.error(f"Error updating product price: {e}")
            self.conn.rollback()
            raise
    
    def get_products_by_shop(self, shop_id: int, limit: int = 100, offset: int = 0) -> List[Dict]:
        """Retrieve products by shop ID with pagination."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT p.*, s.name as shop_name, c.name as category_name
                FROM products p
                LEFT JOIN shops s ON p.shop_id = s.shop_id
                LEFT JOIN categories c ON p.category_id = c.category_id
                WHERE p.shop_id = ?
                ORDER BY p.last_updated DESC
                LIMIT ? OFFSET ?
            ''', (shop_id, limit, offset))
            
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
            
        except sqlite3.Error as e:
            logging.error(f"Error fetching products by shop: {e}")
            raise
    
    def get_products_by_category(self, category_id: int, limit: int = 100, offset: int = 0) -> List[Dict]:
        """Retrieve products by category ID with pagination."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT p.*, s.name as shop_name, c.name as category_name
                FROM products p
                LEFT JOIN shops s ON p.shop_id = s.shop_id
                LEFT JOIN categories c ON p.category_id = c.category_id
                WHERE p.category_id = ?
                ORDER BY p.last_updated DESC
                LIMIT ? OFFSET ?
            ''', (category_id, limit, offset))
            
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
            
        except sqlite3.Error as e:
            logging.error(f"Error fetching products by category: {e}")
            raise
    
    def search_products(self, query: str, limit: int = 100, offset: int = 0) -> List[Dict]:
        """Search products by title or description."""
        try:
            cursor = self.conn.cursor()
            search_term = f"%{query}%"
            cursor.execute('''
                SELECT p.*, s.name as shop_name, c.name as category_name
                FROM products p
                LEFT JOIN shops s ON p.shop_id = s.shop_id
                LEFT JOIN categories c ON p.category_id = c.category_id
                WHERE p.title LIKE ? OR p.description LIKE ?
                ORDER BY
