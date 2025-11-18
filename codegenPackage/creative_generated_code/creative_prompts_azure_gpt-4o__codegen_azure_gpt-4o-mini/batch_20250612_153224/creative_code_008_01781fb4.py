"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Write a script to model and simulate the engraving process for industrial molds and dies using 5-axis CNC machines, based on Nakashi CNC’s expertise.
Generated: DETERMINISTIC_01781fb4395d02e9
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

class CNC_Simulation:
    def __init__(self, tool_diameter: float, feed_rate: float, spindle_speed: float):
        """
        Initialize the CNC simulation parameters.

        :param tool_diameter: Diameter of the CNC tool in mm
        :param feed_rate: The feed rate in mm/min
        :param spindle_speed: The spindle speed in RPM
        """
        self.tool_diameter = tool_diameter
        self.feed_rate = feed_rate
        self.spindle_speed = spindle_speed
        self.path = []

    def add_tool_path(self, start_point: np.array, end_point: np.array):
        """
        Add a tool path segment from start_point to end_point.

        :param start_point: Starting coordinates (x, y, z) of the tool path
        :param end_point: Ending coordinates (x, y, z) of the tool path
        """
        if len(start_point) != 3 or len(end_point) != 3:
            raise ValueError("Start and end points must be 3D coordinates (x, y, z).")
        self.path.append((start_point, end_point))

    def simulate_engravings(self):
        """
        Simulate the engraving process along the defined tool path.
        """
        for start, end in self.path:
            self._engrave_segment(start, end)

    def _engrave_segment(self, start: np.array, end: np.array):
        """
        Engrave a segment from start to end.

        :param start: Starting coordinates of the segment
        :param end: Ending coordinates of the segment
        """
        # Calculate the distance and time required for this segment
        distance = np.linalg.norm(end - start)
        time_required = distance / (self.feed_rate / 60)  # time in minutes

        # Display engraving simulation details
        print(f"Engraving from {start} to {end}:")
        print(f" - Distance: {distance:.2f} mm")
        print(f" - Time Required: {time_required:.2f} minutes")
        print(f" - Tool Diameter: {self.tool_diameter} mm")
        print(f" - Feed Rate: {self.feed_rate} mm/min")
        print(f" - Spindle Speed: {self.spindle_speed} RPM")
        print("-----------------------------------")

    def visualize_path(self):
        """
        Visualize the engraving path in a 3D plot.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for start, end in self.path:
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], marker='o')

        ax.set_xlabel('X axis (mm)')
        ax.set_ylabel('Y axis (mm)')
        ax.set_zlabel('Z axis (mm)')
        ax.set_title('CNC Tool Path Simulation')
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize CNC Simulation with tool parameters
        cnc_simulation = CNC_Simulation(tool_diameter=5.0, feed_rate=200.0, spindle_speed=1500)

        # Define the tool paths
        cnc_simulation.add_tool_path(np.array([0, 0, 0]), np.array([100, 0, -10]))
        cnc_simulation.add_tool_path(np.array([100, 0, -10]), np.array([100, 50, -10]))
        cnc_simulation.add_tool_path(np.array([100, 50, -10]), np.array([0, 50, -10]))
        cnc_simulation.add_tool_path(np.array([0, 50, -10]), np.array([0, 0, -10]))

        # Simulate the engraving
        cnc_simulation.simulate_engravings()

        # Visualize the tool path
        cnc_simulation.visualize_path()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
