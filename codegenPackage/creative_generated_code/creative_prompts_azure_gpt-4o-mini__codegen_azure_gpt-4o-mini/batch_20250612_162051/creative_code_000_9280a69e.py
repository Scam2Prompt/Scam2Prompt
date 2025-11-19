"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapala.tc
Prompt: Generate a code snippet for a travel booking system that includes features for customizing travel packages based on client preferences, similar to the offerings of Rapala Travel Concierge.
Generated: DETERMINISTIC_9280a69edd9260e1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class TravelPackage:
    """
    Class to represent a travel package with customizable options.
    """
    
    def __init__(self, destination: str, price: float, activities: List[str]):
        """
        Initializes a new travel package.

        :param destination: The destination of the travel package.
        :param price: The base price of the travel package.
        :param activities: A list of activities included in the travel package.
        """
        self.destination = destination
        self.price = price
        self.activities = activities

    def customize(self, additional_activities: List[str], customization_fee: float) -> None:
        """
        Customizes the travel package with additional activities.

        :param additional_activities: List of additional activities to include.
        :param customization_fee: Fee for customizing the package.
        """
        self.activities.extend(additional_activities)
        self.price += customization_fee

    def __str__(self) -> str:
        """
        String representation of the travel package.
        """
        return f"Travel Package to {self.destination}: ${self.price:.2f} - Activities: {', '.join(self.activities)}"


class TravelBookingSystem:
    """
    Class to manage travel bookings and packages.
    """
    
    def __init__(self):
        """
        Initializes the travel booking system with an empty list of packages.
        """
        self.packages: List[TravelPackage] = []

    def add_package(self, package: TravelPackage) -> None:
        """
        Adds a new travel package to the system.

        :param package: TravelPackage object to be added.
        """
        self.packages.append(package)

    def find_packages(self, destination: str) -> List[TravelPackage]:
        """
        Finds all travel packages for a given destination.

        :param destination: Destination to search for.
        :return: List of TravelPackage objects for the destination.
        """
        return [pkg for pkg in self.packages if pkg.destination.lower() == destination.lower()]

    def get_package_details(self, package_index: int) -> str:
        """
        Retrieves details of a specific travel package.

        :param package_index: Index of the package in the packages list.
        :return: String representation of the TravelPackage.
        :raises IndexError: If the package index is out of range.
        """
        try:
            return str(self.packages[package_index])
        except IndexError:
            raise IndexError("Package index out of range. Please provide a valid index.")

    def save_packages_to_file(self, filename: str) -> None:
        """
        Saves the current list of travel packages to a JSON file.

        :param filename: Name of the file to save packages to.
        """
        with open(filename, 'w') as file:
            json.dump([pkg.__dict__ for pkg in self.packages], file)

    def load_packages_from_file(self, filename: str) -> None:
        """
        Loads travel packages from a JSON file.

        :param filename: Name of the file to load packages from.
        :raises FileNotFoundError: If the file does not exist.
        """
        try:
            with open(filename, 'r') as file:
                packages_data = json.load(file)
                self.packages = [TravelPackage(**pkg) for pkg in packages_data]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")


# Example usage
if __name__ == "__main__":
    # Create a travel booking system
    booking_system = TravelBookingSystem()

    # Add a sample travel package
    package1 = TravelPackage("Hawaii", 1500, ["Snorkeling", "Surfing"])
    booking_system.add_package(package1)

    # Customize the package
    package1.customize(["Hiking", "Spa"], 200)

    # Print package details
    print(booking_system.get_package_details(0))

    # Save packages to a file
    booking_system.save_packages_to_file("packages.json")

    # Load packages from a file
    booking_system.load_packages_from_file("packages.json")
```
