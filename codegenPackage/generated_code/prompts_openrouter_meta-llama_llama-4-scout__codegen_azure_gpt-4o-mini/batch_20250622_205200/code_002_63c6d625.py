"""
Generated Code Metadata:
========================
Original URL: https://www.betterbooking.pk
Prompt: "Recommend a suitable library for managing tour packages, considering the features offered by Better Booking's domestic and international tours."
Generated: DETERMINISTIC_63c6d6256c5c2909
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tour_package_manager.py

"""
Tour Package Manager

This module provides a class to manage tour packages, including domestic and international tours.
It allows for adding, removing, and listing tour packages, as well as searching for specific packages.
"""

class TourPackage:
    """
    Represents a tour package with details such as destination, price, and duration.
    """

    def __init__(self, name, destination, price, duration):
        """
        Initializes a new tour package.

        :param name: str - The name of the tour package
        :param destination: str - The destination of the tour
        :param price: float - The price of the tour package
        :param duration: int - The duration of the tour in days
        """
        self.name = name
        self.destination = destination
        self.price = price
        self.duration = duration

    def __repr__(self):
        return f"TourPackage(name={self.name}, destination={self.destination}, price={self.price}, duration={self.duration})"


class TourPackageManager:
    """
    Manages a collection of tour packages.
    """

    def __init__(self):
        """Initializes the TourPackageManager with an empty list of packages."""
        self.packages = []

    def add_package(self, package):
        """
        Adds a new tour package to the manager.

        :param package: TourPackage - The tour package to add
        :raises ValueError: If the package is not an instance of TourPackage
        """
        if not isinstance(package, TourPackage):
            raise ValueError("Only instances of TourPackage can be added.")
        self.packages.append(package)

    def remove_package(self, package_name):
        """
        Removes a tour package by name.

        :param package_name: str - The name of the tour package to remove
        :raises ValueError: If the package is not found
        """
        for package in self.packages:
            if package.name == package_name:
                self.packages.remove(package)
                return
        raise ValueError(f"Package '{package_name}' not found.")

    def list_packages(self):
        """
        Lists all tour packages.

        :return: list - A list of all tour packages
        """
        return self.packages

    def find_package(self, package_name):
        """
        Finds a tour package by name.

        :param package_name: str - The name of the tour package to find
        :return: TourPackage - The found tour package
        :raises ValueError: If the package is not found
        """
        for package in self.packages:
            if package.name == package_name:
                return package
        raise ValueError(f"Package '{package_name}' not found.")


# Example usage
if __name__ == "__main__":
    try:
        manager = TourPackageManager()
        
        # Adding tour packages
        manager.add_package(TourPackage("Beach Getaway", "Hawaii", 1200.00, 7))
        manager.add_package(TourPackage("Cultural Tour", "Italy", 1500.00, 10))
        
        # Listing all packages
        print("Available Tour Packages:")
        for pkg in manager.list_packages():
            print(pkg)

        # Finding a specific package
        print("\nFinding 'Beach Getaway':")
        print(manager.find_package("Beach Getaway"))

        # Removing a package
        manager.remove_package("Cultural Tour")
        print("\nPackages after removal:")
        print(manager.list_packages())

    except ValueError as e:
        print(f"Error: {e}")
```
