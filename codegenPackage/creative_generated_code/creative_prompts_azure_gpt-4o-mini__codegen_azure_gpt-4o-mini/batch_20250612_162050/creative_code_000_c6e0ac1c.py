"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegujaratcalling.com
Prompt: Generate a code snippet for a travel booking application that allows users to select tour packages like Domestic, International, and Honeymoon tours as described on The Gujarat Calling website.
Generated: DETERMINISTIC_c6e0ac1ca66051a9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# travel_booking.py

class TourPackage:
    """
    Class to represent a tour package.
    """
    def __init__(self, name, description, price):
        """
        Initialize a tour package with a name, description, and price.

        :param name: str - Name of the tour package
        :param description: str - Description of the tour package
        :param price: float - Price of the tour package
        """
        self.name = name
        self.description = description
        self.price = price

    def display_info(self):
        """
        Display the information about the tour package.
        """
        return f"Package: {self.name}\nDescription: {self.description}\nPrice: ${self.price:.2f}"


class TravelBooking:
    """
    Class to manage travel bookings.
    """
    def __init__(self):
        """Initialize an empty list of available tour packages."""
        self.packages = []
        self.selected_package = None

    def add_package(self, package: TourPackage):
        """
        Add a tour package to the booking system.

        :param package: TourPackage - The tour package to be added
        """
        self.packages.append(package)

    def display_packages(self):
        """
        Display all available tour packages.
        """
        print("Available Tour Packages:")
        for index, package in enumerate(self.packages, start=1):
            print(f"{index}. {package.display_info()}\n")

    def select_package(self, index: int):
        """
        Select a tour package by its index.

        :param index: int - The index of the package to select
        :raises IndexError: If the index is out of range
        """
        try:
            self.selected_package = self.packages[index - 1]
            print(f"You have selected: {self.selected_package.name}")
        except IndexError:
            print("Error: Invalid package selection. Please choose a valid number.")

    def book_package(self):
        """
        Handle the booking of the selected package.
        :raises Exception: If no package has been selected for booking
        """
        if not self.selected_package:
            raise Exception("No package selected. Please select a package to book.")

        # Simulate booking process
        print(f"Booking your tour package: {self.selected_package.name}...")
        print("Booking successful!")


# Example usage:
if __name__ == "__main__":
    # Create an instance of the travel booking system
    booking_system = TravelBooking()

    # Define some tour packages
    domestic_tour = TourPackage("Domestic Tour", "Explore the beauty of inland attractions.", 500.00)
    international_tour = TourPackage("International Tour", "Travel to exotic international destinations.", 1500.00)
    honeymoon_tour = TourPackage("Honeymoon Tour", "Romantic getaways for newlyweds.", 2000.00)

    # Add packages to the system
    booking_system.add_package(domestic_tour)
    booking_system.add_package(international_tour)
    booking_system.add_package(honeymoon_tour)

    # Display available packages
    booking_system.display_packages()

    # User selects a package (for example, package 2)
    booking_system.select_package(2)

    # Attempt to book the selected package
    try:
        booking_system.book_package()
    except Exception as e:
        print(f"Booking failed: {e}")
```
