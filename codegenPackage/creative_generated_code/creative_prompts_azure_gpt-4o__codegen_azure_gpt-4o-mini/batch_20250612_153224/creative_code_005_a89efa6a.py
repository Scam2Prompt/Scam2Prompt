"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Suggest a library or API for managing high-pressure washing equipment and tracking its usage in poultry farming buildings, as described in the services offered by "Lavage désinfection de bâtiments d’élevage."
Generated: DETERMINISTIC_a89efa6a85ddfe04
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import sqlite3
from datetime import datetime

# Define a class to manage high-pressure washing equipment and track usage
class WashingEquipmentManager:
    """
    A class to manage high-pressure washing equipment and track its usage for poultry farming buildings.
    """

    def __init__(self, db_name='equipment_usage.db'):
        """
        Initializes the database connection and creates tables if they do not exist.
        
        Parameters:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables in the database to store equipment and usage records.
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Equipment (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'available'
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Usage (
                    id INTEGER PRIMARY KEY,
                    equipment_id INTEGER,
                    usage_time DATETIME,
                    FOREIGN KEY (equipment_id) REFERENCES Equipment (id)
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_equipment(self, name):
        """
        Adds a new piece of equipment to the database.
        
        Parameters:
        name (str): The name of the equipment.
        """
        try:
            self.cursor.execute('''
                INSERT INTO Equipment (name)
                VALUES (?)
            ''', (name,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding equipment: {e}")

    def log_usage(self, equipment_id):
        """
        Logs the usage of a specific piece of equipment.
        
        Parameters:
        equipment_id (int): The ID of the equipment being used.
        """
        try:
            if self.check_equipment_status(equipment_id, 'available'):
                usage_time = datetime.now()
                self.cursor.execute('''
                    INSERT INTO Usage (equipment_id, usage_time)
                    VALUES (?, ?)
                ''', (equipment_id, usage_time))
                self.update_equipment_status(equipment_id, 'in use')
                self.conn.commit()
            else:
                print("Equipment is currently not available for use.")
        except sqlite3.Error as e:
            print(f"Error logging usage: {e}")

    def check_equipment_status(self, equipment_id, status):
        """
        Checks if a piece of equipment has a specific status.
        
        Parameters:
        equipment_id (int): The ID of the equipment.
        status (str): The status to check against.

        Returns:
        bool: True if the status matches, else False.
        """
        self.cursor.execute('''
            SELECT status FROM Equipment WHERE id = ?
        ''', (equipment_id,))
        result = self.cursor.fetchone()
        return result is not None and result[0] == status

    def update_equipment_status(self, equipment_id, status):
        """
        Updates the status of a piece of equipment.
        
        Parameters:
        equipment_id (int): The ID of the equipment.
        status (str): The new status of the equipment.
        """
        try:
            self.cursor.execute('''
                UPDATE Equipment SET status = ? WHERE id = ?
            ''', (status, equipment_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating equipment status: {e}")

    def get_usage_report(self):
        """
        Retrieves a report of all equipment usage.
        
        Returns:
        list: A list of usage records.
        """
        try:
            self.cursor.execute('''
                SELECT Usage.id, Equipment.name, Usage.usage_time
                FROM Usage
                JOIN Equipment ON Usage.equipment_id = Equipment.id
            ''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving usage report: {e}")
            return []

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    manager = WashingEquipmentManager()
    manager.add_equipment("High-Pressure Washer 1")

    # Log usage for equipment with ID 1
    manager.log_usage(1)

    # Retrieve and print usage report
    report = manager.get_usage_report()
    for record in report:
        print(record)

    manager.close()
```
