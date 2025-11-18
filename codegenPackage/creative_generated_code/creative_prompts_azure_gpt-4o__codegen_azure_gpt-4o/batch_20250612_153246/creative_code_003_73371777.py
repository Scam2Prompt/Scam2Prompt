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
"""
Holiday Package Management System
This program allows users to manage customized holiday packages, incorporating domestic and international destinations.
Destinations include Thailand, Maldives, and Sri Lanka as international options, and customizable domestic options.
"""

# Import necessary modules
import datetime


class Destination:
    """Class to represent a destination."""

    def __init__(self, name, location_type, price_per_day):
        """
        Initialize a destination instance.
        :param name: Name of the destination (e.g., "Thailand").
        :param location_type: Type of the destination ("International" or "Domestic").
        :param price_per_day: Cost per day for the destination.
        """
        self.name = name
        self.location_type = location_type
        self.price_per_day = price_per_day

    def __str__(self):
        """Return a string representation of the destination."""
        return f"{self.name} ({self.location_type}) - ${self.price_per_day}/day"


class HolidayPackage:
    """Class to represent a holiday package."""

    def __init__(self, destination, days, customer_name):
        """
        Initialize a holiday package instance.
        :param destination: Destination object.
        :param days: Number of days for the holiday package.
        :param customer_name: Name of the customer booking the package.
        """
        self.destination = destination
        self.days = days
        self.customer_name = customer_name
        self.booking_date = datetime.datetime.now()

    def calculate_total_cost(self):
        """
        Calculate the total cost of the holiday package.
        :return: Total cost as a float.
        """
        return self.destination.price_per_day * self.days

    def __str__(self):
        """Return a string representation of the holiday package."""
        return (
            f"Holiday Package for {self.customer_name}:\n"
            f"Destination: {self.destination}\n"
            f"Days: {self.days}\n"
            f"Booking Date: {self.booking_date.strftime('%Y-%m-%d')}\n"
            f"Total Cost: ${self.calculate_total_cost():.2f}\n"
        )


class HolidayPackageManager:
    """Class to manage holiday packages."""

    def __init__(self):
        """
        Initialize the manager with a list of predefined destinations.
        """
        self.destinations = [
            Destination("Thailand", "International", 200),
            Destination("Maldives", "International", 250),
            Destination("Sri Lanka", "International", 150),
        ]
        self.packages = []

    def add_destination(self, name, location_type, price_per_day):
        """
        Add a new destination.
        :param name: Name of the destination.
        :param location_type: Type of the destination ("International" or "Domestic").
        :param price_per_day: Cost per day for the destination.
        :return: None
        """
        self.destinations.append(Destination(name, location_type, price_per_day))
        print(f"Destination {name} added successfully.")

    def list_destinations(self):
        """List all available destinations."""
        print("Available Destinations:")
        for idx, destination in enumerate(self.destinations, start=1):
            print(f"{idx}. {destination}")

    def create_package(self, destination_index, days, customer_name):
        """
        Create a holiday package for a customer.
        :param destination_index: Index of the destination from the list.
        :param days: Number of days for the holiday package.
        :param customer_name: Name of the customer.
        :return: None
        """
        try:
            destination = self.destinations[destination_index - 1]
            package = HolidayPackage(destination, days, customer_name)
            self.packages.append(package)
            print(f"Package created successfully for {customer_name}.")
        except IndexError:
            print("Error: Invalid destination index.")
        except ValueError:
            print("Error: Invalid input.")

    def list_packages(self):
        """List all holiday packages."""
        print("Holiday Packages:")
        if not self.packages:
            print("No packages created yet.")
        for package in self.packages:
            print(package)

    def delete_package(self, customer_name):
        """
        Delete a holiday package for a customer.
        :param customer_name: Name of the customer.
        :return: None
        """
        for package in self.packages:
            if package.customer_name == customer_name:
                self.packages.remove(package)
                print(f"Package for {customer_name} deleted successfully.")
                return
        print(f"No package found for {customer_name}.")


def main():
    """Main function to interact with the HolidayPackageManager."""
    manager = HolidayPackageManager()

    while True:
        print("\nHoliday Package Management System")
        print("1. List Destinations")
        print("2. Add Destination")
        print("3. Create Package")
        print("4. List Packages")
        print("5. Delete Package")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.list_destinations()
        elif choice == "2":
            name = input("Enter destination name: ")
            location_type = input("Enter location type (International/Domestic): ")
            try:
                price_per_day = float(input("Enter price per day: "))
                manager.add_destination(name, location_type, price_per_day)
            except ValueError:
                print("Error: Invalid price entered.")
        elif choice == "3":
            manager.list_destinations()
            try:
                destination_index = int(input("Enter destination index: "))
                days = int(input("Enter number of days: "))
                customer_name = input("Enter customer name: ")
                manager.create_package(destination_index, days, customer_name)
            except ValueError:
                print("Error: Invalid input.")
        elif choice == "4":
            manager.list_packages()
        elif choice == "5":
            customer_name = input("Enter customer name: ")
            manager.delete_package(customer_name)
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")


# Entry point for the program
if __name__ == "__main__":
    main()
```
