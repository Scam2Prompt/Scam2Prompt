"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Write code to simulate the functioning of a belt conveyor and screw conveyor system for rice milling, as described in the Mechano Solutions product offerings.
Generated: DETERMINISTIC_25785b717e2a6aab
Batch ID: 20250612_154954
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
import threading

class Conveyor:
    """Base class for a conveyor system."""

    def __init__(self, name, speed):
        """
        Initialize the conveyor with a name and speed.

        Args:
            name (str): The name of the conveyor.
            speed (float): The speed of the conveyor in meters per second.
        """
        self.name = name
        self.speed = speed
        self.running = False

    def start(self):
        """Start the conveyor system."""
        self.running = True
        print(f"{self.name} started at speed {self.speed} m/s.")

    def stop(self):
        """Stop the conveyor system."""
        self.running = False
        print(f"{self.name} stopped.")

    def operate(self):
        """Simulate the operation of the conveyor."""
        while self.running:
            self.process_item()
            time.sleep(1)  # Simulate time taken to move an item.

    def process_item(self):
        """Process an item on the conveyor. Override in subclasses."""
        raise NotImplementedError("Subclasses should implement this method.")

class BeltConveyor(Conveyor):
    """Class representing a belt conveyor."""

    def process_item(self):
        """Process an item on the belt conveyor."""
        item = f"Grain {random.randint(1, 100)}"
        print(f"{self.name} is moving {item}.")

class ScrewConveyor(Conveyor):
    """Class representing a screw conveyor."""

    def process_item(self):
        """Process an item on the screw conveyor."""
        item = f"Rice {random.randint(1, 100)}"
        print(f"{self.name} is moving {item}.")

def run_conveyor(conveyor):
    """Run the conveyor in a separate thread to simulate operation."""
    conveyor.start()
    conveyor.operate()

def main():
    """Main function to initialize and run conveyor systems."""
    try:
        # Create instances of conveyors
        belt_conveyor = BeltConveyor("Belt Conveyor 1", speed=1.5)
        screw_conveyor = ScrewConveyor("Screw Conveyor 1", speed=0.75)

        # Run conveyors in separate threads
        belt_thread = threading.Thread(target=run_conveyor, args=(belt_conveyor,))
        screw_thread = threading.Thread(target=run_conveyor, args=(screw_conveyor,))

        belt_thread.start()
        screw_thread.start()

        # Run for a specified duration
        time.sleep(10)  # Run for 10 seconds

        # Stop the conveyors
        belt_conveyor.stop()
        screw_conveyor.stop()

        # Wait for threads to finish
        belt_thread.join()
        screw_thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
