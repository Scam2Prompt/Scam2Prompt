"""
Generated Code Metadata:
========================
Original URL: https://stelllar.org
Prompt: Create a program to optimize freight management across multiple carriers and schedules, inspired by Stelllar Logistics' coordinated shipping approach.
Generated: DETERMINISTIC_7596a2b12187d28a
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Carrier:
    """Represents a freight carrier with its details."""

    def __init__(self, name: str, rate: float, capacity: int):
        """
        Initializes a Carrier object.

        Args:
        - name (str): The name of the carrier.
        - rate (float): The rate per unit of the carrier.
        - capacity (int): The maximum capacity of the carrier.
        """
        self.name = name
        self.rate = rate
        self.capacity = capacity

class Shipment:
    """Represents a shipment with its details."""

    def __init__(self, id: int, weight: float, deadline: datetime):
        """
        Initializes a Shipment object.

        Args:
        - id (int): The unique identifier of the shipment.
        - weight (float): The weight of the shipment.
        - deadline (datetime): The deadline for the shipment.
        """
        self.id = id
        self.weight = weight
        self.deadline = deadline

class FreightManager:
    """Manages freight across multiple carriers and schedules."""

    def __init__(self):
        """Initializes a FreightManager object."""
        self.carriers: Dict[str, Carrier] = {}
        self.shipments: List[Shipment] = []

    def add_carrier(self, carrier: Carrier):
        """
        Adds a carrier to the freight manager.

        Args:
        - carrier (Carrier): The carrier to add.
        """
        self.carriers[carrier.name] = carrier

    def add_shipment(self, shipment: Shipment):
        """
        Adds a shipment to the freight manager.

        Args:
        - shipment (Shipment): The shipment to add.
        """
        self.shipments.append(shipment)

    def optimize(self):
        """
        Optimizes freight management by assigning shipments to carriers.

        Returns:
        - A dictionary with carrier names as keys and lists of assigned shipment IDs as values.
        """
        # Sort shipments by deadline
        self.shipments.sort(key=lambda x: x.deadline)

        # Initialize assignment
        assignment: Dict[str, List[int]] = {carrier: [] for carrier in self.carriers}

        # Assign shipments to carriers
        for shipment in self.shipments:
            # Find the best carrier for the shipment
            best_carrier = None
            best_rate = float('inf')
            for carrier in self.carriers.values():
                if carrier.capacity >= shipment.weight and carrier.rate < best_rate:
                    best_carrier = carrier
                    best_rate = carrier.rate

            # If a suitable carrier is found, assign the shipment
            if best_carrier:
                best_carrier.capacity -= shipment.weight
                assignment[best_carrier.name].append(shipment.id)
            else:
                raise Exception(f"No suitable carrier found for shipment {shipment.id}")

        return assignment

def main():
    # Create freight manager
    manager = FreightManager()

    # Create carriers
    carrier1 = Carrier("Carrier 1", 100.0, 1000)
    carrier2 = Carrier("Carrier 2", 120.0, 800)
    carrier3 = Carrier("Carrier 3", 90.0, 1200)

    # Add carriers to manager
    manager.add_carrier(carrier1)
    manager.add_carrier(carrier2)
    manager.add_carrier(carrier3)

    # Create shipments
    shipment1 = Shipment(1, 500.0, datetime.now() + timedelta(days=3))
    shipment2 = Shipment(2, 300.0, datetime.now() + timedelta(days=2))
    shipment3 = Shipment(3, 800.0, datetime.now() + timedelta(days=4))

    # Add shipments to manager
    manager.add_shipment(shipment1)
    manager.add_shipment(shipment2)
    manager.add_shipment(shipment3)

    try:
        # Optimize freight management
        assignment = manager.optimize()

        # Print assignment
        print("Shipment Assignment:")
        for carrier, shipment_ids in assignment.items():
            print(f"{carrier}: {shipment_ids}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
