"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-djs.com
Prompt: Generate a code snippet for a DJ event booking system that allows users to select from various DJ packages, including "Pop-Up," "Full," and "Everything" packages.
Generated: DETERMINISTIC_8e5d70a1366f31c3
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# DJ Event Booking System

from datetime import datetime

# Exception classes for error handling
class BookingError(Exception):
    pass

class InvalidPackageError(BookingError):
    pass

# Define DJ Packages
class DJPackage:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} Package - ${self.price}\n{self.description}"

# Predefined packages
PACKAGES = {
    "Pop-Up": DJPackage("Pop-Up", 500, "A quick setup for small events."),
    "Full": DJPackage("Full", 1000, "Full equipment and DJ services for medium-sized events."),
    "Everything": DJPackage("Everything", 2000, "Everything you need for large-scale events.")
}

# Booking class
class DJBookingSystem:
    def __init__(self):
        self.bookings = []

    def show_packages(self):
        """Displays available DJ packages."""
        print("Available DJ Packages:")
        for package in PACKAGES.values():
            print(package)
            print("-" * 50)

    def book_event(self, name, contact, package_name, event_date):
        """
        Allows user to book a DJ event.
        
        Args:
            name (str): Name of the person booking.
            contact (str): Contact information.
            package_name (str): Name of the package chosen.
            event_date (str): Event date in 'YYYY-MM-DD' format.

        Returns:
            str: Confirmation message.
        """
        # Validate package
        if package_name not in PACKAGES:
            raise InvalidPackageError(f"'{package_name}' is not a valid package.")

        # Validate date format
        try:
            event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
        except ValueError:
            raise BookingError("Invalid date format. Please use 'YYYY-MM-DD'.")

        # Store booking
        booking_info = {
            "name": name,
            "contact": contact,
            "package": PACKAGES[package_name],
            "event_date": event_date_obj.date()
        }
        self.bookings.append(booking_info)

        return f"Booking confirmed for {name} on {event_date_obj.date()} with the '{package_name}' package."

    def view_bookings(self):
        """Displays all bookings."""
        if not self.bookings:
            print("No bookings found.")
            return

        print("Current Bookings:")
        for idx, booking in enumerate(self.bookings, start=1):
            print(f"Booking #{idx}:")
            print(f"Name: {booking['name']}")
            print(f"Contact: {booking['contact']}")
            print(f"Package: {booking['package']}")
            print(f"Event Date: {booking['event_date']}")
            print("-" * 50)

# Example usage (commented out for production environments)
if __name__ == "__main__":
    system = DJBookingSystem()

    # Display available packages
    system.show_packages()

    # Book an event
    try:
        confirmation = system.book_event(
            name="John Doe",
            contact="john.doe@example.com",
            package_name="Full",
            event_date="2023-12-25"
        )
        print(confirmation)
    except (BookingError, InvalidPackageError) as e:
        print(f"Error: {e}")

    # View bookings
    system.view_bookings()
```
