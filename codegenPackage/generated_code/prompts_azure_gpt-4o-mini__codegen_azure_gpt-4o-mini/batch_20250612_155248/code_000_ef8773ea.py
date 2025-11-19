"""
Generated Code Metadata:
========================
Original URL: https://localtravelcoupons.com
Prompt: Generate a code snippet for a travel booking application that allows users to customize travel packages based on their budget, similar to the services offered by Local Travel Coupons.
Generated: DETERMINISTIC_ef8773ea265bbaa2
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TravelPackage:
    """Class to represent a travel package."""
    
    def __init__(self, destination, price, activities):
        """
        Initialize a travel package.

        Args:
            destination (str): The destination of the travel package.
            price (float): The price of the travel package.
            activities (list): List of activities included in the package.
        """
        self.destination = destination
        self.price = price
        self.activities = activities

    def __str__(self):
        """Return a string representation of the travel package."""
        return f"Destination: {self.destination}, Price: ${self.price}, Activities: {', '.join(self.activities)}"


class TravelBooking:
    """Class to manage travel bookings."""
    
    def __init__(self):
        """Initialize the travel booking system with an empty package list."""
        self.packages = []

    def add_package(self, package):
        """
        Add a travel package to the booking system.

        Args:
            package (TravelPackage): The travel package to add.
        """
        if not isinstance(package, TravelPackage):
            raise ValueError("Invalid package. Must be an instance of TravelPackage.")
        self.packages.append(package)

    def find_packages_by_budget(self, budget):
        """
        Find travel packages within a specified budget.

        Args:
            budget (float): The budget to filter packages.

        Returns:
            list: List of travel packages within the budget.
        """
        if budget < 0:
            raise ValueError("Budget must be a non-negative value.")
        
        return [pkg for pkg in self.packages if pkg.price <= budget]


def load_packages_from_file(file_path):
    """
    Load travel packages from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing travel packages.

    Returns:
        list: List of TravelPackage instances.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [TravelPackage(pkg['destination'], pkg['price'], pkg['activities']) for pkg in data]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError("Error: The file content is not valid JSON.") from e


def main():
    """Main function to run the travel booking application."""
    booking_system = TravelBooking()

    # Load packages from a JSON file
    try:
        packages = load_packages_from_file('travel_packages.json')
        for package in packages:
            booking_system.add_package(package)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    # User input for budget
    try:
        budget = float(input("Enter your budget: "))
        available_packages = booking_system.find_packages_by_budget(budget)

        if available_packages:
            print("Available travel packages within your budget:")
            for pkg in available_packages:
                print(pkg)
        else:
            print("No packages available within your budget.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the budget.")


if __name__ == "__main__":
    main()
```
