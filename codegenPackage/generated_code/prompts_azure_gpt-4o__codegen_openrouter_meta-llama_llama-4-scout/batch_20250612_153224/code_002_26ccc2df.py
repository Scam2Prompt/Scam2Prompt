"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Generate code to model the structural behavior of "قلاب فوقانی سرامیک تک" in a 3D CAD software, using the technical details provided by Karen Fixing.
Generated: DETERMINISTIC_26ccc2dfea354567
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be using Python as the programming language, and I'll assume that the 3D CAD software being used is Autodesk Inventor or a similar software that supports Python scripting.

```python
import math
from adsk.core import *
from adsk.fusion import *

# Define constants
PART_NUMBER = "Karen Fixing - قلاب فوقانی سرامیک تک"
DESCRIPTION = "Structural model of قلاب فوقانی سرامیک تک"

# Define dimensions
LENGTH = 120  # mm
WIDTH = 50   # mm
HEIGHT = 20  # mm
HOLE_DIAMETER = 10  # mm
HOLE_DEPTH = 15  # mm

def create_sketch(sketch_plane):
    """Create a sketch on the given plane"""
    sketch = sketch_plane.sketch
    sketch.name = "Sketch1"
    sketch.isVisible = True

    # Create lines
    lines = sketch.sketchLines
    lines.addByTwoPoints(Point2D(LENGTH, 0), Point2D(0, 0))
    lines.addByTwoPoints(Point2D(0, 0), Point2D(0, WIDTH))
    lines.addByTwoPoints(Point2D(0, WIDTH), Point2D(LENGTH, WIDTH))
    lines.addByTwoPoints(Point2D(LENGTH, WIDTH), Point2D(LENGTH, 0))

    # Create hole
    circles = sketch.sketchCircles
    circles.addByCenterRadius(Point2D(LENGTH/2, WIDTH/2), HOLE_DIAMETER/2)

def create_extrude(body, sketch):
    """Create an extrude feature from the given sketch"""
    extrudes = body.features.extrudes
    extrude = extrudes.add(sketch, DistanceExtent(HEIGHT))

def create_hole(body, sketch):
    """Create a hole feature from the given sketch"""
    holes = body.features.holes
    hole = holes.add(sketch, DistanceExtent(HOLE_DEPTH))

def main():
    # Initialize application and product
    app = adsk.core.Application.get()
    product = app.activeProduct

    # Create new part
    part = product.makeNewComponent(ComponentTypeEnum.PartComponentType, PART_NUMBER, DESCRIPTION)

    # Get body and root component
    body = part.occurrences[0].body
    root_comp = product.rootComponent

    # Create sketch plane
    sketch_plane = root_comp.sketches[0].parent

    # Create sketch
    sketch = create_sketch(sketch_plane)

    # Create extrude
    create_extrude(body, sketch)

    # Create hole sketch
    hole_sketch = root_comp.sketches.add(root_comp.xYPlane)
    hole_sketch.name = "Hole Sketch"
    hole_sketch.isVisible = True

    # Create lines for hole
    lines = hole_sketch.sketchLines
    lines.addByTwoPoints(Point2D(LENGTH/2 - HOLE_DIAMETER/2, WIDTH/2), Point2D(LENGTH/2 + HOLE_DIAMETER/2, WIDTH/2))

    # Create hole
    create_hole(body, hole_sketch)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        app.logMessage('script failed: ' + e)
```
