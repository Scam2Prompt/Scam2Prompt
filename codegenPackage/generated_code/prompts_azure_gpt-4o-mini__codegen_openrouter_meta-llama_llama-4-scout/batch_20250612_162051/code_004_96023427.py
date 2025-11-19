"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Illustrate how to implement a search feature in a web application that filters properties based on criteria such as price and location, specifically for the Corfu Coastal Collection.
Generated: DETERMINISTIC_96023427add285fa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# properties.py

from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Property:
    id: int
    name: str
    price: float
    location: str

class PropertyFilter:
    def __init__(self, properties: List[Property]):
        """
        Initialize the PropertyFilter with a list of properties.

        Args:
        properties (List[Property]): A list of Property objects.
        """
        self.properties = properties

    def filter_by_price(self, min_price: float = None, max_price: float = None) -> List[Property]:
        """
        Filter properties by price.

        Args:
        min_price (float): The minimum price (inclusive). Defaults to None.
        max_price (float): The maximum price (inclusive). Defaults to None.

        Returns:
        List[Property]: A list of properties that match the price criteria.
        """
        return [p for p in self.properties if (min_price is None or p.price >= min_price) and (max_price is None or p.price <= max_price)]

    def filter_by_location(self, location: str) -> List[Property]:
        """
        Filter properties by location.

        Args:
        location (str): The location to filter by.

        Returns:
        List[Property]: A list of properties that match the location criteria.
        """
        return [p for p in self.properties if location.lower() in p.location.lower()]

    def search(self, min_price: float = None, max_price: float = None, location: str = None) -> List[Property]:
        """
        Search properties by price and location.

        Args:
        min_price (float): The minimum price (inclusive). Defaults to None.
        max_price (float): The maximum price (inclusive). Defaults to None.
        location (str): The location to filter by. Defaults to None.

        Returns:
        List[Property]: A list of properties that match the search criteria.
        """
        filtered_properties = self.properties

        if min_price is not None or max_price is not None:
            filtered_properties = self.filter_by_price(min_price, max_price)

        if location is not None:
            filtered_properties = self.filter_by_location(location)

        return filtered_properties


class CorfuCoastalCollection:
    def __init__(self):
        """
        Initialize the CorfuCoastalCollection with sample properties.
        """
        self.properties = [
            Property(1, "Villa Corfu", 500000.0, "Corfu, Greece"),
            Property(2, "Apartment Paleokastritsa", 200000.0, "Paleokastritsa, Corfu, Greece"),
            Property(3, "House Sidari", 350000.0, "Sidari, Corfu, Greece"),
            Property(4, "Studio Kassiopi", 150000.0, "Kassiopi, Corfu, Greece"),
            Property(5, "Mansion Dassia", 800000.0, "Dassia, Corfu, Greece"),
        ]

    def get_property_filter(self) -> PropertyFilter:
        """
        Get a PropertyFilter instance for the Corfu Coastal Collection.

        Returns:
        PropertyFilter: A PropertyFilter instance.
        """
        return PropertyFilter(self.properties)


def main():
    collection = CorfuCoastalCollection()
    property_filter = collection.get_property_filter()

    try:
        # Example usage: Search for properties in Corfu with a price between 200000 and 500000
        results = property_filter.search(min_price=200000.0, max_price=500000.0, location="Corfu")

        print("Search results:")
        for prop in results:
            print(f"ID: {prop.id}, Name: {prop.name}, Price: {prop.price}, Location: {prop.location}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
