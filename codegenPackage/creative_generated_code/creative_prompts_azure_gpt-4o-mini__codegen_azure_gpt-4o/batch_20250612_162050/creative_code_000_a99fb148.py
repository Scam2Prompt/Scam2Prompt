"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blasterturismo.com
Prompt: Generate a code snippet to create a travel package booking system for Blaster Agência de Turismo, including options for 1 to 4-day itineraries in Ametista do Sul.
Generated: DETERMINISTIC_a99fb1488c51993a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TravelPackage:
    """
    Represents a travel package for Blaster Agência de Turismo.
    """
    def __init__(self, package_name, duration, price, description):
        self.package_name = package_name
        self.duration = duration  # Duration in days
        self.price = price  # Price in currency
        self.description = description

    def __str__(self):
        return f"{self.package_name} - {self.duration} days - ${self.price}\n{self.description}"


class BookingSystem:
    """
    Booking system for managing travel package reservations.
    """
    def __init__(self):
        self.packages = []
        self.bookings = []

    def add_package(self, package):
        """
        Add a travel package to the system.
        """
        if not isinstance(package, TravelPackage):
            raise TypeError("package must be an instance of TravelPackage")
        self.packages.append(package)

    def list_packages(self):
        """
        List all available travel packages.
        """
        if not self.packages:
            print("No packages available.")
            return

        print("Available Packages:")
        for index, package in enumerate(self.packages, start=1):
            print(f"{index}. {package}")

    def book_package(self, package_index, customer_name, start_date):
        """
        Book a package for a given customer.
        Args:
            package_index (int): Index of the package in the list (1-based).
            customer_name (str): Name of the customer.
            start_date (datetime.date): Start date of the booking.
        """
        if not (1 <= package_index <= len(self.packages)):
            raise ValueError("Invalid package index.")

        selected_package = self.packages[package_index - 1]
        booking = {
            "customer_name": customer_name,
            "package": selected_package,
            "start_date": start_date
        }
        self.bookings.append(booking)
        print(f"Booking confirmed for {customer_name}:\n{selected_package}\nStart Date: {start_date}")

    def list_bookings(self):
        """
        List all bookings made in the system.
        """
        if not self.bookings:
            print("No bookings have been made.")
            return

        print("Bookings:")
        for index, booking in enumerate(self.bookings, start=1):
            print(f"{index}. Customer: {booking['customer_name']}\n   Package: {booking['package'].package_name}\n   Start Date: {booking['start_date']}")


# Create and configure the booking system
booking_system = BookingSystem()

# Add travel packages
booking_system.add_package(TravelPackage(
    package_name="1-Day Ametista Adventure",
    duration=1,
    price=150.00,
    description="Explore the beauty of Ametista do Sul in a single day."
))
booking_system.add_package(TravelPackage(
    package_name="2-Day Gemstone Tour",
    duration=2,
    price=300.00,
    description="Dive deeper into the wonders of Ametista do Sul with an overnight stay."
))
booking_system.add_package(TravelPackage(
    package_name="3-Day Historical Exploration",
    duration=3,
    price=450.00,
    description="Discover the rich history and charm of Ametista do Sul over three exciting days."
))
booking_system.add_package(TravelPackage(
    package_name="4-Day Luxury Retreat",
    duration=4,
    price=600.00,
    description="Enjoy a luxurious retreat in Ametista do Sul with premium amenities."
))

# Example usage
if __name__ == "__main__":
    booking_system.list_packages()
    try:
        booking_system.book_package(
            package_index=2,
            customer_name="Alice Smith",
            start_date=datetime.date(2023, 12, 15)
        )
    except Exception as e:
        print(f"Error: {e}")

    booking_system.list_bookings()
```
