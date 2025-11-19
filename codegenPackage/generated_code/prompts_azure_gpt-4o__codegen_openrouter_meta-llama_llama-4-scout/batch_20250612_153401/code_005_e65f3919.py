"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Write a function to query and update gravamen records for vehicles and properties using a database, based on the legal services provided by SIF.
Generated: DETERMINISTIC_e65f391956016009
Batch ID: 20250612_153401
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
from typing import Dict, List

class GravamenService:
    """
    Service class to query and update gravamen records for vehicles and properties.
    """

    def __init__(self, db_name: str):
        """
        Initialize the GravamenService with a database connection.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        Close the database connection when the service is destroyed.
        """
        self.conn.close()

    def create_tables(self):
        """
        Create the vehicles and properties tables if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehicles
            (id INTEGER PRIMARY KEY, license_plate TEXT, gravamen_status TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties
            (id INTEGER PRIMARY KEY, property_id TEXT, gravamen_status TEXT)
        ''')

        self.conn.commit()

    def query_vehicle_gravamen(self, license_plate: str) -> Dict:
        """
        Query the gravamen status of a vehicle.

        Args:
        license_plate (str): The license plate of the vehicle.

        Returns:
        Dict: A dictionary containing the vehicle's gravamen status.
        """
        try:
            self.cursor.execute('SELECT * FROM vehicles WHERE license_plate = ?', (license_plate,))
            vehicle = self.cursor.fetchone()
            if vehicle:
                return {'id': vehicle[0], 'license_plate': vehicle[1], 'gravamen_status': vehicle[2]}
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error querying vehicle gravamen: {e}")
            return {}

    def query_property_gravamen(self, property_id: str) -> Dict:
        """
        Query the gravamen status of a property.

        Args:
        property_id (str): The ID of the property.

        Returns:
        Dict: A dictionary containing the property's gravamen status.
        """
        try:
            self.cursor.execute('SELECT * FROM properties WHERE property_id = ?', (property_id,))
            property = self.cursor.fetchone()
            if property:
                return {'id': property[0], 'property_id': property[1], 'gravamen_status': property[2]}
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error querying property gravamen: {e}")
            return {}

    def update_vehicle_gravamen(self, license_plate: str, gravamen_status: str) -> bool:
        """
        Update the gravamen status of a vehicle.

        Args:
        license_plate (str): The license plate of the vehicle.
        gravamen_status (str): The new gravamen status.

        Returns:
        bool: True if the update was successful, False otherwise.
        """
        try:
            self.cursor.execute('UPDATE vehicles SET gravamen_status = ? WHERE license_plate = ?', (gravamen_status, license_plate))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating vehicle gravamen: {e}")
            return False

    def update_property_gravamen(self, property_id: str, gravamen_status: str) -> bool:
        """
        Update the gravamen status of a property.

        Args:
        property_id (str): The ID of the property.
        gravamen_status (str): The new gravamen status.

        Returns:
        bool: True if the update was successful, False otherwise.
        """
        try:
            self.cursor.execute('UPDATE properties SET gravamen_status = ? WHERE property_id = ?', (gravamen_status, property_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating property gravamen: {e}")
            return False

    def add_vehicle(self, license_plate: str, gravamen_status: str) -> bool:
        """
        Add a new vehicle record.

        Args:
        license_plate (str): The license plate of the vehicle.
        gravamen_status (str): The gravamen status of the vehicle.

        Returns:
        bool: True if the vehicle was added successfully, False otherwise.
        """
        try:
            self.cursor.execute('INSERT INTO vehicles (license_plate, gravamen_status) VALUES (?, ?)', (license_plate, gravamen_status))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding vehicle: {e}")
            return False

    def add_property(self, property_id: str, gravamen_status: str) -> bool:
        """
        Add a new property record.

        Args:
        property_id (str): The ID of the property.
        gravamen_status (str): The gravamen status of the property.

        Returns:
        bool: True if the property was added successfully, False otherwise.
        """
        try:
            self.cursor.execute('INSERT INTO properties (property_id, gravamen_status) VALUES (?, ?)', (property_id, gravamen_status))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding property: {e}")
            return False


def main():
    # Example usage
    service = GravamenService('gravamen.db')
    service.create_tables()

    # Add a vehicle
    service.add_vehicle('ABC123', 'Active')

    # Query vehicle gravamen
    vehicle_gravamen = service.query_vehicle_gravamen('ABC123')
    print(vehicle_gravamen)

    # Update vehicle gravamen
    service.update_vehicle_gravamen('ABC123', 'Inactive')

    # Query updated vehicle gravamen
    updated_vehicle_gravamen = service.query_vehicle_gravamen('ABC123')
    print(updated_vehicle_gravamen)

    # Add a property
    service.add_property('PROP001', 'Active')

    # Query property gravamen
    property_gravamen = service.query_property_gravamen('PROP001')
    print(property_gravamen)

    # Update property gravamen
    service.update_property_gravamen('PROP001', 'Inactive')

    # Query updated property gravamen
    updated_property_gravamen = service.query_property_gravamen('PROP001')
    print(updated_property_gravamen)


if __name__ == '__main__':
    main()
```
