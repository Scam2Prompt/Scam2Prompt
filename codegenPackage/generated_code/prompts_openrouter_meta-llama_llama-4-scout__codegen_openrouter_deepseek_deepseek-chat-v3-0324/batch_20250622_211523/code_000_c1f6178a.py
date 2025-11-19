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
from typing import Dict, List, Optional, Union

class PropertyServiceManager:
    """
    A class to manage property associations and services like administration,
    maintenance, and cleaning.
    """

    def __init__(self, data_file: str = "property_services.json"):
        """
        Initialize the PropertyServiceManager with a data file.

        Args:
            data_file (str): Path to the JSON file storing property data.
        """
        self.data_file = data_file
        self.properties = self._load_data()

    def _load_data(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Load property data from the JSON file.

        Returns:
            Dict[str, Dict[str, List[str]]]: Dictionary containing property data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}

    def _save_data(self) -> None:
        """
        Save property data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.properties, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_property(self, property_id: str) -> bool:
        """
        Add a new property to the manager.

        Args:
            property_id (str): Unique identifier for the property.

        Returns:
            bool: True if property was added, False if it already exists.
        """
        if property_id in self.properties:
            return False
        self.properties[property_id] = {
            "administration": [],
            "maintenance": [],
            "cleaning": []
        }
        self._save_data()
        return True

    def remove_property(self, property_id: str) -> bool:
        """
        Remove a property from the manager.

        Args:
            property_id (str): Unique identifier for the property.

        Returns:
            bool: True if property was removed, False if it doesn't exist.
        """
        if property_id not in self.properties:
            return False
        del self.properties[property_id]
        self._save_data()
        return True

    def add_service(
        self,
        property_id: str,
        service_type: str,
        service_name: str
    ) -> bool:
        """
        Add a service to a property.

        Args:
            property_id (str): Unique identifier for the property.
            service_type (str): Type of service (administration/maintenance/cleaning).
            service_name (str): Name of the service to add.

        Returns:
            bool: True if service was added, False if property or service type doesn't exist.
        """
        if property_id not in self.properties:
            return False
        if service_type not in self.properties[property_id]:
            return False
        if service_name in self.properties[property_id][service_type]:
            return False
        self.properties[property_id][service_type].append(service_name)
        self._save_data()
        return True

    def remove_service(
        self,
        property_id: str,
        service_type: str,
        service_name: str
    ) -> bool:
        """
        Remove a service from a property.

        Args:
            property_id (str): Unique identifier for the property.
            service_type (str): Type of service (administration/maintenance/cleaning).
            service_name (str): Name of the service to remove.

        Returns:
            bool: True if service was removed, False if property, service type, or service doesn't exist.
        """
        if property_id not in self.properties:
            return False
        if service_type not in self.properties[property_id]:
            return False
        if service_name not in self.properties[property_id][service_type]:
            return False
        self.properties[property_id][service_type].remove(service_name)
        self._save_data()
        return True

    def get_services(
        self,
        property_id: str,
        service_type: Optional[str] = None
    ) -> Union[Dict[str, List[str]], List[str], None]:
        """
        Get services for a property.

        Args:
            property_id (str): Unique identifier for the property.
            service_type (Optional[str]): Type of service to filter by.

        Returns:
            Union[Dict[str, List[str]], List[str], None]: Services data or None if property doesn't exist.
        """
        if property_id not in self.properties:
            return None
        if service_type:
            return self.properties[property_id].get(service_type, [])
        return self.properties[property_id]

    def list_properties(self) -> List[str]:
        """
        List all properties.

        Returns:
            List[str]: List of property IDs.
        """
        return list(self.properties.keys())

# Example usage
if __name__ == "__main__":
    manager = PropertyServiceManager()

    # Add a property
    manager.add_property("property_1")

    # Add services
    manager.add_service("property_1", "administration", "rent_collection")
    manager.add_service("property_1", "maintenance", "plumbing")
    manager.add_service("property_1", "cleaning", "weekly_cleaning")

    # List properties
    print("Properties:", manager.list_properties())

    # Get services for a property
    print("Services for property_1:", manager.get_services("property_1"))

    # Remove a service
    manager.remove_service("property_1", "cleaning", "weekly_cleaning")

    # Remove a property
    manager.remove_property("property_1")
```
