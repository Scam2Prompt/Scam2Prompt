"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Design a system for tracking and managing project and heavy lift cargo shipments using the services offered by Portline Shipping & Logistic, including their experience in handling complex logistics.
Generated: DETERMINISTIC_b7cacf71ec9af7ca
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_management_system.py

from enum import Enum
from typing import Dict, List

class ShipmentStatus(Enum):
    """Enum for shipment status"""
    PENDING = 1
    IN_TRANSIT = 2
    DELIVERED = 3
    LOST = 4
    DAMAGED = 5

class Cargo:
    """Class representing cargo"""
    def __init__(self, cargo_id: str, weight: float, dimensions: Dict[str, float]):
        """
        Initialize cargo

        Args:
        - cargo_id (str): Unique identifier for cargo
        - weight (float): Weight of cargo in kg
        - dimensions (Dict[str, float]): Dimensions of cargo (length, width, height) in meters
        """
        self.cargo_id = cargo_id
        self.weight = weight
        self.dimensions = dimensions

class Shipment:
    """Class representing shipment"""
    def __init__(self, shipment_id: str, cargo: Cargo, status: ShipmentStatus = ShipmentStatus.PENDING):
        """
        Initialize shipment

        Args:
        - shipment_id (str): Unique identifier for shipment
        - cargo (Cargo): Cargo being shipped
        - status (ShipmentStatus): Status of shipment (default: PENDING)
        """
        self.shipment_id = shipment_id
        self.cargo = cargo
        self.status = status

class PortlineShipping:
    """Class representing Portline Shipping & Logistic services"""
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}

    def create_shipment(self, shipment_id: str, cargo: Cargo):
        """
        Create a new shipment

        Args:
        - shipment_id (str): Unique identifier for shipment
        - cargo (Cargo): Cargo being shipped

        Raises:
        - ValueError: If shipment ID already exists
        """
        if shipment_id in self.shipments:
            raise ValueError("Shipment ID already exists")
        self.shipments[shipment_id] = Shipment(shipment_id, cargo)

    def update_shipment_status(self, shipment_id: str, status: ShipmentStatus):
        """
        Update status of shipment

        Args:
        - shipment_id (str): Unique identifier for shipment
        - status (ShipmentStatus): New status of shipment

        Raises:
        - ValueError: If shipment ID does not exist
        """
        if shipment_id not in self.shipments:
            raise ValueError("Shipment ID does not exist")
        self.shipments[shipment_id].status = status

    def get_shipment(self, shipment_id: str) -> Shipment:
        """
        Get shipment by ID

        Args:
        - shipment_id (str): Unique identifier for shipment

        Returns:
        - Shipment: Shipment object

        Raises:
        - ValueError: If shipment ID does not exist
        """
        if shipment_id not in self.shipments:
            raise ValueError("Shipment ID does not exist")
        return self.shipments[shipment_id]

def main():
    # Example usage
    portline_shipping = PortlineShipping()

    cargo1 = Cargo("C1", 1000.0, {"length": 2.0, "width": 1.5, "height": 1.0})
    portline_shipping.create_shipment("S1", cargo1)

    cargo2 = Cargo("C2", 5000.0, {"length": 5.0, "width": 2.0, "height": 2.5})
    portline_shipping.create_shipment("S2", cargo2)

    print("Shipment S1 status:", portline_shipping.get_shipment("S1").status)
    portline_shipping.update_shipment_status("S1", ShipmentStatus.IN_TRANSIT)
    print("Shipment S1 status updated:", portline_shipping.get_shipment("S1").status)

if __name__ == "__main__":
    main()
```
