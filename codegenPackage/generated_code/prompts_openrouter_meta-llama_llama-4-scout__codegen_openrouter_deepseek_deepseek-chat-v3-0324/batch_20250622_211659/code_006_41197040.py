"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Recommend a suitable database management system for storing and managing data for a company like Homefoods, which has a wide range of food products and customer information.
Generated: DETERMINISTIC_41197040637932a2
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict, Any
import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """
    A database management class that supports both SQLite (for development/testing)
    and PostgreSQL (for production) with common CRUD operations.
    """
    
    def __init__(self, db_type: str = 'postgresql', **kwargs):
        """
        Initialize the database connection.
        
        Args:
            db_type: Type of database ('sqlite' or 'postgresql')
            kwargs: Connection parameters:
                   For PostgreSQL: host, database, user, password, port
                   For SQLite: database (file path)
        """
        self.db_type = db_type
        self.connection_params = kwargs
        self.conn = None
        
    def connect(self) -> bool:
        """
        Establish a connection to the database.
        
        Returns:
            bool: True if connection succeeded, False otherwise
        """
        try:
            if self.db_type == 'postgresql':
                self.conn = psycopg2.connect(
                    host=self.connection_params.get('host'),
                    database=self.connection_params.get('database'),
                    user=self.connection_params.get('user'),
                    password=self.connection_params.get('password'),
                    port=self.connection_params.get('port', 5432),
                    cursor_factory=DictCursor
                )
            elif self.db_type == 'sqlite':
                self.conn = sqlite3.connect(
                    self.connection_params.get('database'),
                    check_same_thread=False
                )
                self.conn.row_factory = sqlite3.Row
            logger.info(f"Connected to {self.db_type} database successfully")
            return True
        except Exception as e:
            logger.error(f"Error connecting to database: {str(e)}")
            return False
    
    def disconnect(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")
    
    def execute_query(self, query: str, params: Optional[tuple] = None) -> bool:
        """
        Execute a SQL query (INSERT, UPDATE, DELETE).
        
        Args:
            query: SQL query string
            params: Parameters for the query
            
        Returns:
            bool: True if execution succeeded, False otherwise
        """
        try:
            with self.conn.cursor() as cursor:
                if self.db_type == 'postgresql':
                    cursor.execute(sql.SQL(query), params)
                else:
                    cursor.execute(query, params if params else ())
                self.conn.commit()
                return True
        except Exception as e:
            self.conn.rollback()
            logger.error(f"Error executing query: {str(e)}")
            return False
    
    def fetch_all(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """
        Execute a SELECT query and fetch all results.
        
        Args:
            query: SQL query string
            params: Parameters for the query
            
        Returns:
            List of dictionaries representing rows, or empty list on error
        """
        try:
            with self.conn.cursor() as cursor:
                if self.db_type == 'postgresql':
                    cursor.execute(sql.SQL(query), params)
                else:
                    cursor.execute(query, params if params else ())
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            return []
    
    def create_tables(self):
        """Create necessary tables for Homefoods application."""
        try:
            if self.db_type == 'postgresql':
                products_table = """
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    category VARCHAR(100) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL,
                    stock_quantity INTEGER NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
                
                customers_table = """
                CREATE TABLE IF NOT EXISTS customers (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    phone VARCHAR(20),
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
                
                orders_table = """
                CREATE TABLE IF NOT EXISTS orders (
                    id SERIAL PRIMARY KEY,
                    customer_id INTEGER REFERENCES customers(id),
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_amount DECIMAL(10, 2) NOT NULL,
                    status VARCHAR(50) NOT NULL
                );
                """
                
                order_items_table = """
                CREATE TABLE IF NOT EXISTS order_items (
                    id SERIAL PRIMARY KEY,
                    order_id INTEGER REFERENCES orders(id),
                    product_id INTEGER REFERENCES products(id),
                    quantity INTEGER NOT NULL,
                    unit_price DECIMAL(10, 2) NOT NULL
                );
                """
            else:  # SQLite
                products_table = """
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock_quantity INTEGER NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
                
                customers_table = """
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
                
                orders_table = """
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER REFERENCES customers(id),
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_amount REAL NOT NULL,
                    status TEXT NOT NULL
                );
                """
                
                order_items_table = """
                CREATE TABLE IF NOT EXISTS order_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER REFERENCES orders(id),
                    product_id INTEGER REFERENCES products(id),
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL
                );
                """
            
            # Execute all table creation queries
            self.execute_query(products_table)
            self.execute_query(customers_table)
            self.execute_query(orders_table)
            self.execute_query(order_items_table)
            logger.info("Tables created successfully")
            return True
        except Exception as e:
            logger.error(f"Error creating tables: {str(e)}")
            return False

# Example configuration for production (PostgreSQL)
PRODUCTION_DB_CONFIG = {
    'host': 'localhost',
    'database': 'homefoods',
    'user': 'homefoods_admin',
    'password': 'secure_password',
    'port': 5432
}

# Example configuration for development (SQLite)
DEVELOPMENT_DB_CONFIG = {
    'database': 'homefoods_dev.db'
}

def get_database_manager(environment: str = 'production') -> DatabaseManager:
    """
    Factory function to get appropriate database manager based on environment.
    
    Args:
        environment: 'production' or 'development'
        
    Returns:
        DatabaseManager instance
    """
    if environment == 'production':
        return DatabaseManager('postgresql', **PRODUCTION_DB_CONFIG)
    else:
        return DatabaseManager('sqlite', **DEVELOPMENT_DB_CONFIG)
```
