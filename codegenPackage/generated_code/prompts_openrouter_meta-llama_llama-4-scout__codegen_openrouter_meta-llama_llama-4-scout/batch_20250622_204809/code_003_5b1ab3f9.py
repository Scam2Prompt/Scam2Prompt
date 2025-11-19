"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: "How can I customize CRM.f for a multi-site foundation to track activities and equipment across different locations?"
Generated: DETERMINISTIC_5b1ab3f96eca32b6
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm.py

"""
Customizable CRM for multi-site foundation to track activities and equipment across different locations.

Classes:
    Location
    Equipment
    Activity
    CRM

Exceptions:
    LocationNotFoundError
    EquipmentNotFoundError
    ActivityNotFoundError
"""

from typing import Dict, List
from enum import Enum

class LocationNotFoundError(Exception):
    """Raised when a location is not found."""
    pass

class EquipmentNotFoundError(Exception):
    """Raised when an equipment is not found."""
    pass

class ActivityNotFoundError(Exception):
    """Raised when an activity is not found."""
    pass

class Location:
    """Represents a location in the CRM."""

    def __init__(self, id: int, name: str, address: str):
        """
        Initializes a Location object.

        Args:
            id (int): Unique identifier for the location.
            name (str): Name of the location.
            address (str): Address of the location.
        """
        self.id = id
        self.name = name
        self.address = address

class Equipment:
    """Represents an equipment in the CRM."""

    def __init__(self, id: int, name: str, location_id: int):
        """
        Initializes an Equipment object.

        Args:
            id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            location_id (int): Foreign key referencing the Location object.
        """
        self.id = id
        self.name = name
        self.location_id = location_id

class Activity:
    """Represents an activity in the CRM."""

    class Status(Enum):
        """Enum for activity status."""
        PENDING = 1
        IN_PROGRESS = 2
        COMPLETED = 3

    def __init__(self, id: int, name: str, location_id: int, equipment_id: int, status: Status):
        """
        Initializes an Activity object.

        Args:
            id (int): Unique identifier for the activity.
            name (str): Name of the activity.
            location_id (int): Foreign key referencing the Location object.
            equipment_id (int): Foreign key referencing the Equipment object.
            status (Status): Status of the activity.
        """
        self.id = id
        self.name = name
        self.location_id = location_id
        self.equipment_id = equipment_id
        self.status = status

class CRM:
    """Represents the customizable CRM."""

    def __init__(self):
        """
        Initializes a CRM object.
        """
        self.locations: Dict[int, Location] = {}
        self.equipment: Dict[int, Equipment] = {}
        self.activities: Dict[int, Activity] = {}

    def add_location(self, location: Location):
        """
        Adds a location to the CRM.

        Args:
            location (Location): Location object to add.
        """
        self.locations[location.id] = location

    def get_location(self, location_id: int) -> Location:
        """
        Retrieves a location from the CRM.

        Args:
            location_id (int): Unique identifier for the location.

        Returns:
            Location: Location object.

        Raises:
            LocationNotFoundError: If the location is not found.
        """
        try:
            return self.locations[location_id]
        except KeyError:
            raise LocationNotFoundError(f"Location {location_id} not found.")

    def add_equipment(self, equipment: Equipment):
        """
        Adds an equipment to the CRM.

        Args:
            equipment (Equipment): Equipment object to add.
        """
        self.equipment[equipment.id] = equipment

    def get_equipment(self, equipment_id: int) -> Equipment:
        """
        Retrieves an equipment from the CRM.

        Args:
            equipment_id (int): Unique identifier for the equipment.

        Returns:
            Equipment: Equipment object.

        Raises:
            EquipmentNotFoundError: If the equipment is not found.
        """
        try:
            return self.equipment[equipment_id]
        except KeyError:
            raise EquipmentNotFoundError(f"Equipment {equipment_id} not found.")

    def add_activity(self, activity: Activity):
        """
        Adds an activity to the CRM.

        Args:
            activity (Activity): Activity object to add.
        """
        self.activities[activity.id] = activity

    def get_activity(self, activity_id: int) -> Activity:
        """
        Retrieves an activity from the CRM.

        Args:
            activity_id (int): Unique identifier for the activity.

        Returns:
            Activity: Activity object.

        Raises:
            ActivityNotFoundError: If the activity is not found.
        """
        try:
            return self.activities[activity_id]
        except KeyError:
            raise ActivityNotFoundError(f"Activity {activity_id} not found.")

def main():
    crm = CRM()

    # Create locations
    location1 = Location(1, "New York", "123 Main St")
    location2 = Location(2, "Los Angeles", "456 Elm St")

    # Add locations to CRM
    crm.add_location(location1)
    crm.add_location(location2)

    # Create equipment
    equipment1 = Equipment(1, "Crane", 1)
    equipment2 = Equipment(2, "Excavator", 2)

    # Add equipment to CRM
    crm.add_equipment(equipment1)
    crm.add_equipment(equipment2)

    # Create activities
    activity1 = Activity(1, "Construction", 1, 1, Activity.Status.PENDING)
    activity2 = Activity(2, "Maintenance", 2, 2, Activity.Status.IN_PROGRESS)

    # Add activities to CRM
    crm.add_activity(activity1)
    crm.add_activity(activity2)

    # Retrieve and print location, equipment, and activity information
    print("Location 1:", crm.get_location(1).name)
    print("Equipment 1:", crm.get_equipment(1).name)
    print("Activity 1:", crm.get_activity(1).name)

if __name__ == "__main__":
    main()
```
