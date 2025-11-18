"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Develop code to simulate real-time monitoring of shipments, incorporating features like container load tracking and perishable goods handling, as described by Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_7b2597775a9de0a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading
from datetime import datetime, timedelta

# Shipment class to represent each shipment container
class Shipment:
    def __init__(self, container_id, is_perishable, load_weight):
        self.container_id = container_id
        self.is_perishable = is_perishable
        self.load_weight = load_weight
        self.status = 'In Transit'
        self.estimated_arrival = self.calculate_estimated_arrival()

    def calculate_estimated_arrival(self):
        # Assuming a fixed transit time of 5 days
        return datetime.now() + timedelta(days=5)

    def update_status(self, new_status):
        self.status = new_status
        print(f"[{datetime.now()}] Shipment {self.container_id} status updated to: {self.status}")

# ShipmentMonitor class to monitor multiple shipments in real-time
class ShipmentMonitor:
    def __init__(self):
        self.shipments = {}

    def add_shipment(self, shipment):
        self.shipments[shipment.container_id] = shipment
        print(f"[{datetime.now()}] Added shipment: {shipment.container_id}")

    def update_shipments(self):
        while True:
            for shipment in self.shipments.values():
                # Simulate random status updates
                if shipment.status == 'In Transit':
                    if random.random() < 0.1:  # 10% chance to change status
                        shipment.update_status('Delayed')
                    elif random.random() < 0.1:  # 10% chance to change status
                        shipment.update_status('Delivered')

                # Check for perishable goods handling
                if shipment.is_perishable and shipment.status == 'In Transit':
                    time_left = shipment.estimated_arrival - datetime.now()
                    if time_left < timedelta(days=1):  # Less than a day to arrival
                        shipment.update_status('Urgent - Arrive Soon')

            time.sleep(5)  # Update cycle every 5 seconds

# Example Usage
def main():
    # Create a shipment monitor
    monitor = ShipmentMonitor()
    
    # Adding sample shipments
    try:
        shipment1 = Shipment(container_id='C123', is_perishable=True, load_weight=150)
        shipment2 = Shipment(container_id='C124', is_perishable=False, load_weight=200)

        monitor.add_shipment(shipment1)
        monitor.add_shipment(shipment2)

        # Start the shipment monitoring in a separate thread
        monitor_thread = threading.Thread(target=monitor.update_shipments)
        monitor_thread.daemon = True  # Allow program to exit even if thread is running
        monitor_thread.start()

        # Keep the main thread alive to allow monitoring to continue
        while True:
            time.sleep(1)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
