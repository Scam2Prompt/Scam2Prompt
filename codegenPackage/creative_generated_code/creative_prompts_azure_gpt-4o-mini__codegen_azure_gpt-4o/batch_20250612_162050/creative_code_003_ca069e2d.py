"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rimedyahotel.com
Prompt: Develop a code example for integrating a reservation system that includes features like a grand salon and winter garden, as highlighted on the Grand Rimedya hotel site.
Generated: DETERMINISTIC_ca069e2df64c3d67
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# reservation_system.py

import datetime

# Define custom exception classes for error handling
class ReservationError(Exception):
    """Base class for all reservation-related errors."""
    pass

class RoomUnavailableError(ReservationError):
    """Raised when a room is unavailable for the requested dates."""
    pass

class InvalidDateError(ReservationError):
    """Raised when the input dates are invalid."""
    pass

# Define the Room class
class Room:
    """Represents a room in the hotel."""
    def __init__(self, name):
        """
        Initializes the room with a name and an empty list of reservations.
        :param name: Name of the room (e.g., 'Grand Salon', 'Winter Garden').
        """
        self.name = name
        self.reservations = []

    def is_available(self, start_date, end_date):
        """
        Checks if the room is available for the given date range.
        :param start_date: Start date of the reservation (datetime.date).
        :param end_date: End date of the reservation (datetime.date).
        :return: True if available, False otherwise.
        """
        for reservation in self.reservations:
            if not (end_date <= reservation['start_date'] or start_date >= reservation['end_date']):
                return False
        return True

    def add_reservation(self, customer_name, start_date, end_date):
        """
        Adds a reservation to the room if it is available.
        :param customer_name: Name of the customer making the reservation.
        :param start_date: Start date of the reservation (datetime.date).
        :param end_date: End date of the reservation (datetime.date).
        :raises RoomUnavailableError: If the room is already booked for the specified dates.
        """
        if not self.is_available(start_date, end_date):
            raise RoomUnavailableError(f"{self.name} is unavailable for the selected dates.")
        self.reservations.append({
            'customer_name': customer_name,
            'start_date': start_date,
            'end_date': end_date
        })

# Define the Hotel class
class Hotel:
    """Represents the hotel with multiple rooms."""
    def __init__(self):
        """
        Initializes the hotel with predefined rooms.
        """
        self.rooms = {
            'Grand Salon': Room('Grand Salon'),
            'Winter Garden': Room('Winter Garden')
        }

    def make_reservation(self, room_name, customer_name, start_date, end_date):
        """
        Makes a reservation for a specific room if possible.
        :param room_name: Name of the room to reserve.
        :param customer_name: Name of the customer making the reservation.
        :param start_date: Start date of the reservation (datetime.date).
        :param end_date: End date of the reservation (datetime.date).
        :raises InvalidDateError: If the dates are invalid.
        :raises KeyError: If the room does not exist.
        """
        if start_date >= end_date:
            raise InvalidDateError("Start date must be earlier than end date.")
        if room_name not in self.rooms:
            raise KeyError(f"Room '{room_name}' does not exist in the hotel.")
        self.rooms[room_name].add_reservation(customer_name, start_date, end_date)

    def check_availability(self, room_name, start_date, end_date):
        """
        Checks if a specific room is available for the given date range.
        :param room_name: Name of the room to check.
        :param start_date: Start date of the reservation (datetime.date).
        :param end_date: End date of the reservation (datetime.date).
        :return: True if the room is available, False otherwise.
        :raises KeyError: If the room does not exist.
        """
        if room_name not in self.rooms:
            raise KeyError(f"Room '{room_name}' does not exist in the hotel.")
        return self.rooms[room_name].is_available(start_date, end_date)

# Example usage
if __name__ == "__main__":
    try:
        hotel = Hotel()
        
        # Reservation details
        customer_name = "Alice Smith"
        room_name = "Grand Salon"
        start_date = datetime.date(2023, 11, 5)
        end_date = datetime.date(2023, 11, 10)
        
        # Make reservation
        if hotel.check_availability(room_name, start_date, end_date):
            hotel.make_reservation(room_name, customer_name, start_date, end_date)
            print(f"Reservation successful for {customer_name} in {room_name}.")

        # Check availability after reservation
        availability = hotel.check_availability(room_name, start_date, end_date)
        print(f"Is {room_name} available from {start_date} to {end_date}? {'Yes' if availability else 'No'}")

    except ReservationError as e:
        print(f"Reservation error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
