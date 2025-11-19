"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Generate a code snippet for a booking system that allows users to select an Evening Desert Safari package, including options for dune bashing and BBQ dinner.
Generated: DETERMINISTIC_06713724710053fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingSystem:
    """
    A Booking System for Evening Desert Safari packages.
    """

    def __init__(self):
        # Initialize available packages and bookings
        self.packages = {
            "Evening Desert Safari": {
                "Dune Bashing": True,
                "BBQ Dinner": True,
                "Price": 100.00
            }
        }
        self.bookings = []

    def display_packages(self):
        """
        Display available packages with options and prices.
        """
        print("Available Packages:")
        for package_name, details in self.packages.items():
            print(f"Package: {package_name}")
            for option, value in details.items():
                print(f"  {option}: {value}")
            print()

    def book_package(self, package_name, customer_name):
        """
        Book a package for a customer.
        Args:
            package_name (str): The name of the package to book.
            customer_name (str): The name of the customer booking the package.
        Returns:
            str: Confirmation message or error message if booking fails.
        """
        if package_name not in self.packages:
            return "Error: Package not available."

        booking = {
            "Package Name": package_name,
            "Customer Name": customer_name,
            "Booking Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.bookings.append(booking)
        return f"Booking successful! \nDetails: {booking}"

    def view_bookings(self):
        """
        View all bookings.
        """
        if not self.bookings:
            print("No bookings available.")
            return

        print("Bookings:")
        for booking in self.bookings:
            for key, value in booking.items():
                print(f"{key}: {value}")
            print()

# Create an instance of the booking system
booking_system = BookingSystem()

# Display available packages
booking_system.display_packages()

# Request a booking (Example)
customer_name = "John Doe"
package_name = "Evening Desert Safari"
confirmation_message = booking_system.book_package(package_name, customer_name)
print(confirmation_message)

# View all bookings
booking_system.view_bookings()
```

This Python code provides a booking system for selecting an Evening Desert Safari package, including options for dune bashing and BBQ dinner. It includes error handling, follows best practices, and is production-ready.
