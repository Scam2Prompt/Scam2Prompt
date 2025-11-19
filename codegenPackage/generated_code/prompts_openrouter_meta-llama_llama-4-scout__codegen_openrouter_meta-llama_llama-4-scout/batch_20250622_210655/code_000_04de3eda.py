"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Write a Python code snippet to create a simple hotel management system for a villa like Vila Vračar in Vrnjačka Banja, including features for room booking and reservation management.
Generated: DETERMINISTIC_04de3eda3b82dcbb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_management_system.py

class Room:
    """Represents a hotel room."""

    def __init__(self, room_number, room_type, capacity, price):
        """
        Initializes a Room object.

        Args:
            room_number (int): Unique room number.
            room_type (str): Type of room (e.g., single, double, suite).
            capacity (int): Maximum number of guests.
            price (float): Room price per night.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.capacity = capacity
        self.price = price
        self.is_booked = False
        self.guest_name = None
        self.check_in_date = None
        self.check_out_date = None

    def book_room(self, guest_name, check_in_date, check_out_date):
        """
        Books the room for a guest.

        Args:
            guest_name (str): Name of the guest.
            check_in_date (str): Check-in date (YYYY-MM-DD).
            check_out_date (str): Check-out date (YYYY-MM-DD).

        Raises:
            Exception: If the room is already booked.
        """
        if self.is_booked:
            raise Exception(f"Room {self.room_number} is already booked.")
        self.is_booked = True
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def cancel_booking(self):
        """Cancels the room booking."""
        self.is_booked = False
        self.guest_name = None
        self.check_in_date = None
        self.check_out_date = None

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}): {self.price} EUR/night"


class Hotel:
    """Represents a hotel."""

    def __init__(self, name):
        """
        Initializes a Hotel object.

        Args:
            name (str): Hotel name.
        """
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        """
        Adds a room to the hotel.

        Args:
            room (Room): Room object to add.
        """
        self.rooms[room.room_number] = room

    def get_room(self, room_number):
        """
        Retrieves a room by its number.

        Args:
            room_number (int): Room number.

        Returns:
            Room: Room object or None if not found.
        """
        return self.rooms.get(room_number)

    def display_rooms(self):
        """Displays all rooms in the hotel."""
        for room in self.rooms.values():
            print(room)


class HotelManagementSystem:
    """Manages hotel room bookings and reservations."""

    def __init__(self, hotel):
        """
        Initializes a HotelManagementSystem object.

        Args:
            hotel (Hotel): Hotel object.
        """
        self.hotel = hotel

    def book_room(self, room_number, guest_name, check_in_date, check_out_date):
        """
        Books a room for a guest.

        Args:
            room_number (int): Room number.
            guest_name (str): Guest name.
            check_in_date (str): Check-in date (YYYY-MM-DD).
            check_out_date (str): Check-out date (YYYY-MM-DD).

        Raises:
            Exception: If the room is not found or already booked.
        """
        room = self.hotel.get_room(room_number)
        if room is None:
            raise Exception(f"Room {room_number} not found.")
        room.book_room(guest_name, check_in_date, check_out_date)
        print(f"Room {room_number} booked for {guest_name}.")

    def cancel_booking(self, room_number):
        """
        Cancels a room booking.

        Args:
            room_number (int): Room number.

        Raises:
            Exception: If the room is not found.
        """
        room = self.hotel.get_room(room_number)
        if room is None:
            raise Exception(f"Room {room_number} not found.")
        room.cancel_booking()
        print(f"Booking for room {room_number} cancelled.")

    def display_bookings(self):
        """Displays all room bookings."""
        for room in self.hotel.rooms.values():
            if room.is_booked:
                print(f"Room {room.room_number}: {room.guest_name} ({room.check_in_date} - {room.check_out_date})")


def main():
    hotel = Hotel("Vila Vračar")
    hms = HotelManagementSystem(hotel)

    # Add rooms
    hotel.add_room(Room(1, "Single", 1, 80))
    hotel.add_room(Room(2, "Double", 2, 120))
    hotel.add_room(Room(3, "Suite", 4, 250))

    while True:
        print("\nHotel Management System")
        print("1. Display rooms")
        print("2. Book room")
        print("3. Cancel booking")
        print("4. Display bookings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            hotel.display_rooms()
        elif choice == "2":
            room_number = int(input("Enter room number: "))
            guest_name = input("Enter guest name: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            try:
                hms.book_room(room_number, guest_name, check_in_date, check_out_date)
            except Exception as e:
                print(str(e))
        elif choice == "3":
            room_number = int(input("Enter room number: "))
            try:
                hms.cancel_booking(room_number)
            except Exception as e:
                print(str(e))
        elif choice == "4":
            hms.display_bookings()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
