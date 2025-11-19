"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Generate a Python program to simulate the operation of a chain-type pipe cutting machine, ensuring compatibility with manual pipe end heating torches as described on the SPM Equipment website.
Generated: DETERMINISTIC_4005cac0ef2bd4d3
Batch ID: 20250612_153246
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

class PipeCuttingMachine:
    """
    A class to simulate the operation of a chain-type pipe cutting machine.
    This machine is compatible with manual pipe end heating torches.
    """

    def __init__(self, pipe_diameter, cutting_speed):
        """
        Initializes the PipeCuttingMachine with specified pipe diameter and cutting speed.

        :param pipe_diameter: Diameter of the pipe in inches
        :param cutting_speed: Speed of cutting in inches per minute
        """
        self.pipe_diameter = pipe_diameter
        self.cutting_speed = cutting_speed
        self.is_heating = False
        self.is_cutting = False

    def start_heating(self):
        """Simulates the start of the heating process for the pipe ends."""
        print("Starting the heating process...")
        self.is_heating = True
        time.sleep(2)  # Simulate heating time
        print("Heating completed.")

    def start_cutting(self):
        """Simulates the cutting process of the pipe."""
        if not self.is_heating:
            raise RuntimeError("Cannot start cutting without heating the pipe first.")
        
        print("Starting the cutting process...")
        self.is_cutting = True
        cutting_time = self.pipe_diameter / self.cutting_speed * 60  # Time in seconds
        time.sleep(cutting_time)  # Simulate cutting time
        print("Cutting completed.")

    def stop_cutting(self):
        """Stops the cutting process."""
        if self.is_cutting:
            print("Stopping the cutting process...")
            self.is_cutting = False
        else:
            print("Cutting process is not currently active.")

    def reset(self):
        """Resets the machine to its initial state."""
        print("Resetting the machine...")
        self.is_heating = False
        self.is_cutting = False

def main():
    """Main function to run the pipe cutting simulation."""
    try:
        # Initialize the pipe cutting machine with a diameter of 6 inches and a cutting speed of 2 inches per minute
        machine = PipeCuttingMachine(pipe_diameter=6, cutting_speed=2)

        # Start the heating process
        machine.start_heating()

        # Start the cutting process
        machine.start_cutting()

        # Stop the cutting process
        machine.stop_cutting()

        # Reset the machine for the next operation
        machine.reset()

    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
