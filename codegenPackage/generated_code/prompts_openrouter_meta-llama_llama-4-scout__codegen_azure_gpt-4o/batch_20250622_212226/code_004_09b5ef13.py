"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: "Generate a code example for coordinating multiple delivery robots, like BellaBot, to optimize food delivery in a large restaurant or hotel setting."
Generated: DETERMINISTIC_09b5ef138086bad1
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import queue
import time
import random

# Constants
NUM_ROBOTS = 5  # Number of delivery robots
NUM_ORDERS = 20  # Number of food orders
MAX_CAPACITY = 3  # Maximum orders a robot can carry
DELIVERY_TIME = 5  # Time taken for a robot to deliver an order (in seconds)

# Order queue (shared resource)
order_queue = queue.Queue()

# Robot class
class DeliveryRobot(threading.Thread):
    def __init__(self, robot_id):
        super().__init__()
        self.robot_id = robot_id
        self.current_orders = []

    def run(self):
        while True:
            try:
                # Check if the robot can pick up more orders
                while len(self.current_orders) < MAX_CAPACITY and not order_queue.empty():
                    order = order_queue.get_nowait()
                    self.current_orders.append(order)
                    print(f"Robot {self.robot_id} picked up order {order}")

                # Deliver orders if the robot has any
                if self.current_orders:
                    print(f"Robot {self.robot_id} is delivering orders: {self.current_orders}")
                    time.sleep(DELIVERY_TIME)  # Simulate delivery time
                    print(f"Robot {self.robot_id} completed delivery of orders: {self.current_orders}")
                    self.current_orders.clear()

                # Exit if no more orders in the queue and no orders to deliver
                if order_queue.empty() and not self.current_orders:
                    print(f"Robot {self.robot_id} is shutting down (no more orders).")
                    break

            except Exception as e:
                print(f"Error in Robot {self.robot_id}: {e}")

# Function to simulate order generation
def generate_orders():
    for i in range(1, NUM_ORDERS + 1):
        order_queue.put(f"Order-{i}")
        print(f"Generated {order_queue.qsize()} orders in the queue.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random order generation time

# Main function
def main():
    # Start order generation in a separate thread
    order_thread = threading.Thread(target=generate_orders)
    order_thread.start()

    # Initialize and start robots
    robots = [DeliveryRobot(robot_id=i) for i in range(1, NUM_ROBOTS + 1)]
    for robot in robots:
        robot.start()

    # Wait for all threads to complete
    order_thread.join()
    for robot in robots:
        robot.join()

    print("All orders have been delivered. System shutting down.")

# Entry point
if __name__ == "__main__":
    main()
```
