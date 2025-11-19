"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: "Write a Python script to manage property associations, including services like administration, maintenance, and cleaning, similar to BlocPrest."
Generated: DETERMINISTIC_c1f6178af453f7db
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os


class PropertyAssociationManager:
    """
    A class to manage property associations and their services.
    Services include administration, maintenance, and cleaning.
    """

    def __init__(self, data_file="properties.json"):
        """
        Initialize the manager with a data file to store property information.

        :param data_file: Path to the JSON file for storing property data.
        """
        self.data_file = data_file
        self.properties = self._load_properties()

    def _load_properties(self):
        """
        Load properties from the JSON file.

        :return: Dictionary of properties.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading properties file. Starting with an empty list.")
                return {}
        return {}

    def _save_properties(self):
        """
        Save properties to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.properties, file, indent=4)
        except IOError as e:
            print(f"Error saving properties file: {e}")

    def add_property(self, property_id, name, address, services):
        """
        Add a new property to the association.

        :param property_id: Unique identifier for the property.
        :param name: Name of the property.
        :param address: Address of the property.
        :param services: List of services provided (e.g., ["administration", "maintenance", "cleaning"]).
        """
        if property_id in self.properties:
            print(f"Property with ID {property_id} already exists.")
            return

        self.properties[property_id] = {
            "name": name,
            "address": address,
            "services": services,
        }
        self._save_properties()
        print(f"Property '{name}' added successfully.")

    def update_property(self, property_id, name=None, address=None, services=None):
        """
        Update an existing property's details.

        :param property_id: Unique identifier for the property.
        :param name: New name for the property (optional).
        :param address: New address for the property (optional).
        :param services: New list of services provided (optional).
        """
        if property_id not in self.properties:
            print(f"Property with ID {property_id} does not exist.")
            return

        if name:
            self.properties[property_id]["name"] = name
        if address:
            self.properties[property_id]["address"] = address
        if services:
            self.properties[property_id]["services"] = services

        self._save_properties()
        print(f"Property with ID {property_id} updated successfully.")

    def delete_property(self, property_id):
        """
        Delete a property from the association.

        :param property_id: Unique identifier for the property.
        """
        if property_id not in self.properties:
            print(f"Property with ID {property_id} does not exist.")
            return

        del self.properties[property_id]
        self._save_properties()
        print(f"Property with ID {property_id} deleted successfully.")

    def list_properties(self):
        """
        List all properties in the association.

        :return: List of properties.
        """
        if not self.properties:
            print("No properties found.")
            return

        for property_id, details in self.properties.items():
            print(f"ID: {property_id}")
            print(f"  Name: {details['name']}")
            print(f"  Address: {details['address']}")
            print(f"  Services: {', '.join(details['services'])}")
            print("-" * 40)

    def get_property(self, property_id):
        """
        Get details of a specific property.

        :param property_id: Unique identifier for the property.
        :return: Property details or None if not found.
        """
        property_details = self.properties.get(property_id)
        if not property_details:
            print(f"Property with ID {property_id} not found.")
            return None

        print(f"ID: {property_id}")
        print(f"  Name: {property_details['name']}")
        print(f"  Address: {property_details['address']}")
        print(f"  Services: {', '.join(property_details['services'])}")
        return property_details


# Example usage
if __name__ == "__main__":
    manager = PropertyAssociationManager()

    # Add properties
    manager.add_property("P001", "Sunset Villas", "123 Beach Road", ["administration", "maintenance"])
    manager.add_property("P002", "Mountain Retreat", "456 Hilltop Lane", ["cleaning", "maintenance"])

    # List all properties
    manager.list_properties()

    # Update a property
    manager.update_property("P001", services=["administration", "cleaning", "maintenance"])

    # Get details of a specific property
    manager.get_property("P001")

    # Delete a property
    manager.delete_property("P002")

    # List all properties after deletion
    manager.list_properties()
```
