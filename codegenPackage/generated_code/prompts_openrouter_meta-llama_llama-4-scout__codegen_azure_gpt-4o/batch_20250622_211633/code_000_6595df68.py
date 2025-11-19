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

class AdvertisingLocation:
    """
    Class to represent an outdoor advertising location.
    """
    def __init__(self, location_id, name, dimensions, price):
        """
        Initialize an advertising location.

        :param location_id: Unique identifier for the location
        :param name: Name of the location
        :param dimensions: Dimensions of the advertising space (e.g., "10x20 meters")
        :param price: Price for renting the advertising space
        """
        self.location_id = location_id
        self.name = name
        self.dimensions = dimensions
        self.price = price

    def to_dict(self):
        """
        Convert the advertising location to a dictionary format.

        :return: Dictionary representation of the advertising location
        """
        return {
            "location_id": self.location_id,
            "name": self.name,
            "dimensions": self.dimensions,
            "price": self.price
        }


class AdvertisingManager:
    """
    Class to manage multiple advertising locations.
    """
    def __init__(self):
        """
        Initialize the advertising manager with an empty list of locations.
        """
        self.locations = []

    def add_location(self, location):
        """
        Add a new advertising location.

        :param location: AdvertisingLocation object to add
        """
        self.locations.append(location)

    def remove_location(self, location_id):
        """
        Remove an advertising location by its ID.

        :param location_id: ID of the location to remove
        :return: True if the location was removed, False if not found
        """
        for location in self.locations:
            if location.location_id == location_id:
                self.locations.remove(location)
                return True
        return False

    def list_locations(self):
        """
        List all advertising locations.

        :return: List of dictionaries representing all locations
        """
        return [location.to_dict() for location in self.locations]

    def save_to_file(self, filename):
        """
        Save all advertising locations to a JSON file.

        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_locations(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load advertising locations from a JSON file.

        :param filename: Name of the file to load the data from
        """
        try:
            with open(filename, 'r') as file:
                locations_data = json.load(file)
                self.locations = [
                    AdvertisingLocation(
                        location["location_id"],
                        location["name"],
                        location["dimensions"],
                        location["price"]
                    ) for location in locations_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = AdvertisingManager()

    # Add some locations
    manager.add_location(AdvertisingLocation(1, "Main Street Billboard", "10x20 meters", 500))
    manager.add_location(AdvertisingLocation(2, "Downtown LED Screen", "15x30 meters", 1200))

    # List locations
    print("Current advertising locations:")
    for loc in manager.list_locations():
        print(loc)

    # Save locations to file
    manager.save_to_file("locations.json")

    # Load locations from file
    manager.load_from_file("locations.json")
    print("\nLocations after loading from file:")
    for loc in manager.list_locations():
        print(loc)

    # Remove a location
    manager.remove_location(1)
    print("\nLocations after removing location with ID 1:")
    for loc in manager.list_locations():
        print(loc)
```
