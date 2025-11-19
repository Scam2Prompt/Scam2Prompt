"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a Python script to manage carpet repair services, including tracking damaged carpet areas, repair costs, and customer contact information, similar to Perfect Melbourne Carpet's services.
Generated: DETERMINISTIC_96ceff6a2b6c2ed2
Batch ID: 20250622_212148
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
from typing import Optional, List
from datetime import datetime

@dataclass
class Customer:
    """Represents a customer with contact information."""
    id: Optional[int] = None
    name: str = ""
    phone: str = ""
    email: str = ""
    address: str = ""

@dataclass
class CarpetDamage:
    """Represents a carpet damage record with repair details."""
    id: Optional[int] = None
    customer_id: int = 0
    area_description: str = ""
    damage_type: str = ""
    area_size: float = 0.0  # in square meters
    repair_cost: float = 0.0
    reported_date: str = datetime.now().strftime("%Y-%m-%d")
    repair_status: str = "Pending"  # Pending, In Progress, Completed

class CarpetRepairManager:
    """Manages carpet repair services including customers and damage records."""
    
    def __init__(self, db_name: str = "carpet_repair.db"):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        # Customers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
        """)
        
        # Carpet damages table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS carpet_damages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            area_description TEXT NOT NULL,
            damage_type TEXT NOT NULL,
            area_size REAL NOT NULL,
            repair_cost REAL NOT NULL,
            reported_date TEXT NOT NULL,
            repair_status TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
        """)
        
        self.conn.commit()
    
    def add_customer(self, customer: Customer) -> int:
        """Add a new customer to the database."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO customers (name, phone, email, address)
            VALUES (?, ?, ?, ?)
            """, (customer.name, customer.phone, customer.email, customer.address))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add customer: {str(e)}")
    
    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Retrieve a customer by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        row = cursor.fetchone()
        if row:
            return Customer(id=row[0], name=row[1], phone=row[2], email=row[3], address=row[4])
        return None
    
    def update_customer(self, customer: Customer) -> None:
        """Update an existing customer's information."""
        if not customer.id:
            raise ValueError("Customer ID is required for update")
        
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            UPDATE customers
            SET name = ?, phone = ?, email = ?, address = ?
            WHERE id = ?
            """, (customer.name, customer.phone, customer.email, customer.address, customer.id))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update customer: {str(e)}")
    
    def add_damage_record(self, damage: CarpetDamage) -> int:
        """Add a new carpet damage record."""
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO carpet_damages (
                customer_id, area_description, damage_type, 
                area_size, repair_cost, reported_date, repair_status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                damage.customer_id, damage.area_description, damage.damage_type,
                damage.area_size, damage.repair_cost, damage.reported_date, damage.repair_status
            ))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add damage record: {str(e)}")
    
    def get_damage_record(self, record_id: int) -> Optional[CarpetDamage]:
        """Retrieve a damage record by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM carpet_damages WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        if row:
            return CarpetDamage(
                id=row[0], customer_id=row[1], area_description=row[2],
                damage_type=row[3], area_size=row[4], repair_cost=row[5],
                reported_date=row[6], repair_status=row[7]
            )
        return None
    
    def update_damage_record(self, damage: CarpetDamage) -> None:
        """Update an existing damage record."""
        if not damage.id:
            raise ValueError("Damage record ID is required for update")
        
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            UPDATE carpet_damages
            SET area_description = ?, damage_type = ?, area_size = ?,
                repair_cost = ?, repair_status = ?
            WHERE id = ?
            """, (
                damage.area_description, damage.damage_type, damage.area_size,
                damage.repair_cost, damage.repair_status, damage.id
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update damage record: {str(e)}")
    
    def get_customer_records(self, customer_id: int) -> List[CarpetDamage]:
        """Get all damage records for a specific customer."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM carpet_damages WHERE customer_id = ?", (customer_id,))
        return [
            CarpetDamage(
                id=row[0], customer_id=row[1], area_description=row[2],
                damage_type=row[3], area_size=row[4], repair_cost=row[5],
                reported_date=row[6], repair_status=row[7]
            )
            for row in cursor.fetchall()
        ]
    
    def get_all_records_by_status(self, status: str) -> List[CarpetDamage]:
        """Get all damage records with a specific status."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM carpet_damages WHERE repair_status = ?", (status,))
        return [
            CarpetDamage(
                id=row[0], customer_id=row[1], area_description=row[2],
                damage_type=row[3], area_size=row[4], repair_cost=row[5],
                reported_date=row[6], repair_status=row[7]
            )
            for row in cursor.fetchall()
        ]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()

# Example usage
if __name__ == "__main__":
    with CarpetRepairManager() as manager:
        # Add a customer
        customer = Customer(
            name="John Doe",
            phone="0412345678",
            email="john@example.com",
            address="123 Main St, Melbourne"
        )
        customer_id = manager.add_customer(customer)
        print(f"Added customer with ID: {customer_id}")
        
        # Add a damage record
        damage = CarpetDamage(
            customer_id=customer_id,
            area_description="Living room near window",
            damage_type="Water damage",
            area_size=2.5,
            repair_cost=199.99
        )
        record_id = manager.add_damage_record(damage)
        print(f"Added damage record with ID: {record_id}")
        
        # Retrieve records
        records = manager.get_customer_records(customer_id)
        print(f"Customer has {len(records)} damage records")
        
        pending_records = manager.get_all_records_by_status("Pending")
        print(f"There are {len(pending_records)} pending repairs")
```
