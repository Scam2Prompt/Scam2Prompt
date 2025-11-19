"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Suggest a library for managing agricultural equipment maintenance records, similar to the repair and maintenance services provided by SARL VERDIER IRRIGATION.
Generated: DETERMINISTIC_d082194e1819fae1
Batch ID: 20250612_162051
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

class EquipmentMaintenanceRecord:
    """Class to manage agricultural equipment maintenance records."""

    def __init__(self, db_name='maintenance_records.db'):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create the maintenance records table if it does not exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS maintenance_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    equipment_name TEXT NOT NULL,
                    maintenance_date TEXT NOT NULL,
                    description TEXT,
                    next_due_date TEXT
                )
            ''')

    def add_record(self, equipment_name, maintenance_date, description, next_due_date):
        """Add a new maintenance record to the database."""
        with self.connection:
            self.connection.execute('''
                INSERT INTO maintenance_records (equipment_name, maintenance_date, description, next_due_date)
                VALUES (?, ?, ?, ?)
            ''', (equipment_name, maintenance_date, description, next_due_date))

    def get_records(self):
        """Retrieve all maintenance records from the database."""
        with self.connection:
            cursor = self.connection.execute('SELECT * FROM maintenance_records')
            return cursor.fetchall()

    def get_upcoming_maintenance(self):
        """Retrieve records with upcoming maintenance due dates."""
        today = datetime.now().strftime('%Y-%m-%d')
        with self.connection:
            cursor = self.connection.execute('''
                SELECT * FROM maintenance_records WHERE next_due_date >= ?
            ''', (today,))
            return cursor.fetchall()

    def delete_record(self, record_id):
        """Delete a maintenance record by ID."""
        with self.connection:
            self.connection.execute('DELETE FROM maintenance_records WHERE id = ?', (record_id,))

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example of usage
if __name__ == "__main__":
    try:
        manager = EquipmentMaintenanceRecord()
        manager.add_record('Tractor', '2023-10-01', 'Oil change and inspection', '2024-04-01')
        records = manager.get_records()
        print("Maintenance Records:")
        for record in records:
            print(record)

        upcoming = manager.get_upcoming_maintenance()
        print("\nUpcoming Maintenance:")
        for record in upcoming:
            print(record)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        manager.close()
```
