"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Develop code to simulate real-time monitoring of shipments, incorporating features like container load tracking and perishable goods handling, as described by Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_7b2597775a9de0a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List

class ShipmentStatus(Enum):
    """Enum for shipment status"""
    IN_TRANSIT = 1
    DELIVERED = 2
    LOST = 3
    DAMAGED = 4

class Container:
    """Class to represent a container"""
    def __init__(self, container_id: str, capacity: float):
        """
        Initialize a container

        Args:
        - container_id (str): Unique ID for the container
        - capacity (float): Maximum weight capacity of the container
        """
        self.container_id = container_id
        self.capacity = capacity
        self.current_load = 0.0
        self.loads: List[Load] = []

    def add_load(self, load: 'Load'):
        """
        Add a load to the container

        Args:
        - load (Load): Load to be added

        Raises:
        - ValueError: If the load exceeds the container's capacity
        """
        if self.current_load + load.weight > self.capacity:
            raise ValueError("Load exceeds container capacity")
        self.loads.append(load)
        self.current_load += load.weight

    def remove_load(self, load_id: str):
        """
        Remove a load from the container

        Args:
        - load_id (str): ID of the load to be removed

        Raises:
        - ValueError: If the load is not found in the container
        """
        for load in self.loads:
            if load.load_id == load_id:
                self.loads.remove(load)
                self.current_load -= load.weight
                return
        raise ValueError("Load not found in container")

class Load:
    """Class to represent a load"""
    def __init__(self, load_id: str, weight: float, is_perishable: bool = False):
        """
        Initialize a load

        Args:
        - load_id (str): Unique ID for the load
        - weight (float): Weight of the load
        - is_perishable (bool): Whether the load is perishable (default: False)
        """
        self.load_id = load_id
        self.weight = weight
        self.is_perishable = is_perishable
        self.temperature: float = None

    def set_temperature(self, temperature: float):
        """
        Set the temperature for a perishable load

        Args:
        - temperature (float): Temperature in Celsius

        Raises:
        - ValueError: If the load is not perishable
        """
        if not self.is_perishable:
            raise ValueError("Load is not perishable")
        self.temperature = temperature

class Shipment:
    """Class to represent a shipment"""
    def __init__(self, shipment_id: str, container: Container):
        """
        Initialize a shipment

        Args:
        - shipment_id (str): Unique ID for the shipment
        - container (Container): Container for the shipment
        """
        self.shipment_id = shipment_id
        self.container = container
        self.status = ShipmentStatus.IN_TRANSIT
        self.last_updated = datetime.now()

    def update_status(self, status: ShipmentStatus):
        """
        Update the shipment status

        Args:
        - status (ShipmentStatus): New status for the shipment
        """
        self.status = status
        self.last_updated = datetime.now()

def main():
    # Create a container
    container = Container("CONTAINER-001", 10000.0)

    # Create loads
    load1 = Load("LOAD-001", 5000.0, is_perishable=True)
    load1.set_temperature(10.0)
    load2 = Load("LOAD-002", 3000.0)

    # Add loads to container
    container.add_load(load1)
    container.add_load(load2)

    # Create a shipment
    shipment = Shipment("SHIPMENT-001", container)

    # Print shipment details
    print(f"Shipment ID: {shipment.shipment_id}")
    print(f"Container ID: {shipment.container.container_id}")
    print(f"Status: {shipment.status.name}")
    print(f"Last Updated: {shipment.last_updated}")
    print("Loads:")
    for load in shipment.container.loads:
        print(f"- Load ID: {load.load_id}, Weight: {load.weight}, Perishable: {load.is_perishable}")

    # Update shipment status
    shipment.update_status(ShipmentStatus.DELIVERED)

    # Print updated shipment details
    print(f"\nUpdated Status: {shipment.status.name}")
    print(f"Last Updated: {shipment.last_updated}")

if __name__ == "__main__":
    main()
```
