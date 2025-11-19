"""
Generated Code Metadata:
========================
Original URL: https://fantom.de
Prompt: Create a sample code for a print media design project that utilizes the technical services mentioned on the Fantom website.
Generated: DETERMINISTIC_fe45c07c0e87815d
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from PIL import Image, ImageDraw, ImageFont

class PrintMediaDesigner:
    """
    A class used to design print media.

    Attributes:
    ----------
    width : int
        The width of the design in pixels.
    height : int
        The height of the design in pixels.
    background_color : str
        The background color of the design in hex.

    Methods:
    -------
    add_text(text, x, y, font_size, color)
        Adds text to the design at the specified coordinates.
    add_image(image_path, x, y)
        Adds an image to the design at the specified coordinates.
    save_design(output_path)
        Saves the design to a file.
    """

    def __init__(self, width, height, background_color="#FFFFFF"):
        """
        Initializes the PrintMediaDesigner.

        Parameters:
        ----------
        width : int
            The width of the design in pixels.
        height : int
            The height of the design in pixels.
        background_color : str, optional
            The background color of the design in hex (default is "#FFFFFF").
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.design = Image.new("RGB", (width, height), background_color)
        self.draw = ImageDraw.Draw(self.design)

    def add_text(self, text, x, y, font_size, color):
        """
        Adds text to the design at the specified coordinates.

        Parameters:
        ----------
        text : str
            The text to add.
        x : int
            The x-coordinate of the text.
        y : int
            The y-coordinate of the text.
        font_size : int
            The font size of the text.
        color : str
            The color of the text in hex.
        """
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
            self.draw.text((x, y), text, font=font, fill=color)
        except Exception as e:
            print(f"Error adding text: {e}")

    def add_image(self, image_path, x, y):
        """
        Adds an image to the design at the specified coordinates.

        Parameters:
        ----------
        image_path : str
            The path to the image file.
        x : int
            The x-coordinate of the image.
        y : int
            The y-coordinate of the image.
        """
        try:
            image = Image.open(image_path)
            self.design.paste(image, (x, y))
        except Exception as e:
            print(f"Error adding image: {e}")

    def save_design(self, output_path):
        """
        Saves the design to a file.

        Parameters:
        ----------
        output_path : str
            The path to save the design.
        """
        try:
            self.design.save(output_path)
            print("Design saved successfully.")
        except Exception as e:
            print(f"Error saving design: {e}")


def main():
    designer = PrintMediaDesigner(800, 600)
    designer.add_text("Sample Text", 100, 100, 30, "#000000")
    designer.add_image("image.jpg", 200, 200)
    designer.save_design("output.png")


if __name__ == "__main__":
    main()
```
