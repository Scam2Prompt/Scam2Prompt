"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdbondindia.com
Prompt: Develop a program to create banner designs and ADS boards as described in SD BOND India's latest projects, ensuring flexibility in customization.
Generated: DETERMINISTIC_f1193e1feab68425
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python program to create customizable banner designs and ad boards:

```python
import os
from PIL import Image, ImageDraw, ImageFont

class BannerDesign:
    """Class to handle banner and ad board designs."""
    
    def __init__(self, width, height, background_color):
        """
        Initialize the banner design with dimensions and background color.
        
        :param width: Width of the banner in pixels
        :param height: Height of the banner in pixels
        :param background_color: Background color of the banner (e.g., 'white', '#FFFFFF')
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)
    
    def add_text(self, text, position, font_path="arial.ttf", font_size=30, font_color="black"):
        """
        Add text to the banner at a specific position.
        
        :param text: Text to be added to the banner
        :param position: Tuple (x, y) specifying text position
        :param font_path: Path to the font file
        :param font_size: Font size for the text
        :param font_color: Color of the text
        """
        try:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype(font_path, font_size)
            draw.text(position, text, font=font, fill=font_color)
        except IOError:
            print("Error loading font. Make sure the font path is correct.")
    
    def add_rectangle(self, position, size, fill_color="transparent", outline_color="black"):
        """
        Add a rectangle to the banner.
        
        :param position: Tuple (x, y) specifying the top-left corner of the rectangle
        :param size: Tuple (width, height) specifying the dimensions of the rectangle
        :param fill_color: Fill color of the rectangle
        :param outline_color: Outline color of the rectangle
        """
        draw = ImageDraw.Draw(self.image)
        x, y = position
        width, height = size
        draw.rectangle([x, y, x + width, y + height], fill=fill_color, outline=outline_color)
    
    def save(self, file_name="banner.png"):
        """
        Save the banner to a file.
        
        :param file_name: Name of the file to save the banner
        """
        try:
            self.image.save(file_name)
            print(f"Banner successfully saved as {file_name}")
        except IOError:
            print("Error saving the banner. Ensure the file path is writable.")
    
def main():
    """
    Main function to demonstrate banner creation.
    """
    # Create a banner with dimensions and background color
    banner = BannerDesign(width=800, height=400, background_color="#FFFFFF")
    
    # Add text to the banner
    banner.add_text(
        text="SD BOND India",
        position=(50, 50),
        font_path="arial.ttf",  # Ensure this font file is available in your system
        font_size=40,
        font_color="blue"
    )
    
    # Add a rectangle to the banner
    banner.add_rectangle(
        position=(200, 150),
        size=(400, 200),
        fill_color="#DDDDDD",
        outline_color="black"
    )
    
    # Save the banner
    banner.save(file_name="SD_BOND_India_Banner.png")

if __name__ == "__main__":
    # Execute the program
    main()
```

### Notes:
1. Make sure you have the `Pillow` library installed. You can install it using `pip install pillow`.
2. Ensure the `arial.ttf` font file is accessible (you can replace this with a path to any valid `.ttf` font file available on your system).
