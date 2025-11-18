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
import time
import random

# Define classes for handling shipments and containers
class Container:
    """
    Represents a shipping container with a unique ID, type of goods, and weight.
    """
    def __init__(self, container_id, goods_type, weight, is_perishable=False):
        self.container_id = container_id
        self.goods_type = goods_type
        self.weight = weight
        self.is_perishable = is_perishable
        self.temperature = None

        # Set default temperature for perishable goods
        if is_perishable:
            self.temperature = random.uniform(0, 10)  # Default range for perishable goods

    def update_temperature(self):
        """
        Simulates temperature fluctuations for perishable goods.
        """
        if self.is_perishable:
            self.temperature += random.uniform(-1, 1)
            # Ensure temperature stays within a safe range
            if self.temperature < 0 or self.temperature > 10:
                self.temperature = random.uniform(0, 10)

class Shipment:
    """
    Represents a shipment containing multiple containers.
    """
    def __init__(self, shipment_id):
        self.shipment_id = shipment_id
        self.containers = []

    def add_container(self, container):
        """
        Adds a container to the shipment.
        :param container: Instance of Container class to be added to the shipment.
        """
        if not isinstance(container, Container):
            raise ValueError("Invalid container object")
        self.containers.append(container)

    def monitor_containers(self):
        """
        Monitors all containers in the shipment.
        Logs perishable goods temperature and container load status in real-time.
        """
        for container in self.containers:
            if container.is_perishable:
                container.update_temperature()
            print(f"Shipment ID: {self.shipment_id}, "
                  f"Container ID: {container.container_id}, "
                  f"Goods Type: {container.goods_type}, "
                  f"Weight: {container.weight}kg, "
                  f"Perishable: {'Yes' if container.is_perishable else 'No'}, "
                  f"{'Temperature: {:.2f}°C'.format(container.temperature) if container.is_perishable else ''}")

# Utility function for real-time monitoring
def simulate_real_time_monitoring(shipments, interval=5):
    """
    Simulates real-time monitoring of shipments.
    :param shipments: List of Shipment objects to monitor.
    :param interval: Time interval (in seconds) between monitoring updates.
    """
    try:
        while True:
            print("\nReal-time Monitoring Update:")
            for shipment in shipments:
                shipment.monitor_containers()
            time.sleep(interval)
    except KeyboardInterrupt:
        # Gracefully exit monitoring on user interrupt (Ctrl + C)
        print("\nMonitoring stopped by user.")

# Create sample data
def create_sample_shipments():
    shipment1 = Shipment("SHP001")
    shipment2 = Shipment("SHP002")

    shipment1.add_container(Container("CNT001", "Electronics", 1200))
    shipment1.add_container(Container("CNT002", "Fresh Apples", 750, is_perishable=True))

    shipment2.add_container(Container("CNT003", "Furniture", 2200))
    shipment2.add_container(Container("CNT004", "Frozen Fish", 600, is_perishable=True))

    return [shipment1, shipment2]

# Entry point for the script
if __name__ == "__main__":
    print("Starting real-time shipment monitoring...")
    try:
        shipments = create_sample_shipments()
        simulate_real_time_monitoring(shipments)
    except Exception as e:
        print(f"Error occurred: {e}")
```
