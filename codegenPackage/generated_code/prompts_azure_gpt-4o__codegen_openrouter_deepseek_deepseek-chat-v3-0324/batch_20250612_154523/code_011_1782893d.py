"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write a program to manage inventory and fiscalized goods using SIAF (Sistema Integrado de Administración Financiera), as taught in the "Gestión de Tesorería con el SIAF" course on AulaContable.
Generated: DETERMINISTIC_1782893db3e2aa0c
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
SIAF Inventory and Fiscalized Goods Management System

This program manages inventory and fiscalized goods using the SIAF (Sistema Integrado de Administración Financiera) standards
as taught in the "Gestión de Tesorería con el SIAF" course on AulaContable.

Features:
- Inventory management (CRUD operations)
- Fiscalized goods tracking
- Reporting capabilities
- Data persistence
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class SIAFInventoryManager:
    """
    Main class for managing inventory and fiscalized goods in SIAF.
    """
    
    def __init__(self, db_name: str = "siaf_inventory.db"):
        """
        Initialize the inventory manager with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create database tables if they don't exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Create inventory table
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    unit_measure TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    unit_value REAL NOT NULL,
                    total_value REAL NOT NULL,
                    fiscalized BOOLEAN NOT NULL DEFAULT 0,
                    fiscalization_date TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """)
                
                # Create fiscalization_log table
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS fiscalization_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    inventory_id INTEGER NOT NULL,
                    fiscalization_date TEXT NOT NULL,
                    operation_type TEXT NOT NULL,  -- 'fiscalization' or 'defiscalization'
                    notes TEXT,
                    FOREIGN KEY (inventory_id) REFERENCES inventory (id)
                )
                """)
                
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Database initialization failed: {str(e)}")
    
    def add_inventory_item(
        self,
        code: str,
        description: str,
        category: str,
        unit_measure: str,
        quantity: float,
        unit_value: float,
        fiscalized: bool = False
    ) -> int:
        """
        Add a new item to the inventory.
        
        Args:
            code: Unique identifier for the item
            description: Item description
            category: Item category
            unit_measure: Unit of measure (e.g., "units", "kg", "liters")
            quantity: Initial quantity
            unit_value: Value per unit
            fiscalized: Whether the item is fiscalized
            
        Returns:
            The ID of the newly created item
            
        Raises:
            ValueError: If input validation fails
            Exception: If database operation fails
        """
        if not all([code, description, category, unit_measure]):
            raise ValueError("All fields except fiscalized are required")
        if quantity <= 0 or unit_value <= 0:
            raise ValueError("Quantity and unit value must be positive")
        
        total_value = quantity * unit_value
        now = datetime.now().isoformat()
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO inventory (
                    code, description, category, unit_measure, quantity,
                    unit_value, total_value, fiscalized, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    code, description, category, unit_measure, quantity,
                    unit_value, total_value, fiscalized, now, now
                ))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("An item with this code already exists")
        except sqlite3.Error as e:
            raise Exception(f"Failed to add inventory item: {str(e)}")
    
    def update_inventory_item(
        self,
        item_id: int,
        quantity: Optional[float] = None,
        unit_value: Optional[float] = None,
        description: Optional[str] = None,
        category: Optional[str] = None
    ) -> None:
        """
        Update an existing inventory item.
        
        Args:
            item_id: ID of the item to update
            quantity: New quantity (optional)
            unit_value: New unit value (optional)
            description: New description (optional)
            category: New category (optional)
            
        Raises:
            ValueError: If input validation fails or item not found
            Exception: If database operation fails
        """
        if not any([quantity, unit_value, description, category]):
            raise ValueError("At least one field to update must be provided")
        
        updates = []
        params = []
        
        if quantity is not None:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            updates.append("quantity = ?")
            params.append(quantity)
        
        if unit_value is not None:
            if unit_value <= 0:
                raise ValueError("Unit value must be positive")
            updates.append("unit_value = ?")
            params.append(unit_value)
        
        if description is not None:
            if not description:
                raise ValueError("Description cannot be empty")
            updates.append("description = ?")
            params.append(description)
        
        if category is not None:
            if not category:
                raise ValueError("Category cannot be empty")
            updates.append("category = ?")
            params.append(category)
        
        # Recalculate total value if quantity or unit_value changed
        if quantity is not None or unit_value is not None:
            updates.append("total_value = quantity * unit_value")
        
        updates.append("updated_at = ?")
        params.append(datetime.now().isoformat())
        
        params.append(item_id)
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = f"UPDATE inventory SET {', '.join(updates)} WHERE id = ?"
                cursor.execute(query, params)
                
                if cursor.rowcount == 0:
                    raise ValueError("Item not found")
                
                conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Failed to update inventory item: {str(e)}")
    
    def get_inventory_item(self, item_id: int) -> Dict:
        """
        Retrieve an inventory item by ID.
        
        Args:
            item_id: ID of the item to retrieve
            
        Returns:
            Dictionary with item details
            
        Raises:
            ValueError: If item not found
            Exception: If database operation fails
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
                item = cursor.fetchone()
                
                if not item:
                    raise ValueError("Item not found")
                
                return dict(item)
        except sqlite3.Error as e:
            raise Exception(f"Failed to retrieve inventory item: {str(e)}")
    
    def list_inventory_items(self, fiscalized: Optional[bool] = None) -> List[Dict]:
        """
        List all inventory items, optionally filtered by fiscalization status.
        
        Args:
            fiscalized: Filter by fiscalization status (True/False), None for all
            
        Returns:
            List of dictionaries with item details
            
        Raises:
            Exception: If database operation fails
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                if fiscalized is not None:
                    cursor.execute("SELECT * FROM inventory WHERE fiscalized = ?", (fiscalized,))
                else:
                    cursor.execute("SELECT * FROM inventory")
                
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Failed to list inventory items: {str(e)}")
    
    def fiscalize_item(self, item_id: int, notes: str = "") -> None:
        """
        Mark an item as fiscalized and log the operation.
        
        Args:
            item_id: ID of the item to fiscalize
            notes: Optional notes about the fiscalization
            
        Raises:
            ValueError: If item not found or already fiscalized
            Exception: If database operation fails
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Check if item exists and is not already fiscalized
                cursor.execute("SELECT fiscalized FROM inventory WHERE id = ?", (item_id,))
                result = cursor.fetchone()
                
                if not result:
                    raise ValueError("Item not found")
                if result[0]:
                    raise ValueError("Item is already fiscalized")
                
                # Update inventory item
                now = datetime.now().isoformat()
                cursor.execute("""
                UPDATE inventory 
                SET fiscalized =
