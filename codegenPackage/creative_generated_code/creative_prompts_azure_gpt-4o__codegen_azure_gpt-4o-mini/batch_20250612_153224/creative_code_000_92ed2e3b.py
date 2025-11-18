"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Write Python code to create a digital catalog system for managing tourism packages, including destinations like Turkey, Greece, Jordan, Egypt, and Morocco, as described on Skyline International Agent's website.
Generated: DETERMINISTIC_92ed2e3b8a831777
Batch ID: 20250612_153224
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

class TourismPackage:
    """
    Represents a tourism package with relevant details.
    """
    def __init__(self, destination: str, description: str, price: float, duration: int):
        self.destination = destination
        self.description = description
        self.price = price
        self.duration = duration

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the TourismPackage instance to a dictionary representation.
        """
        return {
            'destination': self.destination,
            'description': self.description,
            'price': self.price,
            'duration': self.duration
        }

class Catalog:
    """
    Represents a digital catalog for tourism packages.
    """
    def __init__(self):
        self.packages = []  # List to store tourism packages

    def add_package(self, package: TourismPackage):
        """
        Adds a new tourism package to the catalog.
        """
        self.packages.append(package)
        print(f"Added package: {package.destination}")

    def remove_package(self, destination: str):
        """
        Removes a tourism package from the catalog by destination.
        """
        before_count = len(self.packages)
        self.packages = [pkg for pkg in self.packages if pkg.destination != destination]
        after_count = len(self.packages)
        if before_count == after_count:
            print(f"No package found for destination: {destination}")
        else:
            print(f"Removed package for destination: {destination}")

    def get_package(self, destination: str) -> Dict[str, Any]:
        """
        Retrieves a tourism package by destination.
        Returns the package as a dictionary if found, else None.
        """
        for pkg in self.packages:
            if pkg.destination == destination:
                return pkg.to_dict()
        print(f"No package found for destination: {destination}")
        return None

    def save_to_file(self, filename: str):
        """
        Saves the catalog of packages to a JSON file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([pkg.to_dict() for pkg in self.packages], file, indent=4)
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to {filename}: {e}")

    def load_from_file(self, filename: str):
        """
        Loads the catalog of packages from a JSON file.
        """
        try:
            with open(filename, 'r') as file:
                packages = json.load(file)
                self.packages = [TourismPackage(**pkg) for pkg in packages]
            print(f"Catalog loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from {filename}: {e}")

# Example usage of the Catalog class
if __name__ == "__main__":
    catalog = Catalog()

    # Add tourism packages
    catalog.add_package(TourismPackage("Turkey", "Explore the rich history of Turkey.", 1200.50, 7))
    catalog.add_package(TourismPackage("Greece", "Enjoy the sunny beaches and ancient ruins.", 1500.00, 10))
    catalog.add_package(TourismPackage("Jordan", "Visit the stunning Petra and the Dead Sea.", 1300.75, 5))
    catalog.add_package(TourismPackage("Egypt", "Experience the pyramids and the Nile.", 1600.00, 8))
    catalog.add_package(TourismPackage("Morocco", "Explore the vibrant markets and deserts.", 1400.00, 6))

    # Save catalog to file
    catalog.save_to_file('tourism_catalog.json')

    # Load catalog from file
    catalog.load_from_file('tourism_catalog.json')

    # Retrieve a specific package
    package = catalog.get_package("Greece")
    print(f"Retrieved Package: {package}")

    # Remove a package
    catalog.remove_package("Jordan")
```
