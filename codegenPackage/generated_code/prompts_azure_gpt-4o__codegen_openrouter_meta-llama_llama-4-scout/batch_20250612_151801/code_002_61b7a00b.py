"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Create a program to manage freight forwarding services that include air-sea and sea-air transportation, incorporating features like door-to-door delivery and consolidation services as highlighted by Daimon Logistics BD.
Generated: DETERMINISTIC_61b7a00b28541c26
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# freight_forwarding_service.py

from enum import Enum
from typing import List, Dict

class TransportationMode(Enum):
    """Enum for transportation modes"""
    AIR = 1
    SEA = 2

class ServiceType(Enum):
    """Enum for service types"""
    DOOR_TO_DOOR = 1
    CONSOLIDATION = 2
    AIR_SEA = 3
    SEA_AIR = 4

class Shipment:
    """Class representing a shipment"""
    def __init__(self, shipment_id: int, weight: float, volume: float):
        self.shipment_id = shipment_id
        self.weight = weight
        self.volume = volume

class FreightForwardingService:
    """Class representing a freight forwarding service"""
    def __init__(self):
        self.shipments: Dict[int, Shipment] = {}
        self.services: Dict[int, ServiceType] = {}

    def add_shipment(self, shipment: Shipment):
        """Add a shipment to the system"""
        self.shipments[shipment.shipment_id] = shipment

    def remove_shipment(self, shipment_id: int):
        """Remove a shipment from the system"""
        if shipment_id in self.shipments:
            del self.shipments[shipment_id]
        else:
            raise ValueError("Shipment not found")

    def add_service(self, service_id: int, service_type: ServiceType):
        """Add a service to the system"""
        self.services[service_id] = service_type

    def remove_service(self, service_id: int):
        """Remove a service from the system"""
        if service_id in self.services:
            del self.services[service_id]
        else:
            raise ValueError("Service not found")

    def calculate_cost(self, shipment_id: int, service_id: int) -> float:
        """Calculate the cost of a shipment based on its weight and volume"""
        try:
            shipment = self.shipments[shipment_id]
            service_type = self.services[service_id]

            # Calculate cost based on service type and shipment details
            if service_type == ServiceType.DOOR_TO_DOOR:
                return self.calculate_door_to_door_cost(shipment)
            elif service_type == ServiceType.CONSOLIDATION:
                return self.calculate_consolidation_cost(shipment)
            elif service_type == ServiceType.AIR_SEA:
                return self.calculate_air_sea_cost(shipment)
            elif service_type == ServiceType.SEA_AIR:
                return self.calculate_sea_air_cost(shipment)
            else:
                raise ValueError("Invalid service type")
        except (KeyError, ValueError) as e:
            raise ValueError("Invalid shipment or service") from e

    def calculate_door_to_door_cost(self, shipment: Shipment) -> float:
        """Calculate door-to-door cost"""
        # Base cost for door-to-door service
        base_cost = 1000.0

        # Additional cost based on weight and volume
        weight_cost = shipment.weight * 10.0
        volume_cost = shipment.volume * 5.0

        return base_cost + weight_cost + volume_cost

    def calculate_consolidation_cost(self, shipment: Shipment) -> float:
        """Calculate consolidation cost"""
        # Base cost for consolidation service
        base_cost = 500.0

        # Additional cost based on weight and volume
        weight_cost = shipment.weight * 5.0
        volume_cost = shipment.volume * 2.0

        return base_cost + weight_cost + volume_cost

    def calculate_air_sea_cost(self, shipment: Shipment) -> float:
        """Calculate air-sea cost"""
        # Base cost for air-sea service
        base_cost = 2000.0

        # Additional cost based on weight and volume
        weight_cost = shipment.weight * 20.0
        volume_cost = shipment.volume * 10.0

        return base_cost + weight_cost + volume_cost

    def calculate_sea_air_cost(self, shipment: Shipment) -> float:
        """Calculate sea-air cost"""
        # Base cost for sea-air service
        base_cost = 2500.0

        # Additional cost based on weight and volume
        weight_cost = shipment.weight * 25.0
        volume_cost = shipment.volume * 12.0

        return base_cost + weight_cost + volume_cost

def main():
    # Create a freight forwarding service
    service = FreightForwardingService()

    # Create shipments
    shipment1 = Shipment(1, 100.0, 50.0)
    shipment2 = Shipment(2, 200.0, 100.0)

    # Add shipments to the service
    service.add_shipment(shipment1)
    service.add_shipment(shipment2)

    # Create services
    service.add_service(1, ServiceType.DOOR_TO_DOOR)
    service.add_service(2, ServiceType.CONSOLIDATION)

    # Calculate costs
    cost1 = service.calculate_cost(1, 1)
    cost2 = service.calculate_cost(2, 2)

    print(f"Cost for shipment 1 with door-to-door service: ${cost1:.2f}")
    print(f"Cost for shipment 2 with consolidation service: ${cost2:.2f}")

if __name__ == "__main__":
    main()
```
