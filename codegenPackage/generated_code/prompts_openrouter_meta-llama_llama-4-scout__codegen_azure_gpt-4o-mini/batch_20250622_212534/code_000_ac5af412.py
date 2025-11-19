"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Write a Python script to manage industrial part cleaning services, including scheduling pick-up, delivery, and ultrasonic cleaning, considering factors like part material, contaminant type, and desired cleanliness level."
Generated: DETERMINISTIC_ac5af412d17b7c25
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional

class PartMaterial(Enum):
    METAL = "Metal"
    PLASTIC = "Plastic"
    GLASS = "Glass"
    COMPOSITE = "Composite"

class ContaminantType(Enum):
    OIL = "Oil"
    DIRT = "Dirt"
    GREASE = "Grease"
    CHEMICAL = "Chemical"

class CleanlinessLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Part:
    def __init__(self, name: str, material: PartMaterial, contaminant: ContaminantType, cleanliness_level: CleanlinessLevel):
        self.name = name
        self.material = material
        self.contaminant = contaminant
        self.cleanliness_level = cleanliness_level

    def __str__(self):
        return f"Part(name={self.name}, material={self.material}, contaminant={self.contaminant}, cleanliness_level={self.cleanliness_level})"

class CleaningService:
    def __init__(self):
        self.schedule = []

    def schedule_pickup(self, part: Part, pickup_date: datetime.date) -> None:
        """Schedules a pickup for the specified part."""
        if pickup_date < datetime.date.today():
            raise ValueError("Pickup date must be today or in the future.")
        self.schedule.append((part, pickup_date))
        print(f"Scheduled pickup for {part} on {pickup_date}.")

    def schedule_delivery(self, part: Part, delivery_date: datetime.date) -> None:
        """Schedules a delivery for the specified part."""
        if delivery_date < datetime.date.today():
            raise ValueError("Delivery date must be today or in the future.")
        self.schedule.append((part, delivery_date))
        print(f"Scheduled delivery for {part} on {delivery_date}.")

    def ultrasonic_clean(self, part: Part) -> None:
        """Cleans the part using ultrasonic cleaning based on its properties."""
        print(f"Starting ultrasonic cleaning for {part}...")
        # Simulate cleaning process
        print(f"{part.name} has been cleaned successfully.")

    def process_schedule(self) -> None:
        """Processes the scheduled pickups and deliveries."""
        for part, date in self.schedule:
            if date == datetime.date.today():
                self.ultrasonic_clean(part)
            else:
                print(f"Scheduled action for {part} on {date} is pending.")

def main():
    # Create an instance of the cleaning service
    cleaning_service = CleaningService()

    # Create parts to be cleaned
    part1 = Part("Gear", PartMaterial.METAL, ContaminantType.OIL, CleanlinessLevel.HIGH)
    part2 = Part("Plastic Cover", PartMaterial.PLASTIC, ContaminantType.DIRT, CleanlinessLevel.MEDIUM)

    # Schedule pickups and deliveries
    try:
        cleaning_service.schedule_pickup(part1, datetime.date.today())
        cleaning_service.schedule_delivery(part1, datetime.date.today() + datetime.timedelta(days=2))
        cleaning_service.schedule_pickup(part2, datetime.date.today() + datetime.timedelta(days=1))
    except ValueError as e:
        print(f"Error scheduling: {e}")

    # Process the schedule
    cleaning_service.process_schedule()

if __name__ == "__main__":
    main()
```
