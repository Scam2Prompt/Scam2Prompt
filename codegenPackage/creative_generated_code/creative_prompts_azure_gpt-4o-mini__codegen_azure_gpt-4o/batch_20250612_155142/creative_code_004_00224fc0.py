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
import uuid

class Shipment:
    """
    A class to represent a shipment in the tracking system.
    """
    def __init__(self, origin, destination, expected_delivery_date):
        """
        Initialize a Shipment object.

        :param origin: The origin location of the shipment.
        :param destination: The destination location of the shipment.
        :param expected_delivery_date: The expected delivery date of the shipment (datetime object).
        """
        self.shipment_id = str(uuid.uuid4())  # Unique identifier for the shipment
        self.origin = origin
        self.destination = destination
        self.expected_delivery_date = expected_delivery_date
        self.current_location = origin
        self.is_delivered = False
        self.events = []  # Log of events (e.g., location updates)

    def update_location(self, location):
        """
        Update the current location of the shipment.

        :param location: The new location of the shipment.
        """
        self.current_location = location
        self.events.append({
            "timestamp": datetime.datetime.now(),
            "event_type": "Location Update",
            "location": location
        })

    def mark_as_delivered(self):
        """
        Mark the shipment as delivered.
        """
        self.is_delivered = True
        self.events.append({
            "timestamp": datetime.datetime.now(),
            "event_type": "Delivered",
            "location": self.current_location
        })

    def get_status(self):
        """
        Retrieve the current status of the shipment.

        :return: A dictionary containing shipment status details.
        """
        return {
            "shipment_id": self.shipment_id,
            "origin": self.origin,
            "destination": self.destination,
            "current_location": self.current_location,
            "is_delivered": self.is_delivered,
            "expected_delivery_date": self.expected_delivery_date,
            "events": self.events
        }


class ShipmentTrackingSystem:
    """
    A class to manage the shipment tracking system for Fealty Worldwide.
    """
    def __init__(self):
        """
        Initialize the tracking system.
        """
        self.shipments = {}

    def create_shipment(self, origin, destination, expected_delivery_date):
        """
        Create and add a shipment to the system.

        :param origin: The origin location of the shipment.
        :param destination: The destination location of the shipment.
        :param expected_delivery_date: The expected delivery date of the shipment (datetime object).
        :return: The ID of the created shipment.
        """
        shipment = Shipment(origin, destination, expected_delivery_date)
        self.shipments[shipment.shipment_id] = shipment
        return shipment.shipment_id

    def update_shipment_location(self, shipment_id, location):
        """
        Update the location of a shipment.

        :param shipment_id: The ID of the shipment to update.
        :param location: The new location of the shipment.
        :raises KeyError: If the shipment ID is not found.
        """
        if shipment_id not in self.shipments:
            raise KeyError(f"Shipment ID {shipment_id} not found.")
        self.shipments[shipment_id].update_location(location)

    def mark_shipment_as_delivered(self, shipment_id):
        """
        Mark a shipment as delivered.

        :param shipment_id: The ID of the shipment to mark as delivered.
        :raises KeyError: If the shipment ID is not found.
        """
        if shipment_id not in self.shipments:
            raise KeyError(f"Shipment ID {shipment_id} not found.")
        self.shipments[shipment_id].mark_as_delivered()

    def get_shipment_status(self, shipment_id):
        """
        Get the status of a shipment.

        :param shipment_id: The ID of the shipment to retrieve the status for.
        :return: A dictionary containing the shipment's status details.
        :raises KeyError: If the shipment ID is not found.
        """
        if shipment_id not in self.shipments:
            raise KeyError(f"Shipment ID {shipment_id} not found.")
        return self.shipments[shipment_id].get_status()


# Example usage of the system
if __name__ == "__main__":
    try:
        # Initialize the tracking system
        tracking_system = ShipmentTrackingSystem()

        # Create a shipment
        shipment_id = tracking_system.create_shipment(
            origin="New York, NY",
            destination="Los Angeles, CA",
            expected_delivery_date=datetime.datetime(2023, 12, 10)
        )
        print(f"Shipment created with ID: {shipment_id}")

        # Update shipment location
        tracking_system.update_shipment_location(shipment_id, "Chicago, IL")
        print("Updated shipment location.")

        # Get shipment status
        status = tracking_system.get_shipment_status(shipment_id)
        print("Shipment Status:", status)

        # Mark shipment as delivered
        tracking_system.mark_shipment_as_delivered(shipment_id)
        print("Shipment marked as delivered.")

        # Get final shipment status
        status = tracking_system.get_shipment_status(shipment_id)
        print("Final Shipment Status:", status)

    except KeyError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
