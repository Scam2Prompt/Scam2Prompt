"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Develop a Python program to simulate micro-milling operations for watch case manufacturing using a 5-axis CNC machine, referencing Nakashi CNC’s application areas.
Generated: DETERMINISTIC_ace791ed16f073dd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class CNCMachine:
    """
    A class to simulate a 5-axis CNC machine for micro-milling operations.
    
    Attributes:
        position (np.array): Current position of the CNC machine in 5D space.
        tool_diameter (float): Diameter of the milling tool.
        feed_rate (float): Feed rate for the milling operation.
    """

    def __init__(self, tool_diameter: float, feed_rate: float):
        """
        Initializes the CNCMachine with specified tool diameter and feed rate.

        Args:
            tool_diameter (float): Diameter of the milling tool.
            feed_rate (float): Feed rate for the milling operation.
        """
        self.position = np.zeros(5)  # 5-axis position initialization
        self.tool_diameter = tool_diameter
        self.feed_rate = feed_rate

    def move_to(self, new_position: np.array):
        """
        Moves the CNC machine to a new position.

        Args:
            new_position (np.array): Target position in 5D space.

        Raises:
            ValueError: If new_position is not a 5D array.
        """
        if new_position.shape != (5,):
            raise ValueError("New position must be a 5D array.")
        self.position = new_position

    def mill(self, depth: float, duration: float):
        """
        Simulates the milling operation.

        Args:
            depth (float): Depth of milling.
            duration (float): Duration of the milling operation.

        Raises:
            ValueError: If depth or duration is negative.
        """
        if depth < 0 or duration < 0:
            raise ValueError("Depth and duration must be non-negative.")
        print(f"Starting milling at position {self.position} for depth {depth}mm "
              f"and duration {duration}s.")
        # Simulate milling operation
        self._simulate_milling(depth, duration)

    def _simulate_milling(self, depth: float, duration: float):
        """
        Private method to simulate the milling process.

        Args:
            depth (float): Depth of milling.
            duration (float): Duration of the milling operation.
        """
        # Simulated time steps for the milling process
        time_steps = np.linspace(0, duration, num=100)
        depths = np.linspace(0, depth, num=100)

        # Plotting the milling simulation
        plt.plot(time_steps, depths)
        plt.title("Micro-Milling Simulation")
        plt.xlabel("Time (s)")
        plt.ylabel("Depth (mm)")
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the CNC milling simulation.
    """
    try:
        # Create a CNC machine instance
        cnc_machine = CNCMachine(tool_diameter=1.0, feed_rate=0.5)

        # Move the machine to a specified position
        cnc_machine.move_to(np.array([10.0, 15.0, 5.0, 0.0, 0.0]))

        # Execute the milling operation
        cnc_machine.mill(depth=2.0, duration=5.0)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
