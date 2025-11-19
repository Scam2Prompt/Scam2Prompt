"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Generate code to create a customer and inventory tracking system using DemirSoft's "PetShop ve Veteriner SMS Müşteri ve Stok Takip Programı."
Generated: DETERMINISTIC_4df100a249e7c0db
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
import logging
from typing import Optional, List, Dict, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='petshop_tracking.log'
)

class DatabaseManager:
    """Handles database operations for the PetShop tracking system."""
    
    def __init__(self, db_name: str = 'petshop.db'):
        """Initialize database connection."""
        self.db_name = db_name
        self.conn = None
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            cursor = self.conn.cursor()
            
            # Create customers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL UNIQUE,
                    email TEXT,
                    address TEXT,
                    pet_name TEXT,
                    pet_type TEXT,
                    registration_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT
                )
            ''')
            
            # Create inventory table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    category TEXT,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    barcode TEXT UNIQUE,
                    supplier TEXT,
                    last_restock_date TEXT,
                    min_stock_level INTEGER DEFAULT 0,
                    notes TEXT
                )
            ''')
            
            # Create sales table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL,
                    total_price REAL NOT NULL,
                    sale_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    payment_method TEXT,
                    notes TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customers (id),
                    FOREIGN KEY (product_id) REFERENCES inventory (id)
                )
            ''')
            
            self.conn.commit()
            logging.info("Database initialized successfully")
            
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise
            
    def execute_query(self, query: str, params: Tuple = (), fetch: bool = False) -> Optional[List[Tuple]]:
        """Execute a SQL query with error handling."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            
            if fetch:
                result = cursor.fetchall()
                return result
            
            self.conn.commit()
            return None
            
        except sqlite3.Error as e:
            logging.error(f"Database query error: {e}")
            self.conn.rollback()
            raise
            
    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed")

class CustomerManager:
    """Manages customer-related operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_customer(
        self,
        name: str,
        phone: str,
        email: Optional[str] = None,
        address: Optional[str] = None,
        pet_name: Optional[str] = None,
        pet_type: Optional[str] = None,
        notes: Optional[str] = None
    ) -> int:
        """Add a new customer to the database."""
        query = '''
            INSERT INTO customers (name, phone, email, address, pet_name, pet_type, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        params = (name, phone, email, address, pet_name, pet_type, notes)
        
        try:
            self.db.execute_query(query, params)
            logging.info(f"Added new customer: {name}")
            return self.db.conn.cursor().lastrowid
        except sqlite3.IntegrityError:
            logging.warning(f"Customer with phone {phone} already exists")
            raise ValueError("A customer with this phone number already exists")
    
    def get_customer(self, customer_id: int) -> Optional[Dict]:
        """Retrieve a customer by ID."""
        query = 'SELECT * FROM customers WHERE id = ?'
        result = self.db.execute_query(query, (customer_id,), fetch=True)
        
        if result:
            customer = {
                'id': result[0][0],
                'name': result[0][1],
                'phone': result[0][2],
                'email': result[0][3],
                'address': result[0][4],
                'pet_name': result[0][5],
                'pet_type': result[0][6],
                'registration_date': result[0][7],
                'notes': result[0][8]
            }
            return customer
        return None
    
    def update_customer(
        self,
        customer_id: int,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None,
        pet_name: Optional[str] = None,
        pet_type: Optional[str] = None,
        notes: Optional[str] = None
    ) -> bool:
        """Update customer information."""
        # Get current customer data
        current = self.get_customer(customer_id)
        if not current:
            return False
            
        # Prepare update fields
        updates = []
        params = []
        
        if name and name != current['name']:
            updates.append("name = ?")
            params.append(name)
        if phone and phone != current['phone']:
            updates.append("phone = ?")
            params.append(phone)
        if email != current['email']:
            updates.append("email = ?")
            params.append(email)
        if address != current['address']:
            updates.append("address = ?")
            params.append(address)
        if pet_name != current['pet_name']:
            updates.append("pet_name = ?")
            params.append(pet_name)
        if pet_type != current['pet_type']:
            updates.append("pet_type = ?")
            params.append(pet_type)
        if notes != current['notes']:
            updates.append("notes = ?")
            params.append(notes)
            
        if not updates:
            return False
            
        query = f"UPDATE customers SET {', '.join(updates)} WHERE id = ?"
        params.append(customer_id)
        
        try:
            self.db.execute_query(query, tuple(params))
            logging.info(f"Updated customer ID {customer_id}")
            return True
        except sqlite3.IntegrityError:
            logging.warning(f"Phone number conflict when updating customer {customer_id}")
            raise ValueError("A customer with this phone number already exists")
    
    def search_customers(self, search_term: str) -> List[Dict]:
        """Search customers by name, phone, or pet name."""
        query = '''
            SELECT * FROM customers 
            WHERE name LIKE ? OR phone LIKE ? OR pet_name LIKE ?
            ORDER BY name
        '''
        search_param = f"%{search_term}%"
        results = self.db.execute_query(query, (search_param, search_param, search_param), fetch=True)
        
        customers = []
        for row in results:
            customers.append({
                'id': row[0],
                'name': row[1],
                'phone': row[2],
                'email': row[3],
                'address': row[4],
                'pet_name': row[5],
                'pet_type': row[6],
                'registration_date': row[7],
                'notes': row[8]
            })
        
        return customers

class InventoryManager:
    """Manages inventory-related operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def add_product(
        self,
        product_name: str,
        quantity: int,
        price: float,
        category: Optional[str] = None,
        barcode: Optional[str] = None,
        supplier: Optional[str] = None,
        min_stock_level: int = 0,
        notes: Optional[str] = None
    ) -> int:
        """Add a new product to inventory."""
        query = '''
            INSERT INTO inventory (
                product_name, category, quantity, price, barcode, 
                supplier, last_restock_date, min_stock_level, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        params = (
            product_name, category, quantity, price, barcode,
            supplier, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), min_stock_level, notes
        )
        
        try:
            self.db.execute_query(query, params)
            product_id = self.db.conn.cursor().lastrowid
            logging.info(f"Added new product: {product_name} (ID: {product_id})")
            return product_id
        except sqlite3.IntegrityError:
            logging.warning(f"Product with barcode {barcode} already exists")
            raise ValueError("A product with this barcode already exists")
    
    def get_product(self, product_id: int)
