"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Explain the significance of the Electronic Identity of Buildings (ΗΤΚ) and how it tracks changes over time.
Generated: DETERMINISTIC_b313d48dfee5bfff
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python program that explains the significance of the Electronic Identity of Buildings (ΗΤΚ)
and demonstrates how it tracks changes over time using a simple data model.
"""

import datetime

class BuildingIdentity:
    """
    Represents the Electronic Identity of a Building (ΗΤΚ).
    Tracks information and changes over time.
    """

    def __init__(self, building_name, initial_details):
        """
        Initialize a BuildingIdentity object with a name and initial details.

        :param building_name: Name of the building
        :param initial_details: Dictionary containing initial building details
        """
        self.building_name = building_name
        self.history = []  # List to store change history
        self.current_details = initial_details  # Current state of the building details

        # Record the initial state in the history
        self._record_change("Initial state", initial_details)

    def _record_change(self, change_description, details):
        """
        Record a change in the building's details.

        :param change_description: Description of the change
        :param details: Updated building details
        """
        change_entry = {
            "timestamp": datetime.datetime.now(),  # Time of the change
            "description": change_description,      # What changed
            "details": details                      # Updated details
        }
        self.history.append(change_entry)

    def update_details(self, change_description, updated_details):
        """
        Update the building's details and record the change.

        :param change_description: Description of the update
        :param updated_details: Dictionary containing updated building details
        """
        try:
            # Update current details
            self.current_details.update(updated_details)
            
            # Record the change in history
            self._record_change(change_description, self.current_details)
        except Exception as e:
            # Handle unexpected exceptions
            print(f"Error updating building details: {e}")

    def display_history(self):
        """
        Display the change history of the building.

        :return: None
        """
        print(f"History for Building: {self.building_name}")
        for entry in self.history:
            print(f"Timestamp: {entry['timestamp']}")
            print(f"Description: {entry['description']}")
            print(f"Details: {entry['details']}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    # Initialize the building identity
    initial_details = {
        "address": "123 Main St",
        "year_built": 1990,
        "owner": "John Doe"
    }
    building = BuildingIdentity("Main Street Building", initial_details)

    # Update the building details and track changes
    building.update_details("Ownership change", {"owner": "Jane Smith"})
    building.update_details("Renovation", {"year_renovated": 2020, "new_feature": "Solar Panels"})

    # Display the building's change history
    building.display_history()
```
