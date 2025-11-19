"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Write Python code to generate SVG templates for paper quilling designs, including shapes like coils, teardrops, and scrolls, as described in the art of ペーパークイリング.
Generated: DETERMINISTIC_949cefa15fd82be3
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import svgwrite
from typing import List, Tuple, Optional

class QuillingSVGGenerator:
    """
    A class to generate SVG templates for paper quilling designs.
    Supports shapes like coils, teardrops, scrolls, and more.
    """
    
    def __init__(self, filename: str = "quilling_design.svg", size: Tuple[int, int] = (800, 600)):
        """
        Initialize the SVG generator.
        
        Args:
            filename: Output SVG filename
            size: Tuple of (width, height) for the SVG canvas
        """
        self.dwg = svgwrite.Drawing(filename=filename, size=size)
        self.dwg.add(self.dwg.rect(insert=(0, 0), size=size, fill="white"))
    
    def save(self) -> None:
        """Save the SVG file."""
        self.dwg.save()
    
    def add_coil(
        self,
        center: Tuple[float, float],
        radius: float,
        rotations: int = 5,
        stroke_width: float = 1.0,
        stroke_color: str = "black",
        fill_color: Optional[str] = None
    ) -> None:
        """
        Add a coil shape to the SVG.
        
        Args:
            center: (x, y) coordinates of the center
            radius: Radius of the coil
            rotations: Number of full rotations
            stroke_width: Width of the stroke
            stroke_color: Color of the stroke
            fill_color: Fill color (None for no fill)
        """
        path_data = []
        points = []
        
        for i in range(rotations * 360 + 1):
            angle = math.radians(i)
            r = radius * (1 - (i / (rotations * 360 * 1.5)))
            x = center[0] + r * math.cos(angle)
            y = center[1] + r * math.sin(angle)
            points.append((x, y))
        
        if points:
            path_data.append(f"M {points[0][0]},{points[0][1]}")
            for point in points[1:]:
                path_data.append(f"L {point[0]},{point[1]}")
        
        path = self.dwg.path(
            d=" ".join(path_data),
            fill=fill_color,
            stroke=stroke_color,
            stroke_width=stroke_width,
            fill_opacity=1.0 if fill_color else 0.0
        )
        self.dwg.add(path)
    
    def add_teardrop(
        self,
        center: Tuple[float, float],
        radius: float,
        angle: float = 0,
        stroke_width: float = 1.0,
        stroke_color: str = "black",
        fill_color: Optional[str] = None
    ) -> None:
        """
        Add a teardrop shape to the SVG.
        
        Args:
            center: (x, y) coordinates of the center
            radius: Radius of the teardrop
            angle: Rotation angle in degrees
            stroke_width: Width of the stroke
            stroke_color: Color of the stroke
            fill_color: Fill color (None for no fill)
        """
        angle_rad = math.radians(angle)
        points = []
        
        # Create the circular part
        for i in range(0, 270, 5):
            a = math.radians(i)
            x = center[0] + radius * math.cos(a + angle_rad)
            y = center[1] + radius * math.sin(a + angle_rad)
            points.append((x, y))
        
        # Create the point
        tip_x = center[0] + radius * 1.5 * math.cos(math.radians(225) + angle_rad)
        tip_y = center[1] + radius * 1.5 * math.sin(math.radians(225) + angle_rad)
        points.append((tip_x, tip_y))
        
        # Close the shape
        points.append(points[0])
        
        path_data = []
        if points:
            path_data.append(f"M {points[0][0]},{points[0][1]}")
            for point in points[1:]:
                path_data.append(f"L {point[0]},{point[1]}")
        
        path = self.dwg.path(
            d=" ".join(path_data),
            fill=fill_color,
            stroke=stroke_color,
            stroke_width=stroke_width,
            fill_opacity=1.0 if fill_color else 0.0
        )
        self.dwg.add(path)
    
    def add_scroll(
        self,
        start: Tuple[float, float],
        length: float,
        curl_radius: float,
        direction: str = "left",
        stroke_width: float = 1.0,
        stroke_color: str = "black",
        fill_color: Optional[str] = None
    ) -> None:
        """
        Add a scroll shape to the SVG.
        
        Args:
            start: (x, y) coordinates of the start point
            length: Length of the straight part
            curl_radius: Radius of the curl
            direction: "left" or "right" for curl direction
            stroke_width: Width of the stroke
            stroke_color: Color of the stroke
            fill_color: Fill color (None for no fill)
        """
        if direction not in ["left", "right"]:
            raise ValueError("Direction must be 'left' or 'right'")
        
        sign = -1 if direction == "left" else 1
        path_data = []
        
        # Straight part
        end_x = start[0] + length
        end_y = start[1]
        path_data.append(f"M {start[0]},{start[1]}")
        path_data.append(f"L {end_x},{end_y}")
        
        # Curled part
        center_x = end_x
        center_y = end_y + sign * curl_radius
        
        start_angle = 270 if direction == "left" else 90
        end_angle = 90 if direction == "left" else 270
        
        path_data.append(
            f"A {curl_radius},{curl_radius} 0 0 {1 if direction == 'left' else 0} "
            f"{center_x},{center_y + sign * curl_radius}"
        )
        
        path = self.dwg.path(
            d=" ".join(path_data),
            fill=fill_color,
            stroke=stroke_color,
            stroke_width=stroke_width,
            fill_opacity=1.0 if fill_color else 0.0
        )
        self.dwg.add(path)
    
    def add_marquise(
        self,
        center: Tuple[float, float],
        width: float,
        height: float,
        angle: float = 0,
        stroke_width: float = 1.0,
        stroke_color: str = "black",
        fill_color: Optional[str] = None
    ) -> None:
        """
        Add a marquise (eye) shape to the SVG.
        
        Args:
            center: (x, y) coordinates of the center
            width: Width of the marquise
            height: Height of the marquise
            angle: Rotation angle in degrees
            stroke_width: Width of the stroke
            stroke_color: Color of the stroke
            fill_color: Fill color (None for no fill)
        """
        angle_rad = math.radians(angle)
        points = []
        
        # Create the shape by combining two semicircles
        for i in range(0, 180, 5):
            a = math.radians(i)
            x = center[0] + (width/2) * math.cos(a + angle_rad)
            y = center[1] + (height/2) * math.sin(a + angle_rad)
            points.append((x, y))
        
        for i in range(180, 360, 5):
            a = math.radians(i)
            x = center[0] + (width/2) * math.cos(a + angle_rad)
            y = center[1] + (height/2) * math.sin(a + angle_rad)
            points.append((x, y))
        
        points.append(points[0])  # Close the shape
        
        path_data = []
        if points:
            path_data.append(f"M {points[0][0]},{points[0][1]}")
            for point in points[1:]:
                path_data.append(f"L {point[0]},{point[1]}")
        
        path = self.dwg.path(
            d=" ".join(path_data),
            fill=fill_color,
            stroke=stroke_color,
            stroke_width=stroke_width,
            fill_opacity=1.0 if fill_color else 0.0
        )
        self.dwg.add(path)
    
    def add_square(
        self,
        center: Tuple[float, float],
        size: float,
        angle: float = 0,
        stroke_width: float = 1.0,
        stroke_color: str = "black",
        fill_color: Optional[str] = None
    ) -> None:
        """
        Add a square shape
