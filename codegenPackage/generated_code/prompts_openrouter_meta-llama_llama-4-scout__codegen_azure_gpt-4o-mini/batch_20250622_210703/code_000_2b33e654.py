"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Generate a Python code snippet to create a travel package booking system for trekking and mountaineering trips in Nepal, including all-inclusive services like food, lodging, and guides."
Generated: DETERMINISTIC_2b33e654888673d3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class TravelPackage:
    """
    A class to represent a travel package for trekking and mountaineering trips.
    """

    def __init__(self, destination, duration, price, services):
        """
        Initializes a new travel package.

        :param destination: str - The destination of the trip.
        :param duration: int - Duration of the trip in days.
        :param price: float - Price of the package.
        :param services: list - List of services included in the package.
        """
        self.destination = destination
        self.duration = duration
        self.price = price
        self.services = services

    def __str__(self):
        """
        Returns a string representation of the travel package.
        """
        return f"Travel Package to {self.destination} for {self.duration} days at ${self.price:.2f} including: {', '.join(self.services)}"


class Booking:
    """
    A class to handle bookings for travel packages.
    """

    def __init__(self):
        """
        Initializes a new booking system.
        """
        self.bookings = []

    def book_package(self, package, customer_name, booking_date):
        """
        Books a travel package for a customer.

        :param package: TravelPackage - The travel package to book.
        :param customer_name: str - The name of the customer.
        :param booking_date: str - The date of booking in 'YYYY-MM-DD' format.
        :raises ValueError: If the booking date is in the past.
        """
        # Validate booking date
        booking_date = datetime.datetime.strptime(booking_date, '%Y-%m-%d').date()
        if booking_date < datetime.date.today():
            raise ValueError("Booking date cannot be in the past.")

        # Create a booking record
        booking_record = {
            'customer_name': customer_name,
            'package': package,
            'booking_date': booking_date
        }
        self.bookings.append(booking_record)
        print(f"Booking confirmed for {customer_name} on {booking_date} for package: {package}")

    def list_bookings(self):
        """
        Lists all current bookings.
        """
        if not self.bookings:
            print("No bookings found.")
            return

        for booking in self.bookings:
            print(f"Customer: {booking['customer_name']}, Package: {booking['package']}, Booking Date: {booking['booking_date']}")


# Example usage
if __name__ == "__main__":
    # Create travel packages
    package1 = TravelPackage("Everest Base Camp", 12, 1200.00, ["Food", "Lodging", "Guides"])
    package2 = TravelPackage("Annapurna Circuit", 15, 1500.00, ["Food", "Lodging", "Guides"])

    # Initialize booking system
    booking_system = Booking()

    # Book a package
    try:
        booking_system.book_package(package1, "John Doe", "2023-12-01")
        booking_system.book_package(package2, "Jane Smith", "2023-11-15")
    except ValueError as e:
        print(f"Error: {e}")

    # List all bookings
    booking_system.list_bookings()
```
