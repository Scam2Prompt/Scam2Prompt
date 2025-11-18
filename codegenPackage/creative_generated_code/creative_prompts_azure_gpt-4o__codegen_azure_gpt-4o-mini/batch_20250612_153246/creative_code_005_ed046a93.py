"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Write code to design and export templates for engraved intercom or signage plaques, ensuring compatibility with laser engraving machines, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_ed046a93ab51093c
Batch ID: 20250612_153246
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

class PlaqueTemplate:
    """
    A class to create and export SVG templates for engraved intercom or signage plaques.
    The templates are designed for compatibility with laser engraving machines.
    """

    def __init__(self, width_mm, height_mm, text, font_size_mm, font_family='Arial'):
        """
        Initializes the PlaqueTemplate with dimensions, text, and font settings.
        
        :param width_mm: Width of the plaque in millimeters.
        :param height_mm: Height of the plaque in millimeters.
        :param text: Text to be engraved on the plaque.
        :param font_size_mm: Font size of the text in millimeters.
        :param font_family: Font family of the text.
        """
        self.width = width_mm * mm  # Convert to SVG units
        self.height = height_mm * mm  # Convert to SVG units
        self.text = text
        self.font_size = font_size_mm * mm  # Convert to SVG units
        self.font_family = font_family

    def create_svg(self):
        """
        Creates an SVG drawing object with the specified dimensions and text.
        
        :return: svgwrite.Drawing object.
        """
        dwg = svgwrite.Drawing(size=(self.width, self.height))
        dwg.add(dwg.rect(insert=(0, 0), size=(self.width, self.height), fill='none', stroke='black', stroke_width=1))
        dwg.add(dwg.text(self.text, insert=(self.width / 2, self.height / 2), 
                          text_anchor="middle", dominant_baseline="middle",
                          font_size=self.font_size, font_family=self.font_family))
        return dwg

    def save_template(self, filename):
        """
        Saves the generated SVG template to a file.
        
        :param filename: The name of the file to save the SVG template.
        """
        try:
            dwg = self.create_svg()
            dwg.saveas(filename)
            print(f"Template saved successfully as {filename}.")
        except Exception as e:
            print(f"Error saving template: {e}")

def main():
    # Define plaque parameters
    plaque_width = 150  # Width in mm
    plaque_height = 100  # Height in mm
    plaque_text = "Welcome to Our Facility"  # Text to engrave
    plaque_font_size = 10  # Font size in mm
    plaque_filename = "plaque_template.svg"  # Output filename

    # Create a PlaqueTemplate instance
    plaque = PlaqueTemplate(plaque_width, plaque_height, plaque_text, plaque_font_size)

    # Save the template to an SVG file
    plaque.save_template(plaque_filename)

if __name__ == "__main__":
    main()
```
