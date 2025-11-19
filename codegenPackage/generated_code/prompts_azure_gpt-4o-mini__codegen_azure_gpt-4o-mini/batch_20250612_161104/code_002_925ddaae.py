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
import datetime
from typing import List, Optional

class Shipment:
    """Class representing a shipment in the logistics system."""
    
    def __init__(self, shipment_id: str, origin: str, destination: str, weight: float, volume: float):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.volume = volume
        self.status = "Pending"
        self.created_at = datetime.datetime.now()

    def update_status(self, new_status: str):
        """Update the status of the shipment."""
        self.status = new_status

class Truck:
    """Class representing a truck in the logistics system."""
    
    def __init__(self, truck_id: str, capacity_weight: float, capacity_volume: float):
        self.truck_id = truck_id
        self.capacity_weight = capacity_weight
        self.capacity_volume = capacity_volume
        self.current_load_weight = 0.0
        self.current_load_volume = 0.0
        self.shipments: List[Shipment] = []

    def load_shipment(self, shipment: Shipment) -> bool:
        """Load a shipment onto the truck if capacity allows."""
        if (self.current_load_weight + shipment.weight <= self.capacity_weight and
                self.current_load_volume + shipment.volume <= self.capacity_volume):
            self.shipments.append(shipment)
            self.current_load_weight += shipment.weight
            self.current_load_volume += shipment.volume
            shipment.update_status("Loaded")
            return True
        else:
            raise ValueError("Not enough capacity to load the shipment.")

    def unload_shipment(self, shipment_id: str) -> Optional[Shipment]:
        """Unload a shipment from the truck by shipment ID."""
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                self.shipments.remove(shipment)
                self.current_load_weight -= shipment.weight
                self.current_load_volume -= shipment.volume
                shipment.update_status("Unloaded")
                return shipment
        raise ValueError("Shipment not found on this truck.")

class CrossDockingService:
    """Class representing a cross-docking service."""
    
    def __init__(self):
        self.shipments: List[Shipment] = []

    def receive_shipment(self, shipment: Shipment):
        """Receive a shipment for cross-docking."""
        self.shipments.append(shipment)
        shipment.update_status("Received at Cross-Dock")

    def dispatch_shipment(self, shipment_id: str) -> Optional[Shipment]:
        """Dispatch a shipment from the cross-dock."""
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                self.shipments.remove(shipment)
                shipment.update_status("Dispatched from Cross-Dock")
                return shipment
        raise ValueError("Shipment not found in cross-dock.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a truck with specific capacities
        truck = Truck(truck_id="TRK123", capacity_weight=10000.0, capacity_volume=50.0)

        # Create a shipment
        shipment1 = Shipment(shipment_id="SHP001", origin="Warehouse A", destination="Warehouse B", weight=5000.0, volume=25.0)

        # Load the shipment onto the truck
        truck.load_shipment(shipment1)

        # Create a cross-docking service
        cross_dock = CrossDockingService()

        # Receive a shipment at the cross-dock
        shipment2 = Shipment(shipment_id="SHP002", origin="Warehouse C", destination="Warehouse D", weight=3000.0, volume=15.0)
        cross_dock.receive_shipment(shipment2)

        # Dispatch the shipment from the cross-dock
        dispatched_shipment = cross_dock.dispatch_shipment("SHP002")

        # Unload the shipment from the truck
        unloaded_shipment = truck.unload_shipment("SHP001")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
