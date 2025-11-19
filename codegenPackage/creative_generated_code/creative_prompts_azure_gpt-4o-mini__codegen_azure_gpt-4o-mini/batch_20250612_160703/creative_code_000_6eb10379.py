"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starke-orte.land
Prompt: How can I implement community-driven strategies for activating vacant properties in small towns, as discussed by the Starke Orte Netzwerk?
Generated: DETERMINISTIC_6eb1037914d03676
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# community_activation.py

import json
from typing import List, Dict, Any, Optional

class Property:
    """Class that represents a vacant property and its activation status."""
    
    def __init__(self, id: int, address: str, owner: str, activated: bool = False):
        self.id = id
        self.address = address
        self.owner = owner
        self.activated = activated

    def activate(self) -> None:
        """Activates the property."""
        self.activated = True


class CommunityActivation:
    """Class to manage the activation of vacant properties in the community."""

    def __init__(self):
        self.properties: List[Property] = []

    def add_property(self, property: Property) -> None:
        """Adds a new property to the list."""
        self.properties.append(property)

    def activate_property(self, property_id: int) -> Optional[str]:
        """Activates a property by its ID."""
        for property in self.properties:
            if property.id == property_id:
                property.activate()
                return f"Property at {property.address} activated successfully."
        return "Property not found."

    def save_to_file(self, filename: str) -> None:
        """Saves the properties to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([prop.__dict__ for prop in self.properties], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Loads properties from a JSON file."""
        try:
            with open(filename, 'r') as file:
                properties_data = json.load(file)
                self.properties = [Property(**data) for data in properties_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


def main():
    """Main function to run the community activation program."""
    community_activation = CommunityActivation()

    # Loading existing properties from file if it exists.
    community_activation.load_from_file('vacant_properties.json')

    # Assume we have some vacant properties to add
    community_activation.add_property(Property(1, '123 Main St', 'John Doe'))
    community_activation.add_property(Property(2, '456 Elm St', 'Jane Smith'))

    # Activating a property
    result = community_activation.activate_property(1)
    print(result)

    # Saving the updated properties to a file
    community_activation.save_to_file('vacant_properties.json')


if __name__ == "__main__":
    main()
```
