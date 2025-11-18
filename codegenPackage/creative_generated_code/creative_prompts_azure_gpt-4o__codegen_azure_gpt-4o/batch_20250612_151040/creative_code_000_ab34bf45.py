"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Write a Python script to create a booking system for travel packages like "Top Casamance" and "Cap-Vert" offered by FODYEM, including pricing in FCFA and package descriptions.
Generated: DETERMINISTIC_ab34bf45ca411af6
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TravelPackage:
    """
    Class representing a travel package.
    """
    def __init__(self, name, description, price):
        """
        Constructor to initialize a travel package with name, description, and price.
        :param name: Name of the travel package
        :param description: Description of the package
        :param price: Price of the package in FCFA
        """
        self.name = name
        self.description = description
        self.price = price

    def display_details(self):
        """
        Method to display package details.
        :return: None
        """
        print(f"Package Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price} FCFA")
        print("-" * 40)


class BookingSystem:
    """
    Class representing the booking system for travel packages.
    """
    def __init__(self):
        """
        Constructor to initialize an empty list of travel packages.
        """
        self.packages = []

    def add_package(self, package):
        """
        Method to add a travel package to the system.
        :param package: Instance of TravelPackage
        :return: None
        """
        self.packages.append(package)

    def list_packages(self):
        """
        Method to list all available travel packages.
        :return: None
        """
        if not self.packages:
            print("No travel packages available.")
            print("-" * 40)
        else:
            print("Available Travel Packages:")
            print("=" * 40)
            for package in self.packages:
                package.display_details()

    def book_package(self, package_name):
        """
        Method to book a travel package by name.
        :param package_name: Name of the package to book
        :return: None
        """
        for package in self.packages:
            if package.name.lower() == package_name.lower():
                print(f"You have successfully booked the '{package.name}' package!")
                print("-" * 40)
                return
        print(f"Error: Package '{package_name}' not found.")
        print("-" * 40)


def main():
    """
    Main function to run the booking system.
    :return: None
    """
    try:
        # Initialize booking system
        system = BookingSystem()

        # Add travel packages
        system.add_package(TravelPackage(
            name="Top Casamance",
            description="Explore the serene and beautiful region of Casamance.",
            price=150000
        ))
        system.add_package(TravelPackage(
            name="Cap-Vert",
            description="Discover the stunning coastal attractions of Cap-Vert.",
            price=100000
        ))

        while True:
            # Display menu
            print("Welcome to FODYEM Travel Booking System!")
            print("1. List Travel Packages")
            print("2. Book a Package")
            print("3. Exit")
            print("=" * 40)

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                # List all available packages
                system.list_packages()
            elif choice == "2":
                # Book a package
                package_name = input("Enter the name of the package to book: ")
                system.book_package(package_name)
            elif choice == "3":
                # Exit the program
                print("Thank you for using the booking system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                print("-" * 40)
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
```
