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
from enum import Enum
from typing import Dict, List

class RoomType(Enum):
    """Enum for room types."""
    CASAL_COM_HIDROMASSAGEM = 1
    CASAL = 2
    SOLTEIRO = 3

class AddOn(Enum):
    """Enum for add-ons."""
    BREAKFAST = 1

class RoomBooking:
    """Class to manage room bookings."""

    def __init__(self, room_type: RoomType, add_ons: List[AddOn] = None):
        """
        Initialize a room booking.

        Args:
        room_type (RoomType): The type of room.
        add_ons (List[AddOn], optional): List of add-ons. Defaults to None.
        """
        self.room_type = room_type
        self.add_ons = add_ons if add_ons else []

    def __str__(self):
        return f"Room Type: {self.room_type.name}, Add-ons: {[add_on.name for add_on in self.add_ons]}"

class HotelBookingSystem:
    """Class to manage hotel room bookings."""

    def __init__(self):
        self.bookings: Dict[int, RoomBooking] = {}
        self.room_types: Dict[RoomType, float] = {
            RoomType.CASAL_COM_HIDROMASSAGEM: 200.0,
            RoomType.CASAL: 150.0,
            RoomType.SOLTEIRO: 100.0
        }
        self.add_on_prices: Dict[AddOn, float] = {
            AddOn.BREAKFAST: 20.0
        }

    def add_booking(self, booking_id: int, room_type: RoomType, add_ons: List[AddOn] = None):
        """
        Add a room booking.

        Args:
        booking_id (int): Unique booking ID.
        room_type (RoomType): The type of room.
        add_ons (List[AddOn], optional): List of add-ons. Defaults to None.

        Raises:
        ValueError: If booking ID already exists.
        """
        if booking_id in self.bookings:
            raise ValueError("Booking ID already exists.")
        self.bookings[booking_id] = RoomBooking(room_type, add_ons)

    def remove_booking(self, booking_id: int):
        """
        Remove a room booking.

        Args:
        booking_id (int): Unique booking ID.

        Raises:
        KeyError: If booking ID does not exist.
        """
        if booking_id not in self.bookings:
            raise KeyError("Booking ID does not exist.")
        del self.bookings[booking_id]

    def calculate_price(self, booking_id: int) -> float:
        """
        Calculate the price of a room booking.

        Args:
        booking_id (int): Unique booking ID.

        Returns:
        float: The price of the room booking.

        Raises:
        KeyError: If booking ID does not exist.
        """
        if booking_id not in self.bookings:
            raise KeyError("Booking ID does not exist.")
        booking = self.bookings[booking_id]
        price = self.room_types[booking.room_type]
        for add_on in booking.add_ons:
            price += self.add_on_prices[add_on]
        return price

    def print_bookings(self):
        """Print all room bookings."""
        for booking_id, booking in self.bookings.items():
            print(f"Booking ID: {booking_id}, {booking}, Price: {self.calculate_price(booking_id)}")

def main():
    hotel = HotelBookingSystem()

    while True:
        print("\nHotel Booking System")
        print("1. Add Booking")
        print("2. Remove Booking")
        print("3. Print Bookings")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            booking_id = int(input("Enter booking ID: "))
            print("\nRoom Types:")
            for i, room_type in enumerate(RoomType):
                print(f"{i+1}. {room_type.name}")
            room_type_choice = int(input("Choose a room type: "))
            room_type = list(RoomType)[room_type_choice - 1]
            add_ons = []
            add_on_choice = input("Add add-ons? (yes/no): ")
            if add_on_choice.lower() == "yes":
                print("\nAdd-ons:")
                for i, add_on in enumerate(AddOn):
                    print(f"{i+1}. {add_on.name}")
                add_on_choice = int(input("Choose an add-on: "))
                add_ons.append(list(AddOn)[add_on_choice - 1])
            hotel.add_booking(booking_id, room_type, add_ons)
        elif choice == "2":
            booking_id = int(input("Enter booking ID: "))
            try:
                hotel.remove_booking(booking_id)
            except KeyError as e:
                print(str(e))
        elif choice == "3":
            hotel.print_bookings()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
