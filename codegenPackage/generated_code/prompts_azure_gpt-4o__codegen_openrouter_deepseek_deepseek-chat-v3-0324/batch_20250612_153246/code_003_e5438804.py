"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a program to create laser engraving designs for wedding place cards or baptism plaques, referencing the customization options mentioned on "La Graveuse Normande."
Generated: DETERMINISTIC_e5438804180e03f7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import svgwrite
from svgwrite import cm, mm
import argparse
import os
from typing import List, Dict, Optional

class LaserEngravingDesign:
    """
    A class to generate laser engraving designs for wedding place cards or baptism plaques.
    """
    
    def __init__(self, output_file: str = "design.svg", width: float = 100, height: float = 50):
        """
        Initialize the design with default parameters.
        
        Args:
            output_file: Output SVG filename
            width: Design width in mm
            height: Design height in mm
        """
        self.output_file = output_file
        self.width = width
        self.height = height
        self.dwg = svgwrite.Drawing(output_file, size=(f"{width}mm", f"{height}mm"))
        
    def add_text(
        self,
        text: str,
        x: float,
        y: float,
        font_size: float = 5,
        font_family: str = "Arial",
        font_weight: str = "normal",
        text_anchor: str = "middle",
        rotation: float = 0,
        fill: str = "black"
    ) -> None:
        """
        Add text to the design.
        
        Args:
            text: Text content
            x: X position in mm
            y: Y position in mm
            font_size: Font size in mm
            font_family: Font family
            font_weight: Font weight (normal/bold)
            text_anchor: Text anchor (start/middle/end)
            rotation: Rotation angle in degrees
            fill: Text color
        """
        self.dwg.add(
            self.dwg.text(
                text,
                insert=(x * mm, y * mm),
                font_size=f"{font_size}mm",
                font_family=font_family,
                font_weight=font_weight,
                text_anchor=text_anchor,
                transform=f"rotate({rotation}, {x * mm}, {y * mm})",
                fill=fill
            )
        )
    
    def add_decoration(
        self,
        element_type: str,
        position: List[float],
        size: List[float],
        rotation: float = 0,
        fill: str = "black",
        stroke: str = "none",
        stroke_width: float = 0.1
    ) -> None:
        """
        Add decorative elements to the design.
        
        Args:
            element_type: Type of element (rect/circle/ellipse/path)
            position: [x, y] position in mm
            size: Dimensions [width, height] in mm (or radius for circle)
            rotation: Rotation angle in degrees
            fill: Fill color
            stroke: Stroke color
            stroke_width: Stroke width in mm
        """
        x, y = position
        if element_type == "rect":
            element = self.dwg.rect(
                insert=(x * mm, y * mm),
                size=(size[0] * mm, size[1] * mm),
                fill=fill,
                stroke=stroke,
                stroke_width=f"{stroke_width}mm",
                transform=f"rotate({rotation}, {x * mm}, {y * mm})"
            )
        elif element_type == "circle":
            element = self.dwg.circle(
                center=(x * mm, y * mm),
                r=size[0] * mm,
                fill=fill,
                stroke=stroke,
                stroke_width=f"{stroke_width}mm"
            )
        elif element_type == "ellipse":
            element = self.dwg.ellipse(
                center=(x * mm, y * mm),
                r=(size[0] * mm, size[1] * mm),
                fill=fill,
                stroke=stroke,
                stroke_width=f"{stroke_width}mm",
                transform=f"rotate({rotation}, {x * mm}, {y * mm})"
            )
        elif element_type == "path":
            element = self.dwg.path(
                d=size[0],  # size[0] should contain the path data
                fill=fill,
                stroke=stroke,
                stroke_width=f"{stroke_width}mm",
                transform=f"translate({x * mm}, {y * mm}) rotate({rotation})"
            )
        else:
            raise ValueError(f"Unsupported element type: {element_type}")
        
        self.dwg.add(element)
    
    def add_border(
        self,
        margin: float = 5,
        stroke: str = "black",
        stroke_width: float = 0.2,
        corner_radius: Optional[float] = None
    ) -> None:
        """
        Add a border around the design.
        
        Args:
            margin: Margin from edge in mm
            stroke: Stroke color
            stroke_width: Stroke width in mm
            corner_radius: Corner radius for rounded rectangle (None for sharp corners)
        """
        x, y = margin, margin
        width = self.width - 2 * margin
        height = self.height - 2 * margin
        
        if corner_radius is not None:
            self.dwg.add(
                self.dwg.rect(
                    insert=(x * mm, y * mm),
                    size=(width * mm, height * mm),
                    rx=corner_radius * mm,
                    ry=corner_radius * mm,
                    fill="none",
                    stroke=stroke,
                    stroke_width=f"{stroke_width}mm"
                )
            )
        else:
            self.dwg.add(
                self.dwg.rect(
                    insert=(x * mm, y * mm),
                    size=(width * mm, height * mm),
                    fill="none",
                    stroke=stroke,
                    stroke_width=f"{stroke_width}mm"
                )
            )
    
    def save(self) -> None:
        """Save the design to an SVG file."""
        self.dwg.save()
        print(f"Design saved to {self.output_file}")

def create_wedding_place_card(
    name: str,
    output_file: str = "wedding_place_card.svg",
    font_family: str = "Arial",
    font_size: float = 6,
    decoration: Optional[str] = None
) -> None:
    """
    Create a wedding place card design.
    
    Args:
        name: Name to be engraved
        output_file: Output SVG filename
        font_family: Font family for the text
        font_size: Font size in mm
        decoration: Optional decoration type (hearts/flowers/none)
    """
    design = LaserEngravingDesign(output_file, width=80, height=40)
    
    # Add border
    design.add_border(margin=3, corner_radius=2)
    
    # Add name
    design.add_text(
        text=name,
        x=design.width / 2,
        y=design.height / 2,
        font_size=font_size,
        font_family=font_family,
        font_weight="bold",
        text_anchor="middle"
    )
    
    # Add decoration if specified
    if decoration == "hearts":
        design.add_decoration(
            element_type="path",
            position=[15, 10],
            size=["M10,30 Q15,20 20,30 Q25,40 10,50 Q-5,40 0,30 Q5,20 10,30"],
            fill="none",
            stroke="black",
            stroke_width=0.2
        )
        design.add_decoration(
            element_type="path",
            position=[design.width - 15, 10],
            size=["M10,30 Q15,20 20,30 Q25,40 10,50 Q-5,40 0,30 Q5,20 10,30"],
            fill="none",
            stroke="black",
            stroke_width=0.2
        )
    elif decoration == "flowers":
        design.add_decoration(
            element_type="path",
            position=[15, 10],
            size=["M10,30 Q15,25 20,30 Q25,35 20,40 Q15,45 10,40 Q5,35 10,30"],
            fill="none",
            stroke="black",
            stroke_width=0.2
        )
        design.add_decoration(
            element_type="path",
            position=[design.width - 15, 10],
            size=["M10,30 Q15,25 20,30 Q25,35 20,40 Q15,45 10,40 Q5,35 10,30"],
            fill="none",
            stroke="black",
            stroke_width=0.2
        )
    
    design.save()

def create_baptism_plaque(
    name: str,
    date: str,
    output_file: str = "baptism_plaque.svg",
    font_family: str = "Times New Roman",
    font_size: float = 5,
    decoration: Optional[str] = None
) -> None:
    """
    Create a baptism plaque design.
    
    Args:
        name: Name to be engraved
        date: Date of baptism
        output_file: Output SVG filename
        font_family: Font family for the text
        font_size: Font size in mm
        decoration: Optional decoration type (cross/d
