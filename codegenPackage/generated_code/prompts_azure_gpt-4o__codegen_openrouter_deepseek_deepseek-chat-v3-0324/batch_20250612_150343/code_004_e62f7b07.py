"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a script to manage inventory for a glass installation company, tracking glass types (tempered, laminated), thickness, and associated hardware like roldanas and stainless steel fittings.
Generated: DETERMINISTIC_e62f7b073ca77245
Batch ID: 20250612_150343
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
from typing import List, Optional, Dict, Any
import sys

@dataclass
class GlassItem:
    id: int
    glass_type: str  # 'tempered' or 'laminated'
    thickness: float  # in millimeters
    quantity: int
    price_per_unit: float

@dataclass
class HardwareItem:
    id: int
    name: str  # e.g., 'roldana', 'stainless_steel_fitting'
    quantity: int
    price_per_unit: float

class InventoryManager:
    def __init__(self, db_path: str = 'inventory.db'):
        """Initialize the inventory manager with a SQLite database."""
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS glass_inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    glass_type TEXT NOT NULL CHECK(glass_type IN ('tempered', 'laminated')),
                    thickness REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    price_per_unit REAL NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS hardware_inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price_per_unit REAL NOT NULL
                )
            ''')
            conn.commit()

    def add_glass_item(self, glass_type: str, thickness: float, quantity: int, price_per_unit: float) -> int:
        """Add a new glass item to inventory."""
        if glass_type not in ('tempered', 'laminated'):
            raise ValueError("Glass type must be 'tempered' or 'laminated'")
        
        if thickness <= 0 or quantity < 0 or price_per_unit < 0:
            raise ValueError("Thickness, quantity, and price must be positive values")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO glass_inventory (glass_type, thickness, quantity, price_per_unit)
                VALUES (?, ?, ?, ?)
            ''', (glass_type, thickness, quantity, price_per_unit))
            conn.commit()
            return cursor.lastrowid

    def add_hardware_item(self, name: str, quantity: int, price_per_unit: float) -> int:
        """Add a new hardware item to inventory."""
        if quantity < 0 or price_per_unit < 0:
            raise ValueError("Quantity and price must be positive values")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO hardware_inventory (name, quantity, price_per_unit)
                VALUES (?, ?, ?)
            ''', (name, quantity, price_per_unit))
            conn.commit()
            return cursor.lastrowid

    def update_glass_quantity(self, item_id: int, quantity_change: int) -> None:
        """Update the quantity of a glass item."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE glass_inventory
                SET quantity = quantity + ?
                WHERE id = ?
            ''', (quantity_change, item_id))
            if cursor.rowcount == 0:
                raise ValueError(f"No glass item found with ID {item_id}")
            conn.commit()

    def update_hardware_quantity(self, item_id: int, quantity_change: int) -> None:
        """Update the quantity of a hardware item."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE hardware_inventory
                SET quantity = quantity + ?
                WHERE id = ?
            ''', (quantity_change, item_id))
            if cursor.rowcount == 0:
                raise ValueError(f"No hardware item found with ID {item_id}")
            conn.commit()

    def get_glass_inventory(self) -> List[GlassItem]:
        """Retrieve all glass items from inventory."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, glass_type, thickness, quantity, price_per_unit FROM glass_inventory')
            return [GlassItem(*row) for row in cursor.fetchall()]

    def get_hardware_inventory(self) -> List[HardwareItem]:
        """Retrieve all hardware items from inventory."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, quantity, price_per_unit FROM hardware_inventory')
            return [HardwareItem(*row) for row in cursor.fetchall()]

    def get_glass_item(self, item_id: int) -> Optional[GlassItem]:
        """Retrieve a specific glass item by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, glass_type, thickness, quantity, price_per_unit
                FROM glass_inventory
                WHERE id = ?
            ''', (item_id,))
            row = cursor.fetchone()
            return GlassItem(*row) if row else None

    def get_hardware_item(self, item_id: int) -> Optional[HardwareItem]:
        """Retrieve a specific hardware item by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, quantity, price_per_unit
                FROM hardware_inventory
                WHERE id = ?
            ''', (item_id,))
            row = cursor.fetchone()
            return HardwareItem(*row) if row else None

    def delete_glass_item(self, item_id: int) -> None:
        """Delete a glass item from inventory."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM glass_inventory WHERE id = ?', (item_id,))
            if cursor.rowcount == 0:
                raise ValueError(f"No glass item found with ID {item_id}")
            conn.commit()

    def delete_hardware_item(self, item_id: int) -> None:
        """Delete a hardware item from inventory."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM hardware_inventory WHERE id = ?', (item_id,))
            if cursor.rowcount == 0:
                raise ValueError(f"No hardware item found with ID {item_id}")
            conn.commit()

    def generate_inventory_report(self) -> Dict[str, Any]:
        """Generate a summary report of the inventory."""
        report = {
            'glass_items': [],
            'hardware_items': [],
            'total_glass_value': 0.0,
            'total_hardware_value': 0.0
        }

        glass_items = self.get_glass_inventory()
        for item in glass_items:
            item_value = item.quantity * item.price_per_unit
            report['glass_items'].append({
                'id': item.id,
                'type': item.glass_type,
                'thickness': item.thickness,
                'quantity': item.quantity,
                'value': item_value
            })
            report['total_glass_value'] += item_value

        hardware_items = self.get_hardware_inventory()
        for item in hardware_items:
            item_value = item.quantity * item.price_per_unit
            report['hardware_items'].append({
                'id': item.id,
                'name': item.name,
                'quantity': item.quantity,
                'value': item_value
            })
            report['total_hardware_value'] += item_value

        report['total_inventory_value'] = report['total_glass_value'] + report['total_hardware_value']
        return report

def main():
    """Example usage of the InventoryManager."""
    try:
        manager = InventoryManager()

        # Add some sample items
        glass_id = manager.add_glass_item('tempered', 6.0, 100, 50.0)
        hardware_id = manager.add_hardware_item('roldana', 200, 5.0)

        # Update quantities
        manager.update_glass_quantity(glass_id, -10)  # Sell 10 units
        manager.update_hardware_quantity(hardware_id, -20)  # Sell 20 units

        # Generate report
        report = manager.generate_inventory_report()
        print("Inventory Report:")
        print(f"Total Glass Value: ${report['total_glass_value']:.2f}")
        print(f"Total Hardware Value: ${report['total_hardware_value']:.2f}")
        print(f"Total Inventory Value: ${report['total_inventory_value']:.2f}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
