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
from enum import Enum
from typing import List

class CargoStatus(Enum):
    """Enum representing the status of cargo."""
    RECEIVED = 1
    LOADED = 2
    UNLOADED = 3
    DAMAGED = 4
    LOST = 5

class Cargo:
    """Class representing cargo in the logistics system."""
    
    def __init__(self, cargo_id: str, description: str):
        """
        Initialize a Cargo object.

        Args:
        - cargo_id (str): Unique identifier for the cargo.
        - description (str): Brief description of the cargo.
        """
        self.cargo_id = cargo_id
        self.description = description
        self.status = CargoStatus.RECEIVED

    def update_status(self, status: CargoStatus):
        """
        Update the status of the cargo.

        Args:
        - status (CargoStatus): New status of the cargo.
        """
        self.status = status

class Vessel:
    """Class representing a vessel in the logistics system."""
    
    def __init__(self, vessel_id: str, capacity: int):
        """
        Initialize a Vessel object.

        Args:
        - vessel_id (str): Unique identifier for the vessel.
        - capacity (int): Maximum cargo capacity of the vessel.
        """
        self.vessel_id = vessel_id
        self.capacity = capacity
        self.cargo_list: List[Cargo] = []

    def load_cargo(self, cargo: Cargo):
        """
        Load cargo onto the vessel.

        Args:
        - cargo (Cargo): Cargo to be loaded.

        Raises:
        - ValueError: If the vessel is at full capacity.
        """
        if len(self.cargo_list) < self.capacity:
            self.cargo_list.append(cargo)
            cargo.update_status(CargoStatus.LOADED)
        else:
            raise ValueError("Vessel is at full capacity.")

    def unload_cargo(self, cargo_id: str):
        """
        Unload cargo from the vessel.

        Args:
        - cargo_id (str): ID of the cargo to be unloaded.

        Raises:
        - ValueError: If the cargo is not found on the vessel.
        """
        for cargo in self.cargo_list:
            if cargo.cargo_id == cargo_id:
                self.cargo_list.remove(cargo)
                cargo.update_status(CargoStatus.UNLOADED)
                return
        raise ValueError("Cargo not found on vessel.")

class LogisticsSystem:
    """Class representing the logistics system."""
    
    def __init__(self):
        self.vessels: List[Vessel] = []
        self.cargo_list: List[Cargo] = []

    def add_vessel(self, vessel: Vessel):
        """
        Add a vessel to the logistics system.

        Args:
        - vessel (Vessel): Vessel to be added.
        """
        self.vessels.append(vessel)

    def add_cargo(self, cargo: Cargo):
        """
        Add cargo to the logistics system.

        Args:
        - cargo (Cargo): Cargo to be added.
        """
        self.cargo_list.append(cargo)

    def load_cargo_on_vessel(self, vessel_id: str, cargo_id: str):
        """
        Load cargo onto a vessel.

        Args:
        - vessel_id (str): ID of the vessel.
        - cargo_id (str): ID of the cargo.

        Raises:
        - ValueError: If the vessel or cargo is not found.
        """
        vessel = next((v for v in self.vessels if v.vessel_id == vessel_id), None)
        cargo = next((c for c in self.cargo_list if c.cargo_id == cargo_id), None)
        if vessel and cargo:
            vessel.load_cargo(cargo)
        else:
            raise ValueError("Vessel or cargo not found.")

def main():
    # Create a logistics system
    logistics_system = LogisticsSystem()

    # Create vessels
    vessel1 = Vessel("Vessel1", 10)
    vessel2 = Vessel("Vessel2", 15)

    # Add vessels to the logistics system
    logistics_system.add_vessel(vessel1)
    logistics_system.add_vessel(vessel2)

    # Create cargo
    cargo1 = Cargo("Cargo1", "Electronics")
    cargo2 = Cargo("Cargo2", "Food")

    # Add cargo to the logistics system
    logistics_system.add_cargo(cargo1)
    logistics_system.add_cargo(cargo2)

    # Load cargo onto vessels
    logistics_system.load_cargo_on_vessel("Vessel1", "Cargo1")
    logistics_system.load_cargo_on_vessel("Vessel2", "Cargo2")

    # Print cargo status
    print(f"Cargo {cargo1.cargo_id} status: {cargo1.status}")
    print(f"Cargo {cargo2.cargo_id} status: {cargo2.status}")

    # Unload cargo from vessel
    vessel1.unload_cargo("Cargo1")
    print(f"Cargo {cargo1.cargo_id} status after unloading: {cargo1.status}")

if __name__ == "__main__":
    main()
```
