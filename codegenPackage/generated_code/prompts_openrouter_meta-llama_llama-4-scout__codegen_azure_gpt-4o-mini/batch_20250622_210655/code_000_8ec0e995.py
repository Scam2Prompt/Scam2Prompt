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
from typing import List, Dict, Optional

class Property:
    """Class to represent a real estate property."""
    
    def __init__(self, id: int, property_type: str, location: str, price: float, status: str):
        """
        Initialize a new property.

        :param id: Unique identifier for the property
        :param property_type: Type of the property (e.g., 'apartment', 'house')
        :param location: Location of the property
        :param price: Price of the property
        :param status: Status of the property (e.g., 'for sale', 'for rent')
        """
        self.id = id
        self.property_type = property_type
        self.location = location
        self.price = price
        self.status = status

    def to_dict(self) -> Dict:
        """Convert the property to a dictionary."""
        return {
            "id": self.id,
            "property_type": self.property_type,
            "location": self.location,
            "price": self.price,
            "status": self.status
        }

class PropertyManager:
    """Class to manage a collection of properties."""
    
    def __init__(self):
        """Initialize the property manager with an empty property list."""
        self.properties: List[Property] = []

    def add_property(self, property: Property) -> None:
        """Add a new property to the manager.

        :param property: Property object to be added
        """
        self.properties.append(property)

    def search_properties(self, location: Optional[str] = None, property_type: Optional[str] = None) -> List[Dict]:
        """Search for properties by location and/or property type.

        :param location: Location to filter properties
        :param property_type: Type of property to filter
        :return: List of properties matching the search criteria
        """
        results = self.properties
        if location:
            results = [p for p in results if p.location.lower() == location.lower()]
        if property_type:
            results = [p for p in results if p.property_type.lower() == property_type.lower()]
        return [p.to_dict() for p in results]

    def load_properties(self, file_path: str) -> None:
        """Load properties from a JSON file.

        :param file_path: Path to the JSON file containing properties
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    property = Property(**item)
                    self.add_property(property)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_properties(self, file_path: str) -> None:
        """Save properties to a JSON file.

        :param file_path: Path to the JSON file to save properties
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([p.to_dict() for p in self.properties], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving properties: {e}")

# Example usage
if __name__ == "__main__":
    manager = PropertyManager()
    
    # Load properties from a JSON file
    manager.load_properties('properties.json')
    
    # Add a new property
    new_property = Property(id=1, property_type='apartment', location='Neiva', price=50000, status='for rent')
    manager.add_property(new_property)
    
    # Search for properties
    results = manager.search_properties(location='Neiva', property_type='apartment')
    print("Search Results:", results)
    
    # Save properties back to a JSON file
    manager.save_properties('properties.json')
```
