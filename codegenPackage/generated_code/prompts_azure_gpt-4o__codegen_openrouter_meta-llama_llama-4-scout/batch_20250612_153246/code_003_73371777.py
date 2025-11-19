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
# holiday_package_manager.py

class Destination:
    """Represents a travel destination."""

    def __init__(self, name, location, description):
        """
        Initializes a Destination object.

        Args:
            name (str): Name of the destination.
            location (str): Location of the destination (e.g., country).
            description (str): Brief description of the destination.
        """
        self.name = name
        self.location = location
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.location}: {self.description}"


class HolidayPackage:
    """Represents a customized holiday package."""

    def __init__(self, package_name, destination, duration, price):
        """
        Initializes a HolidayPackage object.

        Args:
            package_name (str): Name of the holiday package.
            destination (Destination): Destination of the package.
            duration (int): Duration of the package in days.
            price (float): Price of the package.
        """
        self.package_name = package_name
        self.destination = destination
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"{self.package_name}: {self.destination}, Duration: {self.duration} days, Price: ${self.price:.2f}"


class PackageManager:
    """Manages customized holiday packages."""

    def __init__(self):
        self.packages = []
        self.destinations = []

    def add_destination(self, name, location, description):
        """
        Adds a new destination.

        Args:
            name (str): Name of the destination.
            location (str): Location of the destination.
            description (str): Brief description of the destination.
        """
        new_destination = Destination(name, location, description)
        self.destinations.append(new_destination)

    def add_package(self, package_name, destination_name, duration, price):
        """
        Adds a new holiday package.

        Args:
            package_name (str): Name of the holiday package.
            destination_name (str): Name of the destination.
            duration (int): Duration of the package in days.
            price (float): Price of the package.

        Raises:
            ValueError: If the destination does not exist.
        """
        destination = next((d for d in self.destinations if d.name == destination_name), None)
        if destination is None:
            raise ValueError(f"Destination '{destination_name}' does not exist.")

        new_package = HolidayPackage(package_name, destination, duration, price)
        self.packages.append(new_package)

    def get_packages(self):
        """Returns a list of all holiday packages."""
        return self.packages

    def get_destinations(self):
        """Returns a list of all destinations."""
        return self.destinations


def main():
    # Create a package manager
    manager = PackageManager()

    # Add destinations
    manager.add_destination("Bangkok", "Thailand", "Explore the city life.")
    manager.add_destination("Malé", "Maldives", "Relax on the beach.")
    manager.add_destination("Colombo", "Sri Lanka", "Discover the culture.")

    # Add holiday packages
    manager.add_package("Thailand Getaway", "Bangkok", 5, 800.0)
    manager.add_package("Maldives Relaxation", "Malé", 7, 1200.0)
    manager.add_package("Sri Lanka Adventure", "Colombo", 10, 1500.0)

    # Display destinations
    print("Destinations:")
    for i, destination in enumerate(manager.get_destinations(), start=1):
        print(f"{i}. {destination}")

    # Display holiday packages
    print("\nHoliday Packages:")
    for i, package in enumerate(manager.get_packages(), start=1):
        print(f"{i}. {package}")


if __name__ == "__main__":
    main()
```
