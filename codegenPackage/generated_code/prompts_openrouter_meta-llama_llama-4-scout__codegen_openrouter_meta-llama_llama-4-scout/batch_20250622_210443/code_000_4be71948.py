"""
Generated Code Metadata:
========================
Original URL: https://villapanorea.com
Prompt: Write a Python script to manage room bookings for a vacation rental property like Villa Panorea, including handling check-in/check-out dates and guest information.
Generated: DETERMINISTIC_4be71948597e14e5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Guest:
    """Represents a guest staying at the vacation rental property."""

    def __init__(self, name, email, phone_number):
        """
        Initializes a Guest object.

        Args:
            name (str): Guest's name.
            email (str): Guest's email address.
            phone_number (str): Guest's phone number.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number

class RoomBooking:
    """Represents a room booking for the vacation rental property."""

    def __init__(self, room_number, guest, check_in_date, check_out_date):
        """
        Initializes a RoomBooking object.

        Args:
            room_number (int): Room number being booked.
            guest (Guest): Guest staying in the room.
            check_in_date (datetime): Check-in date.
            check_out_date (datetime): Check-out date.

        Raises:
            ValueError: If check-in date is after check-out date.
        """
        if check_in_date > check_out_date:
            raise ValueError("Check-in date cannot be after check-out date")

        self.room_number = room_number
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

class VillaBookingSystem:
    """Manages room bookings for the vacation rental property."""

    def __init__(self):
        """Initializes the booking system with an empty list of bookings."""
        self.bookings = []

    def add_booking(self, room_number, guest, check_in_date, check_out_date):
        """
        Adds a new room booking.

        Args:
            room_number (int): Room number being booked.
            guest (Guest): Guest staying in the room.
            check_in_date (datetime): Check-in date.
            check_out_date (datetime): Check-out date.

        Raises:
            ValueError: If a booking already exists for the room during the specified dates.
        """
        for booking in self.bookings:
            if room_number == booking.room_number and not (check_out_date <= booking.check_in_date or check_in_date >= booking.check_out_date):
                raise ValueError("Room is already booked during the specified dates")

        new_booking = RoomBooking(room_number, guest, check_in_date, check_out_date)
        self.bookings.append(new_booking)

    def cancel_booking(self, room_number, check_in_date, check_out_date):
        """
        Cancels a room booking.

        Args:
            room_number (int): Room number of the booking to cancel.
            check_in_date (datetime): Check-in date of the booking to cancel.
            check_out_date (datetime): Check-out date of the booking to cancel.

        Raises:
            ValueError: If no booking exists for the room during the specified dates.
        """
        for booking in self.bookings:
            if room_number == booking.room_number and check_in_date == booking.check_in_date and check_out_date == booking.check_out_date:
                self.bookings.remove(booking)
                return

        raise ValueError("No booking found for the room during the specified dates")

    def print_bookings(self):
        """Prints all room bookings."""
        for booking in self.bookings:
            print(f"Room {booking.room_number}:")
            print(f"  Guest: {booking.guest.name} ({booking.guest.email}, {booking.guest.phone_number})")
            print(f"  Check-in: {booking.check_in_date.strftime('%Y-%m-%d')}")
            print(f"  Check-out: {booking.check_out_date.strftime('%Y-%m-%d')}")
            print()

def main():
    booking_system = VillaBookingSystem()

    while True:
        print("1. Add booking")
        print("2. Cancel booking")
        print("3. Print bookings")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            room_number = int(input("Enter room number: "))
            name = input("Enter guest name: ")
            email = input("Enter guest email: ")
            phone_number = input("Enter guest phone number: ")
            check_in_date_str = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date_str = input("Enter check-out date (YYYY-MM-DD): ")

            try:
                guest = Guest(name, email, phone_number)
                check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
                check_out_date = datetime.strptime(check_out_date_str, '%Y-%m-%d').date()
                booking_system.add_booking(room_number, guest, check_in_date, check_out_date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            room_number = int(input("Enter room number: "))
            check_in_date_str = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date_str = input("Enter check-out date (YYYY-MM-DD): ")

            try:
                check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
                check_out_date = datetime.strptime(check_out_date_str, '%Y-%m-%d').date()
                booking_system.cancel_booking(room_number, check_in_date, check_out_date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            booking_system.print_bookings()

        elif choice == "4":
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
