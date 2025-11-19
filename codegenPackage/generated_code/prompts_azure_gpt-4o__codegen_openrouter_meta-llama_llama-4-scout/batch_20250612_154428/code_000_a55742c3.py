"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Write a Python script to filter rental properties in Gurugram from a dataset based on criteria like location, price range, and amenities such as "high-speed WiFi" or "attached kitchen," as described on the Moms PG website.
Generated: DETERMINISTIC_a55742c372510073
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rental_property_filter.py

class RentalProperty:
    def __init__(self, location, price, amenities):
        """
        Initialize a RentalProperty object.

        Args:
            location (str): Location of the rental property.
            price (float): Price of the rental property.
            amenities (list): List of amenities available.
        """
        self.location = location
        self.price = price
        self.amenities = amenities


class RentalPropertyFilter:
    def __init__(self, properties):
        """
        Initialize a RentalPropertyFilter object.

        Args:
            properties (list): List of RentalProperty objects.
        """
        self.properties = properties

    def filter_by_location(self, location):
        """
        Filter properties by location.

        Args:
            location (str): Location to filter by.

        Returns:
            list: List of RentalProperty objects matching the location.
        """
        return [prop for prop in self.properties if prop.location.lower() == location.lower()]

    def filter_by_price_range(self, min_price, max_price):
        """
        Filter properties by price range.

        Args:
            min_price (float): Minimum price.
            max_price (float): Maximum price.

        Returns:
            list: List of RentalProperty objects within the price range.
        """
        return [prop for prop in self.properties if min_price <= prop.price <= max_price]

    def filter_by_amenities(self, amenities):
        """
        Filter properties by amenities.

        Args:
            amenities (list): List of amenities to filter by.

        Returns:
            list: List of RentalProperty objects with matching amenities.
        """
        return [prop for prop in self.properties if all(amenity.lower() in [a.lower() for a in prop.amenities] for amenity in amenities)]

    def filter_properties(self, location=None, min_price=None, max_price=None, amenities=None):
        """
        Filter properties based on multiple criteria.

        Args:
            location (str, optional): Location to filter by. Defaults to None.
            min_price (float, optional): Minimum price. Defaults to None.
            max_price (float, optional): Maximum price. Defaults to None.
            amenities (list, optional): List of amenities to filter by. Defaults to None.

        Returns:
            list: List of RentalProperty objects matching the filter criteria.
        """
        filtered_properties = self.properties

        if location:
            filtered_properties = self.filter_by_location(location)
        if min_price and max_price:
            filtered_properties = self.filter_by_price_range(min_price, max_price)
        if amenities:
            filtered_properties = self.filter_by_amenities(amenities)

        return filtered_properties


def main():
    # Sample dataset
    properties = [
        RentalProperty("Gurugram", 10000, ["high-speed WiFi", "attached kitchen"]),
        RentalProperty("Gurugram", 8000, ["high-speed WiFi"]),
        RentalProperty("Noida", 12000, ["attached kitchen", "gym"]),
        RentalProperty("Gurugram", 9000, ["high-speed WiFi", "attached kitchen", "gym"]),
    ]

    filter = RentalPropertyFilter(properties)

    try:
        location = "Gurugram"
        min_price = 8000
        max_price = 10000
        amenities = ["high-speed WiFi", "attached kitchen"]

        filtered_properties = filter.filter_properties(location, min_price, max_price, amenities)

        print("Filtered Properties:")
        for prop in filtered_properties:
            print(f"Location: {prop.location}, Price: {prop.price}, Amenities: {prop.amenities}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
