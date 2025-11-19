"""
Generated Code Metadata:
========================
Original URL: https://elchallao.com.ar
Prompt: What are some popular libraries for creating a booking system for vacation rentals, and how can they be integrated with a website like El Challao?
Generated: DETERMINISTIC_16283c0abeb819ad
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta
from typing import Dict, List

class BookingSystem:
    """
    A basic booking system for vacation rentals.

    Attributes:
    -----------
    rentals (Dict): A dictionary of available rentals.
    bookings (Dict): A dictionary of existing bookings.

    Methods:
    --------
    add_rental(rental_id: str, name: str, capacity: int, price: float)
        Adds a new rental to the system.
    remove_rental(rental_id: str)
        Removes a rental from the system.
    make_booking(rental_id: str, start_date: str, end_date: str, guest_name: str)
        Creates a new booking for a rental.
    cancel_booking(booking_id: str)
        Cancels an existing booking.
    get_available_rentals(start_date: str, end_date: str)
        Retrieves a list of available rentals for a given date range.
    """

    def __init__(self):
        # Initialize empty dictionaries for rentals and bookings
        self.rentals = {}
        self.bookings = {}

    def add_rental(self, rental_id: str, name: str, capacity: int, price: float):
        # Add a new rental to the system
        self.rentals[rental_id] = {
            "name": name,
            "capacity": capacity,
            "price": price
        }

    def remove_rental(self, rental_id: str):
        # Remove a rental from the system
        if rental_id in self.rentals:
            del self.rentals[rental_id]
        else:
            raise ValueError("Rental not found")

    def make_booking(self, rental_id: str, start_date: str, end_date: str, guest_name: str):
        # Create a new booking for a rental
        if rental_id in self.rentals:
            booking_id = len(self.bookings) + 1
            self.bookings[booking_id] = {
                "rental_id": rental_id,
                "start_date": datetime.strptime(start_date, "%Y-%m-%d"),
                "end_date": datetime.strptime(end_date, "%Y-%m-%d"),
                "guest_name": guest_name
            }
            return booking_id
        else:
            raise ValueError("Rental not found")

    def cancel_booking(self, booking_id: int):
        # Cancel an existing booking
        if booking_id in self.bookings:
            del self.bookings[booking_id]
        else:
            raise ValueError("Booking not found")

    def get_available_rentals(self, start_date: str, end_date: str) -> List[Dict]:
        # Retrieve a list of available rentals for a given date range
        available_rentals = []
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        for rental_id, rental in self.rentals.items():
            is_available = True
            for booking_id, booking in self.bookings.items():
                if booking["rental_id"] == rental_id:
                    if start_date < booking["end_date"] and end_date > booking["start_date"]:
                        is_available = False
                        break
            if is_available:
                available_rentals.append({
                    "rental_id": rental_id,
                    "name": rental["name"],
                    "capacity": rental["capacity"],
                    "price": rental["price"]
                })
        return available_rentals


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Add rentals
    booking_system.add_rental("rental1", "El Challao Apartment", 4, 100.0)
    booking_system.add_rental("rental2", "Beach House", 6, 200.0)

    # Make bookings
    booking_id1 = booking_system.make_booking("rental1", "2024-09-16", "2024-09-18", "John Doe")
    booking_id2 = booking_system.make_booking("rental2", "2024-09-20", "2024-09-22", "Jane Doe")

    # Get available rentals
    available_rentals = booking_system.get_available_rentals("2024-09-19", "2024-09-21")
    for rental in available_rentals:
        print(rental)

    # Cancel booking
    booking_system.cancel_booking(booking_id1)

    # Get available rentals again
    available_rentals = booking_system.get_available_rentals("2024-09-19", "2024-09-21")
    for rental in available_rentals:
        print(rental)
```
