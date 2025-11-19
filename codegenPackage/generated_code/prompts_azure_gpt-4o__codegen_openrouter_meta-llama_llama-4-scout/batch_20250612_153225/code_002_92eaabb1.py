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
# lease_administration.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Lease:
    def __init__(self, lease_id, property_id, start_date, end_date, rent):
        """
        Initialize a Lease object.

        Args:
            lease_id (int): Unique identifier for the lease.
            property_id (int): Unique identifier for the property.
            start_date (str): Start date of the lease in YYYY-MM-DD format.
            end_date (str): End date of the lease in YYYY-MM-DD format.
            rent (float): Monthly rent amount.
        """
        self.lease_id = lease_id
        self.property_id = property_id
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.rent = rent

    def is_active(self):
        """
        Check if the lease is active.

        Returns:
            bool: True if the lease is active, False otherwise.
        """
        return self.start_date <= datetime.datetime.now() <= self.end_date

    def get_lease_details(self):
        """
        Get lease details.

        Returns:
            dict: Lease details, including lease ID, property ID, start date, end date, and rent.
        """
        return {
            'lease_id': self.lease_id,
            'property_id': self.property_id,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'rent': self.rent
        }


class Property:
    def __init__(self, property_id, address):
        """
        Initialize a Property object.

        Args:
            property_id (int): Unique identifier for the property.
            address (str): Property address.
        """
        self.property_id = property_id
        self.address = address
        self.leases = []

    def add_lease(self, lease):
        """
        Add a lease to the property.

        Args:
            lease (Lease): Lease object to add.
        """
        self.leases.append(lease)

    def get_property_details(self):
        """
        Get property details.

        Returns:
            dict: Property details, including property ID, address, and leases.
        """
        return {
            'property_id': self.property_id,
            'address': self.address,
            'leases': [lease.get_lease_details() for lease in self.leases]
        }


class LeaseAdministration:
    def __init__(self):
        """
        Initialize a LeaseAdministration object.
        """
        self.properties = {}

    def add_property(self, property_id, address):
        """
        Add a property to the lease administration.

        Args:
            property_id (int): Unique identifier for the property.
            address (str): Property address.
        """
        if property_id not in self.properties:
            self.properties[property_id] = Property(property_id, address)
        else:
            logging.warning(f"Property with ID {property_id} already exists.")

    def add_lease(self, property_id, lease_id, start_date, end_date, rent):
        """
        Add a lease to a property.

        Args:
            property_id (int): Unique identifier for the property.
            lease_id (int): Unique identifier for the lease.
            start_date (str): Start date of the lease in YYYY-MM-DD format.
            end_date (str): End date of the lease in YYYY-MM-DD format.
            rent (float): Monthly rent amount.

        Raises:
            ValueError: If the property does not exist.
        """
        if property_id in self.properties:
            lease = Lease(lease_id, property_id, start_date, end_date, rent)
            self.properties[property_id].add_lease(lease)
        else:
            raise ValueError(f"Property with ID {property_id} does not exist.")

    def get_property_report(self, property_id):
        """
        Get a report for a property.

        Args:
            property_id (int): Unique identifier for the property.

        Returns:
            dict: Property report, including property details and lease information.

        Raises:
            ValueError: If the property does not exist.
        """
        if property_id in self.properties:
            return self.properties[property_id].get_property_details()
        else:
            raise ValueError(f"Property with ID {property_id} does not exist.")

    def get_lease_report(self, lease_id):
        """
        Get a report for a lease.

        Args:
            lease_id (int): Unique identifier for the lease.

        Returns:
            dict: Lease report, including lease details.

        Raises:
            ValueError: If the lease does not exist.
        """
        for property in self.properties.values():
            for lease in property.leases:
                if lease.lease_id == lease_id:
                    return lease.get_lease_details()
        raise ValueError(f"Lease with ID {lease_id} does not exist.")


def main():
    # Create a lease administration object
    admin = LeaseAdministration()

    # Add properties
    admin.add_property(1, "123 Main St")
    admin.add_property(2, "456 Elm St")

    # Add leases
    admin.add_lease(1, 1, "2022-01-01", "2023-01-01", 1000.0)
    admin.add_lease(1, 2, "2022-06-01", "2023-06-01", 1200.0)
    admin.add_lease(2, 3, "2022-03-01", "2023-03-01", 900.0)

    # Get property reports
    print(admin.get_property_report(1))
    print(admin.get_property_report(2))

    # Get lease reports
    print(admin.get_lease_report(1))
    print(admin.get_lease_report(2))

    # Test error handling
    try:
        admin.get_property_report(3)
    except ValueError as e:
        logging.error(e)

    try:
        admin.get_lease_report(4)
    except ValueError as e:
        logging.error(e)


if __name__ == "__main__":
    main()
```
