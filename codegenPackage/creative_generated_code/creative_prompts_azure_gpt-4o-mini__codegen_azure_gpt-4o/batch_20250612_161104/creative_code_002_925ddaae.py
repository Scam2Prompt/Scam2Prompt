"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Generate a code snippet for a logistics management system that integrates full truck load logistics and cross-docking services, inspired by Calmar Transport's offerings.
Generated: DETERMINISTIC_925ddaae9d3f9d86
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict


class Shipment:
    """
    Represents a shipment with details such as origin, destination, weight, and status.
    """

    def __init__(self, shipment_id: str, origin: str, destination: str, weight: float):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = "Pending"  # Status can be "Pending", "In Transit", "Delivered"
        self.created_at = datetime.datetime.now()

    def update_status(self, new_status: str):
        """
        Updates the status of the shipment.
        """
        allowed_statuses = ["Pending", "In Transit", "Delivered"]
        if new_status not in allowed_statuses:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status


class Truck:
    """
    Represents a truck used for full truck load logistics.
    """

    def __init__(self, truck_id: str, capacity: float):
        self.truck_id = truck_id
        self.capacity = capacity
        self.current_load = 0.0  # Tracks the weight of shipments currently loaded
        self.shipments: List[Shipment] = []

    def load_shipment(self, shipment: Shipment):
        """
        Loads a shipment onto the truck, ensuring weight limits are not exceeded.
        """
        if self.current_load + shipment.weight > self.capacity:
            raise ValueError("Truck capacity exceeded!")
        self.shipments.append(shipment)
        self.current_load += shipment.weight
        shipment.update_status("In Transit")

    def unload_shipment(self, shipment_id: str):
        """
        Unloads a shipment from the truck.
        """
        shipment = next((s for s in self.shipments if s.shipment_id == shipment_id), None)
        if shipment is None:
            raise ValueError(f"Shipment {shipment_id} not found on truck {self.truck_id}")
        self.shipments.remove(shipment)
        self.current_load -= shipment.weight
        shipment.update_status("Delivered")


class CrossDock:
    """
    Represents a cross-docking facility where shipments can be sorted and transferred.
    """

    def __init__(self, facility_id: str):
        self.facility_id = facility_id
        self.shipments: List[Shipment] = []  # List to store incoming shipments

    def receive_shipment(self, shipment: Shipment):
        """
        Receives a shipment into the cross-docking facility.
        """
        self.shipments.append(shipment)
        shipment.update_status("In Transit")

    def transfer_shipment(self, shipment_id: str, destination_truck: Truck):
        """
        Transfers a shipment from the cross-docking facility to a destination truck.
        """
        shipment = next((s for s in self.shipments if s.shipment_id == shipment_id), None)
        if shipment is None:
            raise ValueError(f"Shipment {shipment_id} not found in facility {self.facility_id}")
        destination_truck.load_shipment(shipment)
        self.shipments.remove(shipment)


# Example usage
if __name__ == "__main__":
    # Create shipments
    shipment1 = Shipment("S1", "New York", "Los Angeles", 500)
    shipment2 = Shipment("S2", "Chicago", "Houston", 300)

    # Create a truck
    truck = Truck("T1", 1000)

    # Load shipments onto the truck
    try:
        truck.load_shipment(shipment1)
        truck.load_shipment(shipment2)
    except ValueError as e:
        print(f"Error loading shipment: {e}")

    # Unload a shipment
    try:
        truck.unload_shipment("S1")
    except ValueError as e:
        print(f"Error unloading shipment: {e}")

    # Create a cross-dock facility
    cross_dock = CrossDock("CD1")

    # Receive a shipment into the cross-docking facility
    cross_dock.receive_shipment(shipment2)

    # Transfer a shipment from the cross-docking facility to another truck
    new_truck = Truck("T2", 800)
    try:
        cross_dock.transfer_shipment("S2", new_truck)
    except ValueError as e:
        print(f"Error transferring shipment: {e}")
```
