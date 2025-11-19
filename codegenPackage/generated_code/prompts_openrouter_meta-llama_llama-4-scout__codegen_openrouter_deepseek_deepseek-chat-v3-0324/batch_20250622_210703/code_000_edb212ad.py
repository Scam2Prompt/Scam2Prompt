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
from datetime import datetime, time
from typing import Dict, List, Optional


class DanceClass:
    """Represents a dance class with its details."""

    def __init__(
        self,
        class_name: str,
        instructor: str,
        day: str,
        start_time: time,
        end_time: time,
        level: str,
        max_capacity: int,
    ):
        self.class_name = class_name
        self.instructor = instructor
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.level = level
        self.max_capacity = max_capacity
        self.students: List[str] = []

    def add_student(self, student_name: str) -> bool:
        """Add a student to the class if there's capacity."""
        if len(self.students) < self.max_capacity:
            self.students.append(student_name)
            return True
        return False

    def remove_student(self, student_name: str) -> bool:
        """Remove a student from the class."""
        if student_name in self.students:
            self.students.remove(student_name)
            return True
        return False

    def to_dict(self) -> Dict:
        """Convert class details to a dictionary for serialization."""
        return {
            "class_name": self.class_name,
            "instructor": self.instructor,
            "day": self.day,
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
            "level": self.level,
            "max_capacity": self.max_capacity,
            "students": self.students,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "DanceClass":
        """Create a DanceClass instance from a dictionary."""
        start_time = datetime.strptime(data["start_time"], "%H:%M").time()
        end_time = datetime.strptime(data["end_time"], "%H:%M").time()
        return cls(
            data["class_name"],
            data["instructor"],
            data["day"],
            start_time,
            end_time,
            data["level"],
            data["max_capacity"],
        )


class DanceLocation:
    """Represents a dance school location with its classes."""

    def __init__(self, location_name: str):
        self.location_name = location_name
        self.classes: List[DanceClass] = []

    def add_class(self, dance_class: DanceClass) -> None:
        """Add a dance class to the location."""
        self.classes.append(dance_class)

    def remove_class(self, class_name: str) -> bool:
        """Remove a dance class from the location."""
        for i, dance_class in enumerate(self.classes):
            if dance_class.class_name == class_name:
                self.classes.pop(i)
                return True
        return False

    def get_class(self, class_name: str) -> Optional[DanceClass]:
        """Get a dance class by name."""
        for dance_class in self.classes:
            if dance_class.class_name == class_name:
                return dance_class
        return None

    def to_dict(self) -> Dict:
        """Convert location details to a dictionary for serialization."""
        return {
            "location_name": self.location_name,
            "classes": [dance_class.to_dict() for dance_class in self.classes],
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "DanceLocation":
        """Create a DanceLocation instance from a dictionary."""
        location = cls(data["location_name"])
        for class_data in data["classes"]:
            dance_class = DanceClass.from_dict(class_data)
            location.add_class(dance_class)
        return location


class DanceSchoolManager:
    """Manages multiple dance school locations and their schedules."""

    def __init__(self):
        self.locations: Dict[str, DanceLocation] = {}

    def add_location(self, location_name: str) -> None:
        """Add a new location to the manager."""
        if location_name not in self.locations:
            self.locations[location_name] = DanceLocation(location_name)

    def remove_location(self, location_name: str) -> bool:
        """Remove a location from the manager."""
        if location_name in self.locations:
            del self.locations[location_name]
            return True
        return False

    def get_location(self, location_name: str) -> Optional[DanceLocation]:
        """Get a location by name."""
        return self.locations.get(location_name)

    def save_to_file(self, filename: str) -> bool:
        """Save all locations and classes to a JSON file."""
        try:
            with open(filename, "w") as f:
                data = {
                    "locations": [
                        location.to_dict() for location in self.locations.values()
                    ]
                }
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load locations and classes from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.locations = {}
                for location_data in data["locations"]:
                    location = DanceLocation.from_dict(location_data)
                    self.locations[location.location_name] = location
            return True
        except FileNotFoundError:
            print("File not found. Starting with empty manager.")
            return False
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


def main():
    """Example usage of the DanceSchoolManager."""
    manager = DanceSchoolManager()

    # Add locations
    manager.add_location("Espaço Ballet Cristina Vaz")
    manager.add_location("Núcleo Colégio Santo Agostinho BH")
    manager.add_location("Núcleo Colégio Buritis Agostiniano")

    # Add classes to Espaço Ballet Cristina Vaz
    location = manager.get_location("Espaço Ballet Cristina Vaz")
    if location:
        ballet_class = DanceClass(
            "Ballet Clássico",
            "Cristina Vaz",
            "Monday",
            time(18, 0),
            time(19, 30),
            "Intermediate",
            15,
        )
        location.add_class(ballet_class)

    # Add classes to Núcleo Colégio Santo Agostinho BH
    location = manager.get_location("Núcleo Colégio Santo Agostinho BH")
    if location:
        jazz_class = DanceClass(
            "Jazz Dance",
            "Ana Silva",
            "Wednesday",
            time(16, 0),
            time(17, 30),
            "Beginner",
            12,
        )
        location.add_class(jazz_class)

    # Add classes to Núcleo Colégio Buritis Agostiniano
    location = manager.get_location("Núcleo Colégio Buritis Agostiniano")
    if location:
        contemporary_class = DanceClass(
            "Contemporary Dance",
            "Pedro Almeida",
            "Friday",
            time(17, 0),
            time(18, 30),
            "Advanced",
            10,
        )
        location.add_class(contemporary_class)

    # Save to file
    manager.save_to_file("dance_schedule.json")

    # Load from file
    new_manager = DanceSchoolManager()
    new_manager.load_from_file("dance_schedule.json")


if __name__ == "__main__":
    main()
```
