"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Write a code snippet to track and manage traffic fines and vehicle licensing for a property management company like Alphamor.
Generated: DETERMINISTIC_db63ff567d1a874e
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# traffic_fine_manager.py

from datetime import datetime
from typing import Dict, List

class Vehicle:
    """Represents a vehicle with its license plate and registration details."""

    def __init__(self, license_plate: str, registration_number: str):
        """
        Initializes a Vehicle object.

        Args:
        - license_plate (str): The vehicle's license plate number.
        - registration_number (str): The vehicle's registration number.
        """
        self.license_plate = license_plate
        self.registration_number = registration_number
        self.fines = []

    def add_fine(self, fine: Dict):
        """Adds a fine to the vehicle's fine record."""
        self.fines.append(fine)


class TrafficFineManager:
    """Manages traffic fines and vehicle licensing for a property management company."""

    def __init__(self):
        """Initializes a TrafficFineManager object."""
        self.vehicles = {}

    def add_vehicle(self, vehicle: Vehicle):
        """
        Adds a vehicle to the manager's records.

        Args:
        - vehicle (Vehicle): The vehicle to add.
        """
        self.vehicles[vehicle.license_plate] = vehicle

    def remove_vehicle(self, license_plate: str):
        """
        Removes a vehicle from the manager's records.

        Args:
        - license_plate (str): The license plate of the vehicle to remove.

        Raises:
        - KeyError: If the vehicle is not found in the records.
        """
        if license_plate not in self.vehicles:
            raise KeyError(f"Vehicle with license plate {license_plate} not found.")
        del self.vehicles[license_plate]

    def add_fine(self, license_plate: str, fine: Dict):
        """
        Adds a fine to a vehicle's record.

        Args:
        - license_plate (str): The license plate of the vehicle.
        - fine (Dict): The fine details.

        Raises:
        - KeyError: If the vehicle is not found in the records.
        """
        if license_plate not in self.vehicles:
            raise KeyError(f"Vehicle with license plate {license_plate} not found.")
        self.vehicles[license_plate].add_fine(fine)

    def get_vehicle_fines(self, license_plate: str) -> List[Dict]:
        """
        Retrieves a vehicle's fine records.

        Args:
        - license_plate (str): The license plate of the vehicle.

        Returns:
        - List[Dict]: A list of fine records for the vehicle.

        Raises:
        - KeyError: If the vehicle is not found in the records.
        """
        if license_plate not in self.vehicles:
            raise KeyError(f"Vehicle with license plate {license_plate} not found.")
        return self.vehicles[license_plate].fines


def main():
    # Example usage
    manager = TrafficFineManager()

    vehicle1 = Vehicle("ABC123", "REG12345")
    vehicle2 = Vehicle("XYZ789", "REG67890")

    manager.add_vehicle(vehicle1)
    manager.add_vehicle(vehicle2)

    fine1 = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": 100,
        "description": "Speeding offense"
    }

    fine2 = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": 200,
        "description": "Parking offense"
    }

    manager.add_fine("ABC123", fine1)
    manager.add_fine("XYZ789", fine2)

    print("Vehicle Fines:")
    for license_plate, vehicle in manager.vehicles.items():
        print(f"License Plate: {license_plate}")
        for fine in vehicle.fines:
            print(f"Date: {fine['date']}, Amount: {fine['amount']}, Description: {fine['description']}")
        print()

    try:
        manager.remove_vehicle("ABC123")
        print("Vehicle removed successfully.")
    except KeyError as e:
        print(e)

    try:
        manager.add_fine("DEF456", fine1)
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()
```
