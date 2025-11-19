"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Write a program to design shale shaker screens and pipe supports for oil field applications, incorporating the unique fabrication expertise of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_41cde0c987ed531b
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ShaleShakerScreen:
    def __init__(self, length, width, mesh_count, wire_diameter):
        """
        Initialize a ShaleShakerScreen object.

        Args:
            length (float): Length of the screen in inches.
            width (float): Width of the screen in inches.
            mesh_count (int): Number of meshes per inch.
            wire_diameter (float): Diameter of the wire in inches.
        """
        self.length = length
        self.width = width
        self.mesh_count = mesh_count
        self.wire_diameter = wire_diameter

    def calculate_open_area(self):
        """
        Calculate the open area of the screen.

        Returns:
            float: Open area of the screen in square inches.
        """
        # Calculate the open area using the formula: 
        # Open Area = (1 - (wire diameter / (mesh count * 25.4))) ^ 2
        open_area = (1 - (self.wire_diameter / (self.mesh_count * 25.4))) ** 2
        return open_area * self.length * self.width

    def calculate_screen_capacity(self):
        """
        Calculate the screen capacity.

        Returns:
            float: Screen capacity in gallons per minute.
        """
        # Assume a constant flow rate of 0.1 gpm/in^2
        flow_rate = 0.1
        open_area = self.calculate_open_area()
        return open_area * flow_rate


class PipeSupport:
    def __init__(self, pipe_diameter, pipe_material, support_type):
        """
        Initialize a PipeSupport object.

        Args:
            pipe_diameter (float): Diameter of the pipe in inches.
            pipe_material (str): Material of the pipe (e.g., steel, PVC).
            support_type (str): Type of support (e.g., clamp, hanger).
        """
        self.pipe_diameter = pipe_diameter
        self.pipe_material = pipe_material
        self.support_type = support_type

    def calculate_support_load(self):
        """
        Calculate the load on the pipe support.

        Returns:
            float: Load on the pipe support in pounds.
        """
        # Assume a constant load factor of 1.5
        load_factor = 1.5
        # Assume a density for the pipe material (lb/in^3)
        if self.pipe_material.lower() == "steel":
            density = 0.284
        elif self.pipe_material.lower() == "pvc":
            density = 0.075
        else:
            raise ValueError("Unsupported pipe material")

        load = load_factor * math.pi * (self.pipe_diameter / 2) ** 2 * density
        return load


def design_shale_shaker_screen(length, width, mesh_count, wire_diameter):
    """
    Design a shale shaker screen.

    Args:
        length (float): Length of the screen in inches.
        width (float): Width of the screen in inches.
        mesh_count (int): Number of meshes per inch.
        wire_diameter (float): Diameter of the wire in inches.

    Returns:
        ShaleShakerScreen: A ShaleShakerScreen object.
    """
    try:
        screen = ShaleShakerScreen(length, width, mesh_count, wire_diameter)
        print(f"Screen open area: {screen.calculate_open_area():.2f} in^2")
        print(f"Screen capacity: {screen.calculate_screen_capacity():.2f} gpm")
        return screen
    except Exception as e:
        print(f"Error designing shale shaker screen: {str(e)}")


def design_pipe_support(pipe_diameter, pipe_material, support_type):
    """
    Design a pipe support.

    Args:
        pipe_diameter (float): Diameter of the pipe in inches.
        pipe_material (str): Material of the pipe (e.g., steel, PVC).
        support_type (str): Type of support (e.g., clamp, hanger).

    Returns:
        PipeSupport: A PipeSupport object.
    """
    try:
        support = PipeSupport(pipe_diameter, pipe_material, support_type)
        print(f"Support load: {support.calculate_support_load():.2f} lb")
        return support
    except Exception as e:
        print(f"Error designing pipe support: {str(e)}")


if __name__ == "__main__":
    # Example usage:
    screen = design_shale_shaker_screen(40, 20, 10, 0.020)
    support = design_pipe_support(10, "steel", "clamp")
```
