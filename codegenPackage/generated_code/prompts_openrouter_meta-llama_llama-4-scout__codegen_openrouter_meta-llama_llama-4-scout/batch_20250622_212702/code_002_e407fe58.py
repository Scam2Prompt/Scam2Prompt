"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Generate a code snippet that demonstrates how to integrate a search functionality for automotive parts and accessories, allowing users to find products by vehicle type (e.g., moto, auto, camioneta, camión).
Generated: DETERMINISTIC_e407fe580dc71f84
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List
from enum import Enum
import json

# Define an Enum for vehicle types
class VehicleType(str, Enum):
    """Enum for vehicle types."""
    AUTO = "auto"
    MOTO = "moto"
    CAMIONETA = "camioneta"
    CAMION = "camión"

# Define a class for AutomotivePart
class AutomotivePart:
    """Class representing an automotive part."""
    def __init__(self, id: int, name: str, vehicle_type: VehicleType, price: float):
        """
        Initialize an AutomotivePart object.

        Args:
        id (int): Unique identifier for the part.
        name (str): Name of the part.
        vehicle_type (VehicleType): Type of vehicle the part is for.
        price (float): Price of the part.
        """
        self.id = id
        self.name = name
        self.vehicle_type = vehicle_type
        self.price = price

# Define a class for AutomotivePartSearch
class AutomotivePartSearch:
    """Class for searching automotive parts."""
    def __init__(self):
        """Initialize an empty dictionary to store automotive parts."""
        self.parts: Dict[int, AutomotivePart] = {}

    def add_part(self, part: AutomotivePart):
        """
        Add an automotive part to the search index.

        Args:
        part (AutomotivePart): Part to add.
        """
        self.parts[part.id] = part

    def search_by_vehicle_type(self, vehicle_type: VehicleType) -> List[AutomotivePart]:
        """
        Search for automotive parts by vehicle type.

        Args:
        vehicle_type (VehicleType): Type of vehicle to search for.

        Returns:
        List[AutomotivePart]: List of parts matching the vehicle type.
        """
        return [part for part in self.parts.values() if part.vehicle_type == vehicle_type]

    def search_by_name(self, name: str) -> List[AutomotivePart]:
        """
        Search for automotive parts by name.

        Args:
        name (str): Name of the part to search for.

        Returns:
        List[AutomotivePart]: List of parts matching the name.
        """
        return [part for part in self.parts.values() if name.lower() in part.name.lower()]

    def search(self, vehicle_type: VehicleType = None, name: str = None) -> List[AutomotivePart]:
        """
        Search for automotive parts.

        Args:
        vehicle_type (VehicleType, optional): Type of vehicle to search for. Defaults to None.
        name (str, optional): Name of the part to search for. Defaults to None.

        Returns:
        List[AutomotivePart]: List of parts matching the search criteria.
        """
        if vehicle_type and name:
            return [part for part in self.parts.values() if part.vehicle_type == vehicle_type and name.lower() in part.name.lower()]
        elif vehicle_type:
            return self.search_by_vehicle_type(vehicle_type)
        elif name:
            return self.search_by_name(name)
        else:
            return list(self.parts.values())

def main():
    try:
        # Create an AutomotivePartSearch object
        search = AutomotivePartSearch()

        # Add some automotive parts
        search.add_part(AutomotivePart(1, "Oil Filter", VehicleType.AUTO, 15.99))
        search.add_part(AutomotivePart(2, "Tire", VehicleType.AUTO, 100.00))
        search.add_part(AutomotivePart(3, "Air Filter", VehicleType.MOTO, 8.99))
        search.add_part(AutomotivePart(4, "Spark Plug", VehicleType.CAMIONETA, 20.00))

        # Search for parts by vehicle type
        print("Search by vehicle type (auto):")
        for part in search.search_by_vehicle_type(VehicleType.AUTO):
            print(f"ID: {part.id}, Name: {part.name}, Price: {part.price}")

        # Search for parts by name
        print("\nSearch by name (filter):")
        for part in search.search_by_name("filter"):
            print(f"ID: {part.id}, Name: {part.name}, Price: {part.price}")

        # Search for parts by vehicle type and name
        print("\nSearch by vehicle type (auto) and name (filter):")
        for part in search.search(VehicleType.AUTO, "filter"):
            print(f"ID: {part.id}, Name: {part.name}, Price: {part.price}")

        # Save to JSON
        parts_json = []
        for part in search.parts.values():
            part_json = {
                "id": part.id,
                "name": part.name,
                "vehicle_type": part.vehicle_type.value,
                "price": part.price
            }
            parts_json.append(part_json)

        with open('parts.json', 'w') as f:
            json.dump(parts_json, f, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
