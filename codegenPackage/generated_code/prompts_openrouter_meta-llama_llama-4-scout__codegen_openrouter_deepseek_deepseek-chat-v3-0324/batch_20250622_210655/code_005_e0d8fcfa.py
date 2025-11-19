"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Develop a system for tracking and managing inventory of fabrics, threads, and other sewing materials for a workshop, including features for supplier management and material requisition."
Generated: DETERMINISTIC_e0d8fcfad08e442f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabric_inventory_system.py
# A system for tracking and managing inventory of sewing materials

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class DatabaseManager:
    """Handles database connection and operations"""
    def __init__(self, db_name: str = "sewing_inventory.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._initialize_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def _initialize_database(self):
        """Create tables if they don't exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_person TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS materials (
                material_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                unit TEXT NOT NULL,
                min_stock_level INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                material_id INTEGER NOT NULL,
                supplier_id INTEGER,
                quantity REAL NOT NULL,
                unit_cost REAL NOT NULL,
                batch_number TEXT,
                expiry_date TEXT,
                received_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (material_id) REFERENCES materials(material_id),
                FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS requisitions (
                requisition_id INTEGER PRIMARY KEY AUTOINCREMENT,
                requester_name TEXT NOT NULL,
                project_name TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS requisition_items (
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                requisition_id INTEGER NOT NULL,
                material_id INTEGER NOT NULL,
                quantity REAL NOT NULL,
                FOREIGN KEY (requisition_id) REFERENCES requisitions(requisition_id),
                FOREIGN KEY (material_id) REFERENCES materials(material_id)
            )
        """)

class SupplierManager:
    """Handles supplier operations"""
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_supplier(self, name: str, contact_person: str = None, phone: str = None,
                    email: str = None, address: str = None) -> int:
        """Add a new supplier to the database"""
        with self.db as db:
            db.cursor.execute("""
                INSERT INTO suppliers (name, contact_person, phone, email, address)
                VALUES (?, ?, ?, ?, ?)
            """, (name, contact_person, phone, email, address))
            return db.cursor.lastrowid

    def get_supplier(self, supplier_id: int) -> Optional[Dict]:
        """Get supplier details by ID"""
        with self.db as db:
            db.cursor.execute("SELECT * FROM suppliers WHERE supplier_id = ?", (supplier_id,))
            row = db.cursor.fetchone()
            if row:
                return {
                    'supplier_id': row[0],
                    'name': row[1],
                    'contact_person': row[2],
                    'phone': row[3],
                    'email': row[4],
                    'address': row[5],
                    'created_at': row[6]
                }
            return None

    def list_suppliers(self) -> List[Dict]:
        """List all suppliers"""
        with self.db as db:
            db.cursor.execute("SELECT * FROM suppliers ORDER BY name")
            return [{
                'supplier_id': row[0],
                'name': row[1],
                'contact_person': row[2],
                'phone': row[3],
                'email': row[4],
                'address': row[5],
                'created_at': row[6]
            } for row in db.cursor.fetchall()]

    def update_supplier(self, supplier_id: int, **kwargs) -> bool:
        """Update supplier information"""
        valid_fields = ['name', 'contact_person', 'phone', 'email', 'address']
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            return False

        set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
        values = list(updates.values())
        values.append(supplier_id)

        with self.db as db:
            db.cursor.execute(f"""
                UPDATE suppliers SET {set_clause} WHERE supplier_id = ?
            """, values)
            return db.cursor.rowcount > 0

class MaterialManager:
    """Handles material operations"""
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_material(self, name: str, category: str, unit: str,
                    description: str = None, min_stock_level: int = 0) -> int:
        """Add a new material to the database"""
        with self.db as db:
            db.cursor.execute("""
                INSERT INTO materials (name, category, description, unit, min_stock_level)
                VALUES (?, ?, ?, ?, ?)
            """, (name, category, description, unit, min_stock_level))
            return db.cursor.lastrowid

    def get_material(self, material_id: int) -> Optional[Dict]:
        """Get material details by ID"""
        with self.db as db:
            db.cursor.execute("SELECT * FROM materials WHERE material_id = ?", (material_id,))
            row = db.cursor.fetchone()
            if row:
                return {
                    'material_id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'description': row[3],
                    'unit': row[4],
                    'min_stock_level': row[5],
                    'created_at': row[6]
                }
            return None

    def list_materials(self) -> List[Dict]:
        """List all materials"""
        with self.db as db:
            db.cursor.execute("SELECT * FROM materials ORDER BY name")
            return [{
                'material_id': row[0],
                'name': row[1],
                'category': row[2],
                'description': row[3],
                'unit': row[4],
                'min_stock_level': row[5],
                'created_at': row[6]
            } for row in db.cursor.fetchall()]

    def update_material(self, material_id: int, **kwargs) -> bool:
        """Update material information"""
        valid_fields = ['name', 'category', 'description', 'unit', 'min_stock_level']
        updates = {k: v for k, v in kwargs.items() if k in valid_fields}
        
        if not updates:
            return False

        set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
        values = list(updates.values())
        values.append(material_id)

        with self.db as db:
            db.cursor.execute(f"""
                UPDATE materials SET {set_clause} WHERE material_id = ?
            """, values)
            return db.cursor.rowcount > 0

class InventoryManager:
    """Handles inventory operations"""
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_inventory(self, material_id: int, quantity: float, unit_cost: float,
                     supplier_id: int = None, batch_number: str = None,
                     expiry_date: str = None) -> int:
        """Add inventory stock"""
        with self.db as db:
            db.cursor.execute("""
                INSERT INTO inventory (
                    material_id, supplier_id, quantity, unit_cost,
                    batch_number, expiry_date
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (material_id, supplier_id, quantity, unit_cost, batch_number, expiry_date))
            return db.cursor.lastrowid

    def get_inventory(self, inventory_id: int) -> Optional[Dict]:
        """Get inventory item by ID"""
        with self.db as db:
            db.cursor.execute("""
                SELECT i.*, m.name as material_name, m.unit as material_unit,
                       s.name as supplier_name
                FROM inventory i
                LEFT JOIN materials m ON i.material_id = m.material_id
                LEFT JOIN suppliers s ON i.supplier_id = s.supplier_id
                WHERE i.inventory_id = ?
            """, (inventory_id,))
