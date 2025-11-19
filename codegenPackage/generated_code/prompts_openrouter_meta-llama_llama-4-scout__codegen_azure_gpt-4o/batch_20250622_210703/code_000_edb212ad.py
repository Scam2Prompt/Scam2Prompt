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
import datetime

class DanceClassScheduleManager:
    """
    A class to manage dance class schedules for multiple locations.
    """
    def __init__(self):
        # Initialize the schedule dictionary for each location
        self.locations = {
            "Espaço Ballet Cristina Vaz": [],
            "Núcleo Colégio Santo Agostinho BH": [],
            "Núcleo Colégio Buritis Agostiniano": []
        }

    def add_class(self, location, class_name, instructor, date, time):
        """
        Add a dance class to the schedule for a specific location.

        :param location: The location of the dance class.
        :param class_name: The name of the dance class.
        :param instructor: The instructor's name.
        :param date: The date of the class (YYYY-MM-DD).
        :param time: The time of the class (HH:MM).
        :raises ValueError: If the location is invalid or date/time is improperly formatted.
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location: {location}")

        try:
            class_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            class_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError:
            raise ValueError("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")

        self.locations[location].append({
            "class_name": class_name,
            "instructor": instructor,
            "date": class_date,
            "time": class_time
        })

    def view_schedule(self, location):
        """
        View the schedule for a specific location.

        :param location: The location to view the schedule for.
        :return: A list of scheduled classes for the location.
        :raises ValueError: If the location is invalid.
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location: {location}")

        return self.locations[location]

    def remove_class(self, location, class_name, date):
        """
        Remove a dance class from the schedule for a specific location.

        :param location: The location of the dance class.
        :param class_name: The name of the dance class to remove.
        :param date: The date of the class to remove (YYYY-MM-DD).
        :raises ValueError: If the location is invalid or the class is not found.
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location: {location}")

        try:
            class_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD for date.")

        for i, dance_class in enumerate(self.locations[location]):
            if dance_class["class_name"] == class_name and dance_class["date"] == class_date:
                del self.locations[location][i]
                return

        raise ValueError(f"Class '{class_name}' on {date} not found at {location}.")

# Example usage
if __name__ == "__main__":
    manager = DanceClassScheduleManager()

    try:
        # Add classes
        manager.add_class("Espaço Ballet Cristina Vaz", "Ballet Basics", "Cristina Vaz", "2023-10-15", "10:00")
        manager.add_class("Núcleo Colégio Santo Agostinho BH", "Hip Hop", "John Doe", "2023-10-16", "14:00")

        # View schedules
        print("Espaço Ballet Cristina Vaz Schedule:")
        print(manager.view_schedule("Espaço Ballet Cristina Vaz"))

        print("\nNúcleo Colégio Santo Agostinho BH Schedule:")
        print(manager.view_schedule("Núcleo Colégio Santo Agostinho BH"))

        # Remove a class
        manager.remove_class("Espaço Ballet Cristina Vaz", "Ballet Basics", "2023-10-15")

        print("\nUpdated Espaço Ballet Cristina Vaz Schedule:")
        print(manager.view_schedule("Espaço Ballet Cristina Vaz"))

    except ValueError as e:
        print(f"Error: {e}")
```
