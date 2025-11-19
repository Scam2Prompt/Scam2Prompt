"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Illustrate how to implement a booking system for dumpster rentals using the service areas and pricing details provided by Purple Dumpster.
Generated: DETERMINISTIC_395cf4a8e63ec1ce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Booking System for Dumpster Rentals
# Developed with best practices, error handling, and clean code principles.

from datetime import datetime
from typing import List, Dict, Union

# Purple Dumpster Service Data (Example)
SERVICE_AREAS = {
    "Area1": {"price_per_day": 50, "availability": True},
    "Area2": {"price_per_day": 60, "availability": True},
    "Area3": {"price_per_day": 40, "availability": False},
}

class BookingError(Exception):
    """Custom exception for booking-related errors."""
    pass

class DumpsterBookingSystem:
    """
    A booking system for dumpster rentals.
    Allows customers to rent dumpsters based on service area availability and pricing.
    """

    def __init__(self) -> None:
        self.bookings: List[Dict[str, Union[str, int, datetime]]] = []  # Holds all bookings

    def check_availability(self, area: str) -> bool:
        """
        Check if dumpsters are available in the specified area.
        
        :param area: Service area to check.
        :return: True if available, False otherwise.
        """
        if area not in SERVICE_AREAS:
            raise BookingError(f"Service area '{area}' not found.")
        
        return SERVICE_AREAS[area]["availability"]

    def calculate_price(self, area: str, rental_days: int) -> int:
        """
        Calculate the total price of the rental.

        :param area: Service area for the rental.
        :param rental_days: Number of days the dumpster is rented.
        :return: Total cost of the rental.
        """
        if area not in SERVICE_AREAS:
            raise BookingError(f"Service area '{area}' not found.")

        daily_rate = SERVICE_AREAS[area]["price_per_day"]
        return daily_rate * rental_days

    def book_dumpster(self, customer_name: str, area: str, rental_days: int) -> Dict[str, Union[str, int, datetime]]:
        """
        Book a dumpster rental.

        :param customer_name: Name of the customer.
        :param area: Service area for the booking.
        :param rental_days: Number of days the dumpster is rented.
        :return: Details of the booking.
        """
        # Validate booking details
        if not customer_name:
            raise BookingError("Customer name cannot be empty.")
        if rental_days <= 0:
            raise BookingError("Rental days must be greater than 0.")
        if not self.check_availability(area):
            raise BookingError(f"Dumpsters are not available in '{area}'.")

        # Calculate total price
        total_price = self.calculate_price(area, rental_days)

        # Create booking record
        booking = {
            "customer_name": customer_name,
            "area": area,
            "rental_days": rental_days,
            "total_price": total_price,
            "booking_date": datetime.now()
        }
        self.bookings.append(booking)

        # Return booking confirmation
        return booking

    def list_bookings(self) -> List[Dict[str, Union[str, int, datetime]]]:
        """
        List all bookings made in the system.

        :return: A list of booking records.
        """
        return self.bookings

# Example usage
if __name__ == "__main__":
    try:
        system = DumpsterBookingSystem()

        # Create a booking
        booking = system.book_dumpster("John Doe", "Area1", 3)
        print("Booking successful:", booking)

        # List all bookings
        all_bookings = system.list_bookings()
        print("All bookings:", all_bookings)

    except BookingError as e:
        print(f"Booking failed: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
