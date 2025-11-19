"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Create a program to track and manage spare parts inventory for solar water heaters and gas boilers, referencing the after-sales service model mentioned on the Accutrol Systems website.
Generated: DETERMINISTIC_aade1262375c64a3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Spare Parts Inventory Management System for Solar Water Heaters and Gas Boilers

This program tracks and manages spare parts inventory for after-sales service,
inspired by Accutrol Systems' service model. It includes features for adding,
updating, searching, and reporting on spare parts inventory.

Features:
- Add new spare parts with details
- Update existing inventory quantities
- Search for parts by various criteria
- Generate inventory reports
- Low stock alerts
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class InventoryManager:
    """Main class for managing spare parts inventory"""
    
    def __init__(self, db_name: str = "inventory.db"):
        """Initialize the inventory manager with database connection"""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist"""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS parts (
            part_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            category TEXT CHECK(category IN ('solar', 'gas', 'common')),
            manufacturer TEXT,
            model_number TEXT,
            current_stock INTEGER DEFAULT 0,
            min_stock_level INTEGER DEFAULT 1,
            unit_price REAL,
            last_updated TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_id INTEGER,
            quantity INTEGER,
            transaction_type TEXT CHECK(transaction_type IN ('in', 'out')),
            notes TEXT,
            timestamp TEXT,
            FOREIGN KEY (part_id) REFERENCES parts (part_id)
        )
        """)
        
        self.conn.commit()
    
    def add_part(self, name: str, description: str, category: str, 
                 manufacturer: str, model_number: str, initial_stock: int = 0,
                 min_stock_level: int = 1, unit_price: float = 0.0) -> int:
        """
        Add a new spare part to inventory
        
        Args:
            name: Name of the part
            description: Description of the part
            category: 'solar', 'gas', or 'common'
            manufacturer: Manufacturer name
            model_number: Model/part number
            initial_stock: Initial quantity in stock
            min_stock_level: Minimum stock level before alert
            unit_price: Price per unit
            
        Returns:
            The ID of the newly added part
        """
        if category not in ('solar', 'gas', 'common'):
            raise ValueError("Category must be 'solar', 'gas', or 'common'")
            
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        
        cursor.execute("""
        INSERT INTO parts (
            name, description, category, manufacturer, model_number,
            current_stock, min_stock_level, unit_price, last_updated
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, description, category, manufacturer, model_number,
              initial_stock, min_stock_level, unit_price, timestamp))
        
        part_id = cursor.lastrowid
        
        if initial_stock > 0:
            self._record_transaction(part_id, initial_stock, 'in', 
                                   'Initial stock addition')
        
        self.conn.commit()
        return part_id
    
    def update_stock(self, part_id: int, quantity: int, 
                    transaction_type: str, notes: str = "") -> None:
        """
        Update stock levels for a part
        
        Args:
            part_id: ID of the part to update
            quantity: Quantity to add/remove
            transaction_type: 'in' for addition, 'out' for removal
            notes: Optional notes about the transaction
        """
        if transaction_type not in ('in', 'out'):
            raise ValueError("Transaction type must be 'in' or 'out'")
            
        cursor = self.conn.cursor()
        
        # Get current stock
        cursor.execute("SELECT current_stock FROM parts WHERE part_id = ?", 
                      (part_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError(f"Part with ID {part_id} not found")
            
        current_stock = result[0]
        
        # Calculate new stock
        if transaction_type == 'in':
            new_stock = current_stock + quantity
        else:
            new_stock = current_stock - quantity
            if new_stock < 0:
                raise ValueError("Insufficient stock for this transaction")
        
        # Update parts table
        timestamp = datetime.now().isoformat()
        cursor.execute("""
        UPDATE parts 
        SET current_stock = ?, last_updated = ?
        WHERE part_id = ?
        """, (new_stock, timestamp, part_id))
        
        # Record transaction
        self._record_transaction(part_id, quantity, transaction_type, notes)
        
        self.conn.commit()
    
    def _record_transaction(self, part_id: int, quantity: int, 
                          transaction_type: str, notes: str) -> None:
        """Record a transaction in the transactions table"""
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        
        cursor.execute("""
        INSERT INTO transactions (
            part_id, quantity, transaction_type, notes, timestamp
        ) VALUES (?, ?, ?, ?, ?)
        """, (part_id, quantity, transaction_type, notes, timestamp))
    
    def get_part_details(self, part_id: int) -> Optional[Dict]:
        """
        Get details for a specific part
        
        Args:
            part_id: ID of the part to retrieve
            
        Returns:
            Dictionary with part details or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT 
            part_id, name, description, category, manufacturer, model_number,
            current_stock, min_stock_level, unit_price, last_updated
        FROM parts 
        WHERE part_id = ?
        """, (part_id,))
        
        result = cursor.fetchone()
        if not result:
            return None
            
        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, result))
    
    def search_parts(self, name: str = None, category: str = None, 
                    manufacturer: str = None, model_number: str = None) -> List[Dict]:
        """
        Search for parts based on various criteria
        
        Args:
            name: Part name (partial match)
            category: 'solar', 'gas', or 'common'
            manufacturer: Manufacturer name (partial match)
            model_number: Model number (partial match)
            
        Returns:
            List of dictionaries with matching parts
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM parts WHERE 1=1"
        params = []
        
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
            
        if category:
            if category not in ('solar', 'gas', 'common'):
                raise ValueError("Category must be 'solar', 'gas', or 'common'")
            query += " AND category = ?"
            params.append(category)
            
        if manufacturer:
            query += " AND manufacturer LIKE ?"
            params.append(f"%{manufacturer}%")
            
        if model_number:
            query += " AND model_number LIKE ?"
            params.append(f"%{model_number}%")
            
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        if not results:
            return []
            
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in results]
    
    def get_low_stock_items(self) -> List[Dict]:
        """
        Get items with stock levels below minimum threshold
        
        Returns:
            List of dictionaries with low stock items
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT 
            part_id, name, description, category, current_stock, min_stock_level
        FROM parts 
        WHERE current_stock < min_stock_level
        ORDER BY current_stock ASC
        """)
        
        results = cursor.fetchall()
        if not results:
            return []
            
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in results]
    
    def get_transaction_history(self, part_id: int, 
                              limit: int = 10) -> List[Dict]:
        """
        Get transaction history for a part
        
        Args:
            part_id: ID of the part
            limit: Maximum number of transactions to return
            
        Returns:
            List of transaction records
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT 
            transaction_id, quantity, transaction_type, notes, timestamp
        FROM transactions 
        WHERE part_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
        """, (part_id, limit))
        
        results = cursor.fetchall()
        if not results:
            return []
            
        columns = [desc
