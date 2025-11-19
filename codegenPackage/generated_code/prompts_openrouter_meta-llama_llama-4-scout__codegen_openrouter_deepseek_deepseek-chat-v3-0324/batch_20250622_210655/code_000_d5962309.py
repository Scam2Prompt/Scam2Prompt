"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Write a Python code snippet to manage hotel room reservations, including simple, double, and family rooms, with options for breakfast and lunch menu selection.
Generated: DETERMINISTIC_d5962309da769531
Batch ID: 20250622_210655
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
from enum import Enum
from typing import Dict, List, Optional


class RoomType(Enum):
    """Enumeration for room types."""
    SINGLE = "single"
    DOUBLE = "double"
    FAMILY = "family"


class MealOption(Enum):
    """Enumeration for meal options."""
    NONE = "none"
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    BOTH = "both"


class Reservation:
    """Class representing a hotel room reservation."""

    def __init__(
        self,
        guest_name: str,
        room_type: RoomType,
        check_in: str,
        check_out: str,
        meal_option: MealOption = MealOption.NONE,
    ):
        """Initialize a reservation.

        Args:
            guest_name: Name of the guest.
            room_type: Type of room (SINGLE, DOUBLE, FAMILY).
            check_in: Check-in date in YYYY-MM-DD format.
            check_out: Check-out date in YYYY-MM-DD format.
            meal_option: Meal option (NONE, BREAKFAST, LUNCH, BOTH).
        """
        self.guest_name = guest_name
        self.room_type = room_type
        self.check_in = check_in
        self.check_out = check_out
        self.meal_option = meal_option

    def to_dict(self) -> Dict:
        """Convert reservation to a dictionary for serialization."""
        return {
            "guest_name": self.guest_name,
            "room_type": self.room_type.value,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "meal_option": self.meal_option.value,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Reservation':
        """Create a reservation from a dictionary."""
        return cls(
            guest_name=data["guest_name"],
            room_type=RoomType(data["room_type"]),
            check_in=data["check_in"],
            check_out=data["check_out"],
            meal_option=MealOption(data["meal_option"]),
        )


class HotelReservationSystem:
    """Class to manage hotel room reservations."""

    def __init__(self, storage_file: str = "reservations.json"):
        """Initialize the reservation system.

        Args:
            storage_file: File to store reservations.
        """
        self.storage_file = storage_file
        self.reservations: List[Reservation] = []
        self._load_reservations()

    def _load_reservations(self) -> None:
        """Load reservations from the storage file."""
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                self.reservations = [Reservation.from_dict(item) for item in data]
        except FileNotFoundError:
            self.reservations = []
        except json.JSONDecodeError:
            raise ValueError("Invalid data in storage file.")

    def _save_reservations(self) -> None:
        """Save reservations to the storage file."""
        with open(self.storage_file, "w") as file:
            json.dump([res.to_dict() for res in self.reservations], file, indent=2)

    def add_reservation(self, reservation: Reservation) -> None:
        """Add a new reservation.

        Args:
            reservation: Reservation object to add.
        """
        self._validate_dates(reservation.check_in, reservation.check_out)
        self.reservations.append(reservation)
        self._save_reservations()

    def get_reservations(self) -> List[Reservation]:
        """Get all reservations.

        Returns:
            List of all reservations.
        """
        return self.reservations

    def get_reservation_by_guest(self, guest_name: str) -> Optional[Reservation]:
        """Get reservation by guest name.

        Args:
            guest_name: Name of the guest.

        Returns:
            Reservation if found, None otherwise.
        """
        for res in self.reservations:
            if res.guest_name.lower() == guest_name.lower():
                return res
        return None

    def cancel_reservation(self, guest_name: str) -> bool:
        """Cancel a reservation by guest name.

        Args:
            guest_name: Name of the guest.

        Returns:
            True if reservation was canceled, False otherwise.
        """
        reservation = self.get_reservation_by_guest(guest_name)
        if reservation:
            self.reservations.remove(reservation)
            self._save_reservations()
            return True
        return False

    def _validate_dates(self, check_in: str, check_out: str) -> None:
        """Validate check-in and check-out dates.

        Args:
            check_in: Check-in date in YYYY-MM-DD format.
            check_out: Check-out date in YYYY-MM-DD format.

        Raises:
            ValueError: If dates are invalid.
        """
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date.")

        if check_in_date < datetime.now():
            raise ValueError("Check-in date cannot be in the past.")


# Example usage
if __name__ == "__main__":
    system = HotelReservationSystem()

    # Add a reservation
    reservation = Reservation(
        guest_name="John Doe",
        room_type=RoomType.DOUBLE,
        check_in="2023-12-01",
        check_out="2023-12-05",
        meal_option=MealOption.BOTH,
    )
    system.add_reservation(reservation)

    # Get all reservations
    reservations = system.get_reservations()
    print(f"Total reservations: {len(reservations)}")

    # Get a specific reservation
    res = system.get_reservation_by_guest("John Doe")
    if res:
        print(f"Found reservation: {res.guest_name}")

    # Cancel a reservation
    if system.cancel_reservation("John Doe"):
        print("Reservation canceled.")
```
