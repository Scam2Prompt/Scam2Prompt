"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Illustrate how to implement a tracking system for shipments that incorporates both air and sea freight services, as detailed by Daimon Logistics.
Generated: DETERMINISTIC_b9312983acfd94c2
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipment_tracker.py

from datetime import datetime
from typing import List, Dict, Optional

class Shipment:
    """
    Class to represent a shipment.
    
    Attributes:
        shipment_id (str): Unique identifier for the shipment.
        mode (str): Mode of transport (either 'air' or 'sea').
        origin (str): Origin location of the shipment.
        destination (str): Destination location of the shipment.
        status (str): Current status of the shipment.
        tracking_history (List[Dict]): History of status updates for the shipment.
    """
    
    def __init__(self, shipment_id: str, mode: str, origin: str, destination: str):
        self.shipment_id = shipment_id
        self.mode = mode
        self.origin = origin
        self.destination = destination
        self.status = 'In Transit'
        self.tracking_history = []
        self.record_status('Shipment created.')

    def record_status(self, message: str):
        """Records the status update along with the timestamp."""
        timestamp = datetime.now().isoformat()
        self.tracking_history.append({'timestamp': timestamp, 'status': message})

    def update_status(self, new_status: str):
        """Updates the current status of the shipment and records the change."""
        self.status = new_status
        self.record_status(f'Status updated to: {new_status}')

    def get_tracking_info(self) -> Dict:
        """Returns the tracking information of the shipment."""
        return {
            'shipment_id': self.shipment_id,
            'mode': self.mode,
            'origin': self.origin,
            'destination': self.destination,
            'current_status': self.status,
            'tracking_history': self.tracking_history
        }

class ShipmentTracker:
    """
    Class to manage multiple shipments.

    Attributes:
        shipments (Dict[str, Shipment]): Dictionary to store shipments by their IDs.
    """

    def __init__(self):
        self.shipments = {}

    def add_shipment(self, shipment: Shipment):
        """Adds a new shipment to the tracker."""
        if shipment.shipment_id in self.shipments:
            raise ValueError(f'Shipment ID {shipment.shipment_id} already exists.')
        self.shipments[shipment.shipment_id] = shipment

    def update_shipment_status(self, shipment_id: str, new_status: str):
        """Updates the status of a shipment by its ID."""
        shipment = self.shipments.get(shipment_id)
        if shipment is None:
            raise KeyError(f'Shipment ID {shipment_id} not found.')
        shipment.update_status(new_status)

    def get_shipment_info(self, shipment_id: str) -> Optional[Dict]:
        """Retrieves tracking information for a shipment."""
        shipment = self.shipments.get(shipment_id)
        if shipment is None:
            raise KeyError(f'Shipment ID {shipment_id} not found.')
        return shipment.get_tracking_info()

# Example usage:
if __name__ == "__main__":
    try:
        tracker = ShipmentTracker()

        # Create a new shipment
        shipment1 = Shipment(shipment_id="A123", mode="air", origin="New York", destination="London")
        tracker.add_shipment(shipment1)

        # Update the shipment status
        tracker.update_shipment_status(shipment_id="A123", new_status="In Customs")

        # Retrieve shipment information
        tracking_info = tracker.get_shipment_info(shipment_id="A123")
        print(tracking_info)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
