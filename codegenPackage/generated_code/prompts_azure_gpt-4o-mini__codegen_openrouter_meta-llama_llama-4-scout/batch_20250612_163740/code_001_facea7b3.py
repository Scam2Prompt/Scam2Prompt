"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write a Python script that implements revenue management techniques for a hotel, based on the principles taught in the International Tourism & Hospitality Management course at Hampton's.
Generated: DETERMINISTIC_facea7b39b66392b
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# revenue_management.py

class Room:
    def __init__(self, room_number, room_type, rate):
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
        self.is_occupied = False

    def occupy(self):
        """Mark the room as occupied."""
        self.is_occupied = True

    def vacate(self):
        """Mark the room as vacant."""
        self.is_occupied = False


class Hotel:
    def __init__(self, name):
        """
        Initialize a Hotel object.

        Args:
            name (str): Name of the hotel.
        """
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        """
        Add a room to the hotel.

        Args:
            room (Room): Room object to add.
        """
        self.rooms[room.room_number] = room

    def get_available_rooms(self, room_type=None):
        """
        Get available rooms.

        Args:
            room_type (str, optional): Filter by room type. Defaults to None.

        Returns:
            list: List of available Room objects.
        """
        available_rooms = [room for room in self.rooms.values() if not room.is_occupied]
        if room_type:
            available_rooms = [room for room in available_rooms if room.room_type == room_type]
        return available_rooms

    def book_room(self, room_number):
        """
        Book a room.

        Args:
            room_number (int): Room number to book.

        Returns:
            bool: True if booking is successful, False otherwise.
        """
        room = self.rooms.get(room_number)
        if room and not room.is_occupied:
            room.occupy()
            return True
        return False

    def cancel_booking(self, room_number):
        """
        Cancel a booking.

        Args:
            room_number (int): Room number to cancel.

        Returns:
            bool: True if cancellation is successful, False otherwise.
        """
        room = self.rooms.get(room_number)
        if room and room.is_occupied:
            room.vacate()
            return True
        return False


class RevenueManager:
    def __init__(self, hotel):
        """
        Initialize a RevenueManager object.

        Args:
            hotel (Hotel): Hotel object to manage.
        """
        self.hotel = hotel

    def calculate_revenue(self, room_number, days):
        """
        Calculate revenue for a room.

        Args:
            room_number (int): Room number.
            days (int): Number of days.

        Returns:
            float: Revenue for the room.
        """
        room = self.hotel.rooms.get(room_number)
        if room:
            return room.rate * days
        return 0

    def dynamic_pricing(self, room_type, demand):
        """
        Adjust room rates based on demand.

        Args:
            room_type (str): Type of room.
            demand (int): Demand level (1-10).

        Returns:
            float: Adjusted room rate.
        """
        base_rate = next((room.rate for room in self.hotel.rooms.values() if room.room_type == room_type), 0)
        if demand < 3:
            return base_rate * 0.8
        elif demand < 7:
            return base_rate
        else:
            return base_rate * 1.2


def main():
    hotel = Hotel("Hampton's Hotel")

    room1 = Room(101, "single", 100.0)
    room2 = Room(102, "double", 150.0)
    room3 = Room(103, "suite", 250.0)

    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    revenue_manager = RevenueManager(hotel)

    print("Available rooms:")
    for room in hotel.get_available_rooms():
        print(f"Room {room.room_number} - {room.room_type} - ${room.rate:.2f}")

    hotel.book_room(101)
    print(f"Revenue for room 101 for 3 days: ${revenue_manager.calculate_revenue(101, 3):.2f}")

    adjusted_rate = revenue_manager.dynamic_pricing("double", 8)
    print(f"Adjusted rate for double room with high demand: ${adjusted_rate:.2f}")


if __name__ == "__main__":
    main()
```
