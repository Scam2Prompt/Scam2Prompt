"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Illustrate how to implement a tracking system for shipments that ensures timely delivery, in line with the logistics strategies of Fealty Worldwide.
Generated: DETERMINISTIC_00224fc030cb17c9
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Shipment:
    """
    A class to represent a shipment.
    """

    def __init__(self, shipment_id, origin, destination, expected_delivery):
        """
        Initializes a new Shipment instance.

        :param shipment_id: Unique identifier for the shipment
        :param origin: Origin address of the shipment
        :param destination: Destination address of the shipment
        :param expected_delivery: Expected delivery date (datetime object)
        """
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.expected_delivery = expected_delivery
        self.status = 'Pending'
        self.history = []

    def update_status(self, new_status):
        """
        Updates the status of the shipment.

        :param new_status: New status of the shipment
        """
        if new_status not in ['Pending', 'In Transit', 'Delivered', 'Delayed']:
            logging.error(f"Invalid status '{new_status}' for shipment ID {self.shipment_id}.")
            raise ValueError("Status must be one of: 'Pending', 'In Transit', 'Delivered', 'Delayed'.")

        self.status = new_status
        self.history.append((datetime.datetime.now(), new_status))
        logging.info(f"Shipment ID {self.shipment_id} status updated to '{new_status}'.")

    def is_on_time(self):
        """
        Checks if the shipment is on time.

        :return: True if the shipment is on time, False otherwise
        """
        is_on_time = datetime.datetime.now() <= self.expected_delivery
        logging.info(f"Shipment ID {self.shipment_id} on time: {is_on_time}.")
        return is_on_time


class ShipmentTracker:
    """
    A class to manage and track multiple shipments.
    """

    def __init__(self):
        """
        Initializes the Shipment Tracker with an empty shipment list.
        """
        self.shipments = {}

    def add_shipment(self, shipment):
        """
        Adds a new shipment to the tracker.

        :param shipment: Shipment object to add
        """
        if not isinstance(shipment, Shipment):
            logging.error("Invalid shipment object.")
            raise TypeError("Expected an instance of Shipment class.")
        
        self.shipments[shipment.shipment_id] = shipment
        logging.info(f"Shipment ID {shipment.shipment_id} added to tracker.")

    def update_shipment_status(self, shipment_id, new_status):
        """
        Updates the status of a shipment by its ID.

        :param shipment_id: Unique identifier for the shipment
        :param new_status: New status of the shipment
        """
        if shipment_id not in self.shipments:
            logging.error(f"Shipment ID {shipment_id} not found.")
            raise KeyError("Shipment ID not found.")

        shipment = self.shipments[shipment_id]
        shipment.update_status(new_status)

    def check_all_shipments(self):
        """
        Checks the status of all shipments and logs their timely status.
        """
        for shipment_id, shipment in self.shipments.items():
            shipment.is_on_time()


# Example usage of the Shipment and ShipmentTracker classes
if __name__ == "__main__":
    # Create a ShipmentTracker instance
    tracker = ShipmentTracker()

    # Create new shipments
    shipment1 = Shipment('001', 'New York', 'Los Angeles', datetime.datetime(2023, 12, 20))
    shipment2 = Shipment('002', 'Chicago', 'Houston', datetime.datetime(2023, 11, 15))

    # Add shipments to the tracker
    tracker.add_shipment(shipment1)
    tracker.add_shipment(shipment2)

    # Update shipment statuses
    tracker.update_shipment_status('001', 'In Transit')
    tracker.update_shipment_status('002', 'Delivered')

    # Check the status of all shipments
    tracker.check_all_shipments()
```
