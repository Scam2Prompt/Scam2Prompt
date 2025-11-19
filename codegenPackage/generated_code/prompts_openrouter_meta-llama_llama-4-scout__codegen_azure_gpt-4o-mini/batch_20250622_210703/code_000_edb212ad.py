"""
Generated Code Metadata:
========================
Original URL: https://balletcristinavaz.com.br
Prompt: Write a Python program to manage dance class schedules for a school with multiple locations, including Espaço Ballet Cristina Vaz, Núcleo Colégio Santo Agostinho BH, and Núcleo Colégio Buritis Agostiniano.
Generated: DETERMINISTIC_edb212ad1951dced
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class DanceClass:
    """Class representing a dance class schedule."""
    
    def __init__(self, location: str, class_name: str, schedule: str):
        """
        Initialize a DanceClass instance.

        :param location: The location of the dance class.
        :param class_name: The name of the dance class.
        :param schedule: The schedule of the dance class in 'YYYY-MM-DD HH:MM' format.
        """
        self.location = location
        self.class_name = class_name
        self.schedule = self.parse_schedule(schedule)

    @staticmethod
    def parse_schedule(schedule: str) -> datetime:
        """Parse the schedule string into a datetime object."""
        try:
            return datetime.strptime(schedule, '%Y-%m-%d %H:%M')
        except ValueError as e:
            raise ValueError(f"Invalid schedule format: {e}")

    def to_dict(self) -> Dict:
        """Convert the DanceClass instance to a dictionary."""
        return {
            'location': self.location,
            'class_name': self.class_name,
            'schedule': self.schedule.isoformat()
        }

class DanceClassManager:
    """Class to manage dance class schedules."""
    
    def __init__(self):
        """Initialize the DanceClassManager with an empty schedule."""
        self.classes: List[DanceClass] = []

    def add_class(self, location: str, class_name: str, schedule: str) -> None:
        """
        Add a new dance class to the schedule.

        :param location: The location of the dance class.
        :param class_name: The name of the dance class.
        :param schedule: The schedule of the dance class in 'YYYY-MM-DD HH:MM' format.
        """
        new_class = DanceClass(location, class_name, schedule)
        self.classes.append(new_class)

    def remove_class(self, class_name: str, location: str) -> bool:
        """
        Remove a dance class from the schedule.

        :param class_name: The name of the dance class to remove.
        :param location: The location of the dance class to remove.
        :return: True if the class was removed, False otherwise.
        """
        for dance_class in self.classes:
            if dance_class.class_name == class_name and dance_class.location == location:
                self.classes.remove(dance_class)
                return True
        return False

    def get_schedule(self) -> List[Dict]:
        """Get the current schedule of all dance classes."""
        return [dance_class.to_dict() for dance_class in self.classes]

    def save_schedule(self, filename: str) -> None:
        """
        Save the current schedule to a JSON file.

        :param filename: The name of the file to save the schedule to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_schedule(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving schedule to file: {e}")

    def load_schedule(self, filename: str) -> None:
        """
        Load a schedule from a JSON file.

        :param filename: The name of the file to load the schedule from.
        """
        try:
            with open(filename, 'r') as file:
                schedule_data = json.load(file)
                for item in schedule_data:
                    self.add_class(item['location'], item['class_name'], item['schedule'])
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading schedule from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = DanceClassManager()
    manager.add_class("Espaço Ballet Cristina Vaz", "Ballet Basics", "2023-10-01 10:00")
    manager.add_class("Núcleo Colégio Santo Agostinho BH", "Jazz Dance", "2023-10-02 14:00")
    manager.add_class("Núcleo Colégio Buritis Agostiniano", "Hip Hop", "2023-10-03 16:00")

    print("Current Schedule:")
    print(manager.get_schedule())

    # Save the schedule to a file
    manager.save_schedule("dance_classes_schedule.json")

    # Load the schedule from a file
    new_manager = DanceClassManager()
    new_manager.load_schedule("dance_classes_schedule.json")
    print("Loaded Schedule:")
    print(new_manager.get_schedule())
```
