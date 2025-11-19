"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Illustrate how to implement a booking system for dumpster rentals using the service areas and pricing details provided by Purple Dumpster.
Generated: DETERMINISTIC_395cf4a8e63ec1ce
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
from typing import List, Dict, Optional

class Dumpster:
    def __init__(self, size: str, price_per_day: float):
        """
        Initialize a dumpster with a specific size and price per day.
        
        :param size: Size of the dumpster (e.g., '10 yard', '20 yard').
        :param price_per_day: Rental price per day for the dumpster.
        """
        self.size = size
        self.price_per_day = price_per_day

class Booking:
    def __init__(self, dumpster: Dumpster, start_date: datetime, rental_days: int):
        """
        Initialize a booking for a dumpster rental.
        
        :param dumpster: The dumpster being rented.
        :param start_date: The start date of the rental.
        :param rental_days: The number of days the dumpster is rented for.
        """
        self.dumpster = dumpster
        self.start_date = start_date
        self.rental_days = rental_days
        self.end_date = start_date + timedelta(days=rental_days)

    def total_cost(self) -> float:
        """
        Calculate the total cost of the rental.
        
        :return: Total cost of the rental.
        """
        return self.dumpster.price_per_day * self.rental_days

class BookingSystem:
    def __init__(self):
        """
        Initialize the booking system with available dumpsters and bookings.
        """
        self.dumpsters: List[Dumpster] = []
        self.bookings: List[Booking] = []

    def add_dumpster(self, size: str, price_per_day: float):
        """
        Add a dumpster to the system.
        
        :param size: Size of the dumpster.
        :param price_per_day: Rental price per day.
        """
        dumpster = Dumpster(size, price_per_day)
        self.dumpsters.append(dumpster)

    def book_dumpster(self, size: str, start_date: datetime, rental_days: int) -> Optional[Booking]:
        """
        Book a dumpster if available.
        
        :param size: Size of the dumpster to book.
        :param start_date: Start date for the rental.
        :param rental_days: Number of days for the rental.
        :return: Booking object if successful, None otherwise.
        """
        # Check if the dumpster is available
        for dumpster in self.dumpsters:
            if dumpster.size == size:
                # Create a new booking
                booking = Booking(dumpster, start_date, rental_days)
                self.bookings.append(booking)
                return booking
        
        print(f"Error: No dumpster of size '{size}' available.")
        return None

    def list_bookings(self) -> List[Dict]:
        """
        List all current bookings.
        
        :return: A list of dictionaries containing booking details.
        """
        return [
            {
                "size": booking.dumpster.size,
                "start_date": booking.start_date.strftime("%Y-%m-%d"),
                "end_date": booking.end_date.strftime("%Y-%m-%d"),
                "total_cost": booking.total_cost()
            }
            for booking in self.bookings
        ]

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Adding dumpsters to the system
    booking_system.add_dumpster('10 yard', 300.0)
    booking_system.add_dumpster('20 yard', 400.0)

    # Booking a dumpster
    start_date = datetime.now()
    rental_days = 5
    booking = booking_system.book_dumpster('10 yard', start_date, rental_days)

    if booking:
        print(f"Booking successful: {booking.size} from {booking.start_date} to {booking.end_date}. Total cost: ${booking.total_cost():.2f}")

    # Listing all bookings
    print("Current bookings:")
    for booking_info in booking_system.list_bookings():
        print(booking_info)
```
