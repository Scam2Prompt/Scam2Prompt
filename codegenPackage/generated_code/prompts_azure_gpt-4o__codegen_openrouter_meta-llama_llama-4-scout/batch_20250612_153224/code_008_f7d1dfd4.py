"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write a program to track repair service areas and locations, referencing the multiple office locations listed by Geeks On Repair.
Generated: DETERMINISTIC_f7d1dfd43ced64fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# repair_service_tracker.py

class OfficeLocation:
    """Represents an office location with address and service area."""

    def __init__(self, name, address, city, state, zip_code, service_area):
        """
        Initializes an OfficeLocation object.

        Args:
            name (str): Office location name.
            address (str): Office location address.
            city (str): Office location city.
            state (str): Office location state.
            zip_code (str): Office location zip code.
            service_area (str): Service area covered by the office location.
        """
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.service_area = service_area

    def __str__(self):
        return f"{self.name} - {self.address}, {self.city}, {self.state} {self.zip_code}"


class RepairServiceTracker:
    """Tracks repair service areas and locations."""

    def __init__(self):
        self.office_locations = []

    def add_office_location(self, office_location):
        """
        Adds an office location to the tracker.

        Args:
            office_location (OfficeLocation): Office location to add.

        Raises:
            TypeError: If office_location is not an OfficeLocation object.
        """
        if not isinstance(office_location, OfficeLocation):
            raise TypeError("Invalid office location type")
        self.office_locations.append(office_location)

    def remove_office_location(self, office_location_name):
        """
        Removes an office location by name.

        Args:
            office_location_name (str): Name of the office location to remove.

        Raises:
            ValueError: If office location not found.
        """
        for location in self.office_locations:
            if location.name == office_location_name:
                self.office_locations.remove(location)
                return
        raise ValueError("Office location not found")

    def get_office_locations(self):
        """Returns a list of all office locations."""
        return self.office_locations

    def get_service_areas(self):
        """Returns a dictionary of service areas and their corresponding office locations."""
        service_areas = {}
        for location in self.office_locations:
            if location.service_area not in service_areas:
                service_areas[location.service_area] = []
            service_areas[location.service_area].append(location)
        return service_areas


def main():
    # Example usage:
    tracker = RepairServiceTracker()

    # Add office locations
    locations = [
        OfficeLocation("New York", "123 Main St", "New York", "NY", "10001", "Northeast"),
        OfficeLocation("Los Angeles", "456 Elm St", "Los Angeles", "CA", "90001", "West"),
        OfficeLocation("Chicago", "789 Oak St", "Chicago", "IL", "60001", "Midwest"),
        OfficeLocation("Houston", "321 Pine St", "Houston", "TX", "77001", "South"),
    ]
    for location in locations:
        tracker.add_office_location(location)

    # Print office locations
    print("Office Locations:")
    for location in tracker.get_office_locations():
        print(location)

    # Print service areas
    print("\nService Areas:")
    for service_area, locations in tracker.get_service_areas().items():
        print(f"{service_area}:")
        for location in locations:
            print(f"  - {location}")

    # Remove an office location
    tracker.remove_office_location("Los Angeles")

    # Print updated office locations
    print("\nUpdated Office Locations:")
    for location in tracker.get_office_locations():
        print(location)


if __name__ == "__main__":
    main()
```
