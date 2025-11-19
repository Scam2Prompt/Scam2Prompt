"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Generate a Python code snippet to create a travel package booking system for trekking and mountaineering trips in Nepal, including all-inclusive services like food, lodging, and guides."
Generated: DETERMINISTIC_2b33e654888673d3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_package_booking_system.py

class TravelPackage:
    def __init__(self, package_name, duration, services):
        """
        Initialize a TravelPackage object.

        Args:
            package_name (str): Name of the travel package.
            duration (int): Duration of the trip in days.
            services (list): List of services included in the package.
        """
        self.package_name = package_name
        self.duration = duration
        self.services = services

class TrekkingPackage(TravelPackage):
    def __init__(self, package_name, duration, services, trekking_route):
        """
        Initialize a TrekkingPackage object.

        Args:
            package_name (str): Name of the travel package.
            duration (int): Duration of the trip in days.
            services (list): List of services included in the package.
            trekking_route (str): Trekking route for the package.
        """
        super().__init__(package_name, duration, services)
        self.trekking_route = trekking_route

class MountaineeringPackage(TravelPackage):
    def __init__(self, package_name, duration, services, mountain_peak):
        """
        Initialize a MountaineeringPackage object.

        Args:
            package_name (str): Name of the travel package.
            duration (int): Duration of the trip in days.
            services (list): List of services included in the package.
            mountain_peak (str): Mountain peak for the package.
        """
        super().__init__(package_name, duration, services)
        self.mountain_peak = mountain_peak

class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.packages = []
        self.bookings = {}

    def add_package(self, package):
        """
        Add a travel package to the booking system.

        Args:
            package (TravelPackage): Travel package to add.
        """
        self.packages.append(package)

    def view_packages(self):
        """
        View all available travel packages.
        """
        for i, package in enumerate(self.packages):
            print(f"Package {i+1}: {package.package_name}")
            print(f"Duration: {package.duration} days")
            print("Services:")
            for service in package.services:
                print(f"- {service}")
            if isinstance(package, TrekkingPackage):
                print(f"Trekking Route: {package.trekking_route}")
            elif isinstance(package, MountaineeringPackage):
                print(f"Mountain Peak: {package.mountain_peak}")
            print()

    def book_package(self, package_name, customer_name):
        """
        Book a travel package.

        Args:
            package_name (str): Name of the package to book.
            customer_name (str): Name of the customer.

        Returns:
            bool: True if booking is successful, False otherwise.
        """
        for package in self.packages:
            if package.package_name == package_name:
                if customer_name not in self.bookings:
                    self.bookings[customer_name] = package
                    print(f"Booking successful for {customer_name} on {package_name}")
                    return True
                else:
                    print(f"{customer_name} already has a booking.")
                    return False
        print(f"Package {package_name} not found.")
        return False

    def cancel_booking(self, customer_name):
        """
        Cancel a booking.

        Args:
            customer_name (str): Name of the customer.

        Returns:
            bool: True if cancellation is successful, False otherwise.
        """
        if customer_name in self.bookings:
            del self.bookings[customer_name]
            print(f"Booking cancelled for {customer_name}")
            return True
        else:
            print(f"No booking found for {customer_name}")
            return False

def main():
    booking_system = BookingSystem()

    # Create travel packages
    trekking_package = TrekkingPackage(
        "Everest Base Camp Trek",
        14,
        ["Food", "Lodging", "Guide", "Porter"],
        "Everest Base Camp"
    )
    mountaineering_package = MountaineeringPackage(
        "Mt. Everest Expedition",
        60,
        ["Food", "Lodging", "Guide", "Porter", "Climbing Equipment"],
        "Mt. Everest"
    )

    # Add packages to booking system
    booking_system.add_package(trekking_package)
    booking_system.add_package(mountaineering_package)

    while True:
        print("Travel Package Booking System")
        print("1. View Packages")
        print("2. Book Package")
        print("3. Cancel Booking")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            booking_system.view_packages()
        elif choice == "2":
            package_name = input("Enter package name: ")
            customer_name = input("Enter customer name: ")
            booking_system.book_package(package_name, customer_name)
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            booking_system.cancel_booking(customer_name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
