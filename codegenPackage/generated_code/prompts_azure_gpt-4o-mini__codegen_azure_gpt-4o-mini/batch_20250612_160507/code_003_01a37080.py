"""
Generated Code Metadata:
========================
Original URL: https://appbalancer.pages.dev
Prompt: Develop a script that lists delivery areas for a takeaway service, inspired by the delivery areas mentioned for Rob N Roll in Kirkcudbright and Auchenlarie.
Generated: DETERMINISTIC_01a370802b211ab3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class DeliveryArea:
    """Class to represent a delivery area for the takeaway service."""
    
    def __init__(self, name: str, postal_code: str):
        """
        Initialize a new DeliveryArea instance.

        Args:
            name (str): The name of the delivery area.
            postal_code (str): The postal code for the delivery area.
        """
        self.name = name
        self.postal_code = postal_code

    def to_dict(self) -> Dict[str, str]:
        """Convert the DeliveryArea instance to a dictionary."""
        return {
            "name": self.name,
            "postal_code": self.postal_code
        }

class DeliveryService:
    """Class to manage delivery areas for the takeaway service."""
    
    def __init__(self):
        """Initialize the DeliveryService with an empty list of delivery areas."""
        self.delivery_areas: List[DeliveryArea] = []

    def add_delivery_area(self, name: str, postal_code: str):
        """
        Add a new delivery area to the service.

        Args:
            name (str): The name of the delivery area.
            postal_code (str): The postal code for the delivery area.
        """
        if not name or not postal_code:
            raise ValueError("Both name and postal code must be provided.")
        
        area = DeliveryArea(name, postal_code)
        self.delivery_areas.append(area)

    def list_delivery_areas(self) -> List[Dict[str, str]]:
        """List all delivery areas in the service.

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing delivery areas.
        """
        return [area.to_dict() for area in self.delivery_areas]

    def save_delivery_areas(self, filename: str):
        """
        Save the delivery areas to a JSON file.

        Args:
            filename (str): The name of the file to save the delivery areas.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_delivery_areas(), file, indent=4)
        except IOError as e:
            print(f"Error saving delivery areas to {filename}: {e}")

def main():
    """Main function to run the delivery service script."""
    service = DeliveryService()
    
    # Adding delivery areas inspired by Rob N Roll
    try:
        service.add_delivery_area("Kirkcudbright", "DG6 4JH")
        service.add_delivery_area("Auchenlarie", "DG6 4TQ")
    except ValueError as e:
        print(f"Error adding delivery area: {e}")

    # List and print delivery areas
    areas = service.list_delivery_areas()
    print("Delivery Areas:")
    for area in areas:
        print(f"{area['name']} - {area['postal_code']}")

    # Save delivery areas to a file
    service.save_delivery_areas("delivery_areas.json")

if __name__ == "__main__":
    main()
```
