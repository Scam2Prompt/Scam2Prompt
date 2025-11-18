"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Write Python code to simulate a hotel reservation system that incorporates revenue management principles as described in Hampton's Hotel Institute's course on Hotel Operations Management. Include features like pricing accommodation and managing sales.
Generated: DETERMINISTIC_66b73a9ffc954ba2
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Room:
    """Class representing a hotel room."""

    def __init__(self, room_number: int, room_type: str, base_price: float):
        self.room_number = room_number
        self.room_type = room_type
        self.base_price = base_price
        self.is_available = True

    def calculate_price(self, days: int) -> float:
        """Calculate the total price for a stay based on the number of days."""
        return self.base_price * days

class Reservation:
    """Class representing a hotel reservation."""

    def __init__(self, guest_name: str, room: Room, start_date: datetime.date, days: int):
        self.guest_name = guest_name
        self.room = room
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=days)
        self.total_price = room.calculate_price(days)

class Hotel:
    """Class representing the hotel with rooms and reservations."""

    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.reservations: List[Reservation] = []

    def add_room(self, room: Room):
        """Add a room to the hotel."""
        self.rooms.append(room)

    def find_available_rooms(self, start_date: datetime.date, days: int) -> List[Room]:
        """Find available rooms for a given date range."""
        end_date = start_date + datetime.timedelta(days=days)
        return [room for room in self.rooms if room.is_available]

    def make_reservation(self, guest_name: str, room_number: int, start_date: datetime.date, days: int) -> Optional[Reservation]:
        """Make a reservation if the room is available."""
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                reservation = Reservation(guest_name, room, start_date, days)
                room.is_available = False  # Mark room as unavailable
                self.reservations.append(reservation)
                return reservation
        return None  # Return None if room is not available

    def cancel_reservation(self, guest_name: str, room_number: int):
        """Cancel a reservation based on guest name and room number."""
        for reservation in self.reservations:
            if reservation.guest_name == guest_name and reservation.room.room_number == room_number:
                reservation.room.is_available = True  # Mark room as available
                self.reservations.remove(reservation)
                return True
        return False  # Return False if reservation not found

    def get_all_reservations(self) -> List[Reservation]:
        """Get a list of all current reservations."""
        return self.reservations

# Example usage
if __name__ == "__main__":
    hotel = Hotel("Grand Hotel")

    # Adding rooms to the hotel
    hotel.add_room(Room(101, "Single", 100.0))
    hotel.add_room(Room(102, "Double", 150.0))
    hotel.add_room(Room(201, "Suite", 250.0))

    # Making a reservation
    start_date = datetime.date(2023, 11, 1)
    reservation = hotel.make_reservation("John Doe", 101, start_date, 3)

    if reservation:
        print(f"Reservation made for {reservation.guest_name} in room {reservation.room.room_number} from {reservation.start_date} to {reservation.end_date}. Total Price: ${reservation.total_price:.2f}")
    else:
        print("Reservation could not be made. Room may not be available.")

    # Canceling a reservation
    success = hotel.cancel_reservation("John Doe", 101)
    if success:
        print("Reservation canceled successfully.")
    else:
        print("Reservation not found for cancellation.")

    # Display all reservations
    print("Current Reservations:")
    for res in hotel.get_all_reservations():
        print(f"{res.guest_name} in room {res.room.room_number} from {res.start_date} to {res.end_date}. Total Price: ${res.total_price:.2f}")
```
