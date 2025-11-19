"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write code to design and export templates for engraved intercom or signage plaques, ensuring compatibility with laser engraving machines, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_ed046a93ab51093c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional
from pathlib import Path
import svgwrite
from svgwrite import mm

class MaterialType(Enum):
    """Supported materials for engraving."""
    ACRYLIC = "acrylic"
    WOOD = "wood"
    METAL = "metal"
    GLASS = "glass"

class FontType(Enum):
    """Supported font types for engraving."""
    SERIF = "serif"
    SANS_SERIF = "sans_serif"
    MONOSPACE = "monospace"
    SCRIPT = "script"

@dataclass
class EngravingText:
    """Text element to be engraved."""
    content: str
    font: FontType = FontType.SANS_SERIF
    size: int = 12  # in points
    bold: bool = False
    italic: bool = False
    x_pos: float = 0.0  # in mm
    y_pos: float = 0.0  # in mm

@dataclass
class EngravingLine:
    """Line element to be engraved."""
    x1: float  # in mm
    y1: float  # in mm
    x2: float  # in mm
    y2: float  # in mm
    thickness: float = 0.5  # in mm

@dataclass
class EngravingRectangle:
    """Rectangle element to be engraved."""
    x: float  # in mm
    y: float  # in mm
    width: float  # in mm
    height: float  # in mm
    thickness: float = 0.5  # in mm
    filled: bool = False

@dataclass
class EngravingTemplate:
    """Template for an engraved plaque."""
    name: str
    width: float  # in mm
    height: float  # in mm
    material: MaterialType
    texts: List[EngravingText] = None
    lines: List[EngravingLine] = None
    rectangles: List[EngravingRectangle] = None

    def __post_init__(self):
        if self.texts is None:
            self.texts = []
        if self.lines is None:
            self.lines = []
        if self.rectangles is None:
            self.rectangles = []

class TemplateExporter:
    """Handles exporting engraving templates to various formats."""
    
    @staticmethod
    def to_svg(template: EngravingTemplate, output_path: str) -> None:
        """Export template to SVG format compatible with laser engravers.
        
        Args:
            template: EngravingTemplate to export
            output_path: Path to save the SVG file
        """
        try:
            dwg = svgwrite.Drawing(output_path, size=(f"{template.width}mm", f"{template.height}mm"))
            dwg.viewbox(0, 0, template.width, template.height)

            # Add background rectangle
            dwg.add(dwg.rect(
                insert=(0, 0),
                size=(f"{template.width}mm", f"{template.height}mm"),
                fill="white"
            ))

            # Add rectangles
            for rect in template.rectangles:
                rect_element = dwg.rect(
                    insert=(rect.x * mm, rect.y * mm),
                    size=(rect.width * mm, rect.height * mm),
                    stroke="black",
                    stroke_width=f"{rect.thickness}mm",
                    fill="black" if rect.filled else "none"
                )
                dwg.add(rect_element)

            # Add lines
            for line in template.lines:
                line_element = dwg.line(
                    start=(line.x1 * mm, line.y1 * mm),
                    end=(line.x2 * mm, line.y2 * mm),
                    stroke="black",
                    stroke_width=f"{line.thickness}mm"
                )
                dwg.add(line_element)

            # Add texts
            for text in template.texts:
                style = []
                if text.bold:
                    style.append("font-weight:bold")
                if text.italic:
                    style.append("font-style:italic")
                
                text_element = dwg.text(
                    text.content,
                    insert=(text.x_pos * mm, text.y_pos * mm),
                    font_family=text.font.value,
                    font_size=f"{text.size}pt",
                    style=";".join(style) if style else None,
                    fill="black"
                )
                dwg.add(text_element)

            dwg.save()
        except Exception as e:
            raise ValueError(f"Failed to export SVG: {str(e)}")

    @staticmethod
    def to_json(template: EngravingTemplate, output_path: str) -> None:
        """Export template to JSON format for storage or transfer.
        
        Args:
            template: EngravingTemplate to export
            output_path: Path to save the JSON file
        """
        try:
            template_dict = asdict(template)
            # Convert Enums to their values
            template_dict["material"] = template_dict["material"]["value"]
            template_dict["texts"] = [
                {
                    **text,
                    "font": text["font"]["value"]
                }
                for text in template_dict["texts"]
            ]

            with open(output_path, 'w') as f:
                json.dump(template_dict, f, indent=2)
        except Exception as e:
            raise ValueError(f"Failed to export JSON: {str(e)}")

    @staticmethod
    def from_json(input_path: str) -> EngravingTemplate:
        """Import template from JSON file.
        
        Args:
            input_path: Path to JSON file
            
        Returns:
            Loaded EngravingTemplate
        """
        try:
            with open(input_path, 'r') as f:
                data = json.load(f)
            
            # Convert back to Enums
            data["material"] = MaterialType(data["material"])
            data["texts"] = [
                EngravingText(
                    content=text["content"],
                    font=FontType(text["font"]),
                    size=text["size"],
                    bold=text["bold"],
                    italic=text["italic"],
                    x_pos=text["x_pos"],
                    y_pos=text["y_pos"]
                )
                for text in data["texts"]
            ]
            data["lines"] = [EngravingLine(**line) for line in data.get("lines", [])]
            data["rectangles"] = [EngravingRectangle(**rect) for rect in data.get("rectangles", [])]

            return EngravingTemplate(**data)
        except Exception as e:
            raise ValueError(f"Failed to import JSON: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a sample template
    sample_template = EngravingTemplate(
        name="Office Door Sign",
        width=100,
        height=60,
        material=MaterialType.ACRYLIC,
        texts=[
            EngravingText(
                content="Conference Room",
                font=FontType.SANS_SERIF,
                size=18,
                bold=True,
                x_pos=10,
                y_pos=30
            )
        ],
        rectangles=[
            EngravingRectangle(
                x=5,
                y=5,
                width=90,
                height=50,
                thickness=1,
                filled=False
            )
        ]
    )

    # Export to SVG
    TemplateExporter.to_svg(sample_template, "office_door_sign.svg")

    # Export to JSON
    TemplateExporter.to_json(sample_template, "office_door_sign.json")

    # Import from JSON
    imported_template = TemplateExporter.from_json("office_door_sign.json")
```
