"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Create a program to simulate multi-modal transport logistics, including air and sea freight, inspired by Bin Qutab Logistics' proven experience in handling large-scale projects.
Generated: DETERMINISTIC_960384e447f999ae
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List

class TransportMode(Enum):
    """Enum for transport modes"""
    AIR = 1
    SEA = 2
    LAND = 3

@dataclass
class Shipment:
    """Dataclass for shipment details"""
    id: int
    weight: float
    volume: float
    origin: str
    destination: str

class Transport(ABC):
    """Abstract base class for transport modes"""
    def __init__(self, shipment: Shipment):
        self.shipment = shipment

    @abstractmethod
    def calculate_cost(self) -> float:
        """Calculate transport cost"""
        pass

    @abstractmethod
    def calculate_transit_time(self) -> int:
        """Calculate transit time in days"""
        pass

class AirFreight(Transport):
    """Class for air freight transport"""
    def __init__(self, shipment: Shipment):
        super().__init__(shipment)

    def calculate_cost(self) -> float:
        # Assume air freight cost is $10 per kg
        cost = self.shipment.weight * 10
        return cost

    def calculate_transit_time(self) -> int:
        # Assume air freight transit time is 3-5 days
        return 4

class SeaFreight(Transport):
    """Class for sea freight transport"""
    def __init__(self, shipment: Shipment):
        super().__init__(shipment)

    def calculate_cost(self) -> float:
        # Assume sea freight cost is $5 per kg
        cost = self.shipment.weight * 5
        return cost

    def calculate_transit_time(self) -> int:
        # Assume sea freight transit time is 20-30 days
        return 25

class Logistics:
    """Class for logistics management"""
    def __init__(self):
        self.shipments = []

    def add_shipment(self, shipment: Shipment, transport_mode: TransportMode):
        if transport_mode == TransportMode.AIR:
            transport = AirFreight(shipment)
        elif transport_mode == TransportMode.SEA:
            transport = SeaFreight(shipment)
        else:
            raise ValueError("Invalid transport mode")

        self.shipments.append((shipment, transport))

    def calculate_total_cost(self) -> float:
        total_cost = 0
        for _, transport in self.shipments:
            total_cost += transport.calculate_cost()
        return total_cost

    def calculate_total_transit_time(self) -> int:
        total_transit_time = 0
        for _, transport in self.shipments:
            total_transit_time += transport.calculate_transit_time()
        return total_transit_time

    def print_shipment_details(self):
        for shipment, transport in self.shipments:
            print(f"Shipment ID: {shipment.id}")
            print(f"Weight: {shipment.weight} kg")
            print(f"Volume: {shipment.volume} cubic meters")
            print(f"Origin: {shipment.origin}")
            print(f"Destination: {shipment.destination}")
            print(f"Transport Mode: {type(transport).__name__}")
            print(f"Cost: ${transport.calculate_cost():.2f}")
            print(f"Transit Time: {transport.calculate_transit_time()} days")
            print("------------------------")

def main():
    logistics = Logistics()

    shipment1 = Shipment(1, 1000, 10, "New York", "Los Angeles")
    logistics.add_shipment(shipment1, TransportMode.AIR)

    shipment2 = Shipment(2, 5000, 50, "Shanghai", "Rotterdam")
    logistics.add_shipment(shipment2, TransportMode.SEA)

    print("Shipment Details:")
    logistics.print_shipment_details()

    print(f"\nTotal Cost: ${logistics.calculate_total_cost():.2f}")
    print(f"Total Transit Time: {logistics.calculate_total_transit_time()} days")

if __name__ == "__main__":
    main()
```
