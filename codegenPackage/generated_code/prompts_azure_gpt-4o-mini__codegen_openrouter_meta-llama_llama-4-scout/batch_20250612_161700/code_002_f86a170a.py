"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: Create a Python script that automates the workflow for a hospitality management system, inspired by the services offered by Sama Al-Naser Group.
Generated: DETERMINISTIC_f86a170a75de9090
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hospitality_management_system.py

"""
Hospitality Management System Script
------------------------------------

Inspired by the services offered by Sama Al-Naser Group.

This script automates the workflow for managing hotels, 
including room reservations, guest check-in/check-out, 
and billing.
"""

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Guest:
    """Represents a hotel guest."""

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

class Room:
    """Represents a hotel room."""

    def __init__(self, room_number, room_type, rate):
        """
        Initializes a Room object.

        Args:
            room_number (int): Room number.
            room_type (str): Room type (e.g., single, double, suite).
            rate (float): Room rate per night.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.is_occupied = False
        self.guest = None
        self.check_in_date = None
        self.check_out_date = None

class Hotel:
    """Represents a hotel."""

    def __init__(self, name):
        """
        Initializes a Hotel object.

        Args:
            name (str): Hotel name.
        """
        self.name = name
        self.rooms = []

    def add_room(self, room):
        """Adds a room to the hotel."""
        self.rooms.append(room)

    def reserve_room(self, room_number, guest):
        """
        Reserves a room for a guest.

        Args:
            room_number (int): Room number to reserve.
            guest (Guest): Guest reserving the room.

        Returns:
            bool: True if reservation is successful, False otherwise.
        """
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room and not room.is_occupied:
            room.is_occupied = True
            room.guest = guest
            logging.info(f"Room {room_number} reserved for {guest.name}")
            return True
        logging.error(f"Room {room_number} is not available or does not exist")
        return False

    def check_in(self, room_number, check_in_date):
        """
        Checks in a guest.

        Args:
            room_number (int): Room number to check in.
            check_in_date (datetime.date): Check-in date.

        Returns:
            bool: True if check-in is successful, False otherwise.
        """
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room and room.is_occupied:
            room.check_in_date = check_in_date
            logging.info(f"Guest {room.guest.name} checked in to room {room_number}")
            return True
        logging.error(f"Room {room_number} is not occupied or does not exist")
        return False

    def check_out(self, room_number, check_out_date):
        """
        Checks out a guest.

        Args:
            room_number (int): Room number to check out.
            check_out_date (datetime.date): Check-out date.

        Returns:
            bool: True if check-out is successful, False otherwise.
        """
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room and room.is_occupied:
            room.check_out_date = check_out_date
            room.is_occupied = False
            logging.info(f"Guest {room.guest.name} checked out of room {room_number}")
            return True
        logging.error(f"Room {room_number} is not occupied or does not exist")
        return False

    def generate_bill(self, room_number):
        """
        Generates a bill for a guest.

        Args:
            room_number (int): Room number to generate bill for.

        Returns:
            float: Total bill amount.
        """
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room and room.is_occupied:
            check_in_date = room.check_in_date
            check_out_date = room.check_out_date or datetime.date.today()
            stay_duration = (check_out_date - check_in_date).days
            bill_amount = room.rate * stay_duration
            logging.info(f"Bill generated for guest {room.guest.name}: ${bill_amount:.2f}")
            return bill_amount
        logging.error(f"Room {room_number} is not occupied or does not exist")
        return 0.0

def main():
    # Create a hotel
    hotel = Hotel("Sama Al-Naser Hotel")

    # Add rooms
    hotel.add_room(Room(101, "Single", 100.0))
    hotel.add_room(Room(102, "Double", 150.0))
    hotel.add_room(Room(103, "Suite", 250.0))

    # Create a guest
    guest = Guest("John Doe", "john.doe@example.com", "1234567890")

    # Reserve a room
    hotel.reserve_room(101, guest)

    # Check in
    hotel.check_in(101, datetime.date.today())

    # Check out
    hotel.check_out(101, datetime.date.today())

    # Generate bill
    bill_amount = hotel.generate_bill(101)
    print(f"Total bill amount: ${bill_amount:.2f}")

if __name__ == "__main__":
    main()
```
