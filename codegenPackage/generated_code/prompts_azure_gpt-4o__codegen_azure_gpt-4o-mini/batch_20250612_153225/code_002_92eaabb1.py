"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Generate a script to manage lease administration and property management reporting, using features mentioned in Vital Corporate Solutions' property manager VA services.
Generated: DETERMINISTIC_92eaabb150a9465c
Batch ID: 20250612_153225
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
from typing import List, Tuple, Optional

# Database connection and setup
class Database:
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for lease administration and property management."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS leases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                property_id INTEGER,
                tenant_name TEXT NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE NOT NULL,
                rent_amount REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (property_id) REFERENCES properties (id)
            )
        ''')
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Property management class
class PropertyManager:
    def __init__(self, db: Database):
        """Initialize the property manager with a database instance."""
        self.db = db

    def add_property(self, name: str, address: str) -> None:
        """Add a new property to the database."""
        try:
            self.db.cursor.execute('''
                INSERT INTO properties (name, address) VALUES (?, ?)
            ''', (name, address))
            self.db.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding property: {e}")

    def add_lease(self, property_id: int, tenant_name: str, start_date: str, end_date: str, rent_amount: float) -> None:
        """Add a new lease to the database."""
        try:
            self.db.cursor.execute('''
                INSERT INTO leases (property_id, tenant_name, start_date, end_date, rent_amount) 
                VALUES (?, ?, ?, ?, ?)
            ''', (property_id, tenant_name, start_date, end_date, rent_amount))
            self.db.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding lease: {e}")

    def get_property_report(self) -> List[Tuple]:
        """Generate a report of all properties and their leases."""
        try:
            self.db.cursor.execute('''
                SELECT p.id, p.name, p.address, l.tenant_name, l.start_date, l.end_date, l.rent_amount
                FROM properties p
                LEFT JOIN leases l ON p.id = l.property_id
            ''')
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error generating property report: {e}")
            return []

# Main execution
if __name__ == "__main__":
    # Initialize the database
    db = Database('property_management.db')
    
    # Create a property manager instance
    manager = PropertyManager(db)

    # Example usage
    manager.add_property("Sunset Apartments", "123 Sunset Blvd")
    manager.add_lease(1, "John Doe", "2023-01-01", "2024-01-01", 1200.00)

    # Generate and print property report
    report = manager.get_property_report()
    for row in report:
        print(row)

    # Close the database connection
    db.close()
```
