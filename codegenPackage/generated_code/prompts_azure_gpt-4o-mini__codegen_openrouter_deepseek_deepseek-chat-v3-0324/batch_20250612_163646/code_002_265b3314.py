"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Write a code snippet that simulates cargo handling operations in a logistics system, inspired by the processes described by ENL Consortium.
Generated: DETERMINISTIC_265b331433863c00
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum, auto


class CargoStatus(Enum):
    """Enum representing the status of a cargo item."""
    PENDING = auto()
    LOADED = auto()
    IN_TRANSIT = auto()
    DELIVERED = auto()
    CANCELLED = auto()


class Cargo:
    """Class representing a cargo item in the logistics system."""

    def __init__(self, cargo_id: str, weight: float, destination: str):
        self.cargo_id = cargo_id
        self.weight = weight
        self.destination = destination
        self.status = CargoStatus.PENDING
        self.load_time: Optional[datetime] = None
        self.delivery_time: Optional[datetime] = None

    def update_status(self, new_status: CargoStatus) -> None:
        """Update the status of the cargo with timestamp."""
        self.status = new_status
        if new_status == CargoStatus.LOADED:
            self.load_time = datetime.now()
        elif new_status == CargoStatus.DELIVERED:
            self.delivery_time = datetime.now()

    def __str__(self) -> str:
        return (f"Cargo ID: {self.cargo_id}, Weight: {self.weight}kg, "
                f"Destination: {self.destination}, Status: {self.status.name}")


class CargoHandler:
    """Class handling cargo operations in the logistics system."""

    def __init__(self):
        self.cargo_list: List[Cargo] = []
        self.shipments: Dict[str, List[Cargo]] = {}

    def add_cargo(self, cargo: Cargo) -> bool:
        """Add a new cargo to the system."""
        if cargo.cargo_id in [c.cargo_id for c in self.cargo_list]:
            return False
        self.cargo_list.append(cargo)
        return True

    def create_shipment(self, shipment_id: str, cargo_ids: List[str]) -> bool:
        """Create a shipment with the given cargo items."""
        if shipment_id in self.shipments:
            return False

        selected_cargo = []
        for cargo_id in cargo_ids:
            cargo = next((c for c in self.cargo_list if c.cargo_id == cargo_id and c.status == CargoStatus.PENDING), None)
            if cargo:
                selected_cargo.append(cargo)

        if not selected_cargo:
            return False

        self.shipments[shipment_id] = selected_cargo
        for cargo in selected_cargo:
            cargo.update_status(CargoStatus.LOADED)
        return True

    def depart_shipment(self, shipment_id: str) -> bool:
        """Mark a shipment as departed (in transit)."""
        if shipment_id not in self.shipments:
            return False

        for cargo in self.shipments[shipment_id]:
            cargo.update_status(CargoStatus.IN_TRANSIT)
        return True

    def deliver_shipment(self, shipment_id: str) -> bool:
        """Mark a shipment as delivered."""
        if shipment_id not in self.shipments:
            return False

        for cargo in self.shipments[shipment_id]:
            cargo.update_status(CargoStatus.DELIVERED)
        return True

    def get_cargo_status(self, cargo_id: str) -> Optional[CargoStatus]:
        """Get the status of a specific cargo item."""
        cargo = next((c for c in self.cargo_list if c.cargo_id == cargo_id), None)
        return cargo.status if cargo else None

    def cancel_cargo(self, cargo_id: str) -> bool:
        """Cancel a cargo item."""
        cargo = next((c for c in self.cargo_list if c.cargo_id == cargo_id), None)
        if not cargo or cargo.status != CargoStatus.PENDING:
            return False

        cargo.update_status(CargoStatus.CANCELLED)
        return True


def generate_cargo_id() -> str:
    """Generate a random cargo ID."""
    return f"CRG{random.randint(10000, 99999)}"


# Example usage
if __name__ == "__main__":
    handler = CargoHandler()

    # Add some cargo
    cargo1 = Cargo(generate_cargo_id(), 100.5, "New York")
    cargo2 = Cargo(generate_cargo_id(), 250.0, "Los Angeles")
    cargo3 = Cargo(generate_cargo_id(), 75.3, "Chicago")

    handler.add_cargo(cargo1)
    handler.add_cargo(cargo2)
    handler.add_cargo(cargo3)

    # Create and process a shipment
    shipment_id = "SHIP123"
    handler.create_shipment(shipment_id, [cargo1.cargo_id, cargo2.cargo_id])
    handler.depart_shipment(shipment_id)

    # Simulate delivery after some time
    handler.deliver_shipment(shipment_id)

    # Print status of all cargo
    for cargo in handler.cargo_list:
        print(cargo)
```
