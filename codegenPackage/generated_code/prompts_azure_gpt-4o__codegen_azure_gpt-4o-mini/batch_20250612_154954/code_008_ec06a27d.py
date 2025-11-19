"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Create a maintenance tracking system for rice mill spares such as strainers, baffles, and conveyors, using the services described by Mechano Solutions.
Generated: DETERMINISTIC_ec06a27d266b77a4
Batch ID: 20250612_154954
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

class MaintenanceTrackingSystem:
    def __init__(self, db_name='maintenance_tracking.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables for tracking maintenance of rice mill spares."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS spares (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                last_maintenance_date TEXT,
                next_maintenance_date TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS maintenance_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                spare_id INTEGER,
                maintenance_date TEXT,
                details TEXT,
                FOREIGN KEY (spare_id) REFERENCES spares (id)
            )
        ''')
        self.connection.commit()

    def add_spare(self, name, description):
        """Add a new spare part to the system."""
        next_maintenance_date = self.calculate_next_maintenance()
        self.cursor.execute('''
            INSERT INTO spares (name, description, last_maintenance_date, next_maintenance_date)
            VALUES (?, ?, ?, ?)
        ''', (name, description, datetime.now().isoformat(), next_maintenance_date))
        self.connection.commit()

    def calculate_next_maintenance(self):
        """Calculate the next maintenance date (e.g., 30 days from now)."""
        return (datetime.now() + timedelta(days=30)).isoformat()

    def record_maintenance(self, spare_id, details):
        """Record maintenance activity for a specific spare part."""
        maintenance_date = datetime.now().isoformat()
        self.cursor.execute('''
            INSERT INTO maintenance_records (spare_id, maintenance_date, details)
            VALUES (?, ?, ?)
        ''', (spare_id, maintenance_date, details))
        self.update_last_maintenance_date(spare_id, maintenance_date)
        self.connection.commit()

    def update_last_maintenance_date(self, spare_id, maintenance_date):
        """Update the last maintenance date for a specific spare part."""
        self.cursor.execute('''
            UPDATE spares
            SET last_maintenance_date = ?, next_maintenance_date = ?
            WHERE id = ?
        ''', (maintenance_date, self.calculate_next_maintenance(), spare_id))
        self.connection.commit()

    def get_spares(self):
        """Retrieve all spares from the system."""
        self.cursor.execute('SELECT * FROM spares')
        return self.cursor.fetchall()

    def get_maintenance_records(self, spare_id):
        """Retrieve maintenance records for a specific spare part."""
        self.cursor.execute('SELECT * FROM maintenance_records WHERE spare_id = ?', (spare_id,))
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

if __name__ == "__main__":
    # Example usage of the MaintenanceTrackingSystem
    try:
        mts = MaintenanceTrackingSystem()
        mts.add_spare('Strainer', 'Used for filtering impurities from rice.')
        mts.add_spare('Baffle', 'Helps in directing the flow of rice in the mill.')
        mts.record_maintenance(1, 'Replaced the mesh of the strainer.')
        
        print("Spares:")
        for spare in mts.get_spares():
            print(spare)

        print("\nMaintenance Records for Strainer:")
        for record in mts.get_maintenance_records(1):
            print(record)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mts.close()
```
