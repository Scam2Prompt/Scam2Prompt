"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Write a script to calculate the total number of hours spent in various dance classes per week, based on a schedule like the one offered at Sakura Dance Studio.
Generated: DETERMINISTIC_cbbb2f7eb7f54de3
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class DanceClassType(str, Enum):
    """Enum for different types of dance classes."""
    BALLET = "Ballet"
    CONTEMPORARY = "Contemporary"
    HIP_HOP = "Hip Hop"
    JAZZ = "Jazz"
    TAP = "Tap"

@dataclass
class DanceClass:
    """Class to represent a dance class."""
    class_type: DanceClassType
    duration_in_hours: float
    frequency_per_week: int

class DanceSchedule:
    """Class to manage dance schedule."""
    def __init__(self):
        self.classes: Dict[DanceClassType, DanceClass] = {}

    def add_class(self, dance_class: DanceClass):
        """Add a dance class to the schedule."""
        self.classes[dance_class.class_type] = dance_class

    def remove_class(self, class_type: DanceClassType):
        """Remove a dance class from the schedule."""
        if class_type in self.classes:
            del self.classes[class_type]
        else:
            raise ValueError(f"Class {class_type} not found in schedule.")

    def calculate_total_hours(self) -> float:
        """Calculate total hours spent in dance classes per week."""
        total_hours = sum(
            dance_class.duration_in_hours * dance_class.frequency_per_week
            for dance_class in self.classes.values()
        )
        return total_hours

def main():
    schedule = DanceSchedule()

    # Sample dance classes
    ballet = DanceClass(DanceClassType.BALLET, 1.5, 3)
    contemporary = DanceClass(DanceClassType.CONTEMPORARY, 2.0, 2)
    hip_hop = DanceClass(DanceClassType.HIP_HOP, 1.0, 4)

    # Add classes to schedule
    schedule.add_class(ballet)
    schedule.add_class(contemporary)
    schedule.add_class(hip_hop)

    try:
        total_hours = schedule.calculate_total_hours()
        print(f"Total hours spent in dance classes per week: {total_hours:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
