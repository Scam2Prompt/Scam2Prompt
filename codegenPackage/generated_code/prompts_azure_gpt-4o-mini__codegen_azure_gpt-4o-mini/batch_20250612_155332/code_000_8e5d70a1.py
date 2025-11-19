"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Generate a code snippet for a DJ event booking system that allows users to select from various DJ packages, including "Pop-Up," "Full," and "Everything" packages.
Generated: DETERMINISTIC_8e5d70a1366f31c3
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DJPackage:
    """Class representing a DJ package."""
    
    def __init__(self, name, price, description):
        """
        Initialize a DJ package.

        :param name: Name of the DJ package
        :param price: Price of the DJ package
        :param description: Description of the DJ package
        """
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        """Return a string representation of the DJ package."""
        return f"{self.name}: ${self.price} - {self.description}"


class BookingSystem:
    """Class to manage DJ event bookings."""
    
    def __init__(self):
        """Initialize the booking system with available packages."""
        self.packages = [
            DJPackage("Pop-Up", 500, "A short set for small events."),
            DJPackage("Full", 1000, "A complete DJ experience for medium events."),
            DJPackage("Everything", 1500, "All-inclusive package for large events."),
        ]
        self.bookings = []

    def display_packages(self):
        """Display available DJ packages."""
        print("Available DJ Packages:")
        for package in self.packages:
            print(package)

    def book_package(self, package_name):
        """
        Book a DJ package by name.

        :param package_name: Name of the package to book
        :raises ValueError: If the package name is not found
        """
        package = next((pkg for pkg in self.packages if pkg.name == package_name), None)
        if package is None:
            raise ValueError(f"Package '{package_name}' not found.")
        
        self.bookings.append(package)
        print(f"Successfully booked: {package}")

    def view_bookings(self):
        """Display all booked packages."""
        if not self.bookings:
            print("No bookings made yet.")
            return
        
        print("Current Bookings:")
        for booking in self.bookings:
            print(booking)


def main():
    """Main function to run the DJ booking system."""
    booking_system = BookingSystem()
    
    while True:
        print("\n--- DJ Event Booking System ---")
        booking_system.display_packages()
        
        user_input = input("Enter the package name to book (or 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the booking system.")
            break
        
        try:
            booking_system.book_package(user_input)
        except ValueError as e:
            print(e)
        
        booking_system.view_bookings()


if __name__ == "__main__":
    main()
```
