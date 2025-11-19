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
import json
from typing import List, Dict, Optional

class TourPackage:
    """
    Represents a tour package with details like name, description, price, and duration.
    """
    def __init__(self, name: str, description: str, price: float, duration_days: int):
        self.name = name
        self.description = description
        self.price = price
        self.duration_days = duration_days

    def to_dict(self) -> Dict:
        """Convert TourPackage object to dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'duration_days': self.duration_days
        }

class Destination:
    """
    Represents a travel destination with packages available.
    """
    def __init__(self, name: str, description: str, packages: List[TourPackage]):
        self.name = name
        self.description = description
        self.packages = packages

    def to_dict(self) -> Dict:
        """Convert Destination object to dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'packages': [pkg.to_dict() for pkg in self.packages]
        }

class DigitalCatalog:
    """
    Main catalog class to manage destinations and packages.
    """
    def __init__(self):
        self.destinations: Dict[str, Destination] = {}

    def add_destination(self, destination: Destination) -> None:
        """Add a destination to the catalog."""
        if destination.name in self.destinations:
            raise ValueError(f"Destination '{destination.name}' already exists.")
        self.destinations[destination.name] = destination

    def remove_destination(self, destination_name: str) -> None:
        """Remove a destination from the catalog."""
        if destination_name not in self.destinations:
            raise ValueError(f"Destination '{destination_name}' not found.")
        del self.destinations[destination_name]

    def get_destination(self, destination_name: str) -> Optional[Destination]:
        """Get a destination by name."""
        return self.destinations.get(destination_name)

    def get_all_destinations(self) -> List[Dict]:
        """Get all destinations as a list of dictionaries."""
        return [dest.to_dict() for dest in self.destinations.values()]

    def save_to_file(self, filename: str) -> None:
        """Save catalog data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {
                        'destinations': [
                            dest.to_dict() for dest in self.destinations.values()
                        ]
                    },
                    f,
                    indent=4
                )
        except IOError as e:
            raise IOError(f"Error saving catalog: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load catalog data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.destinations = {}
                for dest_data in data['destinations']:
                    packages = [
                        TourPackage(
                            name=pkg['name'],
                            description=pkg['description'],
                            price=pkg['price'],
                            duration_days=pkg['duration_days']
                        ) for pkg in dest_data['packages']
                    ]
                    destination = Destination(
                        name=dest_data['name'],
                        description=dest_data['description'],
                        packages=packages
                    )
                    self.destinations[destination.name] = destination
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise IOError(f"Error loading catalog: {e}")

def sample_catalog() -> DigitalCatalog:
    """Create a sample catalog with demo data."""
    catalog = DigitalCatalog()

    # Europe Packages
    europe_packages = [
        TourPackage(
            name="European Highlights",
            description="7-day tour covering major European cities",
            price=1999.99,
            duration_days=7
        ),
        TourPackage(
            name="Mediterranean Cruise",
            description="10-day cruise around the Mediterranean",
            price=2999.99,
            duration_days=10
        )
    ]
    catalog.add_destination(Destination(
        name="Europe",
        description="Explore historic cities and beautiful landscapes",
        packages=europe_packages
    ))

    # Asia Packages
    asia_packages = [
        TourPackage(
            name="Asian Adventure",
            description="14-day tour through multiple Asian countries",
            price=2499.99,
            duration_days=14
        ),
        TourPackage(
            name="Japan Cultural Tour",
            description="8-day immersive Japanese culture experience",
            price=1799.99,
            duration_days=8
        )
    ]
    catalog.add_destination(Destination(
        name="Asia",
        description="Discover ancient cultures and modern metropolises",
        packages=asia_packages
    ))

    return catalog

if __name__ == "__main__":
    try:
        # Initialize and populate catalog
        catalog = sample_catalog()
        
        # Save to file
        catalog.save_to_file("skyline_catalog.json")
        print("Catalog saved successfully.")
        
        # Load from file
        new_catalog = DigitalCatalog()
        new_catalog.load_from_file("skyline_catalog.json")
        print("Catalog loaded successfully.")
        
        # Display all destinations
        print("\nAvailable Destinations:")
        for dest in new_catalog.get_all_destinations():
            print(f"\n{dest['name']}: {dest['description']}")
            print("Packages:")
            for pkg in dest['packages']:
                print(f"- {pkg['name']}: ${pkg['price']} ({pkg['duration_days']} days)")
                
    except Exception as e:
        print(f"Error: {e}")
```
