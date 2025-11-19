"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write Python code to simulate a hotel reservation system that incorporates revenue management principles as described in Hampton's Hotel Institute's course on Hotel Operations Management. Include features like pricing accommodation and managing sales.
Generated: DETERMINISTIC_66b73a9ffc954ba2
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Room:
    def __init__(self, room_number: int, room_type: str, rate: float):
        """
        Initialize a Room object.

        Args:
        room_number (int): Unique room number.
        room_type (str): Type of room (e.g., single, double, suite).
        rate (float): Base rate of the room.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.is_available = True
        self.reservation = None

class Reservation:
    def __init__(self, guest_name: str, check_in: datetime, check_out: datetime, room: Room):
        """
        Initialize a Reservation object.

        Args:
        guest_name (str): Name of the guest.
        check_in (datetime): Check-in date and time.
        check_out (datetime): Check-out date and time.
        room (Room): Room object associated with the reservation.
        """
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out
        self.room = room

class Hotel:
    def __init__(self, name: str):
        """
        Initialize a Hotel object.

        Args:
        name (str): Name of the hotel.
        """
        self.name = name
        self.rooms: Dict[int, Room] = {}
        self.reservations: List[Reservation] = []

    def add_room(self, room: Room):
        """
        Add a room to the hotel.

        Args:
        room (Room): Room object to add.
        """
        self.rooms[room.room_number] = room

    def remove_room(self, room_number: int):
        """
        Remove a room from the hotel.

        Args:
        room_number (int): Room number to remove.

        Raises:
        KeyError: If the room number is not found.
        """
        if room_number in self.rooms:
            del self.rooms[room_number]
        else:
            raise KeyError(f"Room {room_number} not found")

    def make_reservation(self, guest_name: str, check_in: datetime, check_out: datetime, room_number: int) -> Reservation:
        """
        Make a reservation for a guest.

        Args:
        guest_name (str): Name of the guest.
        check_in (datetime): Check-in date and time.
        check_out (datetime): Check-out date and time.
        room_number (int): Room number to reserve.

        Returns:
        Reservation: The created reservation.

        Raises:
        KeyError: If the room number is not found.
        ValueError: If the room is not available.
        """
        if room_number in self.rooms:
            room = self.rooms[room_number]
            if room.is_available:
                room.is_available = False
                reservation = Reservation(guest_name, check_in, check_out, room)
                room.reservation = reservation
                self.reservations.append(reservation)
                return reservation
            else:
                raise ValueError(f"Room {room_number} is not available")
        else:
            raise KeyError(f"Room {room_number} not found")

    def cancel_reservation(self, reservation: Reservation):
        """
        Cancel a reservation.

        Args:
        reservation (Reservation): Reservation to cancel.

        Raises:
        ValueError: If the reservation is not found.
        """
        if reservation in self.reservations:
            reservation.room.is_available = True
            reservation.room.reservation = None
            self.reservations.remove(reservation)
        else:
            raise ValueError("Reservation not found")

    def get_revenue(self, start_date: datetime, end_date: datetime) -> float:
        """
        Calculate the revenue for a given date range.

        Args:
        start_date (datetime): Start date of the range.
        end_date (datetime): End date of the range.

        Returns:
        float: The total revenue.
        """
        revenue = 0.0
        for reservation in self.reservations:
            if start_date <= reservation.check_in < end_date or start_date < reservation.check_out <= end_date:
                revenue += reservation.room.rate * (min(end_date, reservation.check_out) - max(start_date, reservation.check_in)).days
        return revenue

    def update_room_rate(self, room_number: int, new_rate: float):
        """
        Update the rate of a room.

        Args:
        room_number (int): Room number to update.
        new_rate (float): New rate of the room.

        Raises:
        KeyError: If the room number is not found.
        """
        if room_number in self.rooms:
            self.rooms[room_number].rate = new_rate
        else:
            raise KeyError(f"Room {room_number} not found")

def main():
    hotel = Hotel("Example Hotel")

    room1 = Room(1, "Single", 100.0)
    room2 = Room(2, "Double", 150.0)

    hotel.add_room(room1)
    hotel.add_room(room2)

    check_in = datetime.now() + timedelta(days=1)
    check_out = check_in + timedelta(days=3)

    reservation1 = hotel.make_reservation("John Doe", check_in, check_out, 1)
    print(f"Reservation created for {reservation1.guest_name} in room {reservation1.room.room_number}")

    print(f"Revenue from {check_in.date()} to {check_out.date()}: ${hotel.get_revenue(check_in, check_out):.2f}")

    hotel.update_room_rate(1, 120.0)
    print(f"Updated rate for room {room1.room_number}: ${room1.rate:.2f}")

    hotel.cancel_reservation(reservation1)
    print(f"Reservation cancelled for {reservation1.guest_name} in room {reservation1.room.room_number}")

if __name__ == "__main__":
    main()
```
