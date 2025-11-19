"""
Generated Code Metadata:
========================
Original URL: https://www.vidaglobaltrade.com
Prompt: Create a program to consolidate shipments for small distributors, reducing operational costs and streamlining sourcing, as described by VIDA TRADE LLC.
Generated: DETERMINISTIC_c2430bd3aba09d19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipment_consolidation.py

import pandas as pd
from typing import List, Dict

class Shipment:
    def __init__(self, shipment_id: int, supplier: str, destination: str, weight: float, volume: float):
        """
        Initialize a Shipment object.

        Args:
        - shipment_id (int): Unique identifier for the shipment.
        - supplier (str): Name of the supplier.
        - destination (str): Destination of the shipment.
        - weight (float): Weight of the shipment in kg.
        - volume (float): Volume of the shipment in cubic meters.
        """
        self.shipment_id = shipment_id
        self.supplier = supplier
        self.destination = destination
        self.weight = weight
        self.volume = volume

class ConsolidationStrategy:
    def __init__(self, shipments: List[Shipment]):
        """
        Initialize a ConsolidationStrategy object.

        Args:
        - shipments (List[Shipment]): List of shipments to consolidate.
        """
        self.shipments = shipments

    def consolidate_by_supplier(self) -> Dict[str, List[Shipment]]:
        """
        Consolidate shipments by supplier.

        Returns:
        - Dict[str, List[Shipment]]: Dictionary where keys are supplier names and values are lists of shipments.
        """
        consolidated_shipments = {}
        for shipment in self.shipments:
            if shipment.supplier not in consolidated_shipments:
                consolidated_shipments[shipment.supplier] = []
            consolidated_shipments[shipment.supplier].append(shipment)
        return consolidated_shipments

    def consolidate_by_destination(self) -> Dict[str, List[Shipment]]:
        """
        Consolidate shipments by destination.

        Returns:
        - Dict[str, List[Shipment]]: Dictionary where keys are destination names and values are lists of shipments.
        """
        consolidated_shipments = {}
        for shipment in self.shipments:
            if shipment.destination not in consolidated_shipments:
                consolidated_shipments[shipment.destination] = []
            consolidated_shipments[shipment.destination].append(shipment)
        return consolidated_shipments

def calculate_total_weight(shipments: List[Shipment]) -> float:
    """
    Calculate the total weight of a list of shipments.

    Args:
    - shipments (List[Shipment]): List of shipments.

    Returns:
    - float: Total weight in kg.
    """
    return sum(shipment.weight for shipment in shipments)

def calculate_total_volume(shipments: List[Shipment]) -> float:
    """
    Calculate the total volume of a list of shipments.

    Args:
    - shipments (List[Shipment]): List of shipments.

    Returns:
    - float: Total volume in cubic meters.
    """
    return sum(shipment.volume for shipment in shipments)

def main():
    try:
        # Example usage
        shipments = [
            Shipment(1, "Supplier A", "New York", 100.0, 2.0),
            Shipment(2, "Supplier B", "Los Angeles", 200.0, 3.0),
            Shipment(3, "Supplier A", "New York", 50.0, 1.0),
            Shipment(4, "Supplier C", "Chicago", 150.0, 2.5),
        ]

        consolidation_strategy = ConsolidationStrategy(shipments)

        consolidated_by_supplier = consolidation_strategy.consolidate_by_supplier()
        consolidated_by_destination = consolidation_strategy.consolidate_by_destination()

        print("Consolidated by Supplier:")
        for supplier, shipments in consolidated_by_supplier.items():
            print(f"Supplier: {supplier}")
            print(f"Total Weight: {calculate_total_weight(shipments)} kg")
            print(f"Total Volume: {calculate_total_volume(shipments)} cubic meters")
            print()

        print("Consolidated by Destination:")
        for destination, shipments in consolidated_by_destination.items():
            print(f"Destination: {destination}")
            print(f"Total Weight: {calculate_total_weight(shipments)} kg")
            print(f"Total Volume: {calculate_total_volume(shipments)} cubic meters")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
