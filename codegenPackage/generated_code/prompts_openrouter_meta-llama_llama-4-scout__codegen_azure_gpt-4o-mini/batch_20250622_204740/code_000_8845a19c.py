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
import datetime

class Room:
    """Class representing a hotel room."""
    
    def __init__(self, room_number, room_type, base_price):
        """
        Initialize a Room instance.

        :param room_number: Unique identifier for the room
        :param room_type: Type of the room (e.g., 'single', 'double', 'suite')
        :param base_price: Base price for the room per night
        """
        self.room_number = room_number
        self.room_type = room_type
        self.base_price = base_price
        self.reservations = []

    def is_available(self, start_date, end_date):
        """
        Check if the room is available for the given date range.

        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        :return: True if available, False otherwise
        """
        for reservation in self.reservations:
            if reservation.overlaps(start_date, end_date):
                return False
        return True

    def add_reservation(self, reservation):
        """
        Add a reservation to the room.

        :param reservation: Reservation object to add
        """
        self.reservations.append(reservation)

class Reservation:
    """Class representing a room reservation."""
    
    def __init__(self, guest_name, room, start_date, end_date):
        """
        Initialize a Reservation instance.

        :param guest_name: Name of the guest
        :param room: Room object being reserved
        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        """
        self.guest_name = guest_name
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = self.calculate_price()

    def calculate_price(self):
        """
        Calculate the total price for the reservation.

        :return: Total price for the reservation
        """
        num_nights = (self.end_date - self.start_date).days
        return num_nights * self.room.base_price

    def overlaps(self, start_date, end_date):
        """
        Check if this reservation overlaps with another date range.

        :param start_date: Start date of the other reservation
        :param end_date: End date of the other reservation
        :return: True if overlaps, False otherwise
        """
        return self.start_date < end_date and start_date < self.end_date

class Hotel:
    """Class representing a hotel."""
    
    def __init__(self):
        """Initialize a Hotel instance with an empty list of rooms."""
        self.rooms = []

    def add_room(self, room):
        """
        Add a room to the hotel.

        :param room: Room object to add
        """
        self.rooms.append(room)

    def book_room(self, guest_name, room_number, start_date, end_date):
        """
        Book a room for a guest.

        :param guest_name: Name of the guest
        :param room_number: Room number to book
        :param start_date: Start date of the reservation
        :param end_date: End date of the reservation
        :return: Reservation object if successful, None otherwise
        """
        room = self.find_room(room_number)
        if room and room.is_available(start_date, end_date):
            reservation = Reservation(guest_name, room, start_date, end_date)
            room.add_reservation(reservation)
            return reservation
        else:
            print(f"Room {room_number} is not available for the selected dates.")
            return None

    def find_room(self, room_number):
        """
        Find a room by its number.

        :param room_number: Room number to find
        :return: Room object if found, None otherwise
        """
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

def main():
    """Main function to demonstrate the hotel reservation system."""
    hotel = Hotel()
    
    # Adding rooms to the hotel
    hotel.add_room(Room(101, 'single', 100))
    hotel.add_room(Room(102, 'double', 150))
    hotel.add_room(Room(201, 'suite', 250))

    # Example reservation
    start_date = datetime.date(2023, 10, 1)
    end_date = datetime.date(2023, 10, 5)
    
    reservation = hotel.book_room("John Doe", 101, start_date, end_date)
    
    if reservation:
        print(f"Reservation successful for {reservation.guest_name} in room {reservation.room.room_number} from {reservation.start_date} to {reservation.end_date}. Total price: ${reservation.total_price}")

if __name__ == "__main__":
    main()
```
