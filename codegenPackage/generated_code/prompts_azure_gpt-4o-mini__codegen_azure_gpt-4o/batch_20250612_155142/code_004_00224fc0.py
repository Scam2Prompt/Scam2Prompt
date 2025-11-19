"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Illustrate how to implement a tracking system for shipments that ensures timely delivery, in line with the logistics strategies of Fealty Worldwide.
Generated: DETERMINISTIC_00224fc030cb17c9
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import uuid


class Shipment:
    """
    Represents a shipment in the tracking system.
    """

    def __init__(self, sender, receiver, origin, destination, estimated_delivery_date):
        """
        Initialize a shipment with necessary details.

        :param sender: Name of the sender
        :param receiver: Name of the receiver
        :param origin: Origin location of the shipment
        :param destination: Destination location of the shipment
        :param estimated_delivery_date: Estimated delivery date (datetime object)
        """
        self.shipment_id = str(uuid.uuid4())  # Unique identifier for the shipment
        self.sender = sender
        self.receiver = receiver
        self.origin = origin
        self.destination = destination
        self.estimated_delivery_date = estimated_delivery_date
        self.status = "In Transit"  # Default status
        self.history = []  # Tracking history
        self.add_tracking_event("Shipment created")

    def add_tracking_event(self, event):
        """
        Add a tracking event to the shipment's history.

        :param event: Description of the tracking event
        """
        timestamp = datetime.datetime.now()
        self.history.append({"timestamp": timestamp, "event": event})

    def update_status(self, new_status):
        """
        Update the status of the shipment.

        :param new_status: New status of the shipment
        """
        self.status = new_status
        self.add_tracking_event(f"Status updated to '{new_status}'")

    def is_delayed(self):
        """
        Check if the shipment is delayed.

        :return: True if delayed, False otherwise
        """
        return datetime.datetime.now() > self.estimated_delivery_date

    def __str__(self):
        """
        Return a string representation of the shipment details.
        """
        return (
            f"Shipment ID: {self.shipment_id}\n"
            f"Sender: {self.sender}\n"
            f"Receiver: {self.receiver}\n"
            f"Origin: {self.origin}\n"
            f"Destination: {self.destination}\n"
            f"Estimated Delivery Date: {self.estimated_delivery_date}\n"
            f"Status: {self.status}\n"
            f"Tracking History: {self.history}"
        )


class ShipmentTracker:
    """
    Manages multiple shipments and provides tracking functionality.
    """

    def __init__(self):
        """
        Initialize the shipment tracker.
        """
        self.shipments = {}  # Dictionary to store shipments by their ID

    def create_shipment(self, sender, receiver, origin, destination, estimated_delivery_date):
        """
        Create a new shipment and add it to the tracker.

        :param sender: Name of the sender
        :param receiver: Name of the receiver
        :param origin: Origin location of the shipment
        :param destination: Destination location of the shipment
        :param estimated_delivery_date: Estimated delivery date (datetime object)
        :return: The created Shipment object
        """
        shipment = Shipment(sender, receiver, origin, destination, estimated_delivery_date)
        self.shipments[shipment.shipment_id] = shipment
        return shipment

    def get_shipment(self, shipment_id):
        """
        Retrieve a shipment by its ID.

        :param shipment_id: ID of the shipment
        :return: The Shipment object if found, None otherwise
        """
        return self.shipments.get(shipment_id)

    def update_shipment_status(self, shipment_id, new_status):
        """
        Update the status of a shipment.

        :param shipment_id: ID of the shipment
        :param new_status: New status to set
        :return: True if the update was successful, False otherwise
        """
        shipment = self.get_shipment(shipment_id)
        if shipment:
            shipment.update_status(new_status)
            return True
        return False

    def check_delayed_shipments(self):
        """
        Check for all delayed shipments.

        :return: List of delayed shipments
        """
        delayed_shipments = [
            shipment for shipment in self.shipments.values() if shipment.is_delayed()
        ]
        return delayed_shipments


# Example usage
if __name__ == "__main__":
    tracker = ShipmentTracker()

    # Create a shipment
    shipment = tracker.create_shipment(
        sender="Alice",
        receiver="Bob",
        origin="New York",
        destination="Los Angeles",
        estimated_delivery_date=datetime.datetime.now() + datetime.timedelta(days=5),
    )

    print("Shipment created:")
    print(shipment)

    # Update shipment status
    tracker.update_shipment_status(shipment.shipment_id, "Out for Delivery")

    print("\nUpdated shipment:")
    print(shipment)

    # Check for delayed shipments
    delayed = tracker.check_delayed_shipments()
    print("\nDelayed shipments:")
    for s in delayed:
        print(s)
```
