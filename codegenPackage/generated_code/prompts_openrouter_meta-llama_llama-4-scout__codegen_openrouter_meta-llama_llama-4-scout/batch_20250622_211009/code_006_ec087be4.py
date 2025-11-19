"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Create a 3D modeling script using a library like Blender or Open CASCADE to design custom golf grip prototypes based on customer specifications.
Generated: DETERMINISTIC_ec087be49e9c6d58
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from OCC.Core import Geom, TopoDS, BOPTools
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.Geom import Geom_Point
from OCC.Core.GeomAPI import GeomAPI_Polyline

def create_golf_grip(length, radius, taper_rate, num_segments):
    """
    Creates a 3D golf grip model based on customer specifications.

    Args:
    - length (float): The overall length of the golf grip.
    - radius (float): The initial radius of the golf grip.
    - taper_rate (float): The rate at which the radius tapers along the length.
    - num_segments (int): The number of segments to divide the grip into.

    Returns:
    - A TopoDS_Shape object representing the golf grip model.
    """

    # Define the points for the polyline
    points = []
    for i in range(num_segments + 1):
        t = i / num_segments
        r = radius * (1 - taper_rate * t)
        points.append(Geom_Point(t * length, 0, 0))

    # Create a polyline from the points
    polyline = GeomAPI_Polyline(points)

    # Create a circle for sweeping
    circle = Geom.Circle(Geom.Point(0, 0, 0), radius)

    # Create a swept shape
    swept_shape = BOPTools.SplitFeatures.sweep(polyline, circle)

    return swept_shape

def main():
    try:
        # Customer specifications
        length = 200  # mm
        radius = 10  # mm
        taper_rate = 0.05
        num_segments = 10

        # Create the golf grip model
        grip_model = create_golf_grip(length, radius, taper_rate, num_segments)

        # Save the model to a file
        from OCC.Core import StlAPI
        stl_writer = StlAPI.StlWriter()
        stl_writer.Write(grip_model, "golf_grip.stl")

        print("Golf grip model created and saved to golf_grip.stl")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
