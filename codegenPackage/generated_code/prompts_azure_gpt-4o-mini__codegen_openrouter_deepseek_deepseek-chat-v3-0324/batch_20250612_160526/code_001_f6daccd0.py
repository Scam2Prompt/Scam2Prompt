"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: How can I implement a recycling management system that tracks electronic waste, inspired by the practices of SCR Reciclados?
Generated: DETERMINISTIC_f6daccd07b85d5c6
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electronic Waste Recycling Management System
Inspired by SCR Reciclados practices

This system tracks electronic waste (e-waste) through the recycling process,
from collection to final disposal, with proper categorization and reporting.
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import sqlite3
from contextlib import contextmanager

# Database setup constants
DB_NAME = "ewaste_recycling.db"
INIT_DB_SCRIPT = """
CREATE TABLE IF NOT EXISTS waste_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    weight REAL NOT NULL,
    collection_date TEXT NOT NULL,
    source TEXT NOT NULL,
    status TEXT NOT NULL,
    processing_steps TEXT,
    final_disposition TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS processing_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    waste_item_id INTEGER NOT NULL,
    process_date TEXT NOT NULL,
    process_type TEXT NOT NULL,
    technician TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (waste_item_id) REFERENCES waste_items(id)
);

CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_type TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit TEXT NOT NULL,
    last_updated TEXT NOT NULL
);
"""

class WasteCategory(Enum):
    """Categories of electronic waste"""
    COMPUTERS = "Computers and Laptops"
    MOBILES = "Mobile Phones"
    TVS = "Televisions"
    APPLIANCES = "Household Appliances"
    BATTERIES = "Batteries"
    OTHER = "Other Electronic Waste"

class WasteStatus(Enum):
    """Status of waste item in recycling process"""
    COLLECTED = "Collected"
    SORTED = "Sorted"
    DISMANTLED = "Dismantled"
    PROCESSED = "Processed"
    RECYCLED = "Recycled"
    DISPOSED = "Disposed"

@dataclass
class WasteItem:
    """Represents an electronic waste item in the system"""
    id: Optional[int] = None
    category: Optional[WasteCategory] = None
    weight: Optional[float] = None
    collection_date: Optional[str] = None
    source: Optional[str] = None
    status: Optional[WasteStatus] = None
    processing_steps: Optional[str] = None
    final_disposition: Optional[str] = None
    notes: Optional[str] = None

@dataclass
class ProcessingLog:
    """Log entry for processing steps applied to waste items"""
    id: Optional[int] = None
    waste_item_id: Optional[int] = None
    process_date: Optional[str] = None
    process_type: Optional[str] = None
    technician: Optional[str] = None
    notes: Optional[str] = None

@dataclass
class InventoryItem:
    """Represents recycled materials in inventory"""
    id: Optional[int] = None
    material_type: Optional[str] = None
    quantity: Optional[float] = None
    unit: Optional[str] = None
    last_updated: Optional[str] = None

@contextmanager
def db_connection():
    """Context manager for database connections"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    finally:
        conn.close()

def initialize_database():
    """Initialize the database with required tables"""
    with db_connection() as conn:
        conn.executescript(INIT_DB_SCRIPT)
        conn.commit()

class RecyclingSystem:
    """Main class for the recycling management system"""
    
    def __init__(self):
        initialize_database()
    
    def add_waste_item(self, item: WasteItem) -> int:
        """Add a new waste item to the system"""
        if not all([item.category, item.weight, item.source]):
            raise ValueError("Missing required fields for waste item")
            
        with db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO waste_items (
                    category, weight, collection_date, source, status,
                    processing_steps, final_disposition, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.category.value,
                    item.weight,
                    item.collection_date or datetime.date.today().isoformat(),
                    item.source,
                    item.status.value if item.status else WasteStatus.COLLECTED.value,
                    item.processing_steps,
                    item.final_disposition,
                    item.notes
                )
            )
            conn.commit()
            return cursor.lastrowid
    
    def update_waste_item(self, item: WasteItem) -> bool:
        """Update an existing waste item"""
        if not item.id:
            raise ValueError("Item ID is required for update")
            
        with db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE waste_items SET
                    category = ?,
                    weight = ?,
                    collection_date = ?,
                    source = ?,
                    status = ?,
                    processing_steps = ?,
                    final_disposition = ?,
                    notes = ?
                WHERE id = ?
                """,
                (
                    item.category.value if item.category else None,
                    item.weight,
                    item.collection_date,
                    item.source,
                    item.status.value if item.status else None,
                    item.processing_steps,
                    item.final_disposition,
                    item.notes,
                    item.id
                )
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def get_waste_item(self, item_id: int) -> Optional[WasteItem]:
        """Retrieve a waste item by ID"""
        with db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM waste_items WHERE id = ?", (item_id,))
            row = cursor.fetchone()
            if row:
                return WasteItem(
                    id=row['id'],
                    category=WasteCategory(row['category']),
                    weight=row['weight'],
                    collection_date=row['collection_date'],
                    source=row['source'],
                    status=WasteStatus(row['status']),
                    processing_steps=row['processing_steps'],
                    final_disposition=row['final_disposition'],
                    notes=row['notes']
                )
            return None
    
    def add_processing_log(self, log: ProcessingLog) -> int:
        """Add a processing log entry"""
        if not all([log.waste_item_id, log.process_type, log.technician]):
            raise ValueError("Missing required fields for processing log")
            
        with db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO processing_logs (
                    waste_item_id, process_date, process_type, technician, notes
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    log.waste_item_id,
                    log.process_date or datetime.date.today().isoformat(),
                    log.process_type,
                    log.technician,
                    log.notes
                )
            )
            conn.commit()
            return cursor.lastrowid
    
    def get_processing_logs(self, waste_item_id: int) -> List[ProcessingLog]:
        """Get all processing logs for a waste item"""
        with db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM processing_logs WHERE waste_item_id = ?",
                (waste_item_id,)
            )
            return [
                ProcessingLog(
                    id=row['id'],
                    waste_item_id=row['waste_item_id'],
                    process_date=row['process_date'],
                    process_type=row['process_type'],
                    technician=row['technician'],
                    notes=row['notes']
                )
                for row in cursor.fetchall()
            ]
    
    def update_inventory(self, item: InventoryItem) -> int:
        """Add or update inventory item"""
        if not all([item.material_type, item.quantity, item.unit]):
            raise ValueError("Missing required fields for inventory item")
            
        with db_connection() as conn:
            cursor = conn.cursor()
            
            # Check if item exists
            cursor.execute(
                "SELECT id FROM inventory WHERE material_type = ?",
                (item.material_type,)
            )
            existing = cursor.fetchone()
            
            if existing and item.id is None:
                item.id = existing['id']
            
            if item.id:
                # Update existing
                cursor.execute(
                    """
                    UPDATE inventory SET
                        quantity = ?,
                        unit = ?,
                        last_updated = ?
                    WHERE id = ?
                    """,
                    (
                        item.quantity,
                        item.unit,
                        datetime.date.today().isoformat(),
                        item.id
                    )
                )
            else:
                # Insert new
                cursor.execute(
                    """
                    INSERT INTO inventory (
                        material_type, quantity, unit, last_updated
                    ) VALUES (?, ?, ?, ?)
                    """,
                    (
                        item.material_type,
                        item.quantity,
                        item.unit,
                        datetime.date.today().isoformat()
                    )
                )
                item.id = cursor.lastrowid
