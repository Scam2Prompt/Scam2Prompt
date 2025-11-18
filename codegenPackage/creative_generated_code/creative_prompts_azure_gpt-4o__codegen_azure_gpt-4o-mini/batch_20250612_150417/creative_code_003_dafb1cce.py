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
from svgwrite import cm, mm

class VinylTemplateGenerator:
    def __init__(self, width_mm, height_mm, output_file):
        """
        Initializes the VinylTemplateGenerator with the specified dimensions and output file.
        
        :param width_mm: Width of the template in millimeters.
        :param height_mm: Height of the template in millimeters.
        :param output_file: The filename for the output SVG file.
        """
        self.width = width_mm * mm  # Convert mm to SVG units
        self.height = height_mm * mm  # Convert mm to SVG units
        self.output_file = output_file
        self.dwg = svgwrite.Drawing(self.output_file, size=(self.width, self.height))

    def create_rectangle(self, x, y, width, height, fill='none', stroke='black'):
        """
        Adds a rectangle to the SVG drawing.

        :param x: The x-coordinate of the rectangle.
        :param y: The y-coordinate of the rectangle.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param fill: Fill color for the rectangle.
        :param stroke: Stroke color for the rectangle.
        """
        self.dwg.add(self.dwg.rect(insert=(x * mm, y * mm), size=(width * mm, height * mm),
                                    fill=fill, stroke=stroke))

    def create_circle(self, cx, cy, r, fill='none', stroke='black'):
        """
        Adds a circle to the SVG drawing.

        :param cx: The x-coordinate of the center of the circle.
        :param cy: The y-coordinate of the center of the circle.
        :param r: The radius of the circle.
        :param fill: Fill color for the circle.
        :param stroke: Stroke color for the circle.
        """
        self.dwg.add(self.dwg.circle(center=(cx * mm, cy * mm), r=r * mm,
                                      fill=fill, stroke=stroke))

    def save(self):
        """
        Saves the SVG drawing to the specified file.
        """
        try:
            self.dwg.save()
            print(f"SVG file '{self.output_file}' has been saved successfully.")
        except Exception as e:
            print(f"Error saving SVG file: {e}")

    def build_template(self):
        """
        Builds the vinyl cutting template with predefined shapes.
        """
        try:
            # Example: Create a rectangle template
            self.create_rectangle(10, 10, 100, 50, fill='lightblue', stroke='black')
            
            # Example: Create a circle template
            self.create_circle(60, 40, 15, fill='lightgreen', stroke='black')
            
            self.save()
        except Exception as e:
            print(f"Error while building template: {e}")

# Usage example
if __name__ == "__main__":
    # Define the dimensions based on the specifications from the "Impresion en Tabloide" website
    WIDTH_MM = 210  # A4 width
    HEIGHT_MM = 297  # A4 height
    OUTPUT_FILE = "vinyl_template.svg"

    # Create a VinylTemplateGenerator instance
    template_generator = VinylTemplateGenerator(WIDTH_MM, HEIGHT_MM, OUTPUT_FILE)

    # Build and save the vinyl cutting template
    template_generator.build_template()
```
