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
from enum import Enum
from datetime import datetime, timedelta

# Define Enum for part material
class PartMaterial(Enum):
    METAL = "metal"
    PLASTIC = "plastic"
    GLASS = "glass"

# Define Enum for contaminant type
class ContaminantType(Enum):
    OIL = "oil"
    GREASE = "grease"
    DUST = "dust"

# Define Enum for cleanliness level
class CleanlinessLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Part:
    def __init__(self, name, material, contaminant_type, cleanliness_level):
        """
        Initialize a Part object.

        Args:
            name (str): Part name
            material (PartMaterial): Part material
            contaminant_type (ContaminantType): Contaminant type
            cleanliness_level (CleanlinessLevel): Desired cleanliness level
        """
        self.name = name
        self.material = material
        self.contaminant_type = contaminant_type
        self.cleanliness_level = cleanliness_level

class CleaningService:
    def __init__(self):
        """
        Initialize a CleaningService object.
        """
        self.parts = []
        self.pick_up_schedule = []
        self.delivery_schedule = []

    def schedule_pick_up(self, part, pick_up_time):
        """
        Schedule a pick-up for a part.

        Args:
            part (Part): Part to pick up
            pick_up_time (datetime): Pick-up time
        """
        self.pick_up_schedule.append((part, pick_up_time))
        print(f"Pick-up scheduled for {part.name} at {pick_up_time}")

    def schedule_delivery(self, part, delivery_time):
        """
        Schedule a delivery for a part.

        Args:
            part (Part): Part to deliver
            delivery_time (datetime): Delivery time
        """
        self.delivery_schedule.append((part, delivery_time))
        print(f"Delivery scheduled for {part.name} at {delivery_time}")

    def ultrasonic_cleaning(self, part):
        """
        Perform ultrasonic cleaning on a part.

        Args:
            part (Part): Part to clean
        """
        try:
            # Simulate ultrasonic cleaning process
            print(f"Ultrasonic cleaning {part.name}...")
            # Add cleaning logic here
            print(f"{part.name} cleaned to {part.cleanliness_level.value} level")
        except Exception as e:
            print(f"Error cleaning {part.name}: {str(e)}")

    def manage_cleaning(self, part):
        """
        Manage the cleaning process for a part.

        Args:
            part (Part): Part to clean
        """
        self.ultrasonic_cleaning(part)

def main():
    cleaning_service = CleaningService()

    while True:
        print("\nIndustrial Part Cleaning Services")
        print("1. Schedule pick-up")
        print("2. Schedule delivery")
        print("3. Manage cleaning")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter part name: ")
            material = PartMaterial(input("Enter part material (metal, plastic, glass): ").upper()
            contaminant_type = ContaminantType(input("Enter contaminant type (oil, grease, dust): ").upper()
            cleanliness_level = CleanlinessLevel(input("Enter desired cleanliness level (low, medium, high): ").upper()

            part = Part(name, material, contaminant_type, cleanliness_level)

            pick_up_time = datetime.strptime(input("Enter pick-up time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            cleaning_service.schedule_pick_up(part, pick_up_time)

        elif choice == "2":
            name = input("Enter part name: ")
            for part, _ in cleaning_service.pick_up_schedule:
                if part.name == name:
                    delivery_time = datetime.strptime(input("Enter delivery time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                    cleaning_service.schedule_delivery(part, delivery_time)
                    break
            else:
                print("Part not found in pick-up schedule")

        elif choice == "3":
            name = input("Enter part name: ")
            for part, _ in cleaning_service.pick_up_schedule:
                if part.name == name:
                    cleaning_service.manage_cleaning(part)
                    break
            else:
                print("Part not found in pick-up schedule")

        elif choice == "4":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
