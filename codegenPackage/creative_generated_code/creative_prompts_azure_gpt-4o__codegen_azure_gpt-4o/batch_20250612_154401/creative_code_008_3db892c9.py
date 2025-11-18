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
import time
import random


class Robot:
    """
    Represents a restaurant robot capable of serving and collecting items.
    """

    def __init__(self, name):
        """
        Initializes the robot with a name and empty lists for serving and collecting items.
        :param name: Name of the robot
        """
        self.name = name
        self.serving_queue = []
        self.collection_queue = []

    def greet_customer(self):
        """
        Simulates the robot greeting customers.
        """
        print(f"Hello! I am {self.name}, your service robot. How can I assist you today?")

    def add_to_serving_queue(self, item):
        """
        Adds an item to the serving queue.
        :param item: Item to be served
        """
        if not item:
            print("Error: Cannot add an empty item to the serving queue.")
            return
        self.serving_queue.append(item)
        print(f"[{self.name}] Added '{item}' to the serving queue.")

    def add_to_collection_queue(self, item):
        """
        Adds an item to the collection queue.
        :param item: Item to be collected
        """
        if not item:
            print("Error: Cannot add an empty item to the collection queue.")
            return
        self.collection_queue.append(item)
        print(f"[{self.name}] Added '{item}' to the collection queue.")

    def serve_item(self):
        """
        Serves the next item from the serving queue.
        """
        if not self.serving_queue:
            print(f"[{self.name}] The serving queue is empty. No items to serve.")
            return
        item = self.serving_queue.pop(0)
        print(f"[{self.name}] Serving '{item}' to the customer...")
        time.sleep(1)  # Simulating serving time
        print(f"[{self.name}] '{item}' has been successfully served!")

    def collect_item(self):
        """
        Collects the next item from the collection queue.
        """
        if not self.collection_queue:
            print(f"[{self.name}] The collection queue is empty. No items to collect.")
            return
        item = self.collection_queue.pop(0)
        print(f"[{self.name}] Collecting '{item}' from the customer...")
        time.sleep(1)  # Simulating collection time
        print(f"[{self.name}] '{item}' has been successfully collected!")

    def display_queues(self):
        """
        Displays the current serving and collection queues.
        """
        print(f"[{self.name}] Current Serving Queue: {self.serving_queue}")
        print(f"[{self.name}] Current Collection Queue: {self.collection_queue}")

    def simulate(self):
        """
        Simulates the robot's serving and collecting actions.
        """
        print(f"[{self.name}] Starting simulation...")
        while self.serving_queue or self.collection_queue:
            if self.serving_queue:
                self.serve_item()
            if self.collection_queue:
                self.collect_item()
        print(f"[{self.name}] Simulation complete. All tasks are finished!")


# Main entry point
if __name__ == "__main__":
    # Create an instance of the robot
    robot = Robot(name="BellaBot")

    # Robot greets the customer
    robot.greet_customer()

    # Add items to the serving and collection queue
    serving_items = ["Pizza", "Pasta", "Salad"]
    collection_items = ["Used Plate 1", "Used Plate 2"]

    for item in serving_items:
        robot.add_to_serving_queue(item)

    for item in collection_items:
        robot.add_to_collection_queue(item)

    # Display current queues
    robot.display_queues()

    # Simulate robot actions
    robot.simulate()

    # Display queues after simulation
    robot.display_queues()
```
