"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: Describe how to implement a maintenance schedule for the equipment provided by МЕГАМАШ, focusing on the unique components mentioned on their site.
Generated: DETERMINISTIC_107a20df7f1b894f
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Maintenance Schedule Implementation for МЕГАМАШ Equipment

This script generates a maintenance schedule for equipment provided by МЕГАМАШ.
It focuses on unique components mentioned on their site and ensures proper tracking
and scheduling of maintenance tasks.

Requirements:
- Python 3.x
"""

import datetime
import json

# Define a class to represent equipment and its maintenance schedule
class Equipment:
    """
    Represents a piece of equipment and its maintenance schedule.
    """
    def __init__(self, name, components, maintenance_intervals):
        """
        Initialize the equipment object.

        :param name: Name of the equipment
        :param components: List of unique components
        :param maintenance_intervals: Dictionary mapping components to maintenance intervals (in days)
        """
        self.name = name
        self.components = components
        self.maintenance_intervals = maintenance_intervals
        self.last_maintenance = {component: None for component in components}

    def schedule_maintenance(self):
        """
        Generate the next maintenance schedule for each component.

        :return: Dictionary mapping components to their next maintenance date
        """
        next_schedule = {}
        for component, interval in self.maintenance_intervals.items():
            last_date = self.last_maintenance.get(component)
            if last_date:
                next_date = last_date + datetime.timedelta(days=interval)
            else:
                next_date = datetime.datetime.now() + datetime.timedelta(days=interval)
            next_schedule[component] = next_date
        return next_schedule

    def perform_maintenance(self, component):
        """
        Record maintenance for a specific component.

        :param component: Component name
        :raises ValueError: If the component is not part of the equipment
        """
        if component not in self.components:
            raise ValueError(f"Component '{component}' is not part of the equipment '{self.name}'.")
        self.last_maintenance[component] = datetime.datetime.now()

    def to_dict(self):
        """
        Convert the equipment object to a dictionary for serialization.

        :return: Dictionary representation of the equipment
        """
        return {
            "name": self.name,
            "components": self.components,
            "maintenance_intervals": self.maintenance_intervals,
            "last_maintenance": {
                component: date.strftime("%Y-%m-%d %H:%M:%S") if date else None
                for component, date in self.last_maintenance.items()
            },
        }


# Define a function to save equipment data to a file
def save_equipment_data(equipment, filename):
    """
    Save equipment data to a JSON file.

    :param equipment: Equipment object
    :param filename: File name to save the data
    """
    try:
        with open(filename, "w") as file:
            json.dump(equipment.to_dict(), file, indent=4)
    except IOError as e:
        print(f"Error saving equipment data: {e}")


# Define a function to load equipment data from a file
def load_equipment_data(filename):
    """
    Load equipment data from a JSON file.

    :param filename: File name to load the data from
    :return: Equipment object
    :raises IOError: If the file cannot be read
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return Equipment(
                name=data["name"],
                components=data["components"],
                maintenance_intervals=data["maintenance_intervals"],
            )
    except IOError as e:
        print(f"Error loading equipment data: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define equipment and its unique components
    megamash_equipment = Equipment(
        name="МЕГАМАШ Model X",
        components=["Hydraulic Pump", "Cooling System", "Control Panel"],
        maintenance_intervals={"Hydraulic Pump": 30, "Cooling System": 60, "Control Panel": 90},
    )

    # Perform maintenance on a component
    try:
        megamash_equipment.perform_maintenance("Hydraulic Pump")
    except ValueError as e:
        print(e)

    # Generate the next maintenance schedule
    schedule = megamash_equipment.schedule_maintenance()
    print("Next Maintenance Schedule:")
    for component, date in schedule.items():
        print(f"{component}: {date.strftime('%Y-%m-%d %H:%M:%S')}")

    # Save equipment data to a file
    save_equipment_data(megamash_equipment, "megamash_equipment.json")

    # Load equipment data from a file
    loaded_equipment = load_equipment_data("megamash_equipment.json")
    if loaded_equipment:
        print("Loaded Equipment Data:")
        print(loaded_equipment.to_dict())
```
