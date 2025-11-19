"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Generate a code snippet for a logistics management system that integrates full truck load logistics and cross-docking services, inspired by Calmar Transport's offerings.
Generated: DETERMINISTIC_925ddaae9d3f9d86
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logistics_management_system.py

from enum import Enum
from typing import Dict, List

class LogisticsService(Enum):
    """Enum for logistics services"""
    FULL_TRUCK_LOAD = 1
    CROSS_DOCKING = 2

class Location:
    """Class representing a location"""
    def __init__(self, city: str, state: str, zip_code: str):
        """
        Initialize a Location object

        Args:
        city (str): City of the location
        state (str): State of the location
        zip_code (str): Zip code of the location
        """
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.city}, {self.state} {self.zip_code}"

class Shipment:
    """Class representing a shipment"""
    def __init__(self, shipment_id: int, service: LogisticsService, 
                 origin: Location, destination: Location, 
                 weight: float, length: float, width: float, height: float):
        """
        Initialize a Shipment object

        Args:
        shipment_id (int): Unique ID of the shipment
        service (LogisticsService): Type of logistics service
        origin (Location): Origin location of the shipment
        destination (Location): Destination location of the shipment
        weight (float): Weight of the shipment in pounds
        length (float): Length of the shipment in inches
        width (float): Width of the shipment in inches
        height (float): Height of the shipment in inches
        """
        self.shipment_id = shipment_id
        self.service = service
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.dimensions = {
            "length": length,
            "width": width,
            "height": height
        }

    def __str__(self):
        return f"Shipment {self.shipment_id} - {self.service.name}"

class LogisticsManagementSystem:
    """Class representing a logistics management system"""
    def __init__(self):
        self.shipments: Dict[int, Shipment] = {}

    def create_shipment(self, shipment_id: int, service: LogisticsService, 
                       origin: Location, destination: Location, 
                       weight: float, length: float, width: float, height: float):
        """
        Create a new shipment

        Args:
        shipment_id (int): Unique ID of the shipment
        service (LogisticsService): Type of logistics service
        origin (Location): Origin location of the shipment
        destination (Location): Destination location of the shipment
        weight (float): Weight of the shipment in pounds
        length (float): Length of the shipment in inches
        width (float): Width of the shipment in inches
        height (float): Height of the shipment in inches

        Raises:
        ValueError: If shipment ID already exists
        """
        if shipment_id in self.shipments:
            raise ValueError("Shipment ID already exists")

        shipment = Shipment(shipment_id, service, origin, destination, 
                            weight, length, width, height)
        self.shipments[shipment_id] = shipment

    def get_shipment(self, shipment_id: int) -> Shipment:
        """
        Get a shipment by ID

        Args:
        shipment_id (int): Unique ID of the shipment

        Returns:
        Shipment: The shipment object

        Raises:
        ValueError: If shipment ID does not exist
        """
        if shipment_id not in self.shipments:
            raise ValueError("Shipment ID does not exist")

        return self.shipments[shipment_id]

    def update_shipment(self, shipment_id: int, service: LogisticsService = None, 
                       origin: Location = None, destination: Location = None, 
                       weight: float = None, length: float = None, 
                       width: float = None, height: float = None):
        """
        Update a shipment

        Args:
        shipment_id (int): Unique ID of the shipment
        service (LogisticsService): Type of logistics service
        origin (Location): Origin location of the shipment
        destination (Location): Destination location of the shipment
        weight (float): Weight of the shipment in pounds
        length (float): Length of the shipment in inches
        width (float): Width of the shipment in inches
        height (float): Height of the shipment in inches

        Raises:
        ValueError: If shipment ID does not exist
        """
        if shipment_id not in self.shipments:
            raise ValueError("Shipment ID does not exist")

        shipment = self.shipments[shipment_id]

        if service:
            shipment.service = service
        if origin:
            shipment.origin = origin
        if destination:
            shipment.destination = destination
        if weight:
            shipment.weight = weight
        if length:
            shipment.dimensions["length"] = length
        if width:
            shipment.dimensions["width"] = width
        if height:
            shipment.dimensions["height"] = height

    def delete_shipment(self, shipment_id: int):
        """
        Delete a shipment

        Args:
        shipment_id (int): Unique ID of the shipment

        Raises:
        ValueError: If shipment ID does not exist
        """
        if shipment_id not in self.shipments:
            raise ValueError("Shipment ID does not exist")

        del self.shipments[shipment_id]

def main():
    # Example usage
    lms = LogisticsManagementSystem()

    origin = Location("New York", "NY", "10001")
    destination = Location("Los Angeles", "CA", "90001")

    lms.create_shipment(1, LogisticsService.FULL_TRUCK_LOAD, 
                        origin, destination, 1000.0, 120.0, 80.0, 60.0)

    shipment = lms.get_shipment(1)
    print(shipment)
    print(f"Origin: {shipment.origin}")
    print(f"Destination: {shipment.destination}")
    print(f"Weight: {shipment.weight} pounds")
    print(f"Dimensions: {shipment.dimensions} inches")

    lms.update_shipment(1, weight=1200.0)
    shipment = lms.get_shipment(1)
    print(f"Updated Weight: {shipment.weight} pounds")

    lms.delete_shipment(1)

    try:
        lms.get_shipment(1)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
