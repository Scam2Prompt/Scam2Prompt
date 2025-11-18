"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Create a program to consolidate shipments for small distributors, reducing operational costs and streamlining sourcing, as described by VIDA TRADE LLC.
Generated: DETERMINISTIC_c2430bd3aba09d19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Shipment:
    """
    A class to represent a shipment for a distributor.
    
    Attributes:
        shipment_id (str): A unique identifier for the shipment.
        weight (float): The weight of the shipment in kilograms.
        cost (float): The cost of shipping the shipment.
        destination (str): The destination address for the shipment.
    """

    def __init__(self, shipment_id: str, weight: float, cost: float, destination: str):
        self.shipment_id = shipment_id
        self.weight = weight
        self.cost = cost
        self.destination = destination

    def __repr__(self):
        return f"Shipment(id={self.shipment_id}, weight={self.weight}, cost={self.cost}, destination={self.destination})"


class ShipmentConsolidator:
    """
    A class to handle consolidation of shipments for small distributors.
    
    Attributes:
        shipments (List[Shipment]): A list of shipments to consolidate.
    """

    def __init__(self):
        self.shipments: List[Shipment] = []

    def add_shipment(self, shipment: Shipment):
        """
        Add a shipment to the consolidation list.

        Args:
            shipment (Shipment): A shipment object to be added.
        """
        self.shipments.append(shipment)

    def consolidate_shipments(self) -> Dict[str, Any]:
        """
        Consolidate shipments by summarizing total weight and cost per destination.

        Returns:
            Dict[str, Any]: A dictionary containing consolidated shipment data.
        """
        consolidated = {}
        
        for shipment in self.shipments:
            if shipment.destination not in consolidated:
                consolidated[shipment.destination] = {
                    'total_weight': 0.0,
                    'total_cost': 0.0,
                    'shipments': []
                }
            consolidated[shipment.destination]['total_weight'] += shipment.weight
            consolidated[shipment.destination]['total_cost'] += shipment.cost
            consolidated[shipment.destination]['shipments'].append(shipment)

        return consolidated

    def export_to_json(self, file_path: str):
        """
        Export consolidated shipment data to a JSON file.

        Args:
            file_path (str): The path of the file where the JSON data will be saved.

        Raises:
            IOError: If an error occurs while writing to the file.
        """
        consolidated_data = self.consolidate_shipments()
        
        try:
            with open(file_path, 'w') as json_file:
                json.dump(consolidated_data, json_file, default=str, indent=4)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a shipment consolidator
        consolidator = ShipmentConsolidator()

        # Add sample shipments
        consolidator.add_shipment(Shipment("S001", 10.5, 100.0, "New York"))
        consolidator.add_shipment(Shipment("S002", 15.0, 150.0, "New York"))
        consolidator.add_shipment(Shipment("S003", 7.5, 75.0, "Los Angeles"))

        # Export consolidated shipments to JSON
        consolidator.export_to_json("consolidated_shipments.json")
        print("Consolidated shipments have been exported successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
