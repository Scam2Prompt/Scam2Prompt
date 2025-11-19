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
# outdoor_advertising_manager.py

class AdvertisingLocation:
    """Represents an outdoor advertising location."""

    def __init__(self, location_id, name, measure, price):
        """
        Initializes an AdvertisingLocation object.

        Args:
            location_id (int): Unique identifier for the location.
            name (str): Name of the advertising location.
            measure (str): Measure of the advertising location (e.g., "1x2 meters").
            price (float): Price of the advertising location.
        """
        self.location_id = location_id
        self.name = name
        self.measure = measure
        self.price = price

    def __str__(self):
        return f"Location ID: {self.location_id}, Name: {self.name}, Measure: {self.measure}, Price: ${self.price:.2f}"


class AdvertisingManager:
    """Manages outdoor advertising locations."""

    def __init__(self):
        """Initializes an AdvertisingManager object."""
        self.locations = {}

    def add_location(self, location):
        """
        Adds an advertising location to the manager.

        Args:
            location (AdvertisingLocation): The location to add.

        Raises:
            ValueError: If a location with the same ID already exists.
        """
        if location.location_id in self.locations:
            raise ValueError("Location with the same ID already exists.")
        self.locations[location.location_id] = location

    def remove_location(self, location_id):
        """
        Removes an advertising location from the manager.

        Args:
            location_id (int): The ID of the location to remove.

        Raises:
            KeyError: If the location does not exist.
        """
        if location_id not in self.locations:
            raise KeyError("Location does not exist.")
        del self.locations[location_id]

    def update_location(self, location_id, name=None, measure=None, price=None):
        """
        Updates an advertising location.

        Args:
            location_id (int): The ID of the location to update.
            name (str, optional): New name for the location. Defaults to None.
            measure (str, optional): New measure for the location. Defaults to None.
            price (float, optional): New price for the location. Defaults to None.

        Raises:
            KeyError: If the location does not exist.
        """
        if location_id not in self.locations:
            raise KeyError("Location does not exist.")
        location = self.locations[location_id]
        if name:
            location.name = name
        if measure:
            location.measure = measure
        if price:
            location.price = price

    def get_location(self, location_id):
        """
        Retrieves an advertising location.

        Args:
            location_id (int): The ID of the location to retrieve.

        Returns:
            AdvertisingLocation: The advertising location.

        Raises:
            KeyError: If the location does not exist.
        """
        if location_id not in self.locations:
            raise KeyError("Location does not exist.")
        return self.locations[location_id]

    def list_locations(self):
        """Returns a list of all advertising locations."""
        return list(self.locations.values())


def main():
    # Create an advertising manager
    manager = AdvertisingManager()

    # Create some advertising locations
    location1 = AdvertisingLocation(1, "Location 1", "1x2 meters", 1000.0)
    location2 = AdvertisingLocation(2, "Location 2", "2x3 meters", 2000.0)

    # Add locations to the manager
    manager.add_location(location1)
    manager.add_location(location2)

    # List all locations
    print("All Locations:")
    for location in manager.list_locations():
        print(location)

    # Update a location
    manager.update_location(1, price=1500.0)
    print("\nUpdated Location:")
    print(manager.get_location(1))

    # Remove a location
    manager.remove_location(2)

    # Try to retrieve a removed location
    try:
        manager.get_location(2)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
