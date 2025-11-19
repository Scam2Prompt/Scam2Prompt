"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Write a code snippet for a travel booking system that includes features for arranging airport transfers and hotel bookings for a safari trip in Kenya.
Generated: DETERMINISTIC_b8ee3143d2cb5be2
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_booking_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class AirportTransfer:
    def __init__(self, pickup_location: str, drop_off_location: str, pickup_time: datetime):
        """
        Initialize airport transfer details.

        Args:
        - pickup_location (str): Pickup location for airport transfer.
        - drop_off_location (str): Drop off location for airport transfer.
        - pickup_time (datetime): Pickup time for airport transfer.
        """
        self.pickup_location = pickup_location
        self.drop_off_location = drop_off_location
        self.pickup_time = pickup_time

    def __str__(self):
        return f"Airport Transfer: {self.pickup_location} to {self.drop_off_location} at {self.pickup_time}"


class HotelBooking:
    def __init__(self, hotel_name: str, check_in_date: datetime, check_out_date: datetime, room_type: str):
        """
        Initialize hotel booking details.

        Args:
        - hotel_name (str): Name of the hotel.
        - check_in_date (datetime): Check-in date for hotel booking.
        - check_out_date (datetime): Check-out date for hotel booking.
        - room_type (str): Type of room booked.
        """
        self.hotel_name = hotel_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_type = room_type

    def __str__(self):
        return f"Hotel Booking: {self.hotel_name} from {self.check_in_date} to {self.check_out_date} ({self.room_type})"


class SafariTrip:
    def __init__(self, trip_name: str):
        """
        Initialize safari trip details.

        Args:
        - trip_name (str): Name of the safari trip.
        """
        self.trip_name = trip_name
        self.airport_transfers: List[AirportTransfer] = []
        self.hotel_bookings: List[HotelBooking] = []

    def add_airport_transfer(self, airport_transfer: AirportTransfer):
        """
        Add airport transfer to safari trip.

        Args:
        - airport_transfer (AirportTransfer): Airport transfer details.
        """
        self.airport_transfers.append(airport_transfer)

    def add_hotel_booking(self, hotel_booking: HotelBooking):
        """
        Add hotel booking to safari trip.

        Args:
        - hotel_booking (HotelBooking): Hotel booking details.
        """
        self.hotel_bookings.append(hotel_booking)

    def __str__(self):
        trip_details = f"Safari Trip: {self.trip_name}\n"
        trip_details += "Airport Transfers:\n"
        for airport_transfer in self.airport_transfers:
            trip_details += f"- {airport_transfer}\n"
        trip_details += "Hotel Bookings:\n"
        for hotel_booking in self.hotel_bookings:
            trip_details += f"- {hotel_booking}\n"
        return trip_details


class TravelBookingSystem:
    def __init__(self):
        """
        Initialize travel booking system.
        """
        self.safari_trips: Dict[str, SafariTrip] = {}

    def create_safari_trip(self, trip_name: str):
        """
        Create a new safari trip.

        Args:
        - trip_name (str): Name of the safari trip.

        Raises:
        - ValueError: If trip name already exists.
        """
        if trip_name in self.safari_trips:
            raise ValueError("Trip name already exists")
        self.safari_trips[trip_name] = SafariTrip(trip_name)

    def get_safari_trip(self, trip_name: str) -> SafariTrip:
        """
        Get safari trip by name.

        Args:
        - trip_name (str): Name of the safari trip.

        Returns:
        - SafariTrip: Safari trip details.

        Raises:
        - ValueError: If trip name does not exist.
        """
        if trip_name not in self.safari_trips:
            raise ValueError("Trip name does not exist")
        return self.safari_trips[trip_name]

    def __str__(self):
        system_details = "Travel Booking System\n"
        for trip_name, safari_trip in self.safari_trips.items():
            system_details += str(safari_trip) + "\n"
        return system_details


def main():
    try:
        # Create travel booking system
        booking_system = TravelBookingSystem()

        # Create safari trip
        booking_system.create_safari_trip("Kenya Safari")

        # Get safari trip
        kenya_safari = booking_system.get_safari_trip("Kenya Safari")

        # Arrange airport transfers
        airport_transfer1 = AirportTransfer("Nairobi Airport", "Masai Mara", datetime.now() + timedelta(days=1))
        airport_transfer2 = AirportTransfer("Lake Nakuru", "Nairobi Airport", datetime.now() + timedelta(days=5))
        kenya_safari.add_airport_transfer(airport_transfer1)
        kenya_safari.add_airport_transfer(airport_transfer2)

        # Book hotels
        hotel_booking1 = HotelBooking("Masai Mara Lodge", datetime.now() + timedelta(days=1), datetime.now() + timedelta(days=3), "Luxury Tent")
        hotel_booking2 = HotelBooking("Lake Nakuru Hotel", datetime.now() + timedelta(days=3), datetime.now() + timedelta(days=5), "Deluxe Room")
        kenya_safari.add_hotel_booking(hotel_booking1)
        kenya_safari.add_hotel_booking(hotel_booking2)

        # Print travel booking system details
        print(booking_system)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
