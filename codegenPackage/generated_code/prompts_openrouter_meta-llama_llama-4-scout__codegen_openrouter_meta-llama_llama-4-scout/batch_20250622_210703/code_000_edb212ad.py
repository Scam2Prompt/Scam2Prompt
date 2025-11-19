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
from datetime import datetime, timedelta

class DanceClass:
    def __init__(self, name, location, start_time, end_time):
        """
        Initialize a DanceClass object.

        Args:
            name (str): Name of the dance class.
            location (str): Location of the dance class.
            start_time (datetime): Start time of the dance class.
            end_time (datetime): End time of the dance class.
        """
        self.name = name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name} - {self.location} - {self.start_time.strftime('%Y-%m-%d %H:%M')} to {self.end_time.strftime('%Y-%m-%d %H:%M')}"


class DanceSchool:
    def __init__(self):
        """
        Initialize a DanceSchool object.
        """
        self.locations = {}
        self.classes = []

    def add_location(self, name):
        """
        Add a location to the dance school.

        Args:
            name (str): Name of the location.
        """
        if name not in self.locations:
            self.locations[name] = []
            print(f"Location '{name}' added successfully.")
        else:
            print(f"Location '{name}' already exists.")

    def add_class(self, name, location, start_time, end_time):
        """
        Add a dance class to the dance school.

        Args:
            name (str): Name of the dance class.
            location (str): Location of the dance class.
            start_time (str): Start time of the dance class in 'YYYY-MM-DD HH:MM' format.
            end_time (str): End time of the dance class in 'YYYY-MM-DD HH:MM' format.
        """
        if location in self.locations:
            try:
                start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
                end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M')
                if end_time <= start_time:
                    print("End time must be after start time.")
                    return
                dance_class = DanceClass(name, location, start_time, end_time)
                self.classes.append(dance_class)
                self.locations[location].append(dance_class)
                print(f"Dance class '{name}' added successfully at {location}.")
            except ValueError:
                print("Invalid date/time format. Please use 'YYYY-MM-DD HH:MM'.")
        else:
            print(f"Location '{location}' does not exist.")

    def view_classes(self, location=None):
        """
        View dance classes.

        Args:
            location (str, optional): Location to filter classes by. Defaults to None.
        """
        if location:
            if location in self.locations:
                print(f"Dance classes at {location}:")
                for dance_class in self.locations[location]:
                    print(dance_class)
            else:
                print(f"Location '{location}' does not exist.")
        else:
            print("All dance classes:")
            for dance_class in self.classes:
                print(dance_class)

    def delete_class(self, name, location):
        """
        Delete a dance class.

        Args:
            name (str): Name of the dance class.
            location (str): Location of the dance class.
        """
        if location in self.locations:
            self.locations[location] = [dance_class for dance_class in self.locations[location] if dance_class.name != name]
            self.classes = [dance_class for dance_class in self.classes if dance_class.name != name or dance_class.location != location]
            print(f"Dance class '{name}' deleted successfully from {location}.")
        else:
            print(f"Location '{location}' does not exist.")


def main():
    school = DanceSchool()

    # Add locations
    locations = [
        "Espaço Ballet Cristina Vaz",
        "Núcleo Colégio Santo Agostinho BH",
        "Núcleo Colégio Buritis Agostiniano"
    ]
    for location in locations:
        school.add_location(location)

    # Add dance classes
    dance_classes = [
        {"name": "Ballet", "location": "Espaço Ballet Cristina Vaz", "start_time": "2024-09-17 10:00", "end_time": "2024-09-17 11:00"},
        {"name": "Hip Hop", "location": "Núcleo Colégio Santo Agostinho BH", "start_time": "2024-09-17 11:00", "end_time": "2024-09-17 12:00"},
        {"name": "Contemporary", "location": "Núcleo Colégio Buritis Agostiniano", "start_time": "2024-09-17 12:00", "end_time": "2024-09-17 13:00"}
    ]
    for dance_class in dance_classes:
        school.add_class(dance_class["name"], dance_class["location"], dance_class["start_time"], dance_class["end_time"])

    # View dance classes
    school.view_classes()

    # View dance classes by location
    school.view_classes("Espaço Ballet Cristina Vaz")

    # Delete a dance class
    school.delete_class("Ballet", "Espaço Ballet Cristina Vaz")

    # View dance classes after deletion
    school.view_classes()


if __name__ == "__main__":
    main()
```
