"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Recommend libraries for simulating industrial belt systems, focusing on "FAJAS ENVASADORA OSR" and their use in pharmaceutical packaging processes.
Generated: DETERMINISTIC_0d8e1d9e18274eaa
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

class ConveyorBelt:
    """
    A class to simulate an industrial conveyor belt system for pharmaceutical packaging.
    
    Attributes:
    - length (float): The length of the conveyor belt in meters.
    - speed (float): The speed of the conveyor belt in meters per second.
    - items (list): A list to hold items on the conveyor belt.
    """
    
    def __init__(self, length: float, speed: float):
        """
        Initializes the ConveyorBelt with a specified length and speed.

        Parameters:
        - length (float): The length of the conveyor belt.
        - speed (float): The speed of the conveyor belt.
        """
        if length <= 0 or speed <= 0:
            raise ValueError("Length and speed must be positive values.")
        
        self.length = length
        self.speed = speed
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the conveyor belt.

        Parameters:
        - item: The item to be added to the conveyor belt.
        """
        if len(self.items) >= self.length:
            raise OverflowError("Conveyor belt is full. Cannot add more items.")
        
        self.items.append(item)

    def simulate(self, time: float):
        """
        Simulates the movement of items on the conveyor belt over a specified time.

        Parameters:
        - time (float): The time duration for the simulation in seconds.
        """
        distance_covered = self.speed * time
        print(f"Items moved {distance_covered:.2f} meters in {time:.2f} seconds.")
        
        # Move items on the conveyor belt
        if distance_covered >= self.length:
            self.items.clear()  # All items have been processed and removed
            
    def display_items(self):
        """
        Displays the current items on the conveyor belt.
        """
        if not self.items:
            print("No items on the conveyor belt.")
        else:
            print(f"Current items on the conveyor belt: {self.items}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a conveyor belt with specified length and speed
        conveyor = ConveyorBelt(length=10.0, speed=1.0)
        
        # Add items to the conveyor belt
        conveyor.add_item("Box A")
        conveyor.add_item("Box B")
        conveyor.add_item("Box C")
        
        # Display items before simulation
        conveyor.display_items()
        
        # Simulate movement for 8 seconds
        conveyor.simulate(time=8)
        
        # Display items after simulation
        conveyor.display_items()
        
    except (ValueError, OverflowError) as e:
        print(f"Error: {e}")
```
