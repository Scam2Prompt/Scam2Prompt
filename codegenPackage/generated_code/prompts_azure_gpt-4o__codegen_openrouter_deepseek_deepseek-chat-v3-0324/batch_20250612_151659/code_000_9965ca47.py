"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Write Python code to integrate an inventory management system for tracking the availability of stainless steel, aluminum, copper, and other metals, using a database schema tailored for Meta+ product categories.
Generated: DETERMINISTIC_9965ca47193440db
Batch ID: 20250612_151659
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
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class MetalInventory:
    """Data class representing a metal inventory item."""
    id: int
    metal_type: str
    category: str
    quantity: float
    unit: str
    threshold: float
    supplier: str
    last_updated: str

class InventoryManager:
    """Class to manage metal inventory operations."""
    
    def __init__(self, db_path: str = 'metal_inventory.db'):
        """Initialize the inventory manager with database connection."""
        self.db_path = db_path
        self._create_tables()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Create and return a database connection."""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS metals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            metal_type TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity REAL NOT NULL,
            unit TEXT NOT NULL,
            threshold REAL NOT NULL,
            supplier TEXT,
            last_updated TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self._get_connection() as conn:
                conn.execute(create_table_sql)
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating tables: {e}")
            raise
    
    def add_metal(self, metal_type: str, category: str, quantity: float, 
                 unit: str, threshold: float, supplier: str) -> int:
        """Add a new metal to inventory."""
        sql = """
        INSERT INTO metals (metal_type, category, quantity, unit, threshold, supplier)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (metal_type, category, quantity, unit, threshold, supplier))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error adding metal: {e}")
            raise
    
    def update_quantity(self, metal_id: int, quantity_change: float) -> bool:
        """Update the quantity of a metal in inventory."""
        sql = """
        UPDATE metals 
        SET quantity = quantity + ?, 
            last_updated = CURRENT_TIMESTAMP
        WHERE id = ?
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (quantity_change, metal_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            logger.error(f"Error updating quantity: {e}")
            raise
    
    def get_metal(self, metal_id: int) -> Optional[MetalInventory]:
        """Get a metal inventory item by ID."""
        sql = "SELECT * FROM metals WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (metal_id,))
                row = cursor.fetchone()
                if row:
                    return MetalInventory(**row)
                return None
        except sqlite3.Error as e:
            logger.error(f"Error getting metal: {e}")
            raise
    
    def get_all_metals(self) -> List[MetalInventory]:
        """Get all metal inventory items."""
        sql = "SELECT * FROM metals"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                return [MetalInventory(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting all metals: {e}")
            raise
    
    def get_low_stock(self) -> List[MetalInventory]:
        """Get metals with quantity below threshold."""
        sql = "SELECT * FROM metals WHERE quantity < threshold"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                return [MetalInventory(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting low stock metals: {e}")
            raise
    
    def delete_metal(self, metal_id: int) -> bool:
        """Delete a metal from inventory."""
        sql = "DELETE FROM metals WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (metal_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            logger.error(f"Error deleting metal: {e}")
            raise
    
    def get_metals_by_category(self, category: str) -> List[MetalInventory]:
        """Get metals by category."""
        sql = "SELECT * FROM metals WHERE category = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (category,))
                return [MetalInventory(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting metals by category: {e}")
            raise
    
    def get_metals_by_type(self, metal_type: str) -> List[MetalInventory]:
        """Get metals by type."""
        sql = "SELECT * FROM metals WHERE metal_type = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (metal_type,))
                return [MetalInventory(**row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting metals by type: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        manager = InventoryManager()
        
        # Add sample metals
        manager.add_metal("Stainless Steel", "Sheet", 100.0, "kg", 20.0, "Supplier A")
        manager.add_metal("Aluminum", "Bar", 50.0, "kg", 10.0, "Supplier B")
        manager.add_metal("Copper", "Wire", 200.0, "m", 50.0, "Supplier C")
        
        # Get all metals
        metals = manager.get_all_metals()
        for metal in metals:
            print(f"{metal.metal_type} ({metal.category}): {metal.quantity}{metal.unit}")
        
        # Get low stock items
        low_stock = manager.get_low_stock()
        print("\nLow stock items:")
        for item in low_stock:
            print(f"{item.metal_type} is below threshold ({item.quantity}{item.unit} < {item.threshold}{item.unit})")
        
    except Exception as e:
        logger.error(f"Application error: {e}")
```
