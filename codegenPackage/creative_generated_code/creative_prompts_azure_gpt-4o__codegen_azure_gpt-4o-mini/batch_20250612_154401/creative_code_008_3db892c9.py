"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gsj-technology.com
Prompt: Create a simulation of a robot serving and collecting items in a restaurant, inspired by the functionalities of BellaBot and HolaBot described on the GSJ website.
Generated: DETERMINISTIC_3db892c9d285450b
Batch ID: 20250612_154401
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

class Item:
    """Class representing an item in the restaurant."""
    
    def __init__(self, name):
        self.name = name

class Robot:
    """Class representing a robot that serves and collects items in a restaurant."""
    
    def __init__(self, name):
        self.name = name
        self.served_items = []  # List to store served items
        self.collected_items = []  # List to store collected items
        self.lock = threading.Lock()  # To ensure thread-safe operations

    def serve_item(self, item):
        """Method to simulate serving an item."""
        time.sleep(random.uniform(0.5, 1.5))  # Simulate serving time
        with self.lock:
            self.served_items.append(item)
            print(f"{self.name} served {item.name}.")

    def collect_item(self, item):
        """Method to simulate collecting an item."""
        time.sleep(random.uniform(0.5, 1.5))  # Simulate collecting time
        with self.lock:
            self.collected_items.append(item)
            print(f"{self.name} collected {item.name}.")

    def run(self, service_queue, collection_queue):
        """Method to run the robot's serving and collecting tasks."""
        while True:
            if service_queue:
                item_to_serve = service_queue.pop(0)
                self.serve_item(item_to_serve)
            if collection_queue:
                item_to_collect = collection_queue.pop(0)
                self.collect_item(item_to_collect)
            time.sleep(0.5)  # Wait before the next action

def main():
    """Main function to simulate the restaurant robot operations."""
    # Create a list of items to be served
    items_to_serve = [Item(f"Dish {i}") for i in range(1, 6)]
    # Create a list of items to be collected
    items_to_collect = [Item(f"Plate {i}") for i in range(1, 4)]

    # Create a robot instance
    robot = Robot("BellaBot")

    # Setup service and collection queues
    service_queue = items_to_serve.copy()
    collection_queue = items_to_collect.copy()

    # Start the robot's serving and collecting tasks in a separate thread
    robot_thread = threading.Thread(target=robot.run, args=(service_queue, collection_queue), daemon=True)
    robot_thread.start()

    # Allow the simulation to run for a certain period
    try:
        time.sleep(10)  # Run the simulation for 10 seconds
    except KeyboardInterrupt:
        print("Simulation interrupted.")
    finally:
        print("Stopping the robot.")
        # Gracefully exit
        robot_thread.join(timeout=1)

if __name__ == "__main__":
    main()
```
