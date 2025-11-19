"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: "Write a Python code snippet to create a digital catalog for a tourism company like Skyline International Agent, with sections for different tour packages and destinations."
Generated: DETERMINISTIC_e5ea52dd7a60972e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# catalog.py

class TourPackage:
    """Represents a tour package."""

    def __init__(self, name, description, price, duration):
        """
        Initializes a TourPackage.

        Args:
            name (str): Name of the tour package.
            description (str): Description of the tour package.
            price (float): Price of the tour package.
            duration (int): Duration of the tour package in days.
        """
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.description}, Price: ${self.price:.2f}, Duration: {self.duration} days"


class Destination:
    """Represents a destination."""

    def __init__(self, name, description):
        """
        Initializes a Destination.

        Args:
            name (str): Name of the destination.
            description (str): Description of the destination.
        """
        self.name = name
        self.description = description
        self.tour_packages = []

    def add_tour_package(self, tour_package):
        """
        Adds a tour package to the destination.

        Args:
            tour_package (TourPackage): Tour package to add.
        """
        self.tour_packages.append(tour_package)

    def __str__(self):
        return f"{self.name}: {self.description}"


class DigitalCatalog:
    """Represents a digital catalog."""

    def __init__(self):
        """Initializes a DigitalCatalog."""
        self.destinations = {}

    def add_destination(self, destination):
        """
        Adds a destination to the catalog.

        Args:
            destination (Destination): Destination to add.
        """
        self.destinations[destination.name] = destination

    def remove_destination(self, destination_name):
        """
        Removes a destination from the catalog.

        Args:
            destination_name (str): Name of the destination to remove.

        Raises:
            KeyError: If the destination does not exist.
        """
        if destination_name not in self.destinations:
            raise KeyError(f"Destination '{destination_name}' does not exist.")
        del self.destinations[destination_name]

    def print_catalog(self):
        """Prints the digital catalog."""
        for destination in self.destinations.values():
            print(destination)
            for tour_package in destination.tour_packages:
                print(f"  - {tour_package}")
            print()


def main():
    try:
        catalog = DigitalCatalog()

        # Create destinations
        paris = Destination("Paris", "The City of Light")
        rome = Destination("Rome", "The Eternal City")

        # Add destinations to catalog
        catalog.add_destination(paris)
        catalog.add_destination(rome)

        # Create tour packages
        paris_tour_package1 = TourPackage("Parisian Charm", "Explore the Eiffel Tower and Louvre.", 1000.0, 5)
        paris_tour_package2 = TourPackage("Parisian Delight", "Visit the Arc de Triomphe and Montmartre.", 800.0, 4)
        rome_tour_package1 = TourPackage("Roman Holiday", "Discover the Colosseum and Vatican City.", 1200.0, 6)
        rome_tour_package2 = TourPackage("Rome at Night", "Enjoy the Trevi Fountain and Italian cuisine.", 900.0, 3)

        # Add tour packages to destinations
        paris.add_tour_package(paris_tour_package1)
        paris.add_tour_package(paris_tour_package2)
        rome.add_tour_package(rome_tour_package1)
        rome.add_tour_package(rome_tour_package2)

        # Print catalog
        catalog.print_catalog()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
