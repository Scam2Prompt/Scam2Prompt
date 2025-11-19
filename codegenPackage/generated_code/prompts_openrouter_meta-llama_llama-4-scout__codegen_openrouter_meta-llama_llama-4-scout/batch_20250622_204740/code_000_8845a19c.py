"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write a Python script to manage hotel room reservations and pricing using a simple PMS system, considering revenue management techniques.
Generated: DETERMINISTIC_8845a19c9eaf409b
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_pms.py

from datetime import datetime, timedelta
from typing import Dict, List

class Room:
    """Represents a hotel room with its type, rate, and availability."""

    def __init__(self, room_number: int, room_type: str, rate: float):
        """
        Initializes a Room object.

        Args:
        - room_number (int): Unique room number.
        - room_type (str): Type of room (e.g., single, double, suite).
        - rate (float): Base rate of the room.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.is_available = True
        self.reservation = None

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}): ${self.rate:.2f}/night"


class Reservation:
    """Represents a hotel room reservation."""

    def __init__(self, guest_name: str, check_in: datetime, check_out: datetime):
        """
        Initializes a Reservation object.

        Args:
        - guest_name (str): Name of the guest.
        - check_in (datetime): Check-in date and time.
        - check_out (datetime): Check-out date and time.
        """
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out

    def __str__(self):
        return f"Reservation for {self.guest_name} from {self.check_in} to {self.check_out}"


class HotelPMS:
    """Simple Property Management System (PMS) for hotel room reservations and pricing."""

    def __init__(self):
        self.rooms: Dict[int, Room] = {}
        self.reservations: Dict[int, Reservation] = {}

    def add_room(self, room: Room):
        """Adds a room to the hotel."""
        self.rooms[room.room_number] = room

    def remove_room(self, room_number: int):
        """Removes a room from the hotel."""
        if room_number in self.rooms:
            del self.rooms[room_number]
        else:
            print(f"Room {room_number} not found.")

    def make_reservation(self, room_number: int, guest_name: str, check_in: datetime, check_out: datetime):
        """Makes a reservation for a room."""
        if room_number in self.rooms and self.rooms[room_number].is_available:
            room = self.rooms[room_number]
            room.is_available = False
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(guest_name, check_in, check_out)
            self.reservations[reservation_id] = reservation
            room.reservation = reservation
            print(f"Reservation {reservation_id} made for room {room_number}.")
        else:
            print(f"Room {room_number} is not available or does not exist.")

    def cancel_reservation(self, room_number: int):
        """Cancels a reservation and makes the room available."""
        if room_number in self.rooms and not self.rooms[room_number].is_available:
            room = self.rooms[room_number]
            room.is_available = True
            for reservation_id, reservation in self.reservations.items():
                if room.reservation == reservation:
                    del self.reservations[reservation_id]
                    room.reservation = None
                    print(f"Reservation for room {room_number} cancelled.")
                    return
        else:
            print(f"Room {room_number} is already available or does not exist.")

    def update_rate(self, room_number: int, new_rate: float):
        """Updates the rate of a room."""
        if room_number in self.rooms:
            self.rooms[room_number].rate = new_rate
            print(f"Rate for room {room_number} updated to ${new_rate:.2f}/night.")
        else:
            print(f"Room {room_number} not found.")

    def apply_revenue_management(self, room_number: int, demand_multiplier: float):
        """Applies revenue management techniques by adjusting the room rate based on demand."""
        if room_number in self.rooms:
            room = self.rooms[room_number]
            adjusted_rate = room.rate * demand_multiplier
            room.rate = adjusted_rate
            print(f"Rate for room {room_number} adjusted to ${adjusted_rate:.2f}/night based on demand.")
        else:
            print(f"Room {room_number} not found.")

    def print_room_availability(self):
        """Prints the availability of all rooms."""
        for room in self.rooms.values():
            status = "Available" if room.is_available else "Occupied"
            print(f"{room} - {status}")

    def print_reservations(self):
        """Prints all reservations."""
        for reservation_id, reservation in self.reservations.items():
            print(f"{reservation_id}: {reservation}")


def main():
    pms = HotelPMS()

    # Add rooms
    pms.add_room(Room(101, "Single", 100.0))
    pms.add_room(Room(102, "Double", 150.0))
    pms.add_room(Room(103, "Suite", 250.0))

    # Print room availability
    print("Room Availability:")
    pms.print_room_availability()

    # Make reservations
    check_in = datetime.now() + timedelta(days=1)
    check_out = check_in + timedelta(days=2)
    pms.make_reservation(101, "John Doe", check_in, check_out)
    pms.make_reservation(102, "Jane Smith", check_in, check_out)

    # Print room availability
    print("\nRoom Availability after reservations:")
    pms.print_room_availability()

    # Print reservations
    print("\nReservations:")
    pms.print_reservations()

    # Apply revenue management
    pms.apply_revenue_management(101, 1.2)

    # Update rate
    pms.update_rate(102, 180.0)

    # Cancel reservation
    pms.cancel_reservation(101)

    # Print room availability
    print("\nRoom Availability after cancellation:")
    pms.print_room_availability()


if __name__ == "__main__":
    main()
```
