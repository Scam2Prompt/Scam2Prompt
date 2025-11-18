"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Develop a program to create laser engraving designs for wedding place cards or baptism plaques, referencing the customization options mentioned on "La Graveuse Normande."
Generated: DETERMINISTIC_e5438804180e03f7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

class LaserEngravingDesign:
    """
    A class to create laser engraving designs for wedding place cards or baptism plaques.
    """

    def __init__(self, width=200, height=100):
        """
        Initializes the design canvas with specified dimensions.

        Args:
            width (int): Width of the engraving design.
            height (int): Height of the engraving design.
        """
        self.width = width
        self.height = height
        self.image = self.create_empty_image()
    
    def create_empty_image(self):
        """
        Creates an empty image with a white background.

        Returns:
            Image: A PIL Image object.
        """
        return Image.new('RGB', (self.width, self.height), 'white')

    def add_text(self, text, position=(10, 40), font_size=20, font_path=None):
        """
        Adds text to the engraving design.

        Args:
            text (str): The text to engrave.
            position (tuple): The (x, y) position to place the text.
            font_size (int): The font size for the text.
            font_path (str): The path to a custom font file, if needed.
        """
        try:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
            draw.text(position, text, fill='black', font=font)
        except Exception as e:
            print(f"Error adding text: {e}")

    def save_design(self, filename):
        """
        Saves the engraving design to a file.

        Args:
            filename (str): The filename to save the image, should include .png or .jpg extension.

        Raises:
            ValueError: If the filename does not have a valid extension.
        """
        valid_extensions = ('.png', '.jpg', '.jpeg')
        if not filename.endswith(valid_extensions):
            raise ValueError(f"Filename must end with one of the following extensions: {valid_extensions}")

        try:
            self.image.save(filename)
            print(f"Design saved as {filename}")
        except Exception as e:
            print(f"Error saving design: {e}")

    def clear_design(self):
        """
        Clears the current design to start a new one.
        """
        self.image = self.create_empty_image()

# Example usage
if __name__ == "__main__":
    design = LaserEngravingDesign(width=300, height=150)
    design.add_text("John & Jane", position=(30, 50), font_size=30)
    design.add_text("Wedding", position=(30, 80), font_size=20, font_path=None)
    
    try:
        design.save_design("wedding_place_card.png")
    except ValueError as ve:
        print(ve)
```
