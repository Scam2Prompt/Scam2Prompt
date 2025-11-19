"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a Python script to create templates for engraved plaques for machine tools, including material selection and text formatting, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_19312084ffd61d41
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

class Material(Enum):
    """Enum representing available materials for plaques."""
    BRASS = "Brass"
    STAINLESS_STEEL = "Stainless Steel"
    ALUMINUM = "Aluminum"
    PLASTIC = "Plastic"

class FontStyle(Enum):
    """Enum representing available font styles."""
    SERIF = "Serif"
    SANS_SERIF = "Sans-Serif"
    MONOSPACE = "Monospace"
    SCRIPT = "Script"

@dataclass
class PlaqueTemplate:
    """Dataclass representing a plaque template."""
    material: Material
    width_mm: float
    height_mm: float
    text_lines: List[str]
    font_style: FontStyle
    font_size_pt: int
    border_width_mm: float
    include_date: bool
    serial_number: Optional[str] = None

    def validate(self) -> None:
        """Validate the plaque template parameters."""
        if self.width_mm <= 0 or self.height_mm <= 0:
            raise ValueError("Width and height must be positive values")
        if self.border_width_mm < 0:
            raise ValueError("Border width cannot be negative")
        if self.font_size_pt <= 0:
            raise ValueError("Font size must be positive")
        if not self.text_lines:
            raise ValueError("At least one text line is required")

class PlaqueGenerator:
    """Class for generating plaque templates."""
    
    @staticmethod
    def generate_svg(template: PlaqueTemplate) -> str:
        """
        Generate SVG content for the plaque template.
        
        Args:
            template: PlaqueTemplate object containing design parameters
            
        Returns:
            str: SVG content as a string
        """
        template.validate()
        
        # Calculate dimensions
        content_width = template.width_mm - 2 * template.border_width_mm
        content_height = template.height_mm - 2 * template.border_width_mm
        
        # SVG header
        svg = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="{template.width_mm}mm" height="{template.height_mm}mm" 
     viewBox="0 0 {template.width_mm} {template.height_mm}"
     xmlns="http://www.w3.org/2000/svg">
"""
        # Background rectangle
        svg += f"""  <rect x="0" y="0" width="{template.width_mm}" height="{template.height_mm}" 
        fill="#f0f0f0" stroke="#333" stroke-width="0.5"/>
"""
        # Content area
        svg += f"""  <rect x="{template.border_width_mm}" y="{template.border_width_mm}" 
        width="{content_width}" height="{content_height}" 
        fill="white" stroke="#333" stroke-width="0.2"/>
"""
        # Text elements
        y_position = template.border_width_mm + 10  # Start 10mm from top border
        line_height = template.font_size_pt * 1.5 / 2.83465  # Convert pt to mm
        
        for i, line in enumerate(template.text_lines):
            svg += f"""  <text x="{template.width_mm / 2}" y="{y_position + i * line_height}" 
    font-family="{template.font_style.value}" font-size="{template.font_size_pt}" 
    text-anchor="middle" fill="black">{line}</text>
"""
        
        # Optional date
        if template.include_date:
            date_str = datetime.now().strftime("%Y-%m-%d")
            svg += f"""  <text x="{template.width_mm - template.border_width_mm - 5}" 
    y="{template.height_mm - template.border_width_mm - 2}" 
    font-family="{FontStyle.SANS_SERIF.value}" font-size="8" 
    text-anchor="end" fill="#666">{date_str}</text>
"""
        
        # Optional serial number
        if template.serial_number:
            svg += f"""  <text x="{template.border_width_mm + 5}" 
    y="{template.height_mm - template.border_width_mm - 2}" 
    font-family="{FontStyle.MONOSPACE.value}" font-size="8" 
    text-anchor="start" fill="#666">SN: {template.serial_number}</text>
"""
        
        svg += "</svg>"
        return svg
    
    @staticmethod
    def save_to_file(svg_content: str, filename: str) -> None:
        """
        Save SVG content to a file.
        
        Args:
            svg_content: SVG content as string
            filename: Output filename
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(svg_content)
        except IOError as e:
            raise IOError(f"Failed to save file: {e}")

def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate engraved plaque templates for machine tools")
    parser.add_argument('--material', type=str, choices=[m.value for m in Material], 
                        default=Material.BRASS.value, help="Plaque material")
    parser.add_argument('--width', type=float, default=100.0, help="Plaque width in mm")
    parser.add_argument('--height', type=float, default=50.0, help="Plaque height in mm")
    parser.add_argument('--text', type=str, nargs='+', required=True, 
                        help="Text lines for the plaque")
    parser.add_argument('--font', type=str, choices=[f.value for f in FontStyle], 
                        default=FontStyle.SANS_SERIF.value, help="Font style")
    parser.add_argument('--font-size', type=int, default=12, help="Font size in points")
    parser.add_argument('--border', type=float, default=5.0, help="Border width in mm")
    parser.add_argument('--date', action='store_true', help="Include current date")
    parser.add_argument('--serial', type=str, help="Serial number to include")
    parser.add_argument('--output', type=str, default="plaque_template.svg", 
                        help="Output SVG filename")
    
    args = parser.parse_args()
    
    try:
        # Create template
        template = PlaqueTemplate(
            material=Material(args.material),
            width_mm=args.width,
            height_mm=args.height,
            text_lines=args.text,
            font_style=FontStyle(args.font),
            font_size_pt=args.font_size,
            border_width_mm=args.border,
            include_date=args.date,
            serial_number=args.serial
        )
        
        # Generate and save SVG
        generator = PlaqueGenerator()
        svg = generator.generate_svg(template)
        generator.save_to_file(svg, args.output)
        
        print(f"Successfully created plaque template: {args.output}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
