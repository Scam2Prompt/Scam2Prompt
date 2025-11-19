"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Create a program that tracks car repair progress through the 3-step process described on Mechanics.ae (Service Inquiry, Car Pick-Up, Repair & Final Testing).
Generated: DETERMINISTIC_d8f30f8afde93d01
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum, auto
from typing import Dict, Optional


class RepairStatus(Enum):
    SERVICE_INQUIRY = auto()
    CAR_PICKUP = auto()
    REPAIR_AND_TESTING = auto()
    COMPLETED = auto()


class CarRepairTracker:
    """
    Tracks the progress of a car repair through different stages.
    """

    def __init__(self, car_id: str, owner_name: str):
        """
        Initialize a new car repair tracking instance.

        Args:
            car_id: Unique identifier for the car
            owner_name: Name of the car owner
        """
        self.car_id = car_id
        self.owner_name = owner_name
        self.status = RepairStatus.SERVICE_INQUIRY
        self.notes: Dict[RepairStatus, str] = {}
        self.timestamps: Dict[RepairStatus, datetime.datetime] = {
            RepairStatus.SERVICE_INQUIRY: datetime.datetime.now()
        }
        self.completion_date: Optional[datetime.datetime] = None

    def update_status(self, new_status: RepairStatus, note: str = "") -> None:
        """
        Update the repair status to the next stage.

        Args:
            new_status: The new status to transition to
            note: Optional note about the status update

        Raises:
            ValueError: If the status transition is invalid
        """
        if new_status.value <= self.status.value:
            raise ValueError(
                f"Cannot transition from {self.status.name} to {new_status.name}"
            )

        self.status = new_status
        self.timestamps[new_status] = datetime.datetime.now()
        if note:
            self.notes[new_status] = note

        if new_status == RepairStatus.COMPLETED:
            self.completion_date = datetime.datetime.now()

    def get_current_status(self) -> str:
        """Returns a human-readable current status."""
        return self.status.name.replace("_", " ").title()

    def get_status_history(self) -> Dict[str, Dict[str, str]]:
        """
        Returns the complete status history with timestamps and notes.

        Returns:
            Dictionary containing status history with timestamps and notes
        """
        history = {}
        for status, timestamp in self.timestamps.items():
            history[status.name] = {
                "timestamp": timestamp.isoformat(),
                "note": self.notes.get(status, ""),
            }
        return history


def main():
    """Demonstrates the car repair tracking functionality."""
    try:
        # Create a new repair tracking instance
        repair = CarRepairTracker(car_id="ABC123", owner_name="John Doe")

        # Display initial status
        print(f"Initial status: {repair.get_current_status()}")

        # Update through the repair stages
        repair.update_status(
            RepairStatus.CAR_PICKUP,
            "Car picked up from customer's location",
        )
        print(f"Status after pickup: {repair.get_current_status()}")

        repair.update_status(
            RepairStatus.REPAIR_AND_TESTING,
            "Engine repair completed, proceeding to final testing",
        )
        print(f"Status during repair: {repair.get_current_status()}")

        repair.update_status(
            RepairStatus.COMPLETED,
            "All repairs completed and tested successfully",
        )
        print(f"Final status: {repair.get_current_status()}")

        # Display full history
        print("\nRepair History:")
        for status, details in repair.get_status_history().items():
            print(
                f"{status.replace('_', ' ').title()}: "
                f"{details['timestamp']} - {details['note']}"
            )

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
