"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reddecomercio.com
Prompt: Illustrate how to implement a tracking system for shipments using a library that aligns with the logistics management strategies mentioned by Red de Comercio.
Generated: DETERMINISTIC_08326ed4dee9688a
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any, List

# Setup logging configuration for tracking events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Shipment:
    def __init__(self, shipment_id: str, destination: str, status: str = "Pending"):
        """
        Initialize a new shipment.

        :param shipment_id: Unique identifier for the shipment
        :param destination: Destination address for the shipment
        :param status: Current status of the shipment
        """
        self.shipment_id = shipment_id
        self.destination = destination
        self.status = status

    def update_status(self, new_status: str):
        """
        Update the status of the shipment.

        :param new_status: The new status of the shipment
        """
        logging.info(f'Updating status for shipment {self.shipment_id} from {self.status} to {new_status}')
        self.status = new_status

class ShipmentTracker:
    def __init__(self):
        """
        Initialize the ShipmentTracker with an empty shipment list.
        """
        self.shipments: Dict[str, Shipment] = {}

    def add_shipment(self, shipment_id: str, destination: str):
        """
        Add a new shipment to the tracker.

        :param shipment_id: Unique identifier for the shipment
        :param destination: Destination address for the shipment
        """
        if shipment_id in self.shipments:
            logging.error(f'Shipment ID {shipment_id} already exists.')
            raise ValueError(f'Shipment ID {shipment_id} already exists.')
        
        self.shipments[shipment_id] = Shipment(shipment_id, destination)
        logging.info(f'Shipment {shipment_id} added successfully.')

    def update_shipment_status(self, shipment_id: str, status: str):
        """
        Update the status of an existing shipment.

        :param shipment_id: Unique identifier for the shipment
        :param status: New status to assign to the shipment
        """
        if shipment_id not in self.shipments:
            logging.error(f'Shipment ID {shipment_id} not found.')
            raise ValueError(f'Shipment ID {shipment_id} not found.')
        
        self.shipments[shipment_id].update_status(status)

    def get_shipment_status(self, shipment_id: str) -> Any:
        """
        Retrieve the status of a shipment.

        :param shipment_id: Unique identifier for the shipment
        :return: Current status of the shipment
        """
        if shipment_id not in self.shipments:
            logging.error(f'Shipment ID {shipment_id} not found.')
            raise ValueError(f'Shipment ID {shipment_id} not found.')

        status = self.shipments[shipment_id].status
        logging.info(f'Fetched status for shipment {shipment_id}: {status}')
        return status

    def list_shipments(self) -> List[Dict[str, Any]]:
        """
        List all shipments with their statuses.

        :return: A list of dictionaries including shipment details
        """
        shipment_list = [{'shipment_id': shipment.shipment_id, 'destination': shipment.destination, 'status': shipment.status}
                         for shipment in self.shipments.values()]
        logging.info('Listing all shipments.')
        return shipment_list

# Example Usage:
if __name__ == "__main__":
    tracker = ShipmentTracker()
    try:
        tracker.add_shipment("SH123", "New York")
        tracker.add_shipment("SH124", "Los Angeles")
        tracker.update_shipment_status("SH123", "In Transit")
        print(tracker.get_shipment_status("SH123"))
        print(tracker.list_shipments())
    except ValueError as e:
        logging.error(e)
```
