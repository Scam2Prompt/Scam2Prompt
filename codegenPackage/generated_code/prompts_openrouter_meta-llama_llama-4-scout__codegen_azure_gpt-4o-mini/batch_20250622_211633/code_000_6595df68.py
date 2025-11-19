"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Write a Python script to manage outdoor advertising locations, including their measures and prices, similar to the services offered by WOW MEDIA in Honduras."
Generated: DETERMINISTIC_6595df684aa2074d
Batch ID: 20250622_211633
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

class AdvertisingLocation:
    """Class to represent an outdoor advertising location."""
    
    def __init__(self, name: str, dimensions: str, price: float):
        """
        Initialize an advertising location.

        :param name: Name of the advertising location
        :param dimensions: Dimensions of the advertising space (e.g., '10x20')
        :param price: Price for renting the advertising space
        """
        self.name = name
        self.dimensions = dimensions
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the AdvertisingLocation instance to a dictionary."""
        return {
            'name': self.name,
            'dimensions': self.dimensions,
            'price': self.price
        }

class AdvertisingManager:
    """Class to manage a collection of advertising locations."""
    
    def __init__(self):
        """Initialize the advertising manager with an empty list of locations."""
        self.locations: List[AdvertisingLocation] = []

    def add_location(self, location: AdvertisingLocation):
        """Add a new advertising location to the manager.

        :param location: An instance of AdvertisingLocation to add
        """
        self.locations.append(location)

    def remove_location(self, name: str):
        """Remove an advertising location by name.

        :param name: The name of the advertising location to remove
        :raises ValueError: If the location is not found
        """
        for location in self.locations:
            if location.name == name:
                self.locations.remove(location)
                return
        raise ValueError(f"Location '{name}' not found.")

    def get_locations(self) -> List[Dict[str, Any]]:
        """Get a list of all advertising locations as dictionaries."""
        return [location.to_dict() for location in self.locations]

    def save_to_file(self, filename: str):
        """Save the advertising locations to a JSON file.

        :param filename: The name of the file to save the data
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_locations(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load advertising locations from a JSON file.

        :param filename: The name of the file to load the data from
        :raises IOError: If there is an error reading the file
        :raises json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(filename, 'r') as file:
                locations_data = json.load(file)
                for location_data in locations_data:
                    location = AdvertisingLocation(
                        name=location_data['name'],
                        dimensions=location_data['dimensions'],
                        price=location_data['price']
                    )
                    self.add_location(location)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate the AdvertisingManager functionality."""
    manager = AdvertisingManager()

    # Adding some advertising locations
    manager.add_location(AdvertisingLocation("Location A", "10x20", 150.0))
    manager.add_location(AdvertisingLocation("Location B", "15x30", 250.0))

    # Saving locations to a file
    manager.save_to_file("advertising_locations.json")

    # Loading locations from a file
    manager.load_from_file("advertising_locations.json")

    # Displaying all locations
    print("Current Advertising Locations:")
    for location in manager.get_locations():
        print(location)

if __name__ == "__main__":
    main()
```
