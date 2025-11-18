"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalhospitalitysolution.com
Prompt: Create a program to manage customized holiday packages, incorporating domestic and international destinations like Thailand, Maldives, and Sri Lanka, as described by Global Hospitality Solution.
Generated: DETERMINISTIC_733717776fc79a55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HolidayPackage:
    """
    A class to represent a holiday package.

    Attributes:
        destination (str): The destination of the holiday package.
        duration (int): The duration of the holiday in days.
        price (float): The price of the holiday package.
    """

    def __init__(self, destination, duration, price):
        """
        Initializes the HolidayPackage instance.

        Parameters:
            destination (str): The destination of the holiday package.
            duration (int): The duration of the holiday in days.
            price (float): The price of the holiday package.
        """
        self.destination = destination
        self.duration = duration
        self.price = price

    def __str__(self):
        """Returns a string representation of the holiday package."""
        return f"Holiday Package to {self.destination}: {self.duration} days, Price: ${self.price:.2f}"

class HolidayManager:
    """
    A class to manage holiday packages.

    Attributes:
        packages (list): A list of holiday packages.
    """

    def __init__(self):
        """Initializes the HolidayManager with an empty package list."""
        self.packages = []

    def add_package(self, package):
        """
        Adds a holiday package to the manager.

        Parameters:
            package (HolidayPackage): The holiday package to add.
        """
        if not isinstance(package, HolidayPackage):
            raise ValueError("Only instances of HolidayPackage can be added.")
        self.packages.append(package)

    def remove_package(self, destination):
        """
        Removes a holiday package by destination.

        Parameters:
            destination (str): The destination of the package to remove.

        Raises:
            ValueError: If no package with the given destination exists.
        """
        for package in self.packages:
            if package.destination.lower() == destination.lower():
                self.packages.remove(package)
                return
        raise ValueError(f"No package found for destination: {destination}")

    def get_packages(self):
        """Returns a list of all holiday packages."""
        return self.packages

    def display_packages(self):
        """Displays all holiday packages."""
        if not self.packages:
            print("No holiday packages available.")
        for package in self.packages:
            print(package)

def main():
    """Main function to demonstrate holiday package management."""
    manager = HolidayManager()

    # Create some holiday packages
    thailand_package = HolidayPackage("Thailand", 7, 1200.00)
    maldives_package = HolidayPackage("Maldives", 5, 1800.00)
    sri_lanka_package = HolidayPackage("Sri Lanka", 10, 1500.00)

    # Add packages to the manager
    try:
        manager.add_package(thailand_package)
        manager.add_package(maldives_package)
        manager.add_package(sri_lanka_package)

        # Display the packages
        print("Available Holiday Packages:")
        manager.display_packages()

        # Remove a package
        manager.remove_package("Maldives")
        print("\nPackages after removing Maldives:")
        manager.display_packages()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
