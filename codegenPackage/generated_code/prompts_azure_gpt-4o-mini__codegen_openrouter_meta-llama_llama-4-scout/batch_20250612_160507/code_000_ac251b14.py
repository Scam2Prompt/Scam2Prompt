"""
Generated Code Metadata:
========================
Original URL: https://aavego.dk
Prompt: Generate a code snippet for a booking system that integrates with a holiday architecture site like House Aavego in Thy, Denmark, focusing on unique features like private courtyards.
Generated: DETERMINISTIC_ac251b14c55d8de7
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json

class BookingSystem:
    def __init__(self):
        # Initialize an empty dictionary to store bookings
        self.bookings = {}

    def add_property(self, property_id, name, location, private_courtyard=False):
        """
        Add a property to the booking system.

        Args:
            property_id (str): Unique identifier for the property.
            name (str): Name of the property.
            location (str): Location of the property.
            private_courtyard (bool): Whether the property has a private courtyard. Defaults to False.
        """
        # Create a new property dictionary
        property_info = {
            "name": name,
            "location": location,
            "private_courtyard": private_courtyard,
            "availability": []
        }
        # Add the property to the bookings dictionary
        self.bookings[property_id] = property_info

    def remove_property(self, property_id):
        """
        Remove a property from the booking system.

        Args:
            property_id (str): Unique identifier for the property.

        Raises:
            KeyError: If the property does not exist in the booking system.
        """
        # Check if the property exists in the booking system
        if property_id not in self.bookings:
            raise KeyError(f"Property {property_id} does not exist")
        # Remove the property from the bookings dictionary
        del self.bookings[property_id]

    def add_availability(self, property_id, dates):
        """
        Add availability for a property.

        Args:
            property_id (str): Unique identifier for the property.
            dates (list): List of dates in the format "YYYY-MM-DD".

        Raises:
            KeyError: If the property does not exist in the booking system.
        """
        # Check if the property exists in the booking system
        if property_id not in self.bookings:
            raise KeyError(f"Property {property_id} does not exist")
        # Get the property information
        property_info = self.bookings[property_id]
        # Add the dates to the property's availability
        property_info["availability"].extend(dates)

    def book_property(self, property_id, dates):
        """
        Book a property for a set of dates.

        Args:
            property_id (str): Unique identifier for the property.
            dates (list): List of dates in the format "YYYY-MM-DD".

        Raises:
            KeyError: If the property does not exist in the booking system.
            ValueError: If any of the dates are not available.
        """
        # Check if the property exists in the booking system
        if property_id not in self.bookings:
            raise KeyError(f"Property {property_id} does not exist")
        # Get the property information
        property_info = self.bookings[property_id]
        # Check if all dates are available
        for date in dates:
            if date not in property_info["availability"]:
                raise ValueError(f"Date {date} is not available for property {property_id}")
        # Create a new booking
        booking_id = len(self.bookings[property_id].get("bookings", [])) + 1
        booking = {
            "id": booking_id,
            "dates": dates
        }
        # Add the booking to the property's bookings
        if "bookings" not in property_info:
            property_info["bookings"] = []
        property_info["bookings"].append(booking)

    def get_property_info(self, property_id):
        """
        Get information about a property.

        Args:
            property_id (str): Unique identifier for the property.

        Returns:
            dict: Property information.

        Raises:
            KeyError: If the property does not exist in the booking system.
        """
        # Check if the property exists in the booking system
        if property_id not in self.bookings:
            raise KeyError(f"Property {property_id} does not exist")
        # Return the property information
        return self.bookings[property_id]


def main():
    # Create a new booking system
    booking_system = BookingSystem()

    # Add properties
    booking_system.add_property("house1", "House 1", "Thy, Denmark", private_courtyard=True)
    booking_system.add_property("house2", "House 2", "Thy, Denmark")

    # Add availability
    booking_system.add_availability("house1", ["2024-09-16", "2024-09-17", "2024-09-18"])
    booking_system.add_availability("house2", ["2024-09-16", "2024-09-17"])

    # Book properties
    booking_system.book_property("house1", ["2024-09-16", "2024-09-17"])
    try:
        booking_system.book_property("house1", ["2024-09-18", "2024-09-19"])
    except ValueError as e:
        print(e)

    # Get property information
    print(json.dumps(booking_system.get_property_info("house1"), indent=4))


if __name__ == "__main__":
    main()
```
