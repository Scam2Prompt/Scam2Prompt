"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Develop a logistics management system that integrates trucking and connected transportation for import/export fields, as described in Daimon Logistics BD's service offerings.
Generated: DETERMINISTIC_f9575014d7e69802
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid
from typing import List, Optional

# Class representing a vehicle in the logistics system
class Vehicle:
    def __init__(self, vehicle_id: str, vehicle_type: str, capacity: float):
        """
        Initializes a new vehicle instance.

        :param vehicle_id: Unique identifier for the vehicle
        :param vehicle_type: Type of the vehicle (e.g., truck, van)
        :param capacity: Maximum load capacity of the vehicle in tons
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity

    def __str__(self):
        return f"Vehicle(ID: {self.vehicle_id}, Type: {self.vehicle_type}, Capacity: {self.capacity} tons)"

# Class representing a shipment
class Shipment:
    def __init__(self, shipment_id: str, origin: str, destination: str, weight: float, vehicle: Vehicle):
        """
        Initializes a new shipment instance.

        :param shipment_id: Unique identifier for the shipment
        :param origin: Origin location of the shipment
        :param destination: Destination location of the shipment
        :param weight: Weight of the shipment in tons
        :param vehicle: Vehicle assigned to the shipment
        """
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.vehicle = vehicle
        self.status = "Pending"
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return (f"Shipment(ID: {self.shipment_id}, Origin: {self.origin}, "
                f"Destination: {self.destination}, Weight: {self.weight} tons, "
                f"Vehicle: {self.vehicle}, Status: {self.status}, Timestamp: {self.timestamp})")

# Class for managing logistics operations
class LogisticsManager:
    def __init__(self):
        """
        Initializes a new LogisticsManager instance, with lists for vehicles and shipments.
        """
        self.vehicles: List[Vehicle] = []
        self.shipments: List[Shipment] = []

    def add_vehicle(self, vehicle_type: str, capacity: float) -> Vehicle:
        """
        Adds a new vehicle to the logistics management system.

        :param vehicle_type: Type of the vehicle to add
        :param capacity: Capacity of the vehicle
        :return: The newly created Vehicle instance
        """
        vehicle_id = str(uuid.uuid4())
        new_vehicle = Vehicle(vehicle_id, vehicle_type, capacity)
        self.vehicles.append(new_vehicle)
        return new_vehicle

    def create_shipment(self, origin: str, destination: str, weight: float, vehicle_id: str) -> Optional[Shipment]:
        """
        Creates a new shipment and assigns it to a vehicle.

        :param origin: Origin location of the shipment
        :param destination: Destination location of the shipment
        :param weight: Weight of the shipment
        :param vehicle_id: ID of the vehicle to use
        :return: The newly created Shipment instance or None if vehicle not found
        """
        vehicle = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)
        if not vehicle:
            print(f"Error: Vehicle with ID {vehicle_id} not found.")
            return None
        if weight > vehicle.capacity:
            print(f"Error: Shipment weight exceeds vehicle capacity.")
            return None

        shipment_id = str(uuid.uuid4())
        new_shipment = Shipment(shipment_id, origin, destination, weight, vehicle)
        self.shipments.append(new_shipment)
        return new_shipment

    def list_shipments(self) -> List[str]:
        """
        Lists all shipments in the logistics management system.

        :return: A list of string representations of all shipments
        """
        return [str(shipment) for shipment in self.shipments]

# Example usage
if __name__ == "__main__":
    logistics_manager = LogisticsManager()
    
    # Adding vehicles
    logistics_manager.add_vehicle(vehicle_type="Truck", capacity=10.0)
    logistics_manager.add_vehicle(vehicle_type="Van", capacity=5.0)

    # Creating shipments
    shipment1 = logistics_manager.create_shipment("New York", "Los Angeles", 8.0, logistics_manager.vehicles[0].vehicle_id)
    shipment2 = logistics_manager.create_shipment("Chicago", "Houston", 6.0, logistics_manager.vehicles[1].vehicle_id)

    # Listing all shipments
    for shipment in logistics_manager.list_shipments():
        print(shipment)
```
