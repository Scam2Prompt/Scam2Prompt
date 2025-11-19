"""
Generated Code Metadata:
========================
Original URL: https://balajitravelsonline.com
Prompt: Write a Python program to display a list of tour packages offered by Balaji Tours & Travels (e.g., Tirupathi, Sri Kalahasthi, Kerala) and allow users to select one to view more details.
Generated: DETERMINISTIC_85085e03cab6f413
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tour_packages.py

class TourPackage:
    def __init__(self, name, description, duration, price):
        """
        Initialize a TourPackage object.

        Args:
            name (str): Package name
            description (str): Package description
            duration (str): Package duration
            price (float): Package price
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, Duration: {self.duration}, Price: ${self.price:.2f}"


class TourPackages:
    def __init__(self):
        """
        Initialize a TourPackages object with a list of tour packages.
        """
        self.packages = [
            TourPackage("Tirupathi", "Visit the sacred Tirumala Venkateswara Temple", "2 days", 200.0),
            TourPackage("Sri Kalahasthi", "Explore the ancient Sri Kalahasthi Temple", "1 day", 150.0),
            TourPackage("Kerala", "Discover the natural beauty of Kerala's backwaters", "5 days", 800.0),
        ]

    def display_packages(self):
        """
        Display a list of tour packages.
        """
        print("Tour Packages:")
        for i, package in enumerate(self.packages, start=1):
            print(f"{i}. {package.name}")

    def get_package_details(self, package_index):
        """
        Get the details of a tour package.

        Args:
            package_index (int): Index of the package

        Returns:
            TourPackage: The selected tour package
        """
        try:
            package_index = int(package_index) - 1
            if package_index < 0 or package_index >= len(self.packages):
                raise ValueError
            return self.packages[package_index]
        except (ValueError, IndexError):
            print("Invalid package selection. Please try again.")
            return None


def main():
    tour_packages = TourPackages()

    while True:
        print("\nBalaji Tours & Travels")
        print("1. View Tour Packages")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tour_packages.display_packages()
            package_index = input("Enter the package number to view details: ")
            package = tour_packages.get_package_details(package_index)
            if package:
                print(f"\nPackage: {package.name}")
                print(f"Description: {package.description}")
                print(f"Duration: {package.duration}")
                print(f"Price: ${package.price:.2f}")
        elif choice == "2":
            print("Thank you for visiting Balaji Tours & Travels!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
