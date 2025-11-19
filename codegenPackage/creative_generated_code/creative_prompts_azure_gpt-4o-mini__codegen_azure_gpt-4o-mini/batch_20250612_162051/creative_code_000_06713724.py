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
class DesertSafariBooking:
    """
    A class to represent a booking system for an Evening Desert Safari package.
    """

    def __init__(self):
        self.available_packages = {
            "standard": {"dune_bashing": False, "bbq_dinner": False},
            "deluxe": {"dune_bashing": True, "bbq_dinner": True},
        }
        self.bookings = []

    def display_packages(self):
        """Displays available safari packages with options."""
        print("Available Evening Desert Safari Packages:")
        for package, options in self.available_packages.items():
            print(f"- {package.capitalize()}: "
                  f"Dune Bashing: {'Included' if options['dune_bashing'] else 'Not Included'}, "
                  f"BBQ Dinner: {'Included' if options['bbq_dinner'] else 'Not Included'}")

    def book_package(self, package_name: str):
        """
        Books a selected package if available.
        
        :param package_name: Name of the package to book
        :raises ValueError: If the package is not available
        """
        if package_name not in self.available_packages:
            raise ValueError("Invalid package name. Please choose a valid package.")

        booking = {
            "package": package_name,
            "options": self.available_packages[package_name]
        }
        self.bookings.append(booking)
        print(f"Booking confirmed for {package_name} package.")

    def view_bookings(self):
        """Displays all user bookings."""
        if not self.bookings:
            print("No bookings found.")
            return
        
        print("Current Bookings:")
        for booking in self.bookings:
            print(f"- {booking['package'].capitalize()} Package: "
                  f"Dune Bashing: {'Included' if booking['options']['dune_bashing'] else 'Not Included'}, "
                  f"BBQ Dinner: {'Included' if booking['options']['bbq_dinner'] else 'Not Included'}")


if __name__ == "__main__":
    # Instantiate the booking system
    safari_booking = DesertSafariBooking()
    
    # Display available packages
    safari_booking.display_packages()
    
    # User selects a package
    try:
        selected_package = input("Please enter the package you want to book (standard/deluxe): ").lower()
        safari_booking.book_package(selected_package)

        # View all bookings
        safari_booking.view_bookings()
    except ValueError as e:
        print(f"Error: {e}")
```
