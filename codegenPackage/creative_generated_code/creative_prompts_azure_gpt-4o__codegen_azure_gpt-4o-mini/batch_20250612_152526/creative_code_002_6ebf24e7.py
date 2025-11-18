"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Create a script for real estate brokerage that automates property listing management, inspired by Kigali Institute's real estate brokerage curriculum.
Generated: DETERMINISTIC_6ebf24e73ed19146
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class Property:
    def __init__(self, id: int, title: str, price: float, location: str, description: str):
        self.id = id
        self.title = title
        self.price = price
        self.location = location
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert property instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "location": self.location,
            "description": self.description
        }

class PropertyManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.properties: List[Property] = []
        self.load_properties()

    def load_properties(self) -> None:
        """Load properties from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    properties_data = json.load(file)
                    self.properties = [Property(**data) for data in properties_data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading properties: {e}")
                self.properties = []

    def save_properties(self) -> None:
        """Save the current properties list to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([property.to_dict() for property in self.properties], file, indent=4)
        except IOError as e:
            print(f"Error saving properties: {e}")

    def add_property(self, title: str, price: float, location: str, description: str) -> None:
        """Add a new property to the list and save to file."""
        new_id = len(self.properties) + 1  # Simple ID generation
        new_property = Property(new_id, title, price, location, description)
        self.properties.append(new_property)
        self.save_properties()

    def remove_property(self, property_id: int) -> None:
        """Remove a property by ID and save to file."""
        self.properties = [prop for prop in self.properties if prop.id != property_id]
        self.save_properties()

    def list_properties(self) -> None:
        """Print all properties to the console."""
        if not self.properties:
            print("No properties available.")
            return
        
        for prop in self.properties:
            print(f"ID: {prop.id}, Title: {prop.title}, Price: ${prop.price:.2f}, Location: {prop.location}")

def main():
    """Main function to run the property management script."""
    manager = PropertyManager("properties.json")

    # Add example properties
    manager.add_property("Cozy Apartment", 120000.00, "Kigali City Center", "A cozy apartment in the heart of the city.")
    manager.add_property("Luxury Villa", 350000.00, "Kigali Hills", "A luxury villa with breathtaking views.")

    # List current properties
    print("Current property listings:")
    manager.list_properties()

    # Example of removing a property
    manager.remove_property(1)
    print("\nAfter removing a property:")
    manager.list_properties()

if __name__ == "__main__":
    main()
```
