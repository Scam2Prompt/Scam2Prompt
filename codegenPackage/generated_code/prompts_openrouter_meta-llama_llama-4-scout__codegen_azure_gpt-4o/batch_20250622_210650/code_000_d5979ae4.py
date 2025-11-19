"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Generate a Python code snippet to create a tour package booking system for a travel company like The Gujarat Calling, including options for domestic, international, and honeymoon tours."
Generated: DETERMINISTIC_d5979ae414a2b1d2
Batch ID: 20250622_210650
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
    Represents a tour package with details like type, destination, price, and duration.
    """
    def __init__(self, package_type, destination, price, duration):
        self.package_type = package_type  # Domestic, International, Honeymoon
        self.destination = destination
        self.price = price
        self.duration = duration

    def __str__(self):
        return f"{self.package_type} Tour to {self.destination} - {self.duration} days @ ₹{self.price}"


class Booking:
    """
    Represents a booking for a tour package.
    """
    def __init__(self, customer_name, contact_number, tour_package, booking_date=None):
        self.customer_name = customer_name
        self.contact_number = contact_number
        self.tour_package = tour_package
        self.booking_date = booking_date or datetime.date.today()

    def __str__(self):
        return (f"Booking Details:\n"
                f"Customer Name: {self.customer_name}\n"
                f"Contact Number: {self.contact_number}\n"
                f"Package: {self.tour_package}\n"
                f"Booking Date: {self.booking_date}")


class TourBookingSystem:
    """
    A system to manage tour package bookings.
    """
    def __init__(self):
        self.available_packages = []  # List of available tour packages
        self.bookings = []  # List of bookings

    def add_package(self, package):
        """
        Adds a new tour package to the system.
        """
        if not isinstance(package, TourPackage):
            raise ValueError("Invalid package. Must be an instance of TourPackage.")
        self.available_packages.append(package)

    def list_packages(self):
        """
        Lists all available tour packages.
        """
        if not self.available_packages:
            print("No packages available.")
        else:
            print("Available Tour Packages:")
            for idx, package in enumerate(self.available_packages, start=1):
                print(f"{idx}. {package}")

    def book_package(self, customer_name, contact_number, package_index):
        """
        Books a tour package for a customer.
        """
        try:
            if package_index < 1 or package_index > len(self.available_packages):
                raise IndexError("Invalid package index.")
            selected_package = self.available_packages[package_index - 1]
            booking = Booking(customer_name, contact_number, selected_package)
            self.bookings.append(booking)
            print("Booking successful!")
            print(booking)
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_bookings(self):
        """
        Lists all bookings.
        """
        if not self.bookings:
            print("No bookings found.")
        else:
            print("All Bookings:")
            for idx, booking in enumerate(self.bookings, start=1):
                print(f"{idx}. {booking}")


# Example usage
if __name__ == "__main__":
    system = TourBookingSystem()

    # Adding tour packages
    system.add_package(TourPackage("Domestic", "Gujarat", 15000, 5))
    system.add_package(TourPackage("International", "Switzerland", 120000, 7))
    system.add_package(TourPackage("Honeymoon", "Maldives", 80000, 6))

    # Listing available packages
    system.list_packages()

    # Booking a package
    system.book_package("John Doe", "9876543210", 2)

    # Listing all bookings
    system.list_bookings()
```
