"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Explain the significance of the Electronic Identity of Buildings (ΗΤΚ) and how it tracks changes over time.
Generated: DETERMINISTIC_b313d48dfee5bfff
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script explains the significance of the Electronic Identity of Buildings (ΗΤΚ) 
and how it tracks changes over time. It uses a simple data structure to represent 
a building's identity and its historical changes. The script is designed to be 
educational and demonstrate the concept programmatically.
"""

import datetime


class BuildingIdentity:
    """
    Represents the Electronic Identity of a Building (ΗΤΚ).
    Tracks the building's details and changes over time.
    """

    def __init__(self, building_id, name, address, initial_details):
        """
        Initialize a new building identity.

        :param building_id: Unique identifier for the building.
        :param name: Name of the building.
        :param address: Address of the building.
        :param initial_details: Initial details about the building (e.g., size, purpose).
        """
        self.building_id = building_id
        self.name = name
        self.address = address
        self.details = initial_details
        self.history = []  # List to track changes over time
        self._log_change("Initial details added", initial_details)

    def _log_change(self, change_description, updated_details):
        """
        Logs a change to the building's identity.

        :param change_description: Description of the change.
        :param updated_details: Updated details after the change.
        """
        change_record = {
            "timestamp": datetime.datetime.now(),
            "description": change_description,
            "details": updated_details,
        }
        self.history.append(change_record)

    def update_details(self, new_details, change_description):
        """
        Updates the building's details and logs the change.

        :param new_details: New details to update.
        :param change_description: Description of the change.
        :raises ValueError: If new_details is empty or invalid.
        """
        if not new_details:
            raise ValueError("New details cannot be empty.")
        self.details = new_details
        self._log_change(change_description, new_details)

    def get_history(self):
        """
        Retrieves the history of changes for the building.

        :return: List of change records.
        """
        return self.history

    def __str__(self):
        """
        Returns a string representation of the building's identity.

        :return: String representation of the building.
        """
        return f"Building ID: {self.building_id}\nName: {self.name}\nAddress: {self.address}\nDetails: {self.details}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new building identity
        building = BuildingIdentity(
            building_id="B123",
            name="Central Library",
            address="123 Main St, Cityville",
            initial_details={"size": "5000 sq ft", "purpose": "Public Library"},
        )

        print("Initial Building Identity:")
        print(building)

        # Update building details
        building.update_details(
            {"size": "5500 sq ft", "purpose": "Public Library", "renovation": "2023"},
            "Renovation completed and size updated",
        )

        print("\nUpdated Building Identity:")
        print(building)

        # Display history of changes
        print("\nHistory of Changes:")
        for record in building.get_history():
            print(
                f"Timestamp: {record['timestamp']}, Description: {record['description']}, Details: {record['details']}"
            )

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
