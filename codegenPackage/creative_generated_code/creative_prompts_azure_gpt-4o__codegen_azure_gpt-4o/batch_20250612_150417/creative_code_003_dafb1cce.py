"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Create code to design and export vinyl cutting templates in SVG format, optimized for the specifications provided on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_dafb1cce9e03d592
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import svgwrite
import os
from datetime import datetime


class VinylTemplateExporter:
    """
    A class to create and export vinyl cutting templates in SVG format.
    Optimized for "Impresion en Tabloide" specifications.
    """

    def __init__(self, width_mm, height_mm, margin_mm=10):
        """
        Initialize the SVG template exporter.

        :param width_mm: Width of the template in millimeters.
        :param height_mm: Height of the template in millimeters.
        :param margin_mm: Margin size in millimeters (default: 10mm).
        """
        self.width_mm = width_mm
        self.height_mm = height_mm
        self.margin_mm = margin_mm

    def create_template(self, design_elements=None):
        """
        Create an SVG template with optional design elements.

        :param design_elements: List of optional design elements (default: None).
                                Each element should be a dictionary with 'type' and 'parameters'.
                                Supported types: 'circle', 'rectangle', 'line'.
        :return: svgwrite.Drawing object representing the template.
        """
        # Convert dimensions to pixels (SVG uses 96 DPI standard)
        width_px = self.width_mm * 3.7795275591
        height_px = self.height_mm * 3.7795275591
        margin_px = self.margin_mm * 3.7795275591

        # Create SVG drawing
        dwg = svgwrite.Drawing(size=(f"{width_px}px", f"{height_px}px"), profile="tiny")

        # Add margin rectangle
        dwg.add(
            dwg.rect(
                insert=(margin_px, margin_px),
                size=(
                    f"{width_px - 2 * margin_px}px",
                    f"{height_px - 2 * margin_px}px",
                ),
                fill="none",
                stroke="black",
                stroke_width=1,
            )
        )

        # Add optional design elements
        if design_elements:
            for element in design_elements:
                if element["type"] == "circle":
                    dwg.add(
                        dwg.circle(
                            center=element["parameters"]["center"],
                            r=element["parameters"]["radius"],
                            fill=element["parameters"].get("fill", "none"),
                            stroke=element["parameters"].get("stroke", "black"),
                            stroke_width=element["parameters"].get("stroke_width", 1),
                        )
                    )
                elif element["type"] == "rectangle":
                    dwg.add(
                        dwg.rect(
                            insert=element["parameters"]["insert"],
                            size=element["parameters"]["size"],
                            fill=element["parameters"].get("fill", "none"),
                            stroke=element["parameters"].get("stroke", "black"),
                            stroke_width=element["parameters"].get("stroke_width", 1),
                        )
                    )
                elif element["type"] == "line":
                    dwg.add(
                        dwg.line(
                            start=element["parameters"]["start"],
                            end=element["parameters"]["end"],
                            stroke=element["parameters"].get("stroke", "black"),
                            stroke_width=element["parameters"].get("stroke_width", 1),
                        )
                    )
                else:
                    raise ValueError(f"Unsupported design element type: {element['type']}")

        return dwg

    def export_svg(self, filename, design_elements=None):
        """
        Export the SVG template to a file.

        :param filename: Name of the output file (with .svg extension).
        :param design_elements: Optional design elements to include (default: None).
        """
        try:
            # Create the template
            dwg = self.create_template(design_elements)

            # Save to file
            output_dir = "svg_templates"
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            dwg.saveas(filepath)
            print(f"SVG file exported successfully: {filepath}")
        except Exception as e:
            print(f"Error exporting SVG: {e}")


# Example usage
if __name__ == "__main__":
    # Template specifications based on "Impresion en Tabloide"
    WIDTH_MM = 432  # Example width in mm
    HEIGHT_MM = 279  # Example height in mm

    # Instantiate the exporter
    exporter = VinylTemplateExporter(WIDTH_MM, HEIGHT_MM)

    # Define sample design elements
    design_elements = [
        {"type": "circle", "parameters": {"center": (200, 150), "radius": 50, "stroke": "blue", "stroke_width": 2}},
        {"type": "rectangle", "parameters": {"insert": (50, 50), "size": (100, 150), "fill": "red", "stroke": "black"}},
        {"type": "line", "parameters": {"start": (0, 0), "end": (400, 200), "stroke": "green", "stroke_width": 3}},
    ]

    # Export template
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exporter.export_svg(f"vinyl_template_{timestamp}.svg", design_elements)
```
