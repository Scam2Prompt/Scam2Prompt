"""
Generated Code Metadata:
========================
Original URL: https://lhotel-des-chats.com
Prompt: Write a Python program to manage bookings for a cat hotel with services like boarding and daycare, considering factors like room types and availability.
Generated: DETERMINISTIC_873b81b46aeafd42
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class CatHotel:
    """A class to manage bookings for a cat hotel."""

    def __init__(self):
        """Initialize the cat hotel with default rooms and services."""
        self.rooms = {
            "standard": {"price": 30, "capacity": 10, "available": 10},
            "deluxe": {"price": 50, "capacity": 5, "available": 5},
            "suite": {"price": 80, "capacity": 3, "available": 3},
        }
        self.services = {
            "boarding": {"daily_rate": 20},
            "daycare": {"hourly_rate": 10},
        }
        self.bookings = []
        self.next_booking_id = 1

    def check_availability(self, room_type: str, start_date: str, end_date: str) -> bool:
        """Check if a room type is available for the given dates.

        Args:
            room_type: Type of room (standard, deluxe, suite).
            start_date: Start date in 'YYYY-MM-DD' format.
            end_date: End date in 'YYYY-MM-DD' format.

        Returns:
            bool: True if room is available, False otherwise.
        """
        if room_type not in self.rooms:
            return False

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if start >= end:
            return False

        for booking in self.bookings:
            if booking["room_type"] == room_type:
                booking_start = datetime.strptime(booking["start_date"], "%Y-%m-%d")
                booking_end = datetime.strptime(booking["end_date"], "%Y-%m-%d")
                if not (end <= booking_start or start >= booking_end):
                    return False

        return self.rooms[room_type]["available"] > 0

    def make_booking(
        self,
        guest_name: str,
        cat_name: str,
        room_type: str,
        start_date: str,
        end_date: str,
        service_type: str,
    ) -> Optional[Dict]:
        """Create a new booking if room and dates are available.

        Args:
            guest_name: Name of the guest making the booking.
            cat_name: Name of the cat.
            room_type: Type of room (standard, deluxe, suite).
            start_date: Start date in 'YYYY-MM-DD' format.
            end_date: End date in 'YYYY-MM-DD' format.
            service_type: Type of service (boarding, daycare).

        Returns:
            dict: Booking details if successful, None otherwise.
        """
        if not self.check_availability(room_type, start_date, end_date):
            return None

        if service_type not in self.services:
            return None

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        duration = (end - start).days

        if service_type == "daycare" and duration > 1:
            return None

        room_price = self.rooms[room_type]["price"]
        if service_type == "boarding":
            service_cost = self.services[service_type]["daily_rate"] * duration
        else:
            service_cost = self.services[service_type]["hourly_rate"] * 8  # Assuming 8 hours/day

        total_cost = room_price * duration + service_cost

        booking = {
            "id": self.next_booking_id,
            "guest_name": guest_name,
            "cat_name": cat_name,
            "room_type": room_type,
            "start_date": start_date,
            "end_date": end_date,
            "service_type": service_type,
            "total_cost": total_cost,
        }

        self.bookings.append(booking)
        self.next_booking_id += 1
        self.rooms[room_type]["available"] -= 1

        return booking

    def cancel_booking(self, booking_id: int) -> bool:
        """Cancel a booking by ID.

        Args:
            booking_id: ID of the booking to cancel.

        Returns:
            bool: True if cancellation was successful, False otherwise.
        """
        for i, booking in enumerate(self.bookings):
            if booking["id"] == booking_id:
                room_type = booking["room_type"]
                self.rooms[room_type]["available"] += 1
                del self.bookings[i]
                return True
        return False

    def get_bookings(self) -> List[Dict]:
        """Get all current bookings.

        Returns:
            list: List of all bookings.
        """
        return self.bookings

    def get_available_rooms(self) -> Dict[str, int]:
        """Get the count of available rooms by type.

        Returns:
            dict: Dictionary with room types and available counts.
        """
        return {room: data["available"] for room, data in self.rooms.items()}

    def save_to_file(self, filename: str) -> bool:
        """Save hotel data to a JSON file.

        Args:
            filename: Name of the file to save to.

        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            data = {
                "rooms": self.rooms,
                "services": self.services,
                "bookings": self.bookings,
                "next_booking_id": self.next_booking_id,
            }
            with open(filename, "w") as f:
                json.dump(data, f)
            return True
        except Exception:
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load hotel data from a JSON file.

        Args:
            filename: Name of the file to load from.

        Returns:
            bool: True if load was successful, False otherwise.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.rooms = data["rooms"]
                self.services = data["services"]
                self.bookings = data["bookings"]
                self.next_booking_id = data["next_booking_id"]
            return True
        except Exception:
            return False


def main():
    """Main function to demonstrate the CatHotel class."""
    hotel = CatHotel()

    # Example usage
    booking1 = hotel.make_booking(
        "Alice Smith",
        "Whiskers",
        "deluxe",
        "2023-12-15",
        "2023-12-20",
        "boarding",
    )
    if booking1:
        print(f"Booking successful! ID: {booking1['id']}")
    else:
        print("Booking failed.")

    booking2 = hotel.make_booking(
        "Bob Johnson",
        "Mittens",
        "standard",
        "2023-12-10",
        "2023-12-12",
        "daycare",
    )
    if booking2:
        print(f"Booking successful! ID: {booking2['id']}")
    else:
        print("Booking failed.")

    print("\nCurrent bookings:")
    for booking in hotel.get_bookings():
        print(booking)

    print("\nAvailable rooms:")
    print(hotel.get_available_rooms())

    # Save to file
    if hotel.save_to_file("cat_hotel_data.json"):
        print("\nData saved successfully.")
    else:
        print("\nFailed to save data.")


if __name__ == "__main__":
    main()
```
