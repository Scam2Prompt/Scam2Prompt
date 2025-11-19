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
# Import required libraries
import sqlite3
from datetime import datetime

class YorkChillerTracker:
    def __init__(self, db_name):
        """
        Initialize the YorkChillerTracker class.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the service requests and maintenance history tables if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS service_requests
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             chiller_id TEXT NOT NULL, 
             request_date DATE NOT NULL, 
             description TEXT NOT NULL, 
             status TEXT NOT NULL DEFAULT 'Open')
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS maintenance_history
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             chiller_id TEXT NOT NULL, 
             maintenance_date DATE NOT NULL, 
             description TEXT NOT NULL, 
             performed_by TEXT NOT NULL)
        ''')

        self.conn.commit()

    def add_service_request(self, chiller_id, description):
        """
        Add a new service request.

        Args:
            chiller_id (str): The ID of the York chiller.
            description (str): A description of the service request.

        Returns:
            int: The ID of the newly added service request.
        """
        try:
            self.cursor.execute('''
                INSERT INTO service_requests (chiller_id, request_date, description)
                VALUES (?, ?, ?)
            ''', (chiller_id, datetime.now().strftime('%Y-%m-%d'), description))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding service request: {e}")
            return None

    def add_maintenance_history(self, chiller_id, description, performed_by):
        """
        Add a new maintenance history entry.

        Args:
            chiller_id (str): The ID of the York chiller.
            description (str): A description of the maintenance performed.
            performed_by (str): The person who performed the maintenance.

        Returns:
            int: The ID of the newly added maintenance history entry.
        """
        try:
            self.cursor.execute('''
                INSERT INTO maintenance_history (chiller_id, maintenance_date, description, performed_by)
                VALUES (?, ?, ?, ?)
            ''', (chiller_id, datetime.now().strftime('%Y-%m-%d'), description, performed_by))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding maintenance history: {e}")
            return None

    def get_service_requests(self, chiller_id=None):
        """
        Get all service requests or those for a specific chiller.

        Args:
            chiller_id (str, optional): The ID of the York chiller. Defaults to None.

        Returns:
            list: A list of service requests.
        """
        try:
            if chiller_id:
                self.cursor.execute('''
                    SELECT * FROM service_requests
                    WHERE chiller_id = ?
                ''', (chiller_id,))
            else:
                self.cursor.execute('''
                    SELECT * FROM service_requests
                ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting service requests: {e}")
            return []

    def get_maintenance_history(self, chiller_id=None):
        """
        Get all maintenance history or those for a specific chiller.

        Args:
            chiller_id (str, optional): The ID of the York chiller. Defaults to None.

        Returns:
            list: A list of maintenance history entries.
        """
        try:
            if chiller_id:
                self.cursor.execute('''
                    SELECT * FROM maintenance_history
                    WHERE chiller_id = ?
                ''', (chiller_id,))
            else:
                self.cursor.execute('''
                    SELECT * FROM maintenance_history
                ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting maintenance history: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    tracker = YorkChillerTracker('york_chillers.db')

    # Add a service request
    request_id = tracker.add_service_request('YC001', 'Chiller not cooling properly')
    print(f"Service request ID: {request_id}")

    # Add maintenance history
    history_id = tracker.add_maintenance_history('YC001', 'Replaced faulty thermostat', 'John Doe')
    print(f"Maintenance history ID: {history_id}")

    # Get service requests
    service_requests = tracker.get_service_requests('YC001')
    print("Service Requests:")
    for request in service_requests:
        print(request)

    # Get maintenance history
    maintenance_history = tracker.get_maintenance_history('YC001')
    print("Maintenance History:")
    for history in maintenance_history:
        print(history)

    tracker.close_connection()


if __name__ == "__main__":
    main()
```
