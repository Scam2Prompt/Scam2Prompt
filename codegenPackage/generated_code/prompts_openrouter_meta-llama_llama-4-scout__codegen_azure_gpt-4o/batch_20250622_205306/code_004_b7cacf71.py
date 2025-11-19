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
"""
System for Tracking and Managing Project and Heavy Lift Cargo Shipments
using Portline Shipping & Logistic services.

This script provides functionality to manage shipments, track their status,
and handle complex logistics efficiently.
"""

import uuid
from datetime import datetime


class Shipment:
    """
    Represents a shipment in the system.
    """

    def __init__(self, project_name, cargo_description, origin, destination, weight, status="Pending"):
        """
        Initialize a new shipment.

        :param project_name: Name of the project associated with the shipment.
        :param cargo_description: Description of the cargo.
        :param origin: Origin location of the shipment.
        :param destination: Destination location of the shipment.
        :param weight: Weight of the cargo in kilograms.
        :param status: Current status of the shipment (default: "Pending").
        """
        self.shipment_id = str(uuid.uuid4())  # Unique identifier for the shipment
        self.project_name = project_name
        self.cargo_description = cargo_description
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = status
        self.created_at = datetime.now()

    def update_status(self, new_status):
        """
        Update the status of the shipment.

        :param new_status: New status to set for the shipment.
        """
        self.status = new_status

    def __str__(self):
        """
        String representation of the shipment.
        """
        return (
            f"Shipment ID: {self.shipment_id}\n"
            f"Project Name: {self.project_name}\n"
            f"Cargo Description: {self.cargo_description}\n"
            f"Origin: {self.origin}\n"
            f"Destination: {self.destination}\n"
            f"Weight: {self.weight} kg\n"
            f"Status: {self.status}\n"
            f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )


class ShipmentManager:
    """
    Manages shipments in the system.
    """

    def __init__(self):
        """
        Initialize the shipment manager.
        """
        self.shipments = {}  # Dictionary to store shipments by their ID

    def create_shipment(self, project_name, cargo_description, origin, destination, weight):
        """
        Create a new shipment and add it to the system.

        :param project_name: Name of the project associated with the shipment.
        :param cargo_description: Description of the cargo.
        :param origin: Origin location of the shipment.
        :param destination: Destination location of the shipment.
        :param weight: Weight of the cargo in kilograms.
        :return: The created Shipment object.
        """
        try:
            shipment = Shipment(project_name, cargo_description, origin, destination, weight)
            self.shipments[shipment.shipment_id] = shipment
            return shipment
        except Exception as e:
            print(f"Error creating shipment: {e}")
            return None

    def get_shipment(self, shipment_id):
        """
        Retrieve a shipment by its ID.

        :param shipment_id: ID of the shipment to retrieve.
        :return: The Shipment object if found, None otherwise.
        """
        return self.shipments.get(shipment_id, None)

    def update_shipment_status(self, shipment_id, new_status):
        """
        Update the status of a shipment.

        :param shipment_id: ID of the shipment to update.
        :param new_status: New status to set for the shipment.
        :return: True if the update was successful, False otherwise.
        """
        shipment = self.get_shipment(shipment_id)
        if shipment:
            shipment.update_status(new_status)
            return True
        else:
            print(f"Shipment with ID {shipment_id} not found.")
            return False

    def list_shipments(self):
        """
        List all shipments in the system.

        :return: List of all Shipment objects.
        """
        return list(self.shipments.values())


# Example usage
if __name__ == "__main__":
    manager = ShipmentManager()

    # Create a new shipment
    shipment = manager.create_shipment(
        project_name="Project Alpha",
        cargo_description="Heavy machinery for construction",
        origin="Port of Shanghai",
        destination="Port of Rotterdam",
        weight=5000
    )
    if shipment:
        print("Shipment created successfully:")
        print(shipment)

    # Update shipment status
    if manager.update_shipment_status(shipment.shipment_id, "In Transit"):
        print("\nShipment status updated successfully:")
        print(manager.get_shipment(shipment.shipment_id))

    # List all shipments
    print("\nAll shipments:")
    for s in manager.list_shipments():
        print(s)
```
