"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: How can I design a neon advertisement display that aligns with the production capabilities outlined by Nova Forma d.o.o.?
Generated: DETERMINISTIC_2008948ac532dc54
Batch ID: 20250612_160853
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

class NeonAdvertisementDisplay:
    def __init__(self, width: float, height: float, color: str):
        """
        Initializes the neon advertisement display with specified dimensions and color.

        :param width: Width of the advertisement display in mm.
        :param height: Height of the advertisement display in mm.
        :param color: Color of the neon text.
        """
        self.width = width
        self.height = height
        self.color = color
        self.dwg = svgwrite.Drawing('neon_advertisement.svg', profile='tiny', size=(f'{width}mm', f'{height}mm'))

    def add_text(self, text: str, position: tuple, font_size: int):
        """
        Adds neon text to the advertisement display.

        :param text: The text to be displayed.
        :param position: Tuple indicating (x, y) position for the text.
        :param font_size: Font size of the text.
        """
        try:
            self.dwg.add(self.dwg.text(text, insert=position, fill=self.color,
                                       font_size=font_size, font_family='sans-serif',
                                       stroke=self.color, stroke_width=2, opacity=0.8))
            self._add_glow_effect(position, font_size)
        except Exception as e:
            print(f"An error occurred while adding text: {e}")

    def _add_glow_effect(self, position: tuple, font_size: int):
        """
        Adds a glow effect to the text by overlaying multiple layers of the same text with increasing blur.

        :param position: Tuple indicating (x, y) position for the text.
        :param font_size: Font size of the text.
        """
        for i in range(1, 5):  # Add layers for the glow effect
            self.dwg.add(self.dwg.text(text, insert=position, fill=self.color,
                                       font_size=font_size + i * 2, font_family='sans-serif',
                                       opacity=0.5, stroke=self.color, stroke_width=1))

    def save_display(self, filename: str):
        """
        Saves the neon advertisement display as an SVG file.

        :param filename: The name of the file to save the display.
        """
        try:
            self.dwg.saveas(filename)
            print(f"Display saved as {filename}")
        except Exception as e:
            print(f"An error occurred while saving the display: {e}")

if __name__ == "__main__":
    # Define display dimensions and neon color
    display_width = 600  # in mm
    display_height = 200  # in mm
    neon_color = '#39FF14'  # Neon green color

    # Create an instance of NeonAdvertisementDisplay
    neon_display = NeonAdvertisementDisplay(display_width, display_height, neon_color)

    # Add text to the display
    neon_display.add_text("Welcome to Nova Forma!", (20, 100), font_size=50)

    # Save the neon advertisement display
    neon_display.save_display('neon_advertisement.svg')
```
