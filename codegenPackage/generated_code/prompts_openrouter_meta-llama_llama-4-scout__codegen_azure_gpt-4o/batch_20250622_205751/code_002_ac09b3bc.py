"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Develop a code snippet to track and control changes to a building's status using the Electronic Identity of Buildings/ Apartments (ΗΤΚ) system.
Generated: DETERMINISTIC_ac09b3bcab07f53b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid

class BuildingStatusTracker:
    """
    A class to track and control changes to a building's status using the Electronic Identity of Buildings/ Apartments (ΗΤΚ) system.
    """

    def __init__(self):
        """
        Initializes the BuildingStatusTracker with an empty registry.
        """
        self.building_registry = {}  # Dictionary to store building data keyed by unique IDs

    def register_building(self, building_name, address):
        """
        Registers a new building in the ΗΤΚ system.

        Args:
            building_name (str): Name of the building.
            address (str): Address of the building.

        Returns:
            str: Unique ID of the registered building.
        """
        try:
            building_id = str(uuid.uuid4())  # Generate a unique ID for the building
            self.building_registry[building_id] = {
                "name": building_name,
                "address": address,
                "status": "Active"  # Default status is 'Active'
            }
            return building_id
        except Exception as e:
            raise RuntimeError(f"Error registering building: {e}")

    def update_status(self, building_id, new_status):
        """
        Updates the status of a building.

        Args:
            building_id (str): Unique ID of the building.
            new_status (str): New status to set for the building.

        Returns:
            bool: True if the status was updated successfully, False otherwise.
        """
        try:
            if building_id not in self.building_registry:
                raise ValueError("Building ID not found in the registry.")
            
            # Validate new status
            if new_status not in ["Active", "Inactive", "Under Construction", "Demolished"]:
                raise ValueError("Invalid status. Allowed statuses are: Active, Inactive, Under Construction, Demolished.")
            
            self.building_registry[building_id]["status"] = new_status
            return True
        except Exception as e:
            print(f"Error updating building status: {e}")
            return False

    def get_building_info(self, building_id):
        """
        Retrieves information about a building.

        Args:
            building_id (str): Unique ID of the building.

        Returns:
            dict: Building information including name, address, and status.
        """
        try:
            if building_id not in self.building_registry:
                raise ValueError("Building ID not found in the registry.")
            
            return self.building_registry[building_id]
        except Exception as e:
            print(f"Error retrieving building information: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    tracker = BuildingStatusTracker()

    # Register a new building
    building_id = tracker.register_building("Sunset Apartments", "123 Main Street")
    print(f"Building registered with ID: {building_id}")

    # Update building status
    if tracker.update_status(building_id, "Under Construction"):
        print("Building status updated successfully.")

    # Retrieve building information
    building_info = tracker.get_building_info(building_id)
    if building_info:
        print("Building Information:", building_info)
```
