"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: Write Python code to create a digital catalog system for managing tourism packages, including destinations like Turkey, Greece, Jordan, Egypt, and Morocco, as described on Skyline International Agent's website.
Generated: DETERMINISTIC_92ed2e3b8a831777
Batch ID: 20250612_153224
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

class TourismPackage:
    """Class to represent a tourism package."""
    
    def __init__(self, destination: str, description: str, price: float, duration: int):
        """
        Initialize a new tourism package.

        :param destination: The destination of the package.
        :param description: A brief description of the package.
        :param price: The price of the package.
        :param duration: The duration of the package in days.
        """
        self.destination = destination
        self.description = description
        self.price = price
        self.duration = duration

    def to_dict(self) -> Dict[str, Any]:
        """Convert the package to a dictionary for easy serialization."""
        return {
            "destination": self.destination,
            "description": self.description,
            "price": self.price,
            "duration": self.duration
        }

class Catalog:
    """Class to manage a collection of tourism packages."""
    
    def __init__(self):
        """Initialize an empty catalog."""
        self.packages: List[TourismPackage] = []

    def add_package(self, package: TourismPackage) -> None:
        """Add a new tourism package to the catalog.

        :param package: The tourism package to add.
        """
        self.packages.append(package)

    def remove_package(self, destination: str) -> bool:
        """Remove a tourism package from the catalog by destination.

        :param destination: The destination of the package to remove.
        :return: True if the package was removed, False if not found.
        """
        for package in self.packages:
            if package.destination.lower() == destination.lower():
                self.packages.remove(package)
                return True
        return False

    def find_package(self, destination: str) -> TourismPackage:
        """Find a tourism package by destination.

        :param destination: The destination to search for.
        :return: The found tourism package or None if not found.
        """
        for package in self.packages:
            if package.destination.lower() == destination.lower():
                return package
        return None

    def list_packages(self) -> List[Dict[str, Any]]:
        """List all tourism packages in the catalog.

        :return: A list of dictionaries representing the packages.
        """
        return [package.to_dict() for package in self.packages]

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_packages(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file.

        :param filename: The name of the file to load the catalog from.
        """
        try:
            with open(filename, 'r') as file:
                packages = json.load(file)
                for pkg in packages:
                    self.add_package(TourismPackage(**pkg))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    catalog = Catalog()
    
    # Adding tourism packages
    catalog.add_package(TourismPackage("Turkey", "Explore the rich history and culture of Turkey.", 1200.00, 7))
    catalog.add_package(TourismPackage("Greece", "Enjoy the beautiful islands and ancient ruins.", 1500.00, 10))
    catalog.add_package(TourismPackage("Jordan", "Visit the ancient city of Petra and the Dead Sea.", 1300.00, 5))
    catalog.add_package(TourismPackage("Egypt", "Discover the wonders of the Pyramids and Nile.", 1400.00, 8))
    catalog.add_package(TourismPackage("Morocco", "Experience the vibrant culture and landscapes of Morocco.", 1100.00, 6))

    # Listing all packages
    print("Tourism Packages:")
    for package in catalog.list_packages():
        print(package)

    # Saving to file
    catalog.save_to_file("tourism_catalog.json")

    # Loading from file
    new_catalog = Catalog()
    new_catalog.load_from_file("tourism_catalog.json")
    print("\nLoaded Packages:")
    for package in new_catalog.list_packages():
        print(package)
```
