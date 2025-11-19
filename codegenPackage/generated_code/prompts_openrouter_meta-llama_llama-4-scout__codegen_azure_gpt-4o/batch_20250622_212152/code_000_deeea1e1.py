"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Generate a Python code snippet to create a simple tour package booking system for a travel agency like Best Holidays All India, including packages for Rajasthan and Goa."
Generated: DETERMINISTIC_deeea1e11d4392d0
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class TourPackage:
    """
    Represents a tour package with details like name, destination, price, and duration.
    """
    def __init__(self, name, destination, price, duration):
        self.name = name
        self.destination = destination
        self.price = price
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.destination} | Price: ₹{self.price} | Duration: {self.duration} days"


class Booking:
    """
    Represents a booking for a tour package.
    """
    def __init__(self, customer_name, package, booking_date):
        self.customer_name = customer_name
        self.package = package
        self.booking_date = booking_date

    def __str__(self):
        return (f"Booking Details:\n"
                f"Customer Name: {self.customer_name}\n"
                f"Package: {self.package.name}\n"
                f"Destination: {self.package.destination}\n"
                f"Price: ₹{self.package.price}\n"
                f"Duration: {self.package.duration} days\n"
                f"Booking Date: {self.booking_date.strftime('%Y-%m-%d')}")


class TourBookingSystem:
    """
    A simple tour package booking system for a travel agency.
    """
    def __init__(self):
        self.packages = []
        self.bookings = []

    def add_package(self, package):
        """
        Adds a new tour package to the system.
        """
        self.packages.append(package)

    def list_packages(self):
        """
        Lists all available tour packages.
        """
        if not self.packages:
            print("No packages available.")
        else:
            print("Available Tour Packages:")
            for idx, package in enumerate(self.packages, start=1):
                print(f"{idx}. {package}")

    def book_package(self, customer_name, package_index):
        """
        Books a tour package for a customer.
        """
        try:
            if package_index < 1 or package_index > len(self.packages):
                raise ValueError("Invalid package index.")
            
            selected_package = self.packages[package_index - 1]
            booking_date = datetime.datetime.now()
            booking = Booking(customer_name, selected_package, booking_date)
            self.bookings.append(booking)
            print("Booking successful!")
            print(booking)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_bookings(self):
        """
        Lists all bookings made in the system.
        """
        if not self.bookings:
            print("No bookings found.")
        else:
            print("All Bookings:")
            for idx, booking in enumerate(self.bookings, start=1):
                print(f"{idx}. {booking}")


# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    system = TourBookingSystem()

    # Add tour packages
    system.add_package(TourPackage("Rajasthan Heritage Tour", "Rajasthan", 25000, 7))
    system.add_package(TourPackage("Goa Beach Getaway", "Goa", 15000, 5))

    # List available packages
    system.list_packages()

    # Book a package
    customer_name = input("Enter your name: ")
    package_index = int(input("Enter the package number to book: "))
    system.book_package(customer_name, package_index)

    # List all bookings
    system.list_bookings()
```
