"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Generate a Python script to manage real estate properties, including apartments and houses for rent or sale in Neiva, Huila, Colombia, with features for search by location and property type."
Generated: DETERMINISTIC_8ec0e99522165c20
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

class Property:
    """
    Represents a real estate property.
    """
    def __init__(self, property_id, title, property_type, location, price, status):
        """
        Initialize a property instance.

        :param property_id: Unique identifier for the property
        :param title: Title or name of the property
        :param property_type: Type of property (e.g., 'Apartment', 'House')
        :param location: Location of the property (e.g., 'Neiva, Huila, Colombia')
        :param price: Price of the property
        :param status: Status of the property ('For Rent' or 'For Sale')
        """
        self.property_id = property_id
        self.title = title
        self.property_type = property_type
        self.location = location
        self.price = price
        self.status = status

    def to_dict(self):
        """
        Convert the property instance to a dictionary.

        :return: Dictionary representation of the property
        """
        return {
            "property_id": self.property_id,
            "title": self.title,
            "property_type": self.property_type,
            "location": self.location,
            "price": self.price,
            "status": self.status
        }


class PropertyManager:
    """
    Manages a collection of real estate properties.
    """
    def __init__(self):
        """
        Initialize the property manager with an empty list of properties.
        """
        self.properties = []

    def add_property(self, property):
        """
        Add a new property to the collection.

        :param property: Property instance to add
        """
        self.properties.append(property)

    def search_properties(self, location=None, property_type=None):
        """
        Search for properties based on location and/or property type.

        :param location: Location to filter properties (optional)
        :param property_type: Property type to filter properties (optional)
        :return: List of properties matching the search criteria
        """
        results = self.properties
        if location:
            results = [p for p in results if location.lower() in p.location.lower()]
        if property_type:
            results = [p for p in results if property_type.lower() == p.property_type.lower()]
        return results

    def save_to_file(self, filename):
        """
        Save the properties to a JSON file.

        :param filename: Name of the file to save properties
        """
        try:
            with open(filename, 'w') as file:
                json.dump([p.to_dict() for p in self.properties], file, indent=4)
            print(f"Properties saved to {filename}")
        except Exception as e:
            print(f"Error saving properties to file: {e}")

    def load_from_file(self, filename):
        """
        Load properties from a JSON file.

        :param filename: Name of the file to load properties from
        """
        try:
            with open(filename, 'r') as file:
                properties_data = json.load(file)
                self.properties = [Property(**data) for data in properties_data]
            print(f"Properties loaded from {filename}")
        except Exception as e:
            print(f"Error loading properties from file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the property manager
    manager = PropertyManager()

    # Add some properties
    manager.add_property(Property(1, "Modern Apartment", "Apartment", "Neiva, Huila, Colombia", 500, "For Rent"))
    manager.add_property(Property(2, "Family House", "House", "Neiva, Huila, Colombia", 120000, "For Sale"))
    manager.add_property(Property(3, "Luxury Apartment", "Apartment", "Bogotá, Colombia", 800, "For Rent"))

    # Search properties in Neiva
    print("Properties in Neiva:")
    for prop in manager.search_properties(location="Neiva"):
        print(prop.to_dict())

    # Search apartments
    print("\nApartments:")
    for prop in manager.search_properties(property_type="Apartment"):
        print(prop.to_dict())

    # Save properties to a file
    manager.save_to_file("properties.json")

    # Load properties from a file
    manager.load_from_file("properties.json")
```
