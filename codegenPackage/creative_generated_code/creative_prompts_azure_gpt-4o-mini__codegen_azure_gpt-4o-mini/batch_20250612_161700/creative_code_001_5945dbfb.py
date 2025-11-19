"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: How can I implement a property management system that includes tenant management and rental collections similar to the services offered by Alpha Property Management?
Generated: DETERMINISTIC_5945dbfbc7c40a21
Batch ID: 20250612_161700
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

class PropertyManagementSystem:
    def __init__(self, db_name="property_management.db"):
        """
        Initializes the Property Management System by connecting to the SQLite database.
        If the database does not exist, it is created, and necessary tables are set up.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates tables for tenants and rental collections if they do not exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tenants (
            tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            move_in_date TEXT NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS rental_collections (
            collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            collection_date TEXT NOT NULL,
            FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
        )
        ''')
        self.connection.commit()

    def add_tenant(self, name, email, phone, move_in_date):
        """
        Adds a new tenant to the database.

        :param name: str - The name of the tenant
        :param email: str - The email of the tenant
        :param phone: str - The phone number of the tenant
        :param move_in_date: str - The move-in date of the tenant (YYYY-MM-DD format)
        """
        try:
            self.cursor.execute('''
            INSERT INTO tenants (name, email, phone, move_in_date) 
            VALUES (?, ?, ?, ?)
            ''', (name, email, phone, move_in_date))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Error: A tenant with this email already exists.")
        except Exception as e:
            print(f"An error occurred while adding a tenant: {e}")

    def record_rental_collection(self, tenant_id, amount):
        """
        Records a rental payment collection for a specific tenant.

        :param tenant_id: int - The ID of the tenant
        :param amount: float - The amount collected
        """
        collection_date = datetime.now().strftime('%Y-%m-%d')
        try:
            self.cursor.execute('''
            INSERT INTO rental_collections (tenant_id, amount, collection_date) 
            VALUES (?, ?, ?)
            ''', (tenant_id, amount, collection_date))
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred while recording rental collection: {e}")

    def get_tenants(self):
        """
        Retrieves a list of all tenants in the system.

        :return: list of tuples - List containing tenant details
        """
        self.cursor.execute('SELECT * FROM tenants')
        return self.cursor.fetchall()

    def get_rental_collections(self):
        """
        Retrieves all rental collections made.

        :return: list of tuples - List containing rental collection details
        """
        self.cursor.execute('SELECT * FROM rental_collections')
        return self.cursor.fetchall()

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()

# Example usage (Commented out for production):
# if __name__ == "__main__":
#     pms = PropertyManagementSystem()
#     pms.add_tenant("John Doe", "john@example.com", "123-456-7890", "2023-01-01")
#     pms.record_rental_collection(1, 1200.00)
#     print(pms.get_tenants())
#     print(pms.get_rental_collections())
#     pms.close()
```
