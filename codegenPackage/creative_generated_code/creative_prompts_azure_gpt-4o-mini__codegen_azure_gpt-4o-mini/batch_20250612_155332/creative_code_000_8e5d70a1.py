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
class DJPackage:
    """Class representing a DJ package for an event."""
    
    def __init__(self, name, price, description):
        """
        Initialize a new DJ package.
        
        :param name: The name of the package
        :param price: The price of the package
        :param description: A brief description of the package
        """
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        """Return a string representation of the DJ package."""
        return f"{self.name}: {self.description} - ${self.price:.2f}"


class BookingSystem:
    """Class to manage DJ event bookings."""

    def __init__(self):
        """Initialize the booking system with available DJ packages."""
        self.packages = [
            DJPackage("Pop-Up", 500, "A short set for casual events."),
            DJPackage("Full", 1000, "Complete DJ services for a full night."),
            DJPackage("Everything", 1500, "All-inclusive package with extras.")
        ]
        self.bookings = []

    def display_packages(self):
        """Display available DJ packages."""
        print("Available DJ Packages:")
        for idx, package in enumerate(self.packages):
            print(f"{idx + 1}. {package}")

    def book_package(self, package_index, customer_name):
        """
        Book a DJ package for a customer.
        
        :param package_index: Index of the selected package (1-based)
        :param customer_name: Name of the customer making the booking
        :raises ValueError: If the package index is invalid
        """
        try:
            # Validate the package index
            if package_index < 1 or package_index > len(self.packages):
                raise ValueError("Invalid package selection. Please choose a valid package.")

            selected_package = self.packages[package_index - 1]
            booking_details = {
                "customer_name": customer_name,
                "package": selected_package
            }
            self.bookings.append(booking_details)
            print(f"Successfully booked {selected_package.name} for {customer_name}.")

        except ValueError as e:
            print(f"Error: {e}")

    def view_bookings(self):
        """Display all bookings made in the system."""
        if not self.bookings:
            print("No bookings made yet.")
            return
        
        print("Current Bookings:")
        for booking in self.bookings:
            print(f"{booking['customer_name']} - {booking['package']}")


# Example Usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    booking_system.display_packages()

    # Simulate user input for booking
    try:
        user_choice = int(input("Select a DJ package by number: "))
        user_name = input("Enter your name: ")
        booking_system.book_package(user_choice, user_name)
    except ValueError:
        print("Please enter valid input.")

    booking_system.view_bookings()
```
