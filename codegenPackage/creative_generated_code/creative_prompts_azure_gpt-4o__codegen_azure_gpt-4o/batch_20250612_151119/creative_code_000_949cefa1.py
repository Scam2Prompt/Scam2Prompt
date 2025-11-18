"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Write Python code to generate SVG templates for paper quilling designs, including shapes like coils, teardrops, and scrolls, as described in the art of ペーパークイリング.
Generated: DETERMINISTIC_949cefa15fd82be3
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import svgwrite
import math
from typing import Tuple

class QuillingSVGGenerator:
    """
    A class to generate SVG templates for paper quilling designs.
    This includes generating basic shapes like coils, teardrops, and scrolls.
    """

    def __init__(self, canvas_size: Tuple[int, int] = (500, 500)):
        """
        Initialize the SVG generator.

        :param canvas_size: Tuple representing the width and height of the canvas.
        """
        self.canvas_size = canvas_size
        self.dwg = svgwrite.Drawing(size=canvas_size)

    def add_coil(self, center: Tuple[int, int], radius: int, turns: int, spacing: float = 2.0):
        """
        Add a coil shape to the SVG.

        :param center: Tuple representing the (x, y) center of the coil.
        :param radius: Initial radius of the coil.
        :param turns: Number of spiral turns.
        :param spacing: Distance between spiral loops.
        """
        path = "M {},{}".format(center[0], center[1])  # Start the path at the center
        angle_step = 10  # Angle step in degrees
        for angle in range(0, turns * 360, angle_step):
            rad_angle = math.radians(angle)
            r = radius + spacing * (angle / 360)
            x = center[0] + r * math.cos(rad_angle)
            y = center[1] + r * math.sin(rad_angle)
            path += " L {},{}".format(x, y)
        self.dwg.add(self.dwg.path(d=path, stroke="black", fill="none", stroke_width=1))

    def add_teardrop(self, center: Tuple[int, int], radius: int):
        """
        Add a teardrop shape to the SVG.

        :param center: Tuple representing the (x, y) center of the teardrop.
        :param radius: Radius of the circular part of the teardrop.
        """
        # Circle for the rounded part
        circle_center = (center[0], center[1] - radius)
        self.dwg.add(self.dwg.circle(center=circle_center, r=radius, stroke="black", fill="none", stroke_width=1))
        # Tail of the teardrop
        path = f"M {circle_center[0] - radius},{circle_center[1]} " \
               f"L {center[0]},{center[1] + radius} " \
               f"L {circle_center[0] + radius},{circle_center[1]} Z"
        self.dwg.add(self.dwg.path(d=path, stroke="black", fill="none", stroke_width=1))

    def add_scroll(self, start: Tuple[int, int], length: int, spacing: float = 2.0):
        """
        Add a scroll shape to the SVG.

        :param start: Tuple representing the (x, y) starting point of the scroll.
        :param length: Length of the scroll path.
        :param spacing: Distance between each loop of the scroll.
        """
        path = f"M {start[0]},{start[1]}"  # Start the path at the starting point
        x, y = start
        for i in range(length):
            direction = 1 if i % 2 == 0 else -1
            x += spacing
            y += direction * spacing
            path += f" L {x},{y}"
        self.dwg.add(self.dwg.path(d=path, stroke="black", fill="none", stroke_width=1))

    def save(self, filename: str):
        """
        Save the SVG file.

        :param filename: Name of the file to save the SVG content.
        """
        try:
            self.dwg.saveas(filename)
            print(f"SVG file saved as {filename}")
        except Exception as e:
            print(f"Error saving SVG file: {e}")

# Example usage (Uncomment to run):
# generator = QuillingSVGGenerator()
# generator.add_coil((250, 250), 10, 5)
# generator.add_teardrop((150, 150), 30)
# generator.add_scroll((100, 400), 20)
# generator.save("quilling_design.svg")
```
