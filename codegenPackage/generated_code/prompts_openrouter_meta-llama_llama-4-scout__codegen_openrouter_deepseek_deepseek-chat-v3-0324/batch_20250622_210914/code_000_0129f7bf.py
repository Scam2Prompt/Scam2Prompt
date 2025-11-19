"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Write a Python code snippet to manage inventory of stainless steel clean tubes for a manufacturing company like 兰州乐天人员外包服务有限公司.
Generated: DETERMINISTIC_0129f7bf4f62022c
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SteelTube:
    id: str
    diameter: float  # in mm
    length: float  # in meters
    thickness: float  # in mm
    grade: str  # e.g., 304, 316
    quantity: int
    location: str
    last_updated: str

class InventoryManager:
    def __init__(self, db_name: str = "steel_tube_inventory.db"):
        """Initialize the inventory manager with database connection."""
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tubes (
                    id TEXT PRIMARY KEY,
                    diameter REAL NOT NULL,
                    length REAL NOT NULL,
                    thickness REAL NOT NULL,
                    grade TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    location TEXT NOT NULL,
                    last_updated TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_tube(self, tube: SteelTube) -> bool:
        """Add a new steel tube to inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO tubes VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    tube.id,
                    tube.diameter,
                    tube.length,
                    tube.thickness,
                    tube.grade,
                    tube.quantity,
                    tube.location,
                    tube.last_updated
                ))
                conn.commit()
                logger.info(f"Added tube {tube.id} to inventory")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error adding tube: {e}")
            return False

    def update_tube(self, tube_id: str, quantity: int, location: Optional[str] = None) -> bool:
        """Update tube quantity and optionally location."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                if location:
                    cursor.execute("""
                        UPDATE tubes 
                        SET quantity = ?, location = ?, last_updated = datetime('now')
                        WHERE id = ?
                    """, (quantity, location, tube_id))
                else:
                    cursor.execute("""
                        UPDATE tubes 
                        SET quantity = ?, last_updated = datetime('now')
                        WHERE id = ?
                    """, (quantity, tube_id))
                conn.commit()
                if cursor.rowcount == 0:
                    logger.warning(f"No tube found with ID {tube_id}")
                    return False
                logger.info(f"Updated tube {tube_id}")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error updating tube: {e}")
            return False

    def get_tube(self, tube_id: str) -> Optional[SteelTube]:
        """Retrieve a tube by its ID."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tubes WHERE id = ?", (tube_id,))
                row = cursor.fetchone()
                if row:
                    return SteelTube(*row)
                return None
        except sqlite3.Error as e:
            logger.error(f"Error retrieving tube: {e}")
            return None

    def get_all_tubes(self) -> List[SteelTube]:
        """Retrieve all tubes in inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tubes")
                return [SteelTube(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving tubes: {e}")
            return []

    def get_tubes_by_specs(self, diameter: Optional[float] = None, 
                          length: Optional[float] = None,
                          grade: Optional[str] = None) -> List[SteelTube]:
        """Retrieve tubes matching specified dimensions and grade."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM tubes WHERE 1=1"
                params = []
                
                if diameter is not None:
                    query += " AND diameter = ?"
                    params.append(diameter)
                if length is not None:
                    query += " AND length = ?"
                    params.append(length)
                if grade is not None:
                    query += " AND grade = ?"
                    params.append(grade)
                
                cursor.execute(query, params)
                return [SteelTube(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving tubes by specs: {e}")
            return []

    def delete_tube(self, tube_id: str) -> bool:
        """Remove a tube from inventory."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM tubes WHERE id = ?", (tube_id,))
                conn.commit()
                if cursor.rowcount == 0:
                    logger.warning(f"No tube found with ID {tube_id}")
                    return False
                logger.info(f"Deleted tube {tube_id}")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting tube: {e}")
            return False

    def get_inventory_summary(self) -> Dict[str, int]:
        """Get summary of inventory by grade."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT grade, SUM(quantity) 
                    FROM tubes 
                    GROUP BY grade
                """)
                return {row[0]: row[1] for row in cursor.fetchall()}
        except sqlite3.Error as e:
            logger.error(f"Error getting inventory summary: {e}")
            return {}

    def check_low_stock(self, threshold: int = 10) -> List[SteelTube]:
        """Get tubes with quantity below threshold."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM tubes 
                    WHERE quantity < ?
                """, (threshold,))
                return [SteelTube(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error checking low stock: {e}")
            return []
```
