"""
Generated Code Metadata:
========================
Original URL: https://reddecomercio.com
Prompt: Illustrate how to implement a tracking system for shipments using a library that aligns with the logistics management strategies mentioned by Red de Comercio.
Generated: DETERMINISTIC_08326ed4dee9688a
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class Shipment:
    """Class representing a shipment."""
    
    def __init__(self, origin: str, destination: str, weight: float):
        """
        Initialize a new shipment.

        :param origin: The origin location of the shipment.
        :param destination: The destination location of the shipment.
        :param weight: The weight of the shipment in kilograms.
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the shipment
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = "Pending"  # Initial status of the shipment
        self.tracking_history: List[str] = []  # History of status updates
        self.created_at = datetime.now()  # Timestamp of shipment creation

    def update_status(self, new_status: str):
        """
        Update the status of the shipment and log the change.

        :param new_status: The new status to set for the shipment.
        """
        self.status = new_status
        self.tracking_history.append(f"{datetime.now()}: Status updated to '{new_status}'")

    def get_tracking_info(self) -> dict:
        """
        Get the current tracking information of the shipment.

        :return: A dictionary containing shipment details and tracking history.
        """
        return {
            "id": self.id,
            "origin": self.origin,
            "destination": self.destination,
            "weight": self.weight,
            "status": self.status,
            "tracking_history": self.tracking_history,
            "created_at": self.created_at.isoformat()
        }

class ShipmentTracker:
    """Class to manage and track shipments."""
    
    def __init__(self):
        """Initialize the shipment tracker with an empty shipment list."""
        self.shipments: List[Shipment] = []

    def create_shipment(self, origin: str, destination: str, weight: float) -> Shipment:
        """
        Create a new shipment and add it to the tracker.

        :param origin: The origin location of the shipment.
        :param destination: The destination location of the shipment.
        :param weight: The weight of the shipment in kilograms.
        :return: The created Shipment object.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        
        shipment = Shipment(origin, destination, weight)
        self.shipments.append(shipment)
        return shipment

    def update_shipment_status(self, shipment_id: str, new_status: str) -> Optional[Shipment]:
        """
        Update the status of a shipment by its ID.

        :param shipment_id: The unique identifier of the shipment.
        :param new_status: The new status to set for the shipment.
        :return: The updated Shipment object or None if not found.
        """
        shipment = self.find_shipment_by_id(shipment_id)
        if shipment:
            shipment.update_status(new_status)
            return shipment
        else:
            print(f"Shipment with ID {shipment_id} not found.")
            return None

    def find_shipment_by_id(self, shipment_id: str) -> Optional[Shipment]:
        """
        Find a shipment by its ID.

        :param shipment_id: The unique identifier of the shipment.
        :return: The Shipment object if found, otherwise None.
        """
        for shipment in self.shipments:
            if shipment.id == shipment_id:
                return shipment
        return None

    def get_all_shipments(self) -> List[dict]:
        """
        Get a list of all shipments with their tracking information.

        :return: A list of dictionaries containing shipment details.
        """
        return [shipment.get_tracking_info() for shipment in self.shipments]

# Example usage
if __name__ == "__main__":
    tracker = ShipmentTracker()
    
    # Create a new shipment
    shipment1 = tracker.create_shipment("New York", "Los Angeles", 10.5)
    
    # Update the shipment status
    tracker.update_shipment_status(shipment1.id, "In Transit")
    
    # Retrieve all shipments
    all_shipments = tracker.get_all_shipments()
    for shipment in all_shipments:
        print(shipment)
```
