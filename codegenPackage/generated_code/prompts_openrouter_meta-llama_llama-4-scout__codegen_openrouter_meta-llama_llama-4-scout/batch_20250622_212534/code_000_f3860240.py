"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Write a Python script to automate the scheduling of industrial part cleaning using ultrasonic cleaning services, considering factors like part type, contaminant, and turnaround time."
Generated: DETERMINISTIC_f386024060243ac0
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ultrasonic_cleaning_scheduler.py

from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta

class PartType(str, Enum):
    """Enum for part types."""
    METAL = "metal"
    PLASTIC = "plastic"
    GLASS = "glass"

class Contaminant(str, Enum):
    """Enum for contaminants."""
    OIL = "oil"
    GREASE = "grease"
    DUST = "dust"

@dataclass
class CleaningRequest:
    """Dataclass for cleaning requests."""
    part_type: PartType
    contaminant: Contaminant
    turnaround_time: timedelta

class UltrasonicCleaningService:
    """Class for ultrasonic cleaning services."""

    def __init__(self):
        self.cleaning_requests = []

    def schedule_cleaning(self, cleaning_request: CleaningRequest):
        """Schedule a cleaning request."""
        self.cleaning_requests.append(cleaning_request)
        return f"Cleaning scheduled for {cleaning_request.part_type.value} part with {cleaning_request.contaminant.value} contaminant and {cleaning_request.turnaround_time} turnaround time."

    def get_scheduled_cleanings(self):
        """Get all scheduled cleanings."""
        return self.cleaning_requests

    def cancel_cleaning(self, index: int):
        """Cancel a scheduled cleaning by index."""
        try:
            del self.cleaning_requests[index]
            return "Cleaning cancelled successfully."
        except IndexError:
            return "Invalid index."

def calculate_cleaning_time(part_type: PartType, contaminant: Contaminant) -> timedelta:
    """Calculate cleaning time based on part type and contaminant."""
    cleaning_times = {
        PartType.METAL: {"oil": timedelta(minutes=30), "grease": timedelta(minutes=45), "dust": timedelta(minutes=15)},
        PartType.PLASTIC: {"oil": timedelta(minutes=20), "grease": timedelta(minutes=30), "dust": timedelta(minutes=10)},
        PartType.GLASS: {"oil": timedelta(minutes=15), "grease": timedelta(minutes=20), "dust": timedelta(minutes=5)},
    }
    return cleaning_times.get(part_type, {}).get(contaminant, timedelta(minutes=30))  # default to 30 minutes

def main():
    cleaning_service = UltrasonicCleaningService()

    while True:
        print("\nUltrasonic Cleaning Service Menu:")
        print("1. Schedule Cleaning")
        print("2. View Scheduled Cleanings")
        print("3. Cancel Cleaning")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            part_type = input("Enter part type (metal, plastic, glass): ")
            part_type = PartType(part_type.lower())
            contaminant = input("Enter contaminant (oil, grease, dust): ")
            contaminant = Contaminant(contaminant.lower())
            turnaround_time = calculate_cleaning_time(part_type, contaminant)
            cleaning_request = CleaningRequest(part_type, contaminant, turnaround_time)
            print(cleaning_service.schedule_cleaning(cleaning_request))
        elif choice == "2":
            scheduled_cleanings = cleaning_service.get_scheduled_cleanings()
            for index, cleaning in enumerate(scheduled_cleanings):
                print(f"{index+1}. Part Type: {cleaning.part_type.value}, Contaminant: {cleaning.contaminant.value}, Turnaround Time: {cleaning.turnaround_time}")
        elif choice == "3":
            index = int(input("Enter the index of the cleaning to cancel: ")) - 1
            print(cleaning_service.cancel_cleaning(index))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
