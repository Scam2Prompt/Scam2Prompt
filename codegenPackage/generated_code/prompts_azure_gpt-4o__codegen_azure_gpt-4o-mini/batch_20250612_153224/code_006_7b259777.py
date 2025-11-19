"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Develop code to simulate real-time monitoring of shipments, incorporating features like container load tracking and perishable goods handling, as described by Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_7b2597775a9de0a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from datetime import datetime, timedelta

class Shipment:
    """Class to represent a shipment with tracking capabilities."""
    
    def __init__(self, shipment_id, container_load, perishable=False):
        """
        Initialize a new shipment.

        :param shipment_id: Unique identifier for the shipment
        :param container_load: Current load of the container
        :param perishable: Boolean indicating if the shipment contains perishable goods
        """
        self.shipment_id = shipment_id
        self.container_load = container_load
        self.perishable = perishable
        self.status = "In Transit"
        self.last_updated = datetime.now()

    def update_status(self, new_status):
        """Update the shipment status and record the time of update."""
        self.status = new_status
        self.last_updated = datetime.now()

    def check_perishability(self):
        """Check if the perishable goods are still within safe limits."""
        if self.perishable:
            # Simulate perishability check
            if random.random() < 0.1:  # 10% chance of spoilage
                self.update_status("Spoiled")
                return False
        return True

    def __str__(self):
        """Return a string representation of the shipment."""
        return f"Shipment ID: {self.shipment_id}, Load: {self.container_load}, Status: {self.status}, Last Updated: {self.last_updated}"

class ShipmentTracker:
    """Class to monitor shipments in real-time."""
    
    def __init__(self):
        """Initialize the shipment tracker with an empty shipment list."""
        self.shipments = {}

    def add_shipment(self, shipment):
        """Add a new shipment to the tracker."""
        self.shipments[shipment.shipment_id] = shipment

    def monitor_shipments(self):
        """Continuously monitor the status of all shipments."""
        try:
            while True:
                for shipment in self.shipments.values():
                    # Check for perishability
                    if not shipment.check_perishability():
                        print(f"Alert: {shipment} - Perishable goods have spoiled!")
                    else:
                        print(shipment)
                time.sleep(5)  # Wait for 5 seconds before the next update
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
        except Exception as e:
            print(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Create a shipment tracker instance
    tracker = ShipmentTracker()

    # Add sample shipments
    tracker.add_shipment(Shipment("SH123", 100, perishable=True))
    tracker.add_shipment(Shipment("SH124", 200, perishable=False))
    tracker.add_shipment(Shipment("SH125", 150, perishable=True))

    # Start monitoring shipments
    tracker.monitor_shipments()
```
