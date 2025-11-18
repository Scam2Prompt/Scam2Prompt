"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Write a Python script to simulate 3D infrastructure designs using modern libraries, referencing the design principles outlined by Unison Plus.
Generated: DETERMINISTIC_9b110008df5a8614
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
3D Infrastructure Design Simulation Script

This script uses modern Python libraries to simulate 3D infrastructure designs
based on principles inspired by "Unison Plus." The script utilizes PyVista for
3D visualization and numpy for numerical computations.

Dependencies:
- pyvista
- numpy

Install missing dependencies using:
pip install pyvista numpy
"""

import pyvista as pv
import numpy as np

def generate_building(width, length, height):
    """
    Generates a 3D rectangular building with specified dimensions.

    Args:
        width (float): Width of the building.
        length (float): Length of the building.
        height (float): Height of the building.

    Returns:
        pyvista.PolyData: 3D representation of the building.
    """
    return pv.Cube(center=(width / 2, length / 2, height / 2), x_length=width, y_length=length, z_length=height)

def generate_road(start_point, end_point, width=2.0):
    """
    Generates a 3D road model as a rectangular prism connecting two points.

    Args:
        start_point (tuple): Starting coordinates of the road (x, y, z).
        end_point (tuple): Ending coordinates of the road (x, y, z).
        width (float): Width of the road.

    Returns:
        pyvista.PolyData: 3D representation of the road.
    """
    length = np.linalg.norm(np.array(end_point) - np.array(start_point))
    midpoint = [(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2, start_point[2]]
    return pv.Cube(center=(midpoint[0], midpoint[1], midpoint[2]), x_length=length, y_length=width, z_length=0.2)

def generate_park(center, radius=5.0):
    """
    Generates a 3D circular park model.

    Args:
        center (tuple): Center coordinates of the park (x, y, z).
        radius (float): Radius of the park.

    Returns:
        pyvista.PolyData: 3D representation of the park.
    """
    return pv.Sphere(center=center, radius=radius)

def main():
    """
    Main function to simulate and visualize a 3D infrastructure design.
    Error handling is included to ensure smooth execution.
    """
    try:
        # Create a PyVista plotter for visualization
        plotter = pv.Plotter()

        # Generate a sample building
        building = generate_building(width=10, length=15, height=20)
        plotter.add_mesh(building, color="lightblue", label="Building")

        # Generate a sample road
        road = generate_road(start_point=(0, 0, 0), end_point=(20, 0, 0))
        plotter.add_mesh(road, color="gray", label="Road")

        # Generate a sample park
        park = generate_park(center=(10, -10, 0), radius=5)
        plotter.add_mesh(park, color="green", label="Park")

        # Add labels and visualize
        plotter.add_legend()
        plotter.show(title="3D Infrastructure Design Simulation")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
