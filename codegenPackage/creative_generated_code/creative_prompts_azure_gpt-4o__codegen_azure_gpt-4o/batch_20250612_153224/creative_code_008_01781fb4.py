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

class CNCMachine5Axis:
    """
    Class to simulate a 5-axis CNC engraving process for industrial molds and dies.
    """

    def __init__(self, workpiece_dimensions, tool_radius):
        """
        Initialize the CNC Machine with workpiece dimensions and tool specifications.

        :param workpiece_dimensions: Tuple (length, width, height) of the workpiece in mm.
        :param tool_radius: Radius of the engraving tool in mm.
        """
        self.workpiece_dimensions = workpiece_dimensions
        self.tool_radius = tool_radius
        self.workpiece = np.zeros(workpiece_dimensions)  # Simulates the workpiece as a 3D matrix
        self.tool_position = (0, 0, 0)  # Current position of the engraving tool (x, y, z)
        self.toolpath = []  # Stores the toolpath for visualization

    def move_tool(self, x, y, z):
        """
        Move the tool to a specific position in the workpiece.

        :param x: X-coordinate of the tool position.
        :param y: Y-coordinate of the tool position.
        :param z: Z-coordinate of the tool position.
        """
        if (0 <= x < self.workpiece_dimensions[0] and
            0 <= y < self.workpiece_dimensions[1] and
            0 <= z < self.workpiece_dimensions[2]):
            self.tool_position = (x, y, z)
            self.toolpath.append(self.tool_position)
        else:
            raise ValueError("Tool position is out of bounds. Ensure coordinates are within workpiece dimensions.")

    def engrave(self, depth):
        """
        Simulate engraving at the current tool position.

        :param depth: Engraving depth in mm.
        """
        x, y, z = self.tool_position
        engraving_depth = min(depth, self.workpiece_dimensions[2] - z)  # Ensure engraving doesn't exceed bounds
        
        for i in range(max(0, x - self.tool_radius), min(self.workpiece_dimensions[0], x + self.tool_radius + 1)):
            for j in range(max(0, y - self.tool_radius), min(self.workpiece_dimensions[1], y + self.tool_radius + 1)):
                for k in range(max(0, z), max(0, z + engraving_depth)):
                    # Simulate engraving effect by marking workpiece points as "engraved"
                    self.workpiece[i][j][k] = 1

    def visualize_toolpath(self):
        """
        Visualize the toolpath in 2D (projection) for simplicity.
        """
        if not self.toolpath:
            raise ValueError("No toolpath has been generated yet.")
        
        x_coords, y_coords, z_coords = zip(*self.toolpath)
        plt.figure(figsize=(8, 6))
        plt.plot(x_coords, y_coords, marker='o', label="Toolpath")
        plt.title("2D Projection of Toolpath")
        plt.xlabel("X Coordinate (mm)")
        plt.ylabel("Y Coordinate (mm)")
        plt.legend()
        plt.grid()
        plt.show()

def simulate_engraving_process():
    """
    Main function to simulate the engraving process.
    """
    try:
        # Define workpiece dimensions (length=200mm, width=200mm, height=50mm) and tool radius (5mm)
        cnc_machine = CNCMachine5Axis(workpiece_dimensions=(200, 200, 50), tool_radius=5)
        
        # Move tool and engrave along a predefined path
        cnc_machine.move_tool(50, 50, 0)
        cnc_machine.engrave(depth=10)
        
        cnc_machine.move_tool(100, 50, 0)
        cnc_machine.engrave(depth=15)
        
        cnc_machine.move_tool(150, 100, 10)
        cnc_machine.engrave(depth=5)
        
        # Visualize the toolpath
        cnc_machine.visualize_toolpath()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the simulation
if __name__ == "__main__":
    simulate_engraving_process()
```
