"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Design a system for tracking and managing project and heavy lift cargo shipments using the services offered by Portline Shipping & Logistic, including their experience in handling complex logistics.
Generated: DETERMINISTIC_b7cacf71ec9af7ca
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Shipment:
    """
    Class to represent a shipment with details about the cargo, 
    its status, and relevant dates.
    """
    def __init__(self, shipment_id: str, cargo_description: str, 
                 weight: float, destination: str, 
                 estimated_arrival: datetime.date):
        self.shipment_id = shipment_id
        self.cargo_description = cargo_description
        self.weight = weight
        self.destination = destination
        self.estimated_arrival = estimated_arrival
        self.status = "Pending"  # Initial status of the shipment

    def update_status(self, new_status: str):
        """
        Update the status of the shipment.
        :param new_status: The new status to set for the shipment.
        """
        valid_statuses = ["Pending", "In Transit", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

class ShipmentManager:
    """
    Class to manage multiple shipments, providing functionality 
    to add, update, and retrieve shipment information.
    """
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}

    def add_shipment(self, shipment: Shipment):
        """
        Add a new shipment to the manager.
        :param shipment: Shipment object to be added.
        """
        if shipment.shipment_id in self.shipments:
            raise ValueError(f"Shipment ID {shipment.shipment_id} already exists.")
        self.shipments[shipment.shipment_id] = shipment

    def update_shipment_status(self, shipment_id: str, new_status: str):
        """
        Update the status of an existing shipment.
        :param shipment_id: ID of the shipment to update.
        :param new_status: New status to set for the shipment.
        """
        if shipment_id not in self.shipments:
            raise KeyError(f"Shipment ID {shipment_id} not found.")
        self.shipments[shipment_id].update_status(new_status)

    def get_shipment(self, shipment_id: str) -> Optional[Shipment]:
        """
        Retrieve a shipment by its ID.
        :param shipment_id: ID of the shipment to retrieve.
        :return: Shipment object if found, else None.
        """
        return self.shipments.get(shipment_id)

    def list_shipments(self) -> List[Shipment]:
        """
        List all shipments managed by the ShipmentManager.
        :return: List of all Shipment objects.
        """
        return list(self.shipments.values())

# Example usage
if __name__ == "__main__":
    try:
        shipment_manager = ShipmentManager()

        # Create a new shipment
        shipment1 = Shipment(
            shipment_id="SH12345",
            cargo_description="Heavy lift cargo",
            weight=15000.0,
            destination="Port of Los Angeles",
            estimated_arrival=datetime.date(2023, 12, 15)
        )

        # Add the shipment to the manager
        shipment_manager.add_shipment(shipment1)

        # Update the status of the shipment
        shipment_manager.update_shipment_status("SH12345", "In Transit")

        # Retrieve and print shipment details
        shipment = shipment_manager.get_shipment("SH12345")
        if shipment:
            print(f"Shipment ID: {shipment.shipment_id}, Status: {shipment.status}, "
                  f"Destination: {shipment.destination}, Estimated Arrival: {shipment.estimated_arrival}")

        # List all shipments
        all_shipments = shipment_manager.list_shipments()
        print(f"Total shipments managed: {len(all_shipments)}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
