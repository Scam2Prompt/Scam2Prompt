"""
Generated Code Metadata:
========================
Original URL: https://inkawasiollague.cl
Prompt: Generate a code snippet for a booking system that allows users to reserve rooms at a hostel, incorporating hygiene measures for COVID-19.
Generated: DETERMINISTIC_965b08e50087c97c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity):
        """
        Initialize a Room object.

        Args:
            room_number (int): The room number.
            capacity (int): The maximum capacity of the room.
        """
        self.room_number = room_number
        self.capacity = capacity
        self.is_reserved = False
        self.reservation_start = None
        self.reservation_end = None

    def reserve(self, start_date, end_date):
        """
        Reserve the room for a given period.

        Args:
            start_date (datetime): The start date of the reservation.
            end_date (datetime): The end date of the reservation.

        Returns:
            bool: True if the reservation was successful, False otherwise.
        """
        if self.is_reserved:
            return False

        self.is_reserved = True
        self.reservation_start = start_date
        self.reservation_end = end_date
        return True

    def cancel_reservation(self):
        """
        Cancel the current reservation.

        Returns:
            bool: True if the cancellation was successful, False otherwise.
        """
        if not self.is_reserved:
            return False

        self.is_reserved = False
        self.reservation_start = None
        self.reservation_end = None
        return True


class Hostel:
    def __init__(self, name):
        """
        Initialize a Hostel object.

        Args:
            name (str): The name of the hostel.
        """
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        """
        Add a room to the hostel.

        Args:
            room (Room): The room to add.
        """
        self.rooms[room.room_number] = room

    def get_available_rooms(self, date):
        """
        Get a list of available rooms for a given date.

        Args:
            date (datetime): The date to check.

        Returns:
            list: A list of available rooms.
        """
        available_rooms = []
        for room in self.rooms.values():
            if not room.is_reserved or (room.reservation_start <= date and room.reservation_end > date):
                available_rooms.append(room)
        return available_rooms


class BookingSystem:
    def __init__(self, hostel):
        """
        Initialize a BookingSystem object.

        Args:
            hostel (Hostel): The hostel to manage.
        """
        self.hostel = hostel
        self.hygiene_measures = {
            "mask_required": True,
            "sanitize_rooms": True,
            "temperature_check": True
        }

    def display_hygiene_measures(self):
        """
        Display the current hygiene measures.
        """
        print("Current Hygiene Measures:")
        for measure, value in self.hygiene_measures.items():
            print(f"{measure.replace('_', ' ').title()}: {value}")

    def book_room(self, room_number, start_date, end_date):
        """
        Book a room for a given period.

        Args:
            room_number (int): The room number to book.
            start_date (datetime): The start date of the booking.
            end_date (datetime): The end date of the booking.

        Returns:
            bool: True if the booking was successful, False otherwise.
        """
        room = self.hostel.rooms.get(room_number)
        if not room:
            print("Room not found.")
            return False

        if room.reserve(start_date, end_date):
            print(f"Room {room_number} booked successfully from {start_date} to {end_date}.")
            return True
        else:
            print(f"Room {room_number} is not available from {start_date} to {end_date}.")
            return False

    def cancel_booking(self, room_number):
        """
        Cancel a booking.

        Args:
            room_number (int): The room number to cancel.

        Returns:
            bool: True if the cancellation was successful, False otherwise.
        """
        room = self.hostel.rooms.get(room_number)
        if not room:
            print("Room not found.")
            return False

        if room.cancel_reservation():
            print(f"Booking for room {room_number} cancelled successfully.")
            return True
        else:
            print(f"Room {room_number} has no active booking.")
            return False


def main():
    hostel = Hostel("COVID-19 Hostel")
    booking_system = BookingSystem(hostel)

    room1 = Room(1, 2)
    room2 = Room(2, 4)

    hostel.add_room(room1)
    hostel.add_room(room2)

    while True:
        print("\n1. Display Hygiene Measures")
        print("2. Book Room")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            booking_system.display_hygiene_measures()
        elif choice == "2":
            room_number = int(input("Enter room number: "))
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            end_date_str = input("Enter end date (YYYY-MM-DD): ")

            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() + timedelta(days=1)

            booking_system.book_room(room_number, start_date, end_date)
        elif choice == "3":
            room_number = int(input("Enter room number: "))
            booking_system.cancel_booking(room_number)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
