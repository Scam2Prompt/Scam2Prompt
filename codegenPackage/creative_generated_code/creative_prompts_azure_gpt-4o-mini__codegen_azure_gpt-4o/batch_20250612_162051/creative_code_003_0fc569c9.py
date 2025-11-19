"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Describe how to implement a conveyor system for transporting potatoes between washing and frying machines in a production line.
Generated: DETERMINISTIC_0fc569c96ce119cb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# conveyor_system.py

import time
import queue

class ConveyorSystem:
    """
    A class representing a conveyor system for transporting potatoes
    between washing and frying machines in a production line.
    """

    def __init__(self, capacity=100):
        """
        Initialize the conveyor system with a given capacity.

        Args:
            capacity (int): Maximum number of potatoes the conveyor can hold.
        """
        self.capacity = capacity
        self.conveyor_queue = queue.Queue(maxsize=capacity)

    def load_potato(self, potato):
        """
        Load a potato onto the conveyor. If the conveyor is full,
        it will raise an exception.

        Args:
            potato (str): Representation of a potato (e.g., 'Potato 1').

        Raises:
            queue.Full: Raised when the conveyor is full.
        """
        try:
            self.conveyor_queue.put(potato, timeout=5)  # Timeout prevents indefinite blocking.
            print(f"Loaded: {potato}")
        except queue.Full:
            print("Error: Conveyor is full. Cannot load potato.")

    def move_potato(self):
        """
        Move a potato off the conveyor and deliver it to the frying machine.

        Returns:
            str: Representation of the potato that was delivered.

        Raises:
            queue.Empty: Raised when the conveyor is empty.
        """
        try:
            potato = self.conveyor_queue.get(timeout=5)  # Timeout prevents indefinite blocking.
            print(f"Delivered: {potato}")
            return potato
        except queue.Empty:
            print("Error: Conveyor is empty. No potatoes to deliver.")

    def conveyor_status(self):
        """
        Get the current status of the conveyor.

        Returns:
            dict: A dictionary containing the number of potatoes on the conveyor
                  and its capacity.
        """
        return {
            "current_load": self.conveyor_queue.qsize(),
            "capacity": self.capacity
        }


# Simulate the conveyor system operation.
if __name__ == "__main__":
    # Initialize conveyor with a capacity of 10 potatoes.
    conveyor = ConveyorSystem(capacity=10)

    # Simulate loading potatoes onto the conveyor.
    for i in range(1, 12):  # Attempt to load more than the capacity.
        conveyor.load_potato(f"Potato {i}")
        time.sleep(0.5)  # Simulate loading time.

    # Check conveyor status.
    status = conveyor.conveyor_status()
    print(f"Conveyor Status: {status}")

    # Simulate moving potatoes off the conveyor.
    for _ in range(12):  # Attempt to deliver more than what is available.
        conveyor.move_potato()
        time.sleep(0.5)  # Simulate delivery time.

    # Final conveyor status.
    status = conveyor.conveyor_status()
    print(f"Final Conveyor Status: {status}")
```
