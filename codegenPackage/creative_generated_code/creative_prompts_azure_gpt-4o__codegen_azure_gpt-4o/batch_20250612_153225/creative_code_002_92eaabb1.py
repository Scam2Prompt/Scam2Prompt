"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Generate a script to manage lease administration and property management reporting, using features mentioned in Vital Corporate Solutions' property manager VA services.
Generated: DETERMINISTIC_92eaabb150a9465c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime


class PropertyManagement:
    """
    A class to manage lease administration and property management reporting.
    """

    def __init__(self, db_name="property_management.db"):
        """
        Initialize the database connection.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self):
        """
        Create necessary tables for property and lease management.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Table for properties
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    owner TEXT NOT NULL
                )
            """)

            # Table for leases
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS leases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    property_id INTEGER NOT NULL,
                    tenant TEXT NOT NULL,
                    lease_start DATE NOT NULL,
                    lease_end DATE NOT NULL,
                    rent_amount REAL NOT NULL,
                    FOREIGN KEY(property_id) REFERENCES properties(id)
                )
            """)
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            conn.close()

    def add_property(self, name, address, owner):
        """
        Add a new property.
        :param name: Name of the property.
        :param address: Address of the property.
        :param owner: Owner of the property.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO properties (name, address, owner)
                VALUES (?, ?, ?)
            """, (name, address, owner))
            
            conn.commit()
            print("Property added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding property: {e}")
        finally:
            conn.close()

    def add_lease(self, property_id, tenant, lease_start, lease_end, rent_amount):
        """
        Add a new lease.
        :param property_id: ID of the property associated with the lease.
        :param tenant: Name of the tenant.
        :param lease_start: Start date of the lease (YYYY-MM-DD format).
        :param lease_end: End date of the lease (YYYY-MM-DD format).
        :param rent_amount: Monthly rent amount.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO leases (property_id, tenant, lease_start, lease_end, rent_amount)
                VALUES (?, ?, ?, ?, ?)
            """, (property_id, tenant, lease_start, lease_end, rent_amount))
            
            conn.commit()
            print("Lease added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding lease: {e}")
        finally:
            conn.close()

    def generate_report(self):
        """
        Generate a report of all properties and their leases.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query properties and their leases
            cursor.execute("""
                SELECT 
                    p.id AS property_id, 
                    p.name AS property_name, 
                    p.address AS property_address, 
                    p.owner AS property_owner, 
                    l.tenant AS tenant_name, 
                    l.lease_start, 
                    l.lease_end, 
                    l.rent_amount
                FROM properties p
                LEFT JOIN leases l ON p.id = l.property_id
            """)
            
            rows = cursor.fetchall()
            
            if rows:
                print("Property Management Report:")
                for row in rows:
                    print(f"""
                    Property ID: {row[0]}
                    Name: {row[1]}
                    Address: {row[2]}
                    Owner: {row[3]}
                    Tenant: {row[4] if row[4] else 'No tenant'}
                    Lease Start: {row[5] if row[5] else 'N/A'}
                    Lease End: {row[6] if row[6] else 'N/A'}
                    Rent Amount: {row[7] if row[7] else 'N/A'}
                    """)
            else:
                print("No data available.")
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")
        finally:
            conn.close()


# Usage Example
if __name__ == "__main__":
    # Initialize the property management system
    pm = PropertyManagement()
    
    # Add a property
    pm.add_property(name="Sunset Villas", address="123 Main St, Springfield", owner="John Doe")
    
    # Add a lease
    pm.add_lease(property_id=1, tenant="Jane Smith", lease_start="2023-10-01", lease_end="2024-10-01", rent_amount=1200.00)
    
    # Generate a report
    pm.generate_report()
```
