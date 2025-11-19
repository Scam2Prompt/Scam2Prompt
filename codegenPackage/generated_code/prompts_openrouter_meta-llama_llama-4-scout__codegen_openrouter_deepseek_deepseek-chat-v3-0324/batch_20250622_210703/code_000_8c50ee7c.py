"""
Generated Code Metadata:
========================
Original URL: https://gardennovaera.com.br
Prompt: Write a Python program to manage hotel room bookings, including types like casal com hidromassagem, casal, and solteiro, with options for add-ons like breakfast.
Generated: DETERMINISTIC_8c50ee7cee72edfa
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
from typing import Dict, List, Optional, Tuple


class RoomBookingSystem:
    """
    A system to manage hotel room bookings with different room types and add-ons.
    """

    def __init__(self, data_file: str = "bookings.json"):
        """
        Initialize the booking system with a data file for persistence.
        """
        self.data_file = data_file
        self.bookings: List[Dict] = []
        self.room_types = {
            "casal com hidromassagem": {"price": 300, "capacity": 2},
            "casal": {"price": 200, "capacity": 2},
            "solteiro": {"price": 100, "capacity": 1},
        }
        self.add_ons = {
            "breakfast": {"price": 20, "description": "Daily breakfast included"},
        }
        self._load_data()

    def _load_data(self) -> None:
        """Load booking data from the data file."""
        try:
            with open(self.data_file, "r") as f:
                self.bookings = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bookings = []

    def _save_data(self) -> None:
        """Save booking data to the data file."""
        with open(self.data_file, "w") as f:
            json.dump(self.bookings, f, indent=2)

    def _validate_booking_dates(self, check_in: str, check_out: str) -> Tuple[bool, str]:
        """
        Validate booking dates.
        Returns (is_valid, error_message)
        """
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            
            if check_out_date <= check_in_date:
                return False, "Check-out date must be after check-in date."
            
            if check_in_date < datetime.now():
                return False, "Check-in date cannot be in the past."
            
            return True, ""
        except ValueError:
            return False, "Invalid date format. Please use YYYY-MM-DD."

    def _is_room_available(self, room_type: str, check_in: str, check_out: str) -> bool:
        """
        Check if a room of given type is available for the specified dates.
        """
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

        for booking in self.bookings:
            if booking["room_type"] != room_type:
                continue

            existing_check_in = datetime.strptime(booking["check_in"], "%Y-%m-%d")
            existing_check_out = datetime.strptime(booking["check_out"], "%Y-%m-%d")

            if not (check_out_date <= existing_check_in or check_in_date >= existing_check_out):
                return False

        return True

    def create_booking(
        self,
        guest_name: str,
        room_type: str,
        check_in: str,
        check_out: str,
        add_ons: Optional[List[str]] = None,
    ) -> Dict:
        """
        Create a new room booking.
        Returns the booking details or raises an exception if invalid.
        """
        if room_type not in self.room_types:
            raise ValueError(f"Invalid room type. Available types: {list(self.room_types.keys())}")

        is_valid, error_msg = self._validate_booking_dates(check_in, check_out)
        if not is_valid:
            raise ValueError(error_msg)

        if not self._is_room_available(room_type, check_in, check_out):
            raise ValueError("Room not available for the selected dates")

        if add_ons:
            invalid_add_ons = [add_on for add_on in add_ons if add_on not in self.add_ons]
            if invalid_add_ons:
                raise ValueError(f"Invalid add-ons: {invalid_add_ons}")

        base_price = self.room_types[room_type]["price"]
        add_ons_price = sum(self.add_ons[add_on]["price"] for add_on in add_ons) if add_ons else 0
        total_price = base_price + add_ons_price

        booking = {
            "id": len(self.bookings) + 1,
            "guest_name": guest_name,
            "room_type": room_type,
            "check_in": check_in,
            "check_out": check_out,
            "add_ons": add_ons or [],
            "base_price": base_price,
            "add_ons_price": add_ons_price,
            "total_price": total_price,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.bookings.append(booking)
        self._save_data()
        return booking

    def get_booking(self, booking_id: int) -> Optional[Dict]:
        """Retrieve a booking by ID."""
        for booking in self.bookings:
            if booking["id"] == booking_id:
                return booking
        return None

    def cancel_booking(self, booking_id: int) -> bool:
        """Cancel a booking by ID. Returns True if successful."""
        for i, booking in enumerate(self.bookings):
            if booking["id"] == booking_id:
                del self.bookings[i]
                self._save_data()
                return True
        return False

    def list_bookings(self) -> List[Dict]:
        """List all current bookings."""
        return self.bookings

    def list_available_rooms(self, check_in: str, check_out: str) -> Dict[str, bool]:
        """
        List availability of all room types for given dates.
        Returns a dictionary of room_type: availability_status.
        """
        is_valid, error_msg = self._validate_booking_dates(check_in, check_out)
        if not is_valid:
            raise ValueError(error_msg)

        availability = {}
        for room_type in self.room_types:
            availability[room_type] = self._is_room_available(room_type, check_in, check_out)
        return availability

    def get_add_ons(self) -> Dict[str, Dict]:
        """Get available add-ons with their details."""
        return self.add_ons


# Example usage
if __name__ == "__main__":
    booking_system = RoomBookingSystem()

    # Create a booking
    try:
        booking = booking_system.create_booking(
            guest_name="John Doe",
            room_type="casal com hidromassagem",
            check_in="2023-12-15",
            check_out="2023-12-20",
            add_ons=["breakfast"],
        )
        print("Booking created successfully:")
        print(json.dumps(booking, indent=2))
    except ValueError as e:
        print(f"Error creating booking: {e}")

    # List all bookings
    print("\nAll bookings:")
    for booking in booking_system.list_bookings():
        print(f"{booking['id']}: {booking['guest_name']} - {booking['room_type']}")

    # Check room availability
    print("\nRoom availability for 2023-12-15 to 2023-12-20:")
    availability = booking_system.list_available_rooms("2023-12-15", "2023-12-20")
    for room_type, is_available in availability.items():
        print(f"{room_type}: {'Available' if is_available else 'Booked'}")
```
