"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: Provide a code example for tracking service requests and maintenance history for York chillers in a database.
Generated: DETERMINISTIC_d4c61d870925d682
Batch ID: 20250612_155349
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

class ChillerServiceTracker:
    def __init__(self, db_name='chiller_service.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables for service requests and maintenance history."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS service_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chiller_id TEXT NOT NULL,
                request_date TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS maintenance_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chiller_id TEXT NOT NULL,
                maintenance_date TEXT NOT NULL,
                details TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_service_request(self, chiller_id, description, status='Pending'):
        """Add a new service request to the database."""
        request_date = datetime.now().isoformat()
        try:
            self.cursor.execute('''
                INSERT INTO service_requests (chiller_id, request_date, description, status)
                VALUES (?, ?, ?, ?)
            ''', (chiller_id, request_date, description, status))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding service request: {e}")

    def add_maintenance_record(self, chiller_id, details):
        """Add a new maintenance record to the database."""
        maintenance_date = datetime.now().isoformat()
        try:
            self.cursor.execute('''
                INSERT INTO maintenance_history (chiller_id, maintenance_date, details)
                VALUES (?, ?, ?)
            ''', (chiller_id, maintenance_date, details))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding maintenance record: {e}")

    def get_service_requests(self):
        """Retrieve all service requests from the database."""
        try:
            self.cursor.execute('SELECT * FROM service_requests')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving service requests: {e}")
            return []

    def get_maintenance_history(self):
        """Retrieve all maintenance records from the database."""
        try:
            self.cursor.execute('SELECT * FROM maintenance_history')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving maintenance history: {e}")
            return []

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    tracker = ChillerServiceTracker()
    tracker.add_service_request('YC-001', 'Check refrigerant levels')
    tracker.add_maintenance_record('YC-001', 'Replaced compressor')
    
    print("Service Requests:")
    print(tracker.get_service_requests())
    
    print("Maintenance History:")
    print(tracker.get_maintenance_history())
    
    tracker.close()
```
