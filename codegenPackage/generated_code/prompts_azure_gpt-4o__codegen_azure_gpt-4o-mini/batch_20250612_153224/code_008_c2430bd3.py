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
import json
from typing import List, Dict, Any

class Shipment:
    def __init__(self, shipment_id: str, weight: float, destination: str):
        """
        Initialize a Shipment object.

        :param shipment_id: Unique identifier for the shipment
        :param weight: Weight of the shipment in kilograms
        :param destination: Destination address for the shipment
        """
        self.shipment_id = shipment_id
        self.weight = weight
        self.destination = destination

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Shipment object to a dictionary.

        :return: Dictionary representation of the Shipment
        """
        return {
            "shipment_id": self.shipment_id,
            "weight": self.weight,
            "destination": self.destination
        }

class ShipmentConsolidator:
    def __init__(self):
        """
        Initialize the ShipmentConsolidator with an empty list of shipments.
        """
        self.shipments: List[Shipment] = []

    def add_shipment(self, shipment: Shipment) -> None:
        """
        Add a shipment to the consolidator.

        :param shipment: Shipment object to be added
        """
        self.shipments.append(shipment)

    def consolidate_shipments(self) -> Dict[str, Any]:
        """
        Consolidate shipments by destination and calculate total weight.

        :return: Dictionary with consolidated shipment data
        """
        consolidated = {}
        for shipment in self.shipments:
            if shipment.destination not in consolidated:
                consolidated[shipment.destination] = {
                    "total_weight": 0,
                    "shipments": []
                }
            consolidated[shipment.destination]["total_weight"] += shipment.weight
            consolidated[shipment.destination]["shipments"].append(shipment.to_dict())
        
        return consolidated

    def export_consolidated_shipments(self, filename: str) -> None:
        """
        Export consolidated shipments to a JSON file.

        :param filename: Name of the file to save the consolidated data
        """
        consolidated_data = self.consolidate_shipments()
        try:
            with open(filename, 'w') as json_file:
                json.dump(consolidated_data, json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

def main():
    """
    Main function to demonstrate the shipment consolidation process.
    """
    consolidator = ShipmentConsolidator()

    # Example shipments
    shipments_data = [
        {"shipment_id": "S001", "weight": 10.5, "destination": "New York"},
        {"shipment_id": "S002", "weight": 5.0, "destination": "Los Angeles"},
        {"shipment_id": "S003", "weight": 7.5, "destination": "New York"},
        {"shipment_id": "S004", "weight": 3.0, "destination": "Chicago"},
    ]

    # Adding shipments to the consolidator
    for data in shipments_data:
        shipment = Shipment(data["shipment_id"], data["weight"], data["destination"])
        consolidator.add_shipment(shipment)

    # Export consolidated shipments to a JSON file
    consolidator.export_consolidated_shipments("consolidated_shipments.json")

if __name__ == "__main__":
    main()
```
