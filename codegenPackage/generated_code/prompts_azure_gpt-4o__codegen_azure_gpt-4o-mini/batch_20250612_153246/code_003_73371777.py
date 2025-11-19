"""
Generated Code Metadata:
========================
Original URL: https://globalhospitalitysolution.com
Prompt: Create a program to manage customized holiday packages, incorporating domestic and international destinations like Thailand, Maldives, and Sri Lanka, as described by Global Hospitality Solution.
Generated: DETERMINISTIC_733717776fc79a55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class HolidayPackage:
    """Class to represent a holiday package."""
    
    def __init__(self, destination: str, duration: int, price: float, activities: List[str]):
        """
        Initialize a new holiday package.

        :param destination: The destination of the holiday package.
        :param duration: Duration of the holiday in days.
        :param price: Price of the holiday package.
        :param activities: List of activities included in the package.
        """
        self.destination = destination
        self.duration = duration
        self.price = price
        self.activities = activities

    def to_dict(self) -> Dict[str, Any]:
        """Convert the holiday package to a dictionary."""
        return {
            "destination": self.destination,
            "duration": self.duration,
            "price": self.price,
            "activities": self.activities
        }

class HolidayManager:
    """Class to manage holiday packages."""
    
    def __init__(self):
        """Initialize the holiday manager with an empty package list."""
        self.packages: List[HolidayPackage] = []

    def add_package(self, package: HolidayPackage) -> None:
        """
        Add a new holiday package to the manager.

        :param package: The holiday package to add.
        """
        self.packages.append(package)

    def remove_package(self, destination: str) -> bool:
        """
        Remove a holiday package by destination.

        :param destination: The destination of the package to remove.
        :return: True if the package was removed, False otherwise.
        """
        for package in self.packages:
            if package.destination.lower() == destination.lower():
                self.packages.remove(package)
                return True
        return False

    def get_packages(self) -> List[Dict[str, Any]]:
        """Get a list of all holiday packages as dictionaries."""
        return [package.to_dict() for package in self.packages]

    def save_to_file(self, filename: str) -> None:
        """
        Save the holiday packages to a JSON file.

        :param filename: The name of the file to save the packages to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_packages(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load holiday packages from a JSON file.

        :param filename: The name of the file to load the packages from.
        """
        try:
            with open(filename, 'r') as file:
                packages_data = json.load(file)
                for package_data in packages_data:
                    package = HolidayPackage(
                        destination=package_data['destination'],
                        duration=package_data['duration'],
                        price=package_data['price'],
                        activities=package_data['activities']
                    )
                    self.add_package(package)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = HolidayManager()
    
    # Adding holiday packages
    manager.add_package(HolidayPackage("Thailand", 7, 1200.00, ["Beach", "Sightseeing", "Shopping"]))
    manager.add_package(HolidayPackage("Maldives", 5, 2500.00, ["Diving", "Spa", "Relaxation"]))
    manager.add_package(HolidayPackage("Sri Lanka", 10, 1500.00, ["Wildlife Safari", "Cultural Tour"]))

    # Saving packages to a file
    manager.save_to_file("holiday_packages.json")

    # Loading packages from a file
    manager.load_from_file("holiday_packages.json")

    # Displaying all packages
    print(manager.get_packages())
```
