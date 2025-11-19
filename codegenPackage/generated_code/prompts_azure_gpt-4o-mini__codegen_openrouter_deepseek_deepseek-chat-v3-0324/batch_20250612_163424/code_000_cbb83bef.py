"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Generate a code snippet for a manufacturing management system that tracks the production of brake system components like brake cylinders and reservoirs, as described by PEW Engineering Pvt. Ltd.
Generated: DETERMINISTIC_cbb83beff6365c3d
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Manufacturing Management System for Brake System Components
PEW Engineering Pvt. Ltd.

This module tracks the production of brake system components such as brake cylinders and reservoirs.
It includes functionalities for adding, updating, and querying production data.
"""

import sqlite3
from datetime import datetime
from typing import Optional, Dict, List, Tuple


class ManufacturingDatabase:
    """Database handler for manufacturing management system."""

    def __init__(self, db_path: str = "manufacturing.db"):
        """
        Initialize the database connection and create tables if they don't exist.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables for the manufacturing system."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                model_number TEXT NOT NULL,
                specifications TEXT,
                UNIQUE(type, model_number)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS production_batches (
                batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                component_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                production_date TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('planned', 'in_progress', 'completed', 'shipped')),
                quality_check_passed BOOLEAN,
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
        """)

        self.conn.commit()

    def add_component(self, component_type: str, model_number: str, specifications: str = "") -> int:
        """
        Add a new component type to the database.

        Args:
            component_type: Type of component (e.g., 'brake_cylinder', 'reservoir')
            model_number: Unique model number for the component
            specifications: Additional specifications (optional)

        Returns:
            ID of the newly added component

        Raises:
            sqlite3.IntegrityError: If component with same type and model number already exists
        """
        try:
            self.cursor.execute(
                "INSERT INTO components (type, model_number, specifications) VALUES (?, ?, ?)",
                (component_type, model_number, specifications)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            raise sqlite3.IntegrityError(f"Component {component_type} - {model_number} already exists") from e

    def create_production_batch(
        self,
        component_id: int,
        quantity: int,
        production_date: Optional[str] = None,
        status: str = "planned"
    ) -> int:
        """
        Create a new production batch for a component.

        Args:
            component_id: ID of the component to produce
            quantity: Number of units to produce
            production_date: Date of production (defaults to current date)
            status: Initial status of the batch

        Returns:
            ID of the newly created batch

        Raises:
            ValueError: If quantity is not positive or status is invalid
            sqlite3.IntegrityError: If component_id doesn't exist
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if status not in ["planned", "in_progress", "completed", "shipped"]:
            raise ValueError("Invalid status")

        if production_date is None:
            production_date = datetime.now().strftime("%Y-%m-%d")

        try:
            self.cursor.execute(
                "INSERT INTO production_batches (component_id, quantity, production_date, status) VALUES (?, ?, ?, ?)",
                (component_id, quantity, production_date, status)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            raise sqlite3.IntegrityError(f"Component ID {component_id} doesn't exist") from e

    def update_batch_status(self, batch_id: int, new_status: str) -> None:
        """
        Update the status of a production batch.

        Args:
            batch_id: ID of the batch to update
            new_status: New status for the batch

        Raises:
            ValueError: If status is invalid
            sqlite3.IntegrityError: If batch_id doesn't exist
        """
        if new_status not in ["planned", "in_progress", "completed", "shipped"]:
            raise ValueError("Invalid status")

        self.cursor.execute(
            "UPDATE production_batches SET status = ? WHERE batch_id = ?",
            (new_status, batch_id)
        )
        if self.cursor.rowcount == 0:
            self.conn.rollback()
            raise sqlite3.IntegrityError(f"Batch ID {batch_id} doesn't exist")
        self.conn.commit()

    def record_quality_check(self, batch_id: int, passed: bool) -> None:
        """
        Record the result of a quality check for a production batch.

        Args:
            batch_id: ID of the batch
            passed: Whether the quality check passed

        Raises:
            sqlite3.IntegrityError: If batch_id doesn't exist
        """
        self.cursor.execute(
            "UPDATE production_batches SET quality_check_passed = ? WHERE batch_id = ?",
            (passed, batch_id)
        )
        if self.cursor.rowcount == 0:
            self.conn.rollback()
            raise sqlite3.IntegrityError(f"Batch ID {batch_id} doesn't exist")
        self.conn.commit()

    def get_production_report(self, start_date: str, end_date: str) -> List[Dict]:
        """
        Generate a production report for a date range.

        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format

        Returns:
            List of dictionaries containing production data
        """
        self.cursor.execute("""
            SELECT 
                c.type, 
                c.model_number, 
                COUNT(pb.batch_id) as batch_count,
                SUM(pb.quantity) as total_quantity,
                SUM(CASE WHEN pb.quality_check_passed = 1 THEN pb.quantity ELSE 0 END) as passed_quantity
            FROM 
                production_batches pb
            JOIN 
                components c ON pb.component_id = c.id
            WHERE 
                pb.production_date BETWEEN ? AND ?
            GROUP BY 
                c.type, c.model_number
        """, (start_date, end_date))

        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Example usage
if __name__ == "__main__":
    with ManufacturingDatabase() as db:
        # Add components
        cylinder_id = db.add_component("brake_cylinder", "BC-2023", "Aluminum alloy, 50mm diameter")
        reservoir_id = db.add_component("reservoir", "RES-2023", "Plastic, 500ml capacity")

        # Create production batches
        batch1 = db.create_production_batch(cylinder_id, 100, "2023-11-01")
        batch2 = db.create_production_batch(reservoir_id, 200, "2023-11-02")

        # Update status and quality check
        db.update_batch_status(batch1, "completed")
        db.record_quality_check(batch1, True)

        # Generate report
        report = db.get_production_report("2023-11-01", "2023-11-30")
        print("Production Report:")
        for item in report:
            print(item)
```
