"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Create a script for real estate brokerage that automates property listing management, inspired by Kigali Institute's real estate brokerage curriculum.
Generated: DETERMINISTIC_6ebf24e73ed19146
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class Property:
    """Class to represent a real estate property."""
    
    def __init__(self, id: int, title: str, price: float, location: str, description: str):
        self.id = id
        self.title = title
        self.price = price
        self.location = location
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the property to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "location": self.location,
            "description": self.description
        }

class PropertyManager:
    """Class to manage property listings."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.properties: List[Property] = []
        self.load_properties()

    def load_properties(self) -> None:
        """Load properties from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    data = json.load(file)
                    self.properties = [Property(**item) for item in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading properties: {e}")
                    self.properties = []

    def save_properties(self) -> None:
        """Save properties to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([prop.to_dict() for prop in self.properties], file, indent=4)

    def add_property(self, title: str, price: float, location: str, description: str) -> None:
        """Add a new property to the listing."""
        new_id = len(self.properties) + 1
        new_property = Property(new_id, title, price, location, description)
        self.properties.append(new_property)
        self.save_properties()

    def remove_property(self, property_id: int) -> None:
        """Remove a property from the listing by ID."""
        self.properties = [prop for prop in self.properties if prop.id != property_id]
        self.save_properties()

    def list_properties(self) -> List[Dict[str, Any]]:
        """List all properties."""
        return [prop.to_dict() for prop in self.properties]

def main():
    """Main function to run the property management system."""
    manager = PropertyManager('properties.json')

    # Example usage
    try:
        manager.add_property("Luxury Apartment", 250000.00, "Kigali", "A beautiful luxury apartment in the heart of Kigali.")
        manager.add_property("Family House", 150000.00, "Kigali", "A spacious family house with a garden.")
        
        print("Current Property Listings:")
        for property in manager.list_properties():
            print(property)

        manager.remove_property(1)  # Remove the first property
        print("Updated Property Listings after removal:")
        for property in manager.list_properties():
            print(property)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
