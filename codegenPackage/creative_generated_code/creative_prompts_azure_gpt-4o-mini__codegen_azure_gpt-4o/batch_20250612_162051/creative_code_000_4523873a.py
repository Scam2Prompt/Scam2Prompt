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
import datetime

class TourPackage:
    """
    Represents a tour package with its details.
    """
    def __init__(self, name, destination, price_per_person, start_date, end_date):
        self.name = name
        self.destination = destination
        self.price_per_person = price_per_person
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return (f"Package: {self.name}\n"
                f"Destination: {self.destination}\n"
                f"Price per Person: ${self.price_per_person}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                f"End Date: {self.end_date.strftime('%Y-%m-%d')}")


class TravelBookingSystem:
    """
    A simple travel booking system to manage tour packages.
    """
    def __init__(self):
        self.packages = []

    def add_package(self, package):
        """
        Adds a new tour package to the system.
        :param package: TourPackage object
        """
        if not isinstance(package, TourPackage):
            raise TypeError("Expected a TourPackage object")
        self.packages.append(package)

    def list_packages(self):
        """
        Lists all available tour packages.
        """
        if not self.packages:
            print("No packages available at the moment.")
        else:
            for idx, package in enumerate(self.packages, start=1):
                print(f"\nPackage {idx}:\n{package}")

    def book_package(self, package_name, number_of_people):
        """
        Books a tour package based on the name.
        :param package_name: Name of the tour package
        :param number_of_people: Number of people for the booking
        """
        for package in self.packages:
            if package.name.lower() == package_name.lower():
                total_cost = package.price_per_person * number_of_people
                print(f"Successfully booked '{package.name}' for {number_of_people} people.")
                print(f"Total Cost: ${total_cost}")
                return
        print(f"Package '{package_name}' not found. Please check the name and try again.")


# Main execution
if __name__ == "__main__":
    # Create the travel booking system
    booking_system = TravelBookingSystem()

    # Define tour packages
    fairy_meadows_package = TourPackage(
        name="Fairy Meadows Adventure",
        destination="Fairy Meadows, Pakistan",
        price_per_person=150,
        start_date=datetime.datetime(2024, 5, 10),
        end_date=datetime.datetime(2024, 5, 15)
    )

    hunza_valley_package = TourPackage(
        name="Hunza Valley Retreat",
        destination="Hunza Valley, Pakistan",
        price_per_person=200,
        start_date=datetime.datetime(2024, 6, 20),
        end_date=datetime.datetime(2024, 6, 25)
    )

    # Add packages to the system
    booking_system.add_package(fairy_meadows_package)
    booking_system.add_package(hunza_valley_package)

    # List available packages
    print("Available Tour Packages:")
    booking_system.list_packages()

    # Example booking
    print("\nBooking a package:")
    booking_system.book_package("Fairy Meadows Adventure", 3)
```
