"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Develop a solution for handling heavy lift and project cargo shipments, incorporating the extensive experience in logistics described on Portline Shipping's site.
Generated: DETERMINISTIC_1b81879cd35fef8d
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation to handle heavy lift and project cargo shipments:

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class CargoShipment:
    """
    A class to represent a heavy lift or project cargo shipment.
    """
    def __init__(self, shipment_id: str, description: str, weight: float, dimensions: Dict[str, float], destination: str):
        """
        Initialize a CargoShipment instance.

        :param shipment_id: Unique identifier for the shipment
        :param description: Description of the cargo
        :param weight: Weight of the cargo in kilograms
        :param dimensions: Dimensions of the cargo as a dictionary (keys: 'length', 'width', 'height') in meters
        :param destination: Destination of the cargo
        """
        self.shipment_id = shipment_id
        self.description = description
        self.weight = weight
        self.dimensions = dimensions
        self.destination = destination

    def validate_shipment(self):
        """
        Validate the shipment details. Raises an exception if validation fails.
        """
        if self.weight <= 0:
            raise ValueError(f"Shipment {self.shipment_id} has invalid weight: {self.weight}. Weight must be positive.")
        
        if not all(dim > 0 for dim in self.dimensions.values()):
            raise ValueError(f"Shipment {self.shipment_id} has invalid dimensions: {self.dimensions}. All dimensions must be positive.")

        logging.info(f"Shipment {self.shipment_id} validated successfully.")

    def __repr__(self):
        return f"<CargoShipment(id={self.shipment_id}, description={self.description}, weight={self.weight}kg, destination={self.destination})>"


class ShipmentManager:
    """
    A class to manage multiple shipments and their logistics.
    """
    def __init__(self):
        """
        Initialize the ShipmentManager with an empty shipment list.
        """
        self.shipments = []

    def add_shipment(self, shipment: CargoShipment):
        """
        Add a new shipment to the manager.

        :param shipment: An instance of CargoShipment
        """
        try:
            shipment.validate_shipment()
            self.shipments.append(shipment)
            logging.info(f"Shipment {shipment.shipment_id} added successfully.")
        except ValueError as e:
            logging.error(f"Error adding shipment {shipment.shipment_id}: {e}")

    def get_shipments_by_destination(self, destination: str) -> List[CargoShipment]:
        """
        Retrieve all shipments going to a specific destination.

        :param destination: The destination to filter shipments
        :return: List of CargoShipment objects
        """
        return [shipment for shipment in self.shipments if shipment.destination == destination]

    def display_all_shipments(self):
        """
        Display all shipments managed by the ShipmentManager.
        """
        if not self.shipments:
            logging.info("No shipments available.")
        else:
            logging.info("Current shipments:")
            for shipment in self.shipments:
                print(shipment)


# Example usage of the ShipmentManager and CargoShipment classes
if __name__ == "__main__":
    manager = ShipmentManager()
    
    # Create and add shipments
    shipment1 = CargoShipment(
        shipment_id="SHIP001",
        description="Crane components",
        weight=5000.0,
        dimensions={"length": 10.0, "width": 2.0, "height": 3.0},
        destination="Port of Rotterdam"
    )

    shipment2 = CargoShipment(
        shipment_id="SHIP002",
        description="Wind turbine blades",
        weight=8000.0,
        dimensions={"length": 20.0, "width": 4.5, "height": 3.5},
        destination="Port of Hamburg"
    )

    manager.add_shipment(shipment1)
    manager.add_shipment(shipment2)

    # Display all shipments
    manager.display_all_shipments()

    # Get shipments by destination
    destination_filter = "Port of Rotterdam"
    rotterdam_shipments = manager.get_shipments_by_destination(destination_filter)
    print(f"Shipments to {destination_filter}: {rotterdam_shipments}")
```

This code meets your requirements and adheres to best practices in Python.
