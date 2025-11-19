"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tkcjourneys.com
Prompt: Generate a code snippet for a travel booking system that includes tour packages for Fairy Meadows and Hunza Valley in Pakistan.
Generated: DETERMINISTIC_4523873ad1aa1f8c
Batch ID: 20250612_162051
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
    """Class representing a tour package"""

    def __init__(self, name, destination, price, duration, itinerary):
        """
        Initialize a new TourPackage instance.

        :param name: Name of the tour package
        :param destination: Destination of the tour package
        :param price: Price of the tour package
        :param duration: Duration of the tour package in days
        :param itinerary: List of activities included in the tour
        """
        self.name = name
        self.destination = destination
        self.price = price
        self.duration = duration
        self.itinerary = itinerary

    def __str__(self):
        """Return a string representation of the tour package"""
        return f"{self.name} to {self.destination}: {self.duration} days, ${self.price}"

class BookingSystem:
    """Class to manage tour package bookings"""

    def __init__(self):
        """Initialize the booking system with a list of tour packages"""
        self.packages = []

    def add_package(self, package):
        """
        Add a new tour package to the system.

        :param package: TourPackage instance to add
        """
        if not isinstance(package, TourPackage):
            raise ValueError("Only TourPackage instances can be added")
        self.packages.append(package)

    def list_packages(self):
        """List all available tour packages"""
        if not self.packages:
            print("No tour packages available.")
            return
        
        print("Available Tour Packages:")
        for package in self.packages:
            print(package)

    def book_package(self, package_name):
        """
        Book a tour package by name.

        :param package_name: Name of the tour package to book
        :raises ValueError: If the package is not found
        """
        for package in self.packages:
            if package.name.lower() == package_name.lower():
                print(f"You have successfully booked the package: {package}")
                return
        raise ValueError(f"Tour package '{package_name}' not found.")

# Create an instance of the booking system
booking_system = BookingSystem()

# Add tour packages for Fairy Meadows and Hunza Valley
fairy_meadows_package = TourPackage(
    name="Fairy Meadows Adventure",
    destination="Fairy Meadows, Pakistan",
    price=599,
    duration=5,
    itinerary=[
        "Day 1: Arrival in Islamabad",
        "Day 2: Travel to Naran",
        "Day 3: Trek to Fairy Meadows",
        "Day 4: Explore Nanga Parbat Base Camp",
        "Day 5: Return to Islamabad"
    ]
)

hunza_valley_package = TourPackage(
    name="Hunza Valley Experience",
    destination="Hunza Valley, Pakistan",
    price=799,
    duration=7,
    itinerary=[
        "Day 1: Arrival in Gilgit",
        "Day 2: Drive to Hunza Valley",
        "Day 3: Visit Karimabad and Baltit Fort",
        "Day 4: Explore Passu Cones",
        "Day 5: Day trip to Khunjerab Pass",
        "Day 6: Visit Attabad Lake",
        "Day 7: Return to Gilgit"
    ]
)

# Add packages to the booking system
booking_system.add_package(fairy_meadows_package)
booking_system.add_package(hunza_valley_package)

# List all available packages
booking_system.list_packages()

# Example of booking a package
try:
    booking_system.book_package("Fairy Meadows Adventure")
except ValueError as e:
    print(e)
```
