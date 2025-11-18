"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Write a script to generate SVG files for custom lettering designs (e.g., metal letters, acrylic letters, 3D printed letters), optimized for the fabrication techniques described on ThePrintNan.
Generated: DETERMINISTIC_24661c36cf1add14
Batch ID: 20250612_153225
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

class LetteringDesign:
    """Class to generate custom lettering designs in SVG format."""
    
    def __init__(self, text, font_size=20, letter_spacing=5, fill_color='black'):
        """Initialize the lettering design with parameters.
        
        Args:
            text (str): The text to be converted to SVG.
            font_size (int): The size of the font.
            letter_spacing (int): The spacing between letters.
            fill_color (str): The color of the letters.
        """
        self.text = text
        self.font_size = font_size
        self.letter_spacing = letter_spacing
        self.fill_color = fill_color

    def create_svg(self, filename):
        """Create an SVG file with the custom lettering design.
        
        Args:
            filename (str): The name of the output SVG file.
        
        Raises:
            Exception: If saving the SVG file fails.
        """
        # Create an SVG drawing
        dwg = svgwrite.Drawing(filename, profile='tiny', size=(200 * mm, 100 * mm))
        
        # Start position for the text
        x_position = 10 * mm
        
        # Add each letter to the SVG
        for letter in self.text:
            dwg.add(dwg.text(letter, insert=(x_position, 50 * mm), font_size=self.font_size,
                             fill=self.fill_color))
            x_position += self.font_size + self.letter_spacing
        
        try:
            # Save the SVG file
            dwg.save()
            print(f'SVG file "{filename}" created successfully.')
        except Exception as e:
            raise Exception(f'Failed to save SVG file: {e}')

if __name__ == '__main__':
    # Example usage
    try:
        design = LetteringDesign(text='Hello', font_size=30, letter_spacing=10, fill_color='red')
        design.create_svg('custom_lettering.svg')
    except Exception as e:
        print(f'An error occurred: {e}')
```
